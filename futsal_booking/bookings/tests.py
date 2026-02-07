from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta, time
from bookings.models import TimeSlot, Booking, FutsalSettings


class TimeSlotModelTest(TestCase):
    def setUp(self):
        self.time_slot = TimeSlot.objects.create(
            start_time=time(10, 0),
            end_time=time(11, 0),
            duration_minutes=60,
            is_active=True
        )
    
    def test_time_slot_creation(self):
        """Test time slot is created correctly"""
        self.assertEqual(str(self.time_slot), "10:00 AM - 11:00 AM")
        self.assertTrue(self.time_slot.is_active)
    
    def test_time_slot_duration(self):
        """Test time slot duration"""
        self.assertEqual(self.time_slot.duration_minutes, 60)


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.time_slot = TimeSlot.objects.create(
            start_time=time(10, 0),
            end_time=time(11, 0),
            duration_minutes=60,
            is_active=True
        )
        self.booking_date = timezone.now().date() + timedelta(days=1)
        self.booking = Booking.objects.create(
            user=self.user,
            time_slot=self.time_slot,
            booking_date=self.booking_date,
            status='pending',
            price=1000.00,
            contact_number='+977-9800000000'
        )
    
    def test_booking_creation(self):
        """Test booking is created correctly"""
        self.assertEqual(self.booking.user, self.user)
        self.assertEqual(self.booking.time_slot, self.time_slot)
        self.assertEqual(self.booking.status, 'pending')
        self.assertEqual(self.booking.price, 1000.00)
    
    def test_can_cancel_booking(self):
        """Test booking cancellation logic"""
        # Booking is tomorrow, should be cancellable
        self.assertTrue(self.booking.can_cancel())
        
        # Set booking to past date
        self.booking.booking_date = timezone.now().date() - timedelta(days=1)
        self.booking.save()
        self.assertFalse(self.booking.can_cancel())
    
    def test_cancel_booking(self):
        """Test booking cancellation"""
        result = self.booking.cancel(reason='Test cancellation')
        self.assertTrue(result)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.status, 'cancelled')
        self.assertIsNotNone(self.booking.cancelled_at)


class FutsalSettingsTest(TestCase):
    def test_singleton_pattern(self):
        """Test that only one FutsalSettings instance exists"""
        settings1 = FutsalSettings.load()
        settings2 = FutsalSettings.load()
        self.assertEqual(settings1.pk, settings2.pk)
        self.assertEqual(FutsalSettings.objects.count(), 1)


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        FutsalSettings.load()  # Create settings
    
    def test_home_page(self):
        """Test home page loads"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Futsal Arena')
    
    def test_login_required_for_booking(self):
        """Test that booking pages require authentication"""
        response = self.client.get('/create-booking/')
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_authenticated_user_access(self):
        """Test authenticated user can access booking pages"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/available-slots/')
        self.assertEqual(response.status_code, 200)
    
    def test_about_page(self):
        """Test about page loads"""
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    
    def test_contact_page(self):
        """Test contact page loads"""
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)


class BookingValidationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.time_slot = TimeSlot.objects.create(
            start_time=time(10, 0),
            end_time=time(11, 0),
            duration_minutes=60,
            is_active=True
        )
        self.booking_date = timezone.now().date() + timedelta(days=1)
    
    def test_prevent_double_booking(self):
        """Test that double booking is prevented"""
        # Create first booking
        Booking.objects.create(
            user=self.user,
            time_slot=self.time_slot,
            booking_date=self.booking_date,
            status='confirmed',
            price=1000.00,
            contact_number='+977-9800000000'
        )
        
        # Try to create second booking for same slot/date
        from django.core.exceptions import ValidationError
        booking2 = Booking(
            user=self.user,
            time_slot=self.time_slot,
            booking_date=self.booking_date,
            status='pending',
            price=1000.00,
            contact_number='+977-9800000000'
        )
        
        with self.assertRaises(ValidationError):
            booking2.full_clean()
    
    def test_past_date_booking_prevented(self):
        """Test that booking for past dates is prevented"""
        from django.core.exceptions import ValidationError
        past_booking = Booking(
            user=self.user,
            time_slot=self.time_slot,
            booking_date=timezone.now().date() - timedelta(days=1),
            status='pending',
            price=1000.00,
            contact_number='+977-9800000000'
        )
        
        with self.assertRaises(ValidationError):
            past_booking.full_clean()
