from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils import timezone
from .models import TimeSlot, Booking, FutsalSettings, BookingHistory, Payment


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ['start_time', 'end_time',
                    'duration_minutes', 'is_active', 'created_at']
    list_filter = ['is_active', 'duration_minutes']
    search_fields = ['start_time', 'end_time']
    ordering = ['start_time']

    fieldsets = (
        ('Time Information', {
            'fields': ('start_time', 'end_time', 'duration_minutes')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ['created_at', 'updated_at']


class BookingHistoryInline(admin.TabularInline):
    model = BookingHistory
    extra = 0
    readonly_fields = ['action', 'changed_by',
                       'changed_at', 'changes', 'ip_address']
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user_email',
        'booking_date',
        'time_slot',
        'status_badge',
        'payment_status_badge',
        'price',
        'created_at'
    ]
    list_filter = [
        'status',
        'payment_status',
        'booking_date',
        'created_at',
        'time_slot'
    ]
    search_fields = [
        'user__email',
        'user__first_name',
        'user__last_name',
        'contact_number',
        'id'
    ]
    readonly_fields = [
        'id',
        'created_at',
        'updated_at',
        'created_by_ip',
        'cancelled_at'
    ]

    fieldsets = (
        ('Booking Information', {
            'fields': ('id', 'user', 'booking_date', 'time_slot')
        }),
        ('Status', {
            'fields': ('status', 'payment_status', 'price')
        }),
        ('Contact Details', {
            'fields': ('contact_number', 'notes')
        }),
        ('Cancellation', {
            'fields': ('cancelled_at', 'cancellation_reason'),
            'classes': ('collapse',)
        }),
        ('Security & Tracking', {
            'fields': ('created_at', 'updated_at', 'created_by_ip'),
            'classes': ('collapse',)
        }),
    )

    inlines = [BookingHistoryInline]

    date_hierarchy = 'booking_date'
    ordering = ['-booking_date', 'time_slot__start_time']

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'User Email'
    user_email.admin_order_field = 'user__email'

    def status_badge(self, obj):
        colors = {
            'pending': '#ffc107',
            'confirmed': '#28a745',
            'cancelled': '#dc3545',
            'completed': '#6c757d'
        }
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; border-radius: 3px;">{}</span>',
            colors.get(obj.status, '#6c757d'),
            obj.get_status_display()
        )
    status_badge.short_description = 'Status'

    def payment_status_badge(self, obj):
        colors = {
            'pending': '#ffc107',
            'paid': '#28a745',
            'refunded': '#dc3545'
        }
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; border-radius: 3px;">{}</span>',
            colors.get(obj.payment_status, '#6c757d'),
            obj.get_payment_status_display()
        )
    payment_status_badge.short_description = 'Payment Status'

    actions = ['mark_as_confirmed', 'mark_as_completed', 'mark_as_cancelled']

    def mark_as_confirmed(self, request, queryset):
        updated = queryset.update(status='confirmed')
        self.message_user(
            request, f'{updated} booking(s) marked as confirmed.')
    mark_as_confirmed.short_description = 'Mark selected bookings as confirmed'

    def mark_as_completed(self, request, queryset):
        updated = queryset.update(status='completed')
        self.message_user(
            request, f'{updated} booking(s) marked as completed.')
    mark_as_completed.short_description = 'Mark selected bookings as completed'

    def mark_as_cancelled(self, request, queryset):
        updated = queryset.update(
            status='cancelled',
            cancelled_at=timezone.now()
        )
        self.message_user(
            request, f'{updated} booking(s) marked as cancelled.')
    mark_as_cancelled.short_description = 'Mark selected bookings as cancelled'


@admin.register(FutsalSettings)
class FutsalSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {
            'fields': ('futsal_name', 'contact_email', 'contact_phone', 'address')
        }),
        ('Pricing', {
            'fields': ('default_price_per_hour',)
        }),
        ('Business Hours', {
            'fields': ('opening_time', 'closing_time')
        }),
        ('Booking Rules', {
            'fields': (
                'advance_booking_days',
                'min_cancellation_hours',
                'max_bookings_per_user_per_day'
            )
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ['created_at', 'updated_at']

    def has_add_permission(self, request):
        # Only allow one instance
        return not FutsalSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of settings
        return False


@admin.register(BookingHistory)
class BookingHistoryAdmin(admin.ModelAdmin):
    list_display = ['booking', 'action',
                    'changed_by', 'changed_at', 'ip_address']
    list_filter = ['action', 'changed_at']
    search_fields = ['booking__id', 'changed_by__email']
    readonly_fields = ['booking', 'action', 'changed_by',
                       'changed_at', 'changes', 'ip_address']
    ordering = ['-changed_at']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        'transaction_uuid_short',
        'booking',
        'amount',
        'status_badge',
        'created_at',
        'completed_at'
    ]
    list_filter = ['status', 'created_at', 'completed_at']
    search_fields = [
        'transaction_uuid',
        'booking__id',
        'esewa_transaction_code',
        'booking__user__email'
    ]
    readonly_fields = [
        'id',
        'transaction_uuid',
        'created_at',
        'updated_at',
        'completed_at',
        'signature'
    ]

    fieldsets = (
        ('Payment Information', {
            'fields': ('id', 'booking', 'amount', 'status')
        }),
        ('eSewa Details', {
            'fields': (
                'transaction_uuid',
                'esewa_transaction_code',
                'esewa_refund_code',
                'product_code',
                'signature'
            )
        }),
        ('Tracking', {
            'fields': ('ip_address', 'user_agent'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'completed_at'),
            'classes': ('collapse',)
        }),
    )

    date_hierarchy = 'created_at'
    ordering = ['-created_at']

    actions = ['mark_as_completed', 'mark_as_failed']

    def transaction_uuid_short(self, obj):
        return f"{obj.transaction_uuid[:8]}..."
    transaction_uuid_short.short_description = 'Transaction ID'

    def status_badge(self, obj):
        colors = {
            'pending': '#ffc107',
            'initiated': '#0dcaf0',
            'completed': '#28a745',
            'failed': '#dc3545',
            'cancelled': '#6c757d'
        }
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; border-radius: 3px;">{}</span>',
            colors.get(obj.status, '#6c757d'),
            obj.get_status_display()
        )
    status_badge.short_description = 'Status'

    def mark_as_completed(self, request, queryset):
        updated = queryset.filter(status__in=['pending', 'initiated']).update(
            status='completed', completed_at=timezone.now())
        self.message_user(
            request, f'{updated} payment(s) marked as completed.')
    mark_as_completed.short_description = 'Mark selected payments as completed'

    def mark_as_failed(self, request, queryset):
        updated = queryset.filter(
            status__in=['pending', 'initiated']).update(status='failed')
        self.message_user(request, f'{updated} payment(s) marked as failed.')
    mark_as_failed.short_description = 'Mark selected payments as failed'

    def has_add_permission(self, request):
        # Payments should be created through the payment gateway, not manually
        return False

    def has_delete_permission(self, request, obj=None):
        # Prevent accidental deletion of payment records
        return False
