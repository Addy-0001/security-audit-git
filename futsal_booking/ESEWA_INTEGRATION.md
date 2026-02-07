# eSewa Payment Integration Guide

## Overview

This project now includes full eSewa payment gateway integration for futsal booking payments. The integration is production-ready and includes security features like signature verification, payment verification, and comprehensive logging.

## Features

- **Secure Payment Processing**: HMAC-SHA256 signature generation and verification
- **Transaction Tracking**: All payments are tracked in the database with transaction UUIDs
- **Payment Verification**: Responses from eSewa are verified before updating booking status
- **Automatic Booking Status Updates**: Bookings are automatically marked as confirmed when payment is successful
- **Comprehensive Logging**: All payment operations are logged for audit purposes
- **Admin Interface**: View, track, and manage all payment transactions from Django admin
- **Error Handling**: Graceful error handling with user-friendly messages

## Configuration

The following settings are already configured in `futsal_project/settings.py`:

### Test Environment (UAT)
```python
ESEWA_MERCHANT_CODE = "EPAYTEST"
ESEWA_SECRET_KEY = "8gBm/:&EnhH.1/q"
ESEWA_PAYMENT_URL = "https://uat.esewa.com.np/epay/main"
ESEWA_VERIFICATION_URL = "https://uat.esewa.com.np/epay/transrec"
```

### Production Environment (Uncomment when ready)
```python
ESEWA_PAYMENT_URL = "https://esewa.com.np/epay/main"
ESEWA_VERIFICATION_URL = "https://esewa.com.np/epay/transrec"
```

### Callback URLs
```python
ESEWA_SUCCESS_URL = "http://127.0.0.1:8000/payment/success/"
ESEWA_FAILURE_URL = "http://127.0.0.1:8000/payment/failed/"
ESEWA_CANCEL_URL = "http://127.0.0.1:8000/payment/cancelled/"
```

**⚠️ Important**: Update these URLs in the settings to point to your actual domain in production!

## Database Models

### Payment Model
The `Payment` model tracks all payment transactions:

```python
class Payment(models.Model):
    booking              # ForeignKey to Booking
    amount               # Payment amount
    status               # pending, initiated, completed, failed, cancelled
    transaction_uuid     # Unique transaction identifier
    esewa_transaction_code  # eSewa transaction code
    esewa_refund_code    # For refunds
    product_code         # Always 'BOOKINGFEE'
    signature            # Payment signature
    created_at           # Creation timestamp
    completed_at         # Completion timestamp
    ip_address           # Client IP for tracking
    user_agent           # Client browser info
```

## Payment Flow

### 1. Initiate Payment
- User clicks "Pay Now" button on booking detail page
- Views generate unique transaction UUID
- Payment record is created with 'initiated' status
- User is redirected to eSewa payment gateway

```
URL: /booking/<booking_id>/payment/initiate/
```

### 2. User Pays on eSewa
- User completes payment on eSewa gateway
- eSewa redirects back to your site with payment confirmation

### 3. Payment Success
- System verifies eSewa signature
- Payment amount is verified
- Payment record is updated to 'completed'
- Booking status changes to 'confirmed'
- User is redirected to booking detail page

```
URL: /payment/success/
Parameters: transaction_uuid, signature, total_amount, product_code, oid
```

### 4. Payment Failed/Cancelled
- User is informed of the failure
- Payment record is updated to 'failed' or 'cancelled'
- Booking remains unpaid
- User can retry payment

```
URLs: /payment/failed/ and /payment/cancelled/
```

## API Usage

### ESewaPaymentGateway Class

The `bookings/esewa.py` module provides the `ESewaPaymentGateway` class:

#### Methods

**`generate_signature(total_amount, transaction_uuid, product_code)`**
- Generates HMAC-SHA256 signature for payment
- Returns (signature, encoded_signature)

**`prepare_payment_data(booking, request=None)`**
- Prepares payment parameters for eSewa redirect
- Returns (payment_data, transaction_uuid)

**`verify_payment(transaction_uuid, product_code, total_amount, signature)`**
- Verifies payment signature from eSewa response
- Returns boolean

**`verify_transaction_with_esewa(transaction_uuid)`**
- Optional: Verify transaction with eSewa servers
- Returns eSewa response dict

**`get_payment_url(payment_data)`**
- Generates full eSewa payment URL
- Returns URL string

**`create_payment_record(booking, transaction_uuid, amount, ip_address, user_agent)`**
- Creates Payment record in database
- Returns Payment instance

## Admin Interface

Access payments from Django admin at: `/admin/bookings/payment/`

Features:
- View all payment transactions
- Filter by status, date range, booking
- Search by transaction ID, eSewa code, user email
- Mark payments as completed or failed (for manual interventions)
- View full payment details including signatures
- Track IP addresses and user agents for security

## Security Considerations

1. **Signature Verification**: All incoming payments are verified using HMAC-SHA256
2. **Amount Verification**: Payment amount is verified against booking price
3. **Transaction UUID**: Unique for each payment attempt to prevent duplicates
4. **HTTPS Only**: Always use HTTPS in production (enabled via SECURE_SSL_REDIRECT)
5. **CSRF Protection**: All POST requests are protected by Django's CSRF middleware
6. **Logging**: All payment operations are logged for audit trails
7. **Rate Limiting**: Payment endpoints can be protected with rate limiting if needed

## Testing

### Test with eSewa UAT Environment

The system is pre-configured for testing with eSewa's test environment.

**Test Card Details** (Use eSewa's official test details):
- Use any valid test credentials provided by eSewa
- Test both successful and failed payment scenarios

### Manual Testing Steps

1. Create a booking
2. Click "Pay Now" button
3. You'll be redirected to eSewa test environment
4. Complete the payment flow
5. eSewa redirects back to your success/failure page
6. Check booking status - should update automatically
7. Check Payment record in admin for details

## Logging

All payment operations are logged to:
- Console (INFO level and above)
- `logs/django.log` (WARNING level and above)

Log entries include:
- Signature generation
- Payment data preparation
- Payment verification (success/failure)
- Transaction verification with eSewa
- Payment record creation
- Errors and exceptions

## Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Create Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Update Settings (If Needed)
Update callback URLs in `futsal_project/settings.py` to your domain:
```python
ESEWA_SUCCESS_URL = "https://yourdomain.com/payment/success/"
ESEWA_FAILURE_URL = "https://yourdomain.com/payment/failed/"
ESEWA_CANCEL_URL = "https://yourdomain.com/payment/cancelled/"
```

### 4. For Production
- Change ESEWA_PAYMENT_URL and ESEWA_VERIFICATION_URL to production URLs
- Update ALLOWED_HOSTS with your domain
- Set DEBUG = False
- Ensure SECURE_SSL_REDIRECT = True

## Troubleshooting

### Payment Verification Failed
- Check if signature is correct in Payment model
- Verify amount matches booking price
- Check server time synchronization (important for signature verification)

### Transaction Not Found
- Ensure transaction_uuid is being passed correctly from eSewa
- Check database for Payment record with that UUID
- Check logs for detailed error messages

### eSewa Redirect Not Working
- Verify ESEWA_PAYMENT_URL is correct for test/production
- Check if callback URLs are accessible from internet
- Ensure all payment parameters are properly formatted

### Signature Mismatch
- Verify ESEWA_SECRET_KEY is correct
- Check if merchant code matches
- Ensure amount formatting (2 decimal places)
- Verify transaction_uuid matches

## Future Enhancements

1. **Refund Processing**: Add refund API integration
2. **Webhook Verification**: Add server-side webhook verification
3. **Payment Retry**: Implement automatic retry logic for failed payments
4. **Multiple Payment Methods**: Integrate additional payment gateways
5. **Invoice Generation**: Automatic invoice creation after successful payment
6. **Email Notifications**: Send payment confirmation emails
7. **SMS Notifications**: Send payment status via SMS

## Support & Documentation

For eSewa API documentation, visit:
- [eSewa Developer Portal](https://developer.esewa.com.np)
- [eSewa Integration Guide](https://www.esewa.com.np)

For issues or questions about this integration:
1. Check the logs in `logs/django.log`
2. Review Payment records in Django admin
3. Check the eSewa API documentation
4. Debug using Django's debug toolbar or logging

## File Structure

```
bookings/
├── esewa.py                 # eSewa Payment Gateway Implementation
├── models.py                # Payment Model + existing models
├── views.py                 # Payment Views + existing views
├── urls.py                  # Payment URLs + existing URLs
├── admin.py                 # Payment Admin + existing admins
└── ...other files...

futsal_project/
├── settings.py              # eSewa Configuration
└── ...

templates/
├── bookings/
│   ├── booking_detail.html  # Updated with Pay Now button
│   └── ...other templates...
```

---

**Last Updated**: 2026-02-07
**Version**: 1.0
**Status**: Production Ready
