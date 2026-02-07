from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Booking, TimeSlot, FutsalSettings


class BookingForm(forms.ModelForm):
    """Form for creating and updating bookings"""
    
    class Meta:
        model = Booking
        fields = ['time_slot', 'booking_date', 'contact_number', 'notes']
        widgets = {
            'booking_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'min': timezone.now().date().isoformat()
                }
            ),
            'time_slot': forms.Select(attrs={'class': 'form-select'}),
            'contact_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '+977-9800000000',
                    'pattern': '[0-9+\\-\\s()]+',
                    'title': 'Please enter a valid phone number'
                }
            ),
            'notes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Any special requirements or notes...',
                    'maxlength': 500
                }
            ),
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Only show active time slots
        self.fields['time_slot'].queryset = TimeSlot.objects.filter(is_active=True)
        
        # Set maximum booking date based on settings
        settings = FutsalSettings.load()
        max_date = timezone.now().date() + timedelta(days=settings.advance_booking_days)
        self.fields['booking_date'].widget.attrs['max'] = max_date.isoformat()
        
        # Add help text
        self.fields['booking_date'].help_text = f'You can book up to {settings.advance_booking_days} days in advance'
    
    def clean_booking_date(self):
        booking_date = self.cleaned_data.get('booking_date')
        
        if not booking_date:
            raise ValidationError('Please select a booking date')
        
        # Check if date is not in the past
        if booking_date < timezone.now().date():
            raise ValidationError('Cannot book for past dates')
        
        # Check maximum advance booking
        settings = FutsalSettings.load()
        max_date = timezone.now().date() + timedelta(days=settings.advance_booking_days)
        if booking_date > max_date:
            raise ValidationError(
                f'You can only book up to {settings.advance_booking_days} days in advance'
            )
        
        return booking_date
    
    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        
        if not contact_number:
            raise ValidationError('Contact number is required')
        
        # Remove spaces and special characters for validation
        cleaned_number = ''.join(filter(str.isdigit, contact_number))
        
        if len(cleaned_number) < 10:
            raise ValidationError('Please enter a valid contact number')
        
        return contact_number
    
    def clean(self):
        cleaned_data = super().clean()
        time_slot = cleaned_data.get('time_slot')
        booking_date = cleaned_data.get('booking_date')
        
        if time_slot and booking_date:
            # Check if user has exceeded daily booking limit
            if self.user:
                settings = FutsalSettings.load()
                user_bookings_count = Booking.objects.filter(
                    user=self.user,
                    booking_date=booking_date,
                    status__in=['pending', 'confirmed']
                ).count()
                
                if user_bookings_count >= settings.max_bookings_per_user_per_day:
                    raise ValidationError(
                        f'You can only make {settings.max_bookings_per_user_per_day} '
                        f'booking(s) per day'
                    )
            
            # Check if slot is available
            existing_booking = Booking.objects.filter(
                time_slot=time_slot,
                booking_date=booking_date,
                status__in=['pending', 'confirmed']
            )
            
            # Exclude current instance if updating
            if self.instance.pk:
                existing_booking = existing_booking.exclude(pk=self.instance.pk)
            
            if existing_booking.exists():
                raise ValidationError(
                    'This time slot is already booked. Please choose another slot.'
                )
        
        return cleaned_data


class CancellationForm(forms.Form):
    """Form for cancelling bookings"""
    reason = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Please provide a reason for cancellation (optional)...',
                'maxlength': 500
            }
        ),
        label='Cancellation Reason'
    )
    confirm = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label='I confirm that I want to cancel this booking'
    )


class DateRangeFilterForm(forms.Form):
    """Form for filtering bookings by date range"""
    start_date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        ),
        label='From Date'
    )
    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        ),
        label='To Date'
    )
    status = forms.ChoiceField(
        required=False,
        choices=[('', 'All Statuses')] + Booking.STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Status'
    )
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
        if start_date and end_date:
            if start_date > end_date:
                raise ValidationError('Start date must be before end date')
        
        return cleaned_data
