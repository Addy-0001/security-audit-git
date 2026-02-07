# Futsal Booking System

A secure, feature-rich Django web application for managing futsal court bookings with Google OAuth authentication.

## Features

### Core Features
- **Google OAuth Authentication**: Secure login using Google accounts
- **Online Booking System**: Book futsal slots online with real-time availability
- **User Dashboard**: View and manage all bookings in one place
- **Booking Management**: Create, view, and cancel bookings
- **Admin Panel**: Comprehensive admin interface for managing bookings and settings
- **Responsive Design**: Mobile-friendly interface using Bootstrap 5

### Security Features
- **CSRF Protection**: Django's built-in CSRF protection
- **XSS Protection**: Content Security Policy (CSP) headers
- **Rate Limiting**: Prevents abuse with django-ratelimit
- **Secure Session Management**: HTTPOnly cookies and secure session handling
- **IP Tracking**: Log IP addresses for security auditing
- **Password Validation**: Strong password requirements
- **SQL Injection Protection**: Django ORM prevents SQL injection
- **Booking History**: Complete audit trail of all booking changes

### Business Rules
- Book up to 30 days in advance (configurable)
- Cancel bookings up to 24 hours before scheduled time
- Maximum 2 bookings per user per day (configurable)
- Prevent double bookings
- Automatic price calculation based on slot duration
- Email notifications (configurable)

## Technology Stack

- **Backend**: Django 5.0.1
- **Authentication**: django-allauth with Google OAuth
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Security**: django-csp, django-ratelimit
- **Caching**: Redis (optional)
- **Forms**: django-crispy-forms with Bootstrap 5

## Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- Virtual environment tool (venv or virtualenv)
- Google Cloud account (for OAuth credentials)
- PostgreSQL (for production deployment)
- Redis (optional, for caching and rate limiting)

## Installation

### 1. Clone the Repository

```bash
cd futsal_booking
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

Edit `.env` with your settings:

```env
# Django Settings
SECRET_KEY=your-secret-key-here-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (SQLite for development)
DATABASE_ENGINE=django.db.backends.sqlite3
DATABASE_NAME=db.sqlite3

# Google OAuth Settings
GOOGLE_OAUTH_CLIENT_ID=your-google-client-id.apps.googleusercontent.com
GOOGLE_OAUTH_CLIENT_SECRET=your-google-client-secret
```

### 5. Generate Secret Key

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output and use it as your `SECRET_KEY` in `.env`.

### 6. Set Up Google OAuth

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable Google+ API
4. Go to Credentials → Create Credentials → OAuth 2.0 Client ID
5. Configure OAuth consent screen
6. Add Authorized redirect URIs:
   - `http://localhost:8000/accounts/google/login/callback/`
   - `http://127.0.0.1:8000/accounts/google/login/callback/`
7. Copy Client ID and Client Secret to your `.env` file

### 7. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Create Superuser

```bash
python manage.py createsuperuser
```

### 9. Create Initial Data (Optional)

Create time slots via Django admin or shell:

```bash
python manage.py shell
```

```python
from bookings.models import TimeSlot, FutsalSettings
from datetime import time

# Create futsal settings
settings = FutsalSettings.load()
settings.futsal_name = "My Futsal Arena"
settings.default_price_per_hour = 1000
settings.save()

# Create time slots
slots = [
    (time(6, 0), time(7, 0), 60),
    (time(7, 0), time(8, 0), 60),
    (time(8, 0), time(9, 0), 60),
    (time(9, 0), time(10, 0), 60),
    (time(10, 0), time(11, 0), 60),
    (time(14, 0), time(15, 0), 60),
    (time(15, 0), time(16, 0), 60),
    (time(16, 0), time(17, 0), 60),
    (time(17, 0), time(18, 0), 60),
    (time(18, 0), time(19, 0), 60),
    (time(19, 0), time(20, 0), 60),
    (time(20, 0), time(21, 0), 60),
]

for start, end, duration in slots:
    TimeSlot.objects.create(
        start_time=start,
        end_time=end,
        duration_minutes=duration,
        is_active=True
    )
```

### 10. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 11. Run Development Server

```bash
python manage.py runserver
```

Visit: `http://localhost:8000`

## Project Structure

```
futsal_booking/
├── bookings/                 # Main app
│   ├── migrations/          # Database migrations
│   ├── admin.py            # Admin configuration
│   ├── apps.py             # App configuration
│   ├── forms.py            # Forms with validation
│   ├── models.py           # Database models
│   ├── urls.py             # URL routing
│   └── views.py            # View logic
├── futsal_project/          # Project settings
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py             # WSGI configuration
│   └── asgi.py             # ASGI configuration
├── templates/               # HTML templates
│   ├── base.html           # Base template
│   ├── account/            # Authentication templates
│   └── bookings/           # Booking templates
├── static/                  # Static files
│   ├── css/                # Stylesheets
│   └── js/                 # JavaScript files
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in git)
├── .env.example           # Example environment file
└── README.md              # This file
```

## Usage

### For Users

1. **Sign In**: Click "Login" and sign in with Google
2. **View Available Slots**: Navigate to "Available Slots" to see open time slots
3. **Create Booking**: Select a date and time, then confirm
4. **Manage Bookings**: View all bookings in "My Bookings"
5. **Cancel Booking**: Cancel up to 24 hours before scheduled time

### For Administrators

1. Access admin panel at `/admin`
2. Manage time slots, bookings, and settings
3. View booking history and audit logs
4. Configure pricing and business rules
5. Monitor system security logs

## Security Best Practices

### For Development
- Keep `.env` file secure and never commit it
- Use `DEBUG=True` only in development
- Use SQLite for development

### For Production
- Set `DEBUG=False`
- Use strong `SECRET_KEY`
- Enable HTTPS and set `SECURE_SSL_REDIRECT=True`
- Use PostgreSQL database
- Set up Redis for caching
- Configure proper `ALLOWED_HOSTS`
- Enable all security headers
- Set up email notifications
- Regular database backups
- Monitor logs for suspicious activity

## Production Deployment

### Environment Variables for Production

```env
DEBUG=False
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# PostgreSQL
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=futsal_db
DATABASE_USER=futsal_user
DATABASE_PASSWORD=strong-password
DATABASE_HOST=localhost
DATABASE_PORT=5432

# Update Google OAuth redirect URIs to production URLs
```

### Deployment Checklist

- [ ] Set `DEBUG=False`
- [ ] Configure production database (PostgreSQL)
- [ ] Set up static file serving (WhiteNoise configured)
- [ ] Configure HTTPS
- [ ] Update Google OAuth redirect URIs
- [ ] Set strong SECRET_KEY
- [ ] Enable all security settings
- [ ] Set up email backend
- [ ] Configure logging
- [ ] Set up backups
- [ ] Monitor error logs

## API Endpoints

- `/` - Home page
- `/accounts/login/` - Login page
- `/accounts/logout/` - Logout
- `/available-slots/` - View available slots
- `/create-booking/` - Create new booking
- `/my-bookings/` - User's bookings
- `/booking/<id>/` - Booking details
- `/booking/<id>/cancel/` - Cancel booking
- `/api/check-availability/` - AJAX endpoint for slot availability
- `/admin/` - Admin panel

## Database Models

### TimeSlot
- Defines available booking time slots
- Configurable duration (60, 90, 120 minutes)
- Can be activated/deactivated

### Booking
- User bookings with status tracking
- Links user, date, and time slot
- Includes pricing and payment status
- Tracks cancellations and IP addresses

### FutsalSettings
- Global configuration
- Pricing settings
- Business rules
- Contact information

### BookingHistory
- Complete audit trail
- Tracks all changes to bookings
- Security logging

## Troubleshooting

### Google OAuth Not Working
- Verify Client ID and Secret in `.env`
- Check authorized redirect URIs in Google Console
- Ensure you're using the correct callback URL

### Database Errors
- Run migrations: `python manage.py migrate`
- Check database configuration in `.env`

### Static Files Not Loading
- Run: `python manage.py collectstatic`
- Check `STATIC_ROOT` and `STATIC_URL` in settings

### Permission Denied Errors
- Check file permissions
- Ensure virtual environment is activated

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support, please contact: info@futsal.com

## Changelog

### Version 1.0.0 (Initial Release)
- Google OAuth authentication
- Booking management system
- Admin panel
- Security features
- Responsive design
- Email notifications
- Rate limiting
- Audit logging
