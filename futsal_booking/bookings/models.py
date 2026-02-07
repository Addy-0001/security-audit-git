from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from datetime import datetime, timedelta
import uuid


class TimeSlot(models.Model):
    """Available time slots for futsal booking"""
    SLOT_DURATION_CHOICES = [
        (60, '1 Hour'),
        (90, '1.5 Hours'),
        (120, '2 Hours'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration_minutes = models.IntegerField(
        choices=SLOT_DURATION_CHOICES,
        default=60,
        validators=[MinValueValidator(30), MaxValueValidator(180)]
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['start_time']
        verbose_name = 'Time Slot'
        verbose_name_plural = 'Time Slots'
    
    def __str__(self):
        return f"{self.start_time.strftime('%I:%M %p')} - {self.end_time.strftime('%I:%M %p')}"
    
    def clean(self):
        from django.core.exceptions import ValidationError
        if self.start_time >= self.end_time:
            raise ValidationError('End time must be after start time')


class Booking(models.Model):
    """Futsal booking records"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('refunded', 'Refunded'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    time_slot = models.ForeignKey(
        TimeSlot,
        on_delete=models.PROTECT,
        related_name='bookings'
    )
    booking_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default='pending'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    contact_number = models.CharField(max_length=15)
    notes = models.TextField(blank=True, null=True)
    
    # Security and tracking fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_ip = models.GenericIPAddressField(null=True, blank=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    cancellation_reason = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['-booking_date', 'time_slot__start_time']
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        unique_together = ['time_slot', 'booking_date']
        indexes = [
            models.Index(fields=['booking_date', 'time_slot']),
            models.Index(fields=['user', 'status']),
            models.Index(fields=['status', 'booking_date']),
        ]
    
    def __str__(self):
        return f"{self.user.email} - {self.booking_date} {self.time_slot}"
    
    def clean(self):
        from django.core.exceptions import ValidationError
        
        # Cannot book past dates
        if self.booking_date < timezone.now().date():
            raise ValidationError('Cannot book for past dates')
        
        # Check if slot is already booked (excluding current instance in updates)
        existing_booking = Booking.objects.filter(
            time_slot=self.time_slot,
            booking_date=self.booking_date,
            status__in=['pending', 'confirmed']
        ).exclude(pk=self.pk)
        
        if existing_booking.exists():
            raise ValidationError('This time slot is already booked for the selected date')
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def can_cancel(self):
        """Check if booking can be cancelled (at least 24 hours before)"""
        booking_datetime = datetime.combine(
            self.booking_date,
            self.time_slot.start_time
        )
        now = timezone.now()
        time_until_booking = booking_datetime - now.replace(tzinfo=None)
        return time_until_booking > timedelta(hours=24) and self.status in ['pending', 'confirmed']
    
    def cancel(self, reason=''):
        """Cancel the booking"""
        if self.can_cancel():
            self.status = 'cancelled'
            self.cancelled_at = timezone.now()
            self.cancellation_reason = reason
            self.save()
            return True
        return False


class FutsalSettings(models.Model):
    """Global settings for the futsal"""
    futsal_name = models.CharField(max_length=200, default='Futsal Arena')
    default_price_per_hour = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=1000.00,
        validators=[MinValueValidator(0)]
    )
    advance_booking_days = models.IntegerField(
        default=30,
        validators=[MinValueValidator(1), MaxValueValidator(90)],
        help_text='Maximum days in advance for booking'
    )
    min_cancellation_hours = models.IntegerField(
        default=24,
        validators=[MinValueValidator(1)],
        help_text='Minimum hours before booking to allow cancellation'
    )
    contact_email = models.EmailField(default='info@futsal.com')
    contact_phone = models.CharField(max_length=15, default='')
    address = models.TextField(default='')
    
    # Business hours
    opening_time = models.TimeField(default='06:00')
    closing_time = models.TimeField(default='22:00')
    
    # Security settings
    max_bookings_per_user_per_day = models.IntegerField(
        default=2,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Futsal Settings'
        verbose_name_plural = 'Futsal Settings'
    
    def __str__(self):
        return self.futsal_name
    
    def save(self, *args, **kwargs):
        # Ensure only one settings instance exists
        self.pk = 1
        super().save(*args, **kwargs)
    
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class BookingHistory(models.Model):
    """Track all changes to bookings for audit purposes"""
    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE,
        related_name='history'
    )
    action = models.CharField(max_length=50)
    changed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    changed_at = models.DateTimeField(auto_now_add=True)
    changes = models.JSONField(default=dict)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    
    class Meta:
        ordering = ['-changed_at']
        verbose_name = 'Booking History'
        verbose_name_plural = 'Booking Histories'
    
    def __str__(self):
        return f"{self.booking} - {self.action} at {self.changed_at}"
