# Deployment Guide for Futsal Booking System

This guide covers deploying the Futsal Booking System to production.

## Pre-Deployment Checklist

- [ ] Domain name registered and configured
- [ ] SSL certificate obtained
- [ ] Server provisioned (minimum: 1GB RAM, 1 CPU)
- [ ] PostgreSQL database set up
- [ ] Redis installed (optional but recommended)
- [ ] Google OAuth credentials configured for production domain
- [ ] Email service configured (Gmail, SendGrid, etc.)

## Server Requirements

### Minimum Requirements
- Ubuntu 20.04 LTS or higher
- Python 3.10+
- PostgreSQL 12+
- Nginx
- Supervisor (for process management)
- 1GB RAM
- 10GB Storage

### Recommended Requirements
- Ubuntu 22.04 LTS
- Python 3.11+
- PostgreSQL 14+
- Redis 6+
- Nginx
- 2GB RAM
- 20GB Storage

## Deployment Steps

### 1. Server Setup

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y python3-pip python3-venv python3-dev
sudo apt install -y postgresql postgresql-contrib
sudo apt install -y nginx supervisor
sudo apt install -y redis-server  # Optional

# Install build tools
sudo apt install -y build-essential libpq-dev
```

### 2. PostgreSQL Setup

```bash
# Switch to postgres user
sudo -u postgres psql

# In PostgreSQL shell:
CREATE DATABASE futsal_booking;
CREATE USER futsal_user WITH PASSWORD 'your_strong_password';
ALTER ROLE futsal_user SET client_encoding TO 'utf8';
ALTER ROLE futsal_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE futsal_user SET timezone TO 'Asia/Kathmandu';
GRANT ALL PRIVILEGES ON DATABASE futsal_booking TO futsal_user;
\q
```

### 3. Application Setup

```bash
# Create application user
sudo useradd -m -s /bin/bash futsal
sudo su - futsal

# Clone repository
cd /home/futsal
git clone <your-repo-url> futsal_booking
cd futsal_booking

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install gunicorn psycopg2-binary
```

### 4. Environment Configuration

Create production `.env` file:

```bash
nano /home/futsal/futsal_booking/.env
```

Add production settings:

```env
# Django Settings
SECRET_KEY=<generate-new-secret-key>
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=futsal_booking
DATABASE_USER=futsal_user
DATABASE_PASSWORD=your_strong_password
DATABASE_HOST=localhost
DATABASE_PORT=5432

# Google OAuth
GOOGLE_OAUTH_CLIENT_ID=your-production-client-id
GOOGLE_OAUTH_CLIENT_SECRET=your-production-client-secret

# Email
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Security
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True

# Redis
REDIS_URL=redis://localhost:6379/0

# Site
SITE_URL=https://yourdomain.com
```

### 5. Django Setup

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

# Create logs directory
mkdir -p /home/futsal/futsal_booking/logs
```

### 6. Gunicorn Configuration

Create Gunicorn service file:

```bash
sudo nano /etc/systemd/system/futsal.service
```

Add:

```ini
[Unit]
Description=Futsal Booking Gunicorn daemon
After=network.target

[Service]
User=futsal
Group=www-data
WorkingDirectory=/home/futsal/futsal_booking
Environment="PATH=/home/futsal/futsal_booking/venv/bin"
ExecStart=/home/futsal/futsal_booking/venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/home/futsal/futsal_booking/futsal.sock \
    --timeout 120 \
    --access-logfile /home/futsal/futsal_booking/logs/gunicorn-access.log \
    --error-logfile /home/futsal/futsal_booking/logs/gunicorn-error.log \
    futsal_project.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start Gunicorn:

```bash
sudo systemctl start futsal
sudo systemctl enable futsal
sudo systemctl status futsal
```

### 7. Nginx Configuration

```bash
sudo nano /etc/nginx/sites-available/futsal
```

Add:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    
    # Redirect HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    # SSL Configuration
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    client_max_body_size 10M;

    # Security headers
    add_header X-Frame-Options "DENY" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;

    location = /favicon.ico {
        access_log off;
        log_not_found off;
    }

    location /static/ {
        alias /home/futsal/futsal_booking/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location /media/ {
        alias /home/futsal/futsal_booking/media/;
        expires 7d;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/futsal/futsal_booking/futsal.sock;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_redirect off;
    }

    access_log /var/log/nginx/futsal-access.log;
    error_log /var/log/nginx/futsal-error.log;
}
```

Enable site:

```bash
sudo ln -s /etc/nginx/sites-available/futsal /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 8. SSL Certificate (Let's Encrypt)

```bash
# Install Certbot
sudo apt install -y certbot python3-certbot-nginx

# Obtain certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Auto-renewal is set up automatically
# Test renewal:
sudo certbot renew --dry-run
```

### 9. Firewall Configuration

```bash
# Enable UFW
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
sudo ufw status
```

### 10. Monitoring and Logging

Set up log rotation:

```bash
sudo nano /etc/logrotate.d/futsal
```

Add:

```
/home/futsal/futsal_booking/logs/*.log {
    daily
    missingok
    rotate 14
    compress
    delaycompress
    notifempty
    create 0640 futsal www-data
    sharedscripts
    postrotate
        systemctl reload futsal > /dev/null
    endscript
}
```

## Post-Deployment Tasks

### 1. Update Google OAuth

1. Go to Google Cloud Console
2. Add production URLs to authorized redirect URIs:
   - `https://yourdomain.com/accounts/google/login/callback/`

### 2. Create Initial Time Slots

Access Django shell:

```bash
python manage.py shell
```

Run initial data script (from README.md)

### 3. Test Booking Flow

1. Sign in with Google
2. Create a test booking
3. View booking details
4. Cancel booking
5. Check admin panel

### 4. Set Up Backups

Create backup script:

```bash
sudo nano /home/futsal/backup.sh
```

Add:

```bash
#!/bin/bash
BACKUP_DIR="/home/futsal/backups"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p $BACKUP_DIR

# Database backup
pg_dump futsal_booking > $BACKUP_DIR/db_$DATE.sql

# Application backup
tar -czf $BACKUP_DIR/app_$DATE.tar.gz -C /home/futsal futsal_booking

# Keep only last 7 days
find $BACKUP_DIR -type f -mtime +7 -delete
```

Make executable and add to cron:

```bash
chmod +x /home/futsal/backup.sh
crontab -e
```

Add daily backup at 2 AM:

```
0 2 * * * /home/futsal/backup.sh
```

## Maintenance

### Updating Application

```bash
# As futsal user
cd /home/futsal/futsal_booking
source venv/bin/activate

# Pull latest changes
git pull origin main

# Install new dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Restart Gunicorn
sudo systemctl restart futsal
```

### Monitoring

Check application status:

```bash
# Gunicorn status
sudo systemctl status futsal

# Nginx status
sudo systemctl status nginx

# View logs
tail -f /home/futsal/futsal_booking/logs/gunicorn-error.log
tail -f /var/log/nginx/futsal-error.log
```

### Database Maintenance

```bash
# Vacuum database
sudo -u postgres psql futsal_booking -c "VACUUM ANALYZE;"

# Check database size
sudo -u postgres psql futsal_booking -c "SELECT pg_size_pretty(pg_database_size('futsal_booking'));"
```

## Troubleshooting

### Common Issues

1. **502 Bad Gateway**
   - Check Gunicorn is running: `sudo systemctl status futsal`
   - Check socket permissions
   - View error logs

2. **Static files not loading**
   - Run `python manage.py collectstatic`
   - Check Nginx configuration
   - Verify file permissions

3. **Database connection errors**
   - Verify PostgreSQL is running
   - Check database credentials in `.env`
   - Test connection: `psql -U futsal_user -d futsal_booking`

4. **Google OAuth not working**
   - Verify redirect URIs in Google Console
   - Check HTTPS is properly configured
   - Clear browser cookies

## Security Checklist

- [ ] DEBUG=False in production
- [ ] Strong SECRET_KEY
- [ ] HTTPS enabled
- [ ] Firewall configured
- [ ] Regular backups scheduled
- [ ] Log monitoring set up
- [ ] Database password is strong
- [ ] Server kept updated
- [ ] Google OAuth credentials secure
- [ ] Email credentials secure

## Performance Optimization

1. **Enable Redis caching** (configured in settings.py)
2. **Database indexing** (already configured in models)
3. **CDN for static files** (optional)
4. **Database connection pooling** (pgBouncer)
5. **Monitor query performance**

## Support

For deployment issues, contact: support@yourdomain.com
