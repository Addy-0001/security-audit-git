# Quick Start Guide

Get your Futsal Booking System up and running in 5 minutes!

## Prerequisites

- Python 3.10 or higher installed
- pip installed
- Google account for OAuth setup

## Installation Steps

### 1. Set Up Virtual Environment

```bash
# Navigate to project directory
cd futsal_booking

# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Generate a new SECRET_KEY
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Edit .env and paste the SECRET_KEY
# For development, you can leave other settings as default
```

### 4. Set Up Google OAuth (Required)

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable Google+ API
4. Go to Credentials → Create Credentials → OAuth 2.0 Client ID
5. Configure consent screen (Internal/External)
6. Application type: Web application
7. Add authorized redirect URIs:
   ```
   http://localhost:8000/accounts/google/login/callback/
   http://127.0.0.1:8000/accounts/google/login/callback/
   ```
8. Copy Client ID and Client Secret
9. Update `.env` file:
   ```env
   GOOGLE_OAUTH_CLIENT_ID=your-client-id.apps.googleusercontent.com
   GOOGLE_OAUTH_CLIENT_SECRET=your-client-secret
   ```

### 5. Initialize Database

```bash
# Run migrations
python manage.py migrate

# Create initial data (time slots and settings)
python manage.py create_initial_data

# Create admin user
python manage.py createsuperuser
# Enter email and password when prompted
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Visit: **http://localhost:8000**

## First Time Setup

### Access Admin Panel

1. Go to http://localhost:8000/admin
2. Login with superuser credentials
3. Verify time slots are created
4. Update Futsal Settings if needed

### Test User Flow

1. Go to http://localhost:8000
2. Click "Login"
3. Sign in with Google
4. Browse available slots
5. Create a test booking
6. View in "My Bookings"

## Common Issues & Solutions

### Google OAuth Not Working

**Problem**: OAuth redirect fails

**Solution**:
- Double-check redirect URIs in Google Console
- Ensure they match exactly: `http://localhost:8000/accounts/google/login/callback/`
- Clear browser cache and cookies
- Restart development server

### Database Migration Errors

**Problem**: Migration fails

**Solution**:
```bash
# Delete db.sqlite3 and try again
rm db.sqlite3
python manage.py migrate
python manage.py create_initial_data
```

### Static Files Not Loading

**Problem**: CSS/JS not appearing

**Solution**:
```bash
python manage.py collectstatic --noinput
```

### Port Already in Use

**Problem**: Port 8000 is already in use

**Solution**:
```bash
# Use a different port
python manage.py runserver 8080
```

## Development Tips

### View Database

```bash
python manage.py dbshell
```

### Create Test Data

```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User
from bookings.models import Booking, TimeSlot
from django.utils import timezone
from datetime import timedelta

# Create test booking
user = User.objects.first()
slot = TimeSlot.objects.first()
booking = Booking.objects.create(
    user=user,
    time_slot=slot,
    booking_date=timezone.now().date() + timedelta(days=1),
    price=1000,
    contact_number='+977-9800000000',
    status='confirmed'
)
```

### Run Tests

```bash
python manage.py test
```

### View Logs

Check `logs/django.log` for application logs

## Next Steps

1. **Customize**: Update futsal name and settings in admin panel
2. **Add Slots**: Create more time slots if needed
3. **Test**: Create test bookings and verify email notifications
4. **Deploy**: See DEPLOYMENT.md for production deployment

## Need Help?

- Check README.md for detailed documentation
- Check DEPLOYMENT.md for production setup
- Review models.py to understand data structure
- Explore admin panel to see all features

## Quick Commands Reference

```bash
# Start server
python manage.py runserver

# Create admin user
python manage.py createsuperuser

# Run migrations
python manage.py migrate

# Create initial data
python manage.py create_initial_data

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test

# Django shell
python manage.py shell

# Database shell
python manage.py dbshell
```

## Security Reminders for Development

- Never commit `.env` file
- Use `DEBUG=True` only in development
- Change SECRET_KEY before deployment
- Keep Google OAuth credentials secure

## Ready for Production?

See **DEPLOYMENT.md** for complete production deployment guide including:
- PostgreSQL setup
- Nginx configuration
- SSL certificates
- Security hardening
- Backup strategies

---

Happy Coding! 🎉
