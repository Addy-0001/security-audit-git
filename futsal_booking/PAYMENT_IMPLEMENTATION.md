# eSewa Payment Integration - Implementation Details

## Architecture Overview

```
User Creates Booking
    ↓
Views: create_booking()
    ├── Creates Booking with status='pending', payment_status='pending'
    └── Redirects to booking_detail
    
User Clicks "Pay Now"
    ↓
Views: initiate_payment()
    ├── Generates unique transaction UUID
    ├── Prepares payment data with signature
    ├── Creates Payment record in database
    └── Redirects to eSewa payment gateway
    
User Pays on eSewa
    ↓
eSewa Payment Gateway
    └── Processes payment & redirects to callback URL
    
eSewa Sends Response
    ↓
Views: payment_success() / payment_failed() / payment_cancelled()
    ├── Verifies signature
    ├── Verifies amount
    ├── Updates Payment record
    ├── Updates Booking status (if successful)
    └── Redirects user to booking detail or my bookings
```

## Code Walkthrough

### 1. Payment Initiation Flow

**User Action**: Click "Pay Now" button
**Template**: `booking_detail.html`
```django
{% if booking.payment_status == 'pending' and booking.status != 'cancelled' %}
<a href="{% url 'initiate_payment' booking.id %}" class="btn btn-success">
    <i class="bi bi-credit-card"></i> Pay Now (NPR {{ booking.price }})
</a>
{% endif %}
```

**View**: `views.py` - `initiate_payment()`
```python
@login_required
def initiate_payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    # Prepare payment
    payment_data, transaction_uuid = esewa_gateway.prepare_payment_data(booking)
    
    # Create payment record
    payment = esewa_gateway.create_payment_record(
        booking=booking,
        transaction_uuid=transaction_uuid,
        amount=booking.price,
        ip_address=get_client_ip(request),
        user_agent=request.META.get('HTTP_USER_AGENT', '')
    )
    
    # Get eSewa payment URL and redirect
    payment_url = esewa_gateway.get_payment_url(payment_data)
    return redirect(payment_url)
```

### 2. Payment Data Preparation

**Module**: `esewa.py`
```python
def prepare_payment_data(self, booking, request=None):
    """
    Flow:
    1. Generate unique transaction UUID
    2. Format amount (e.g., "1000.00")
    3. Create signature using HMAC-SHA256
    4. Prepare all eSewa parameters
    5. Return payment_data dict and transaction_uuid
    """
    
    # Generate UUID
    transaction_uuid = str(uuid.uuid4())
    
    # Format amount
    amount = f"{booking.price:.2f}"  # e.g., "1000.00"
    
    # Generate signature
    signature, encoded_signature = self.generate_signature(
        amount, transaction_uuid, "BOOKINGFEE"
    )
    
    # Prepare eSewa parameters
    payment_data = {
        'amount': amount,
        'failure_url': self.failure_url,
        'product_code': 'BOOKINGFEE',
        'product_service_charge': '0',
        'product_delivery_charge': '0',
        'success_url': self.success_url,
        'tax_amount': '0',
        'total_amount': amount,
        'transaction_uuid': transaction_uuid,
        'signed_field_names': 'total_amount,product_code,transaction_uuid',
        'signature': encoded_signature,
    }
    
    return payment_data, transaction_uuid
```

### 3. Signature Generation

**Security**: HMAC-SHA256 is used to sign payment data
```python
def generate_signature(self, total_amount: str, transaction_uuid: str, product_code: str) -> tuple:
    """
    Steps:
    1. Create message: "total_amount,product_code,transaction_uuid"
    2. Generate HMAC-SHA256 using secret key
    3. Base64 encode the signature
    """
    
    # Message to sign: total_amount,product_code,transaction_uuid
    message = f"{total_amount},{product_code},{transaction_uuid}"
    
    # HMAC-SHA256 signature
    signature = hmac.new(
        self.secret_key.encode('utf-8'),      # Secret key from settings
        message.encode('utf-8'),               # Message to sign
        hashlib.sha256
    ).digest()
    
    # Base64 encode
    encoded_signature = base64.b64encode(signature).decode('utf-8')
    
    return signature, encoded_signature
```

**Example**:
```
Secret Key: "8gBm/:&EnhH.1/q"
Amount: "1000.00"
Product Code: "BOOKINGFEE"
Transaction UUID: "550e8400-e29b-41d4-a716-446655440000"

Message: "1000.00,BOOKINGFEE,550e8400-e29b-41d4-a716-446655440000"

HMAC-SHA256 = [binary hash]
Base64 = "abc123def456..." (Base64 encoded hash)
```

### 4. Payment Success Handler

**URL**: `/payment/success/?transaction_uuid=...&signature=...&total_amount=...`

**View**: `views.py` - `payment_success()`
```python
@login_required
def payment_success(request):
    """
    Called by eSewa after successful payment
    
    Steps:
    1. Get parameters from eSewa response
    2. Verify signature
    3. Verify amount
    4. Update Payment record to 'completed'
    5. Update Booking status to 'confirmed'
    6. Create audit log entry
    7. Redirect user
    """
    
    # 1. Get eSewa response parameters
    transaction_uuid = request.GET.get('transaction_uuid')
    signature = request.GET.get('signature')
    total_amount = request.GET.get('total_amount')
    esewa_transaction_code = request.GET.get('oid')  # eSewa code
    
    # 2. Verify signature
    if not esewa_gateway.verify_payment(
        transaction_uuid, 
        product_code, 
        total_amount, 
        signature
    ):
        messages.error(request, 'Payment verification failed.')
        return redirect('my_bookings')
    
    # 3. Get and verify payment record
    payment = Payment.objects.get(transaction_uuid=transaction_uuid)
    
    # 4. Verify amount matches
    if Decimal(total_amount) != payment.amount:
        messages.error(request, 'Payment amount mismatch.')
        return redirect('my_bookings')
    
    # 5. Mark payment as completed
    payment.mark_completed(
        esewa_code=esewa_transaction_code,
        signature=signature
    )
    
    # 6. Booking status automatically updated via Payment.mark_completed()
    # Booking.status = 'confirmed'
    # Booking.payment_status = 'paid'
    
    # 7. Create audit log
    BookingHistory.objects.create(
        booking=payment.booking,
        action='payment_completed',
        changes={'transaction_id': transaction_uuid}
    )
    
    messages.success(request, 'Payment successful! Your booking is confirmed.')
    return redirect('booking_detail', booking_id=payment.booking.id)
```

### 5. Payment Model Updates

**Model**: `models.py` - `Payment`
```python
def mark_completed(self, esewa_code=None, signature=None):
    """Update payment as completed and confirm booking"""
    
    # Update payment record
    self.status = 'completed'
    self.completed_at = timezone.now()
    self.esewa_transaction_code = esewa_code
    self.signature = signature
    self.save()
    
    # Update booking status
    self.booking.payment_status = 'paid'
    self.booking.status = 'confirmed'
    self.booking.save()
```

## Data Flow Example

### Complete Payment Flow with Data

```
STEP 1: User Creates Booking
  - Enters booking_date, time_slot, contact_number
  - System generates:
    - Booking ID: 123e4567-e89b-12d3-a456-426614174000
    - Status: pending
    - Payment Status: pending
    - Price: 1000.00

STEP 2: User Clicks "Pay Now"
  - System generates:
    - Transaction UUID: 550e8400-e29b-41d4-a716-446655440000
    - Creates Payment record:
      * amount: 1000.00
      * status: initiated
      * transaction_uuid: 550e8400-e29b-41d4-a716-446655440000
    - Generates signature:
      * Message: "1000.00,BOOKINGFEE,550e8400-e29b-41d4-a716-446655440000"
      * Signature: "base64encodedhmac..."
    - User redirected to eSewa with all data

STEP 3: User Pays on eSewa
  - User completes payment on eSewa gateway
  - eSewa receives payment confirmation from bank

STEP 4: eSewa Redirects Back
  - URL: http://yoursite.com/payment/success/
  - Parameters:
    * transaction_uuid: 550e8400-e29b-41d4-a716-446655440000
    * total_amount: 1000.00
    * product_code: BOOKINGFEE
    * signature: [eSewa's signature]
    * oid: [eSewa's transaction code]

STEP 5: System Verifies Payment
  - Retrieves Payment record using transaction_uuid
  - Regenerates signature with same message
  - Compares with eSewa's signature
  - ✓ If signatures match: Continue
  - ✗ If signatures don't match: Reject payment

STEP 6: System Updates Records
  - Payment.status = 'completed'
  - Payment.completed_at = now()
  - Payment.esewa_transaction_code = oid
  - Booking.status = 'confirmed'
  - Booking.payment_status = 'paid'
  - BookingHistory.create(action='payment_completed')

STEP 7: User Confirmation
  - Success message shown
  - Redirected to booking detail
  - Booking shows as "Confirmed"
  - Payment shows as "Paid"
```

## Database State Changes

### Before Payment
```
Booking
├── id: 123e4567-e89b-12d3-a456-426614174000
├── user: john@example.com
├── booking_date: 2026-02-20
├── time_slot: 6:00 PM - 7:00 PM
├── status: pending
├── payment_status: pending
├── price: 1000.00
└── created_at: 2026-02-07 10:00:00

Payment
└── (Not yet created)
```

### After Payment Initiation
```
Booking (unchanged)
├── status: pending
├── payment_status: pending
└── ...

Payment (created)
├── id: 987f6543-e89b-12d3-a456-426614174999
├── booking_id: 123e4567-e89b-12d3-a456-426614174000
├── amount: 1000.00
├── status: initiated
├── transaction_uuid: 550e8400-e29b-41d4-a716-446655440000
├── created_at: 2026-02-07 10:05:00
└── completed_at: NULL
```

### After Successful Payment
```
Booking (updated)
├── id: 123e4567-e89b-12d3-a456-426614174000
├── status: confirmed ← CHANGED
├── payment_status: paid ← CHANGED
└── ...

Payment (updated)
├── id: 987f6543-e89b-12d3-a456-426614174999
├── status: completed ← CHANGED
├── esewa_transaction_code: "300000123456" ← ADDED
├── completed_at: 2026-02-07 10:07:00 ← ADDED
└── ...

BookingHistory (new record)
├── booking: 123e4567-e89b-12d3-a456-426614174000
├── action: payment_completed
├── changed_at: 2026-02-07 10:07:00
└── changes: {'transaction_id': '550e8400-e29b-41d4-a716-446655440000'}
```

## Security Mechanisms

### 1. Signature Verification
- Each payment is signed with HMAC-SHA256
- Client can't modify amount without invalidating signature
- Server regenerates signature and compares
- Only valid signatures are accepted

### 2. Amount Verification
- After signature verification, amount is checked again
- System amount must match eSewa amount exactly
- Prevents amount tampering

### 3. Transaction UUID
- Each payment attempt gets unique UUID
- Prevents duplicate payments
- Enables tracking and audit trails

### 4. Database Constraints
- Unique constraint on transaction_uuid
- Foreign key link to Booking
- All payment operations logged in BookingHistory
- IP address and user agent recorded

### 5. HTTPS/TLS
- All eSewa communication over HTTPS
- Callback URLs use HTTPS in production
- Certificates verified before connection

## Error Handling

### Signature Verification Failure
```python
if not esewa_gateway.verify_payment(...):
    # Log error
    logger.error("Payment signature verification failed")
    
    # Notify user
    messages.error(request, 'Payment verification failed. Please contact support.')
    
    # Update payment status
    payment.mark_failed()
    
    # Redirect
    return redirect('my_bookings')
```

### Amount Mismatch
```python
if Decimal(total_amount) != payment.amount:
    # Log error
    logger.error("Amount mismatch")
    
    # Notify user
    messages.error(request, 'Payment amount mismatch')
    
    # Don't mark as completed, keep as pending
    return redirect('my_bookings')
```

### Missing Payment Record
```python
try:
    payment = Payment.objects.get(transaction_uuid=transaction_uuid)
except Payment.DoesNotExist:
    logger.error(f"Payment not found: {transaction_uuid}")
    messages.error(request, 'Payment record not found')
    return redirect('my_bookings')
```

## Logging Examples

```python
# Signature generation
logger.info(f"Signature generated for transaction {transaction_uuid}")

# Payment initiation
logger.info(f"Initiating payment for booking {booking_id}, transaction {transaction_uuid}")

# Payment verification
logger.info(f"Payment signature verified for transaction {transaction_uuid}")
logger.warning(f"Payment signature verification failed for transaction {transaction_uuid}")

# Payment completed
logger.info(f"Payment successful for booking {booking.id}, transaction {transaction_uuid}")

# Payment failed
logger.warning(f"Payment failed for transaction {transaction_uuid}")
logger.error(f"Payment record not found for transaction {transaction_uuid}")
```

## Testing Checklist

- [ ] Generate signature correctly with test credentials
- [ ] Verify signature with same credentials
- [ ] Payment record created with correct initial status
- [ ] Redirect to eSewa with correct URL and parameters
- [ ] eSewa callback URL receives correct parameters
- [ ] Signature verification works for valid signatures
- [ ] Signature verification fails for tampered signatures
- [ ] Amount verification works correctly
- [ ] Booking status updates on successful payment
- [ ] Payment record updated with completion timestamp
- [ ] BookingHistory entry created for payment
- [ ] Failed payment handled gracefully
- [ ] Cancelled payment handled gracefully
- [ ] User messages are clear and helpful
- [ ] Admin can view all payment records
- [ ] Payment filtering works in admin
- [ ] Payment search works in admin

---

**Version**: 1.0  
**Last Updated**: 2026-02-07
