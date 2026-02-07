# bookings/management/commands/create_initial_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import time, date, timedelta
from bookings.models import TimeSlot, FutsalSettings, Booking, BookingHistory
import random


class Command(BaseCommand):
    help = 'Creates initial time slots, futsal settings, and sample/test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(
            'Starting initial data creation...'))

        # ────────────────────────────────────────────────
        # 1. Futsal Settings (singleton)
        # ────────────────────────────────────────────────
        settings, created = FutsalSettings.objects.get_or_create(pk=1)
        if created or settings.futsal_name == '':
            settings.futsal_name = "Thimi Futsal Arena"
            settings.contact_email = "info@thimifutsal.com"
            settings.contact_phone = "+977-980-1234567"
            settings.address = "Madhyapur Thimi, Bhaktapur, Nepal"
            settings.default_price_per_hour = 1200.00
            settings.advance_booking_days = 30
            settings.min_cancellation_hours = 24
            settings.max_bookings_per_user_per_day = 2
            settings.opening_time = time(6, 0)
            settings.closing_time = time(22, 0)
            settings.save()
            self.stdout.write(self.style.SUCCESS(
                '✓ Futsal settings created/updated'))
        else:
            self.stdout.write(self.style.WARNING(
                'Futsal settings already exist → skipping update'))

        # ────────────────────────────────────────────────
        # 2. Time Slots (hourly slots from 6:00 to 22:00)
        # ────────────────────────────────────────────────
        time_slots_data = []
        current_time = time(6, 0)
        end_time = time(22, 0)

        while current_time < end_time:
            start = current_time
            end_hour = current_time.hour + 1
            end = time(end_hour, 0) if end_hour < 24 else time(0, 0)
            time_slots_data.append((start, end, 60))
            current_time = end

        created_slots = 0
        for start, end, duration in time_slots_data:
            if not TimeSlot.objects.filter(start_time=start, end_time=end).exists():
                TimeSlot.objects.create(
                    start_time=start,
                    end_time=end,
                    duration_minutes=duration,
                    is_active=True
                )
                created_slots += 1

        self.stdout.write(self.style.SUCCESS(
            f'✓ Created {created_slots} new time slots (total now: {TimeSlot.objects.count()})'))

        # ────────────────────────────────────────────────
        # 3. Test Users
        # ────────────────────────────────────────────────
        test_users_data = [
            {"username": "player1", "email": "player1@example.com",
                "first_name": "Ramesh", "last_name": "Shrestha"},
            {"username": "player2", "email": "player2@example.com",
                "first_name": "Sita", "last_name": "Gurung"},
            {"username": "player3", "email": "player3@example.com",
                "first_name": "Hari", "last_name": "Thapa"},
        ]

        created_users = 0
        users = []
        for data in test_users_data:
            user, created = User.objects.get_or_create(
                username=data["username"],
                defaults={
                    "email": data["email"],
                    "first_name": data["first_name"],
                    "last_name": data["last_name"],
                    "is_active": True,
                }
            )
            if created:
                user.set_password("testpass123")
                user.save()
                created_users += 1
            users.append(user)

        self.stdout.write(self.style.SUCCESS(
            f'✓ Created/verified {created_users} test users'))

        # ────────────────────────────────────────────────
        # 4. Sample Bookings
        # ────────────────────────────────────────────────
        today = timezone.now().date()
        slots = TimeSlot.objects.filter(is_active=True).order_by('start_time')

        if not slots.exists():
            self.stdout.write(self.style.ERROR(
                'No active time slots found → cannot create bookings'))
            return

        sample_bookings = [
            # Past – completed
            {"user": users[0], "date": today - timedelta(
                days=5), "slot": slots[4], "status": "completed", "price": 1200},
            # Past – cancelled
            {"user": users[1], "date": today - timedelta(
                days=2), "slot": slots[7], "status": "cancelled", "price": 1200},
            # Today – confirmed
            {"user": users[2], "date": today, "slot": slots[5],
                "status": "confirmed", "price": 1200},
            # Tomorrow – pending
            {"user": users[0], "date": today + timedelta(
                days=1), "slot": slots[8], "status": "pending", "price": 1200},
            # In 3 days – confirmed
            {"user": users[1], "date": today + timedelta(
                days=3), "slot": slots[3], "status": "confirmed", "price": 1200},
            # In 7 days – confirmed (extra for variety)
            {"user": users[2], "date": today + timedelta(
                days=7), "slot": slots[6], "status": "confirmed", "price": 1200},
        ]

        created_bookings = 0
        for data in sample_bookings:
            if not Booking.objects.filter(
                user=data["user"],
                booking_date=data["date"],
                time_slot=data["slot"]
            ).exists():
                booking = Booking(
                    user=data["user"],
                    time_slot=data["slot"],
                    booking_date=data["date"],
                    status=data["status"],
                    payment_status="paid" if data["status"] in [
                        "confirmed", "completed"] else "pending",
                    price=data["price"],
                    contact_number="+977-98" +
                    str(random.randint(10000000, 99999999)),
                    notes="Test booking created by initial data command"
                )

                # For past dates → save without full_clean to bypass date validation
                if data["date"] < today:
                    booking.save()  # direct save – no clean()
                else:
                    booking.full_clean()   # normal validation for future/today
                    booking.save()

                # Create history record
                BookingHistory.objects.create(
                    booking=booking,
                    action="created",
                    changed_by=None,  # system
                    changes={"status": booking.status,
                             "price": str(booking.price)},
                    ip_address="127.0.0.1"
                )
                created_bookings += 1

        self.stdout.write(self.style.SUCCESS(
            f'✓ Created {created_bookings} sample bookings'))

        self.stdout.write(self.style.SUCCESS(
            '\nInitial data & test records created successfully!'))
        self.stdout.write(self.style.NOTICE('Test login credentials:'))
        for user in test_users_data:
            self.stdout.write(
                f"  • Username: {user['username']}    Password: testpass123")
