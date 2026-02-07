from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q, Count
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from django_ratelimit.decorators import ratelimit
from datetime import datetime, timedelta
from decimal import Decimal
import logging

from .models import Booking, TimeSlot, FutsalSettings, BookingHistory
from .forms import BookingForm, CancellationForm, DateRangeFilterForm

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
    settings = FutsalSettings.load()
    recent_bookings_count = Booking.objects.filter(
        status__in=['pending', 'confirmed']
    ).count()

    context = {
        'settings': settings,
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
    settings = FutsalSettings.load()
    selected_date = request.GET.get('date', timezone.now().date())

    try:
        selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
    except (ValueError, TypeError):
        selected_date = timezone.now().date()

    # Get all active time slots
    time_slots = TimeSlot.objects.filter(is_active=True).order_by('start_time')

    # Check availability for each slot on the selected date
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
        'settings': settings,
        'slots': slots_with_availability,
        'selected_date': selected_date,
        'min_date': timezone.now().date(),
        'max_date': timezone.now().date() + timedelta(days=settings.advance_booking_days),
    }
    return render(request, 'bookings/available_slots.html', context)


@login_required
def create_booking(request):
    """Create a new booking"""
    settings = FutsalSettings.load()

    if request.method == 'POST':
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user

            # Calculate price correctly using Decimal
            duration_minutes = Decimal(booking.time_slot.duration_minutes)
            duration_hours = duration_minutes / Decimal('60')
            booking.price = settings.default_price_per_hour * duration_hours
            booking.price = booking.price.quantize(
                Decimal('0.01'))  # Round to 2 decimal places

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

    context = {
        'form': form,
        'settings': settings,
    }
    return render(request, 'bookings/create_booking.html', context)


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
            if booking.can_be_cancelled():
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
                    request, 'This booking cannot be cancelled (too late or already cancelled).')
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

    # Split into upcoming and past
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


def about(request):
    """About page"""
    settings = FutsalSettings.load()
    context = {'settings': settings}
    return render(request, 'bookings/about.html', context)


def contact(request):
    """Contact page"""
    settings = FutsalSettings.load()
    context = {'settings': settings}
    return render(request, 'bookings/contact.html', context)
