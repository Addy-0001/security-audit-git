from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q, Count
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django_ratelimit.decorators import ratelimit
from datetime import datetime, timedelta
from decimal import Decimal
import logging
import uuid

from django.conf import settings

from .models import Booking, TimeSlot, FutsalSettings, BookingHistory, Payment
from .forms import BookingForm, CancellationForm, DateRangeFilterForm
from .esewa import esewa_gateway

logger = logging.getLogger(__name__)


def get_client_ip(request):
    """Get the client's IP address from the request"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def home(request):
    """Home page view"""
    settings_obj = FutsalSettings.load()
    recent_bookings_count = Booking.objects.filter(
        status__in=['pending', 'confirmed']
    ).count()

    context = {
        'settings': settings_obj,
        'recent_bookings_count': recent_bookings_count,
    }

    if request.user.is_authenticated:
        user_bookings = Booking.objects.filter(
            user=request.user,
            booking_date__gte=timezone.now().date()
        ).order_by('booking_date', 'time_slot__start_time')[:3]
        context['upcoming_bookings'] = user_bookings

    return render(request, 'bookings/home.html', context)


@login_required
@ratelimit(key='user', rate='10/h', method='GET')
def available_slots(request):
    """View to show available time slots for a selected date"""
    settings_obj = FutsalSettings.load()
    selected_date_str = request.GET.get('date')

    try:
        selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date()
    except (ValueError, TypeError):
        selected_date = timezone.now().date()

    time_slots = TimeSlot.objects.filter(is_active=True).order_by('start_time')

    slots_with_availability = []
    for slot in time_slots:
        is_booked = Booking.objects.filter(
            time_slot=slot,
            booking_date=selected_date,
            status__in=['pending', 'confirmed']
        ).exists()
        slots_with_availability.append({
            'slot': slot,
            'is_available': not is_booked,
        })

    context = {
        'settings': settings_obj,
        'slots': slots_with_availability,
        'selected_date': selected_date,
        'min_date': timezone.now().date(),
        'max_date': timezone.now().date() + timedelta(days=settings_obj.advance_booking_days),
    }
    return render(request, 'bookings/available_slots.html', context)


@login_required
def create_booking(request):
    """Create a new booking"""
    settings_obj = FutsalSettings.load()

    if request.method == 'POST':
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user

            # Calculate price correctly using Decimal
            duration_minutes = Decimal(booking.time_slot.duration_minutes)
            duration_hours = duration_minutes / Decimal('60')
            booking.price = settings_obj.default_price_per_hour * duration_hours
            booking.price = booking.price.quantize(Decimal('0.01'))

            # Prevent past dates (extra safety)
            if booking.booking_date < timezone.now().date():
                form.add_error('booking_date', "Cannot book for past dates.")
                return render(request, 'bookings/create_booking.html', {
                    'form': form,
                    'settings': settings_obj,
                })

            booking.save()

            # Create history entry
            BookingHistory.objects.create(
                booking=booking,
                action='created',
                changed_by=request.user,
                changes={
                    'status': booking.status,
                    'price': str(booking.price),
                    'booking_date': str(booking.booking_date),
                    'time_slot': str(booking.time_slot),
                },
                ip_address=get_client_ip(request)
            )

            messages.success(
                request, 'Your booking has been created successfully!')
            return redirect('booking_detail', booking_id=booking.id)

        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookingForm(user=request.user)

        # Prefill from URL parameters (?slot=...&date=...)
        slot_id = request.GET.get('slot')
        date_str = request.GET.get('date')

        initial = {}
        if slot_id:
            try:
                slot = TimeSlot.objects.get(id=slot_id)
                initial['time_slot'] = slot
            except TimeSlot.DoesNotExist:
                pass

        if date_str:
            try:
                initial['booking_date'] = datetime.strptime(
                    date_str, '%Y-%m-%d').date()
            except ValueError:
                pass

        form.initial.update(initial)

    return render(request, 'bookings/create_booking.html', {
        'form': form,
        'settings': settings_obj,
    })


@login_required
def booking_detail(request, booking_id):
    """View details of a specific booking"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    history = booking.history.all().order_by('-changed_at')

    context = {
        'booking': booking,
        'history': history,
    }
    return render(request, 'bookings/booking_detail.html', context)


@login_required
def cancel_booking(request, booking_id):
    """Cancel an existing booking"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        form = CancellationForm(request.POST)
        if form.is_valid():
            if booking.status in ['pending', 'confirmed']:
                old_status = booking.status
                booking.status = 'cancelled'
                booking.save()

                BookingHistory.objects.create(
                    booking=booking,
                    action='cancelled',
                    changed_by=request.user,
                    changes={'status': f"{old_status} → cancelled"},
                    ip_address=get_client_ip(request)
                )

                messages.success(
                    request, 'Your booking has been cancelled successfully.')
                return redirect('my_bookings')
            else:
                messages.error(
                    request, 'This booking cannot be cancelled at this time.')
        else:
            messages.error(request, 'Please confirm cancellation.')
    else:
        form = CancellationForm()

    context = {
        'booking': booking,
        'form': form,
    }
    return render(request, 'bookings/cancel_booking.html', context)


@login_required
def my_bookings(request):
    """List all bookings for the current user"""
    filter_form = DateRangeFilterForm(request.GET or None)

    bookings = Booking.objects.filter(user=request.user).order_by(
        '-booking_date', '-created_at')

    if filter_form.is_valid():
        start_date = filter_form.cleaned_data.get('start_date')
        end_date = filter_form.cleaned_data.get('end_date')
        status = filter_form.cleaned_data.get('status')

        if start_date:
            bookings = bookings.filter(booking_date__gte=start_date)
        if end_date:
            bookings = bookings.filter(booking_date__lte=end_date)
        if status:
            bookings = bookings.filter(status=status)

    today = timezone.now().date()
    upcoming = bookings.filter(booking_date__gte=today)
    past = bookings.filter(booking_date__lt=today)

    context = {
        'filter_form': filter_form,
        'upcoming_bookings': upcoming,
        'past_bookings': past,
    }
    return render(request, 'bookings/my_bookings.html', context)


@login_required
@require_http_methods(["GET"])
def check_slot_availability(request):
    """AJAX endpoint to check slot availability"""
    date_str = request.GET.get('date')
    slot_id = request.GET.get('slot_id')

    if not date_str or not slot_id:
        return JsonResponse({'available': False, 'error': 'Missing parameters'})

    try:
        booking_date = datetime.strptime(date_str, '%Y-%m-%d').date()

        is_available = not Booking.objects.filter(
            time_slot_id=slot_id,
            booking_date=booking_date,
            status__in=['pending', 'confirmed']
        ).exists()

        return JsonResponse({'available': is_available})
    except (ValueError, TimeSlot.DoesNotExist):
        return JsonResponse({'available': False, 'error': 'Invalid parameters'})


@login_required
@login_required
def initiate_payment(request, booking_id):
    """Start (or resume) eSewa payment for a specific booking – idempotent"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    # State checks
    if booking.status != 'pending':
        messages.error(request, "This booking is not in a payable state.")
        return redirect('booking_detail', booking_id=booking.id)

    if booking.payment_status == 'paid':
        messages.info(request, "This booking has already been paid.")
        return redirect('booking_detail', booking_id=booking.id)

    # Check for existing payment record (idempotent)
    payment = Payment.objects.filter(booking=booking).first()

    if payment:
        # Already exists – reuse it (e.g. user retried / refreshed)
        if payment.status in ['completed', 'paid']:
            messages.info(
                request, "Payment already processed for this booking.")
            return redirect('booking_detail', booking_id=booking.id)

        if payment.status in ['failed', 'cancelled']:
            # Allow retry – update status back to initiated
            payment.status = 'initiated'
            payment.save(update_fields=['status'])
            logger.info(f"Retrying payment for existing record: {payment.id}")
        else:
            logger.info(f"Resuming existing initiated payment: {payment.id}")
    else:
        # No payment yet – create new one
        transaction_uuid = str(uuid.uuid4())
        payment = Payment.objects.create(
            booking=booking,
            amount=booking.price,
            status='initiated',
            transaction_uuid=transaction_uuid,
            product_code='FUTSAL_BOOKING',
            ip_address=get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', '')
        )
        logger.info(f"Created new payment record: {payment.id}")

    # Prepare eSewa form parameters
    params = esewa_gateway.get_payment_form_data(
        amount=booking.price,
        booking_id=str(booking.id)
    )

    context = {
        'payment_url': settings.ESEWA_PAYMENT_URL,
        'params': params,
        'booking': booking,
        'payment': payment,
    }

    return render(request, 'bookings/esewa_redirect.html', context)


@csrf_exempt
def payment_success(request):
    """eSewa success callback – verify & confirm"""
    ref_id = request.GET.get('refId')
    amount = request.GET.get('amt')
    order_id = request.GET.get('oid')  # = booking.id

    if not all([ref_id, amount, order_id]):
        messages.error(request, "Invalid payment response from eSewa.")
        return redirect('my_bookings')

    try:
        booking = get_object_or_404(Booking, id=order_id)
        payment = get_object_or_404(
            Payment, booking=booking, transaction_uuid__startswith=order_id[:8])
    except:
        messages.error(request, "Booking or payment record not found.")
        return redirect('my_bookings')

    # Verify with eSewa server
    if esewa_gateway.verify_payment(ref_id, amount, order_id):
        payment.mark_completed(esewa_code=ref_id)

        BookingHistory.objects.create(
            booking=booking,
            action='payment_completed',
            changed_by=request.user if request.user.is_authenticated else None,
            changes={'amount': amount, 'ref_id': ref_id},
            ip_address=get_client_ip(request)
        )

        messages.success(
            request, f"Payment of NPR {amount} successful! Booking confirmed.")
    else:
        payment.mark_failed()
        messages.error(
            request, "Payment could not be verified. Please contact support if amount was deducted.")

    return redirect('booking_detail', booking_id=booking.id)


@csrf_exempt
def payment_failed(request):
    messages.error(request, "Payment failed or was declined by eSewa.")
    return redirect('my_bookings')


@csrf_exempt
def payment_cancelled(request):
    messages.warning(request, "You cancelled the payment.")
    return redirect('my_bookings')


def about(request):
    """About page"""
    settings_obj = FutsalSettings.load()
    context = {'settings': settings_obj}
    return render(request, 'bookings/about.html', context)


def contact(request):
    """Contact page"""
    settings_obj = FutsalSettings.load()
    context = {'settings': settings_obj}
    return render(request, 'bookings/contact.html', context)
