"""
eSewa Payment Gateway Integration – Testing Ready (2026)

Handles payment initiation, form data preparation,
server-to-server verification, and logging.
Uses eSewa sandbox / testing environment.
"""

import hashlib
import hmac
import base64
import requests
import logging
import uuid
from decimal import Decimal
from django.conf import settings
from django.utils import timezone

logger = logging.getLogger(__name__)


class ESewaPaymentGateway:
    """
    eSewa Payment Gateway handler for testing environment.
    Implements the classic form POST + server verification flow.
    """

    def __init__(self):
        self.merchant_code = settings.ESEWA_MERCHANT_CODE
        self.secret_key = settings.ESEWA_SECRET_KEY
        self.payment_url = settings.ESEWA_PAYMENT_URL
        self.verification_url = settings.ESEWA_VERIFICATION_URL
        self.success_url = settings.ESEWA_SUCCESS_URL
        self.failure_url = settings.ESEWA_FAILURE_URL
        self.cancel_url = settings.ESEWA_CANCEL_URL

        logger.info(
            f"eSewa Gateway initialized with merchant: {self.merchant_code}")

    def get_payment_form_data(self, amount: Decimal, booking_id: str) -> dict:
        """
        Prepare the POST parameters for the eSewa payment form.
        Returns a dict ready to be rendered as hidden inputs.
        """
        amount_str = str(float(amount))  # eSewa expects string/float format

        params = {
            'amt': amount_str,
            'txAmt': '0',
            'psc': '0',
            'pdc': '0',
            'tAmt': amount_str,
            'pid': str(booking_id),             # Use booking ID as product ID
            'scd': self.merchant_code,
            'su': self.success_url,
            'fu': self.failure_url,
            # Optional fields (can be added if needed)
            # 'pid': str(booking_id),           # already set
            # 'txAmt': '0',                     # tax
            # 'psc': '0',                       # service charge
        }

        logger.debug(
            f"Prepared eSewa form data for booking {booking_id}: {params}")
        return params

    def verify_payment(self, ref_id: str, amount: str, order_id: str) -> bool:
        """
        Verify transaction using eSewa v2 status endpoint (GET request)
        """
        try:
            params = {
                'product_code': self.merchant_code,
                'total_amount': amount,
                'transaction_uuid': order_id,  # or ref_id — test shows transaction_uuid is primary
            }

            logger.info(f"Verifying eSewa payment (v2): {params}")

            response = requests.get(
                self.verification_url,
                params=params,
                timeout=15
            )

            if response.status_code == 200:
                try:
                    data = response.json()
                    if data.get('status') == 'COMPLETE' or 'success' in str(data).lower():
                        logger.info(f"v2 Verification SUCCESS: {data}")
                        return True
                except ValueError:
                    # Fallback for non-JSON responses (rare)
                    if 'COMPLETE' in response.text or 'Success' in response.text:
                        logger.info(
                            f"v2 Verification SUCCESS (text fallback): {response.text}")
                        return True

            logger.warning(
                f"v2 Verification FAILED: status={response.status_code}, body={response.text}")
            return False

        except requests.RequestException as e:
            logger.error(f"eSewa v2 network error: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Unexpected v2 verification error: {str(e)}")
            return False


# Global singleton instance (used in views)
esewa_gateway = ESewaPaymentGateway()
