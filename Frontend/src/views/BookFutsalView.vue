<template>
    <div class="booking-page">
        <!-- Header Section -->
        <div class="page-header">
            <div class="container">
                <h1 class="page-title">Confirm Your Booking</h1>
                <p class="page-description">Review and confirm your booking for {{ futsal.futsal_name }}</p>
            </div>
        </div>

        <div class="container">
            <div class="booking-container">
                <!-- Booking Summary Section -->
                <div class="booking-summary-section">
                    <div class="booking-summary-card">
                        <h2 class="summary-title">Booking Summary</h2>

                        <div class="futsal-summary" v-if="!isLoading">
                            <img :src="futsal.futsal_image_1 || '/placeholder.jpg'" :alt="futsal.futsal_name"
                                class="futsal-image">
                            <div class="futsal-info">
                                <h3 class="futsal-name">{{ futsal.futsal_name }}</h3>
                                <div class="futsal-location">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="location-icon" width="16" height="16"
                                        viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                        stroke-linecap="round" stroke-linejoin="round">
                                        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                                        <circle cx="12" cy="10" r="3"></circle>
                                    </svg>
                                    {{ futsal.location }}
                                </div>
                            </div>
                        </div>

                        <div class="booking-details" v-if="!isLoading">
                            <div class="detail-item">
                                <span class="detail-label">Date:</span>
                                <span class="detail-value">{{ formatDate(bookingDate) }}</span>
                            </div>
                            <div class="detail-item">
                                <span class="detail-label">Time:</span>
                                <span class="detail-value">{{ bookingTime }}</span>
                            </div>
                            <div class="detail-item">
                                <span class="detail-label">Duration:</span>
                                <span class="detail-value">1 hour</span>
                            </div>
                            <div class="detail-item">
                                <span class="detail-label">Court Type:</span>
                                <span class="detail-value">{{ futsal.a_side }}-a-side</span>
                            </div>
                        </div>

                        <div class="price-breakdown" v-if="!isLoading">
                            <h3 class="breakdown-title">Price</h3>
                            <div class="breakdown-item">
                                <span class="breakdown-label">Court Rental (1 hour)</span>
                                <span class="breakdown-value">Rs. {{ formatPrice(futsal.price_per_hour) }}</span>
                            </div>
                            <div class="breakdown-total">
                                <span class="total-label">Total</span>
                                <span class="total-value">Rs. {{ formatPrice(futsal.price_per_hour) }}</span>
                            </div>
                        </div>

                        <div class="terms-agreement">
                            <input type="checkbox" id="terms" v-model="termsAgreed" required>
                            <label for="terms">
                                I agree to the <RouterLink to="/terms">Terms and Conditions</RouterLink> and <RouterLink
                                    to="/privacy-policy">Privacy Policy</RouterLink>
                            </label>
                        </div>

                        <button class="submit-booking-btn" @click="submitBooking"
                            :disabled="!termsAgreed || isSubmitting || isLoading">
                            {{ isSubmitting ? 'Booking...' : 'Confirm Booking' }}
                        </button>

                        <div class="need-help">
                            <h3 class="help-title">Need Help?</h3>
                            <p class="help-text">Contact us at <a href="tel:+9779767649598">+977 9841234567</a> or <a
                                    href="mailto:support@booksall.app">support@booksall.app</a></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Booking Success Modal -->
        <div v-if="bookingSuccessModal" class="modal-overlay">
            <div class="success-modal">
                <div class="success-icon-container">
                    <svg xmlns="http://www.w3.org/2000/svg" class="success-icon" width="32" height="32"
                        viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                        stroke-linejoin="round">
                        <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                        <polyline points="22 4 12 14.01 9 11.01"></polyline>
                    </svg>
                </div>
                <h3>Booking Confirmed!</h3>
                <p>Your futsal court has been successfully booked.</p>
                <p class="booking-details-text">
                    <strong>{{ futsal.futsal_name }}</strong><br>
                    Date: {{ formatDate(bookingDate) }}<br>
                    Time: {{ bookingTime }}<br>
                    Duration: 1 hour
                </p>
                <div class="success-buttons">
                    <router-link to="/bookings" class="view-bookings-btn">
                        View My Bookings
                    </router-link>
                    <router-link to="/" class="close-success-btn">
                        Back to Home
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';
import { RouterLink, useRoute, useRouter } from 'vue-router';
import apiClient from '@/axios';

// Router and Route
const route = useRoute();
const router = useRouter();

// State
const bookingDate = ref('');
const bookingTime = ref('');
const bookingSuccessModal = ref(false);
const futsalId = ref('');
const isLoading = ref(true);
const isSubmitting = ref(false);
const termsAgreed = ref(false);
const userId = ref(null);
const futsal = ref({});

// Computed properties
const totalPrice = computed(() => {
    return parseFloat(futsal.value.price_per_hour || 0);
});

// Methods
const formatDate = (dateString) => {
    if (!dateString) return '';
    const [year, month, day] = dateString.split('-').map(Number);
    const date = new Date(year, month - 1, day, 12, 0, 0);
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    return date.toLocaleDateString(undefined, options);
};

const formatPrice = (price) => {
    return parseFloat(price).toLocaleString();
};

const fetchUserData = async () => {
    try {
        const response = await apiClient.get('auth/user/');
        userId.value = response.data.pk || response.data.id; // Use 'pk' or 'id' based on your API response
    } catch (error) {
        console.error('Error fetching user data:', error);
        router.push('/login'); // Redirect to login if user not authenticated
    }
};

const fetchFutsalData = async (id) => {
    try {
        isLoading.value = true;
        const response = await apiClient.get(`futsal/retrieve-futsal/${id}/`);
        futsal.value = response.data;
    } catch (error) {
        console.error('Error fetching futsal data:', error);
        futsal.value = {};
    } finally {
        isLoading.value = false;
    }
};

const checkExistingBooking = async () => {
    try {
        const [startHour] = bookingTime.value.split('-');
        const startTime = `${startHour.padStart(2, '0')}:00:00`;
        const endTime = `${(parseInt(startHour) + 1).toString().padStart(2, '0')}:00:00`;

        const response = await apiClient.get(`booking/list-bookings/${futsalId.value}`);
        const bookings = response.data;

        const existingBooking = bookings.find(booking =>
            booking.booking_date === bookingDate.value &&
            booking.booking_start_time === startTime &&
            booking.booking_end_time === endTime
        );

        if (existingBooking) {
            alert('This time slot is already booked. Please choose a different time.');
            router.push(`/futsals/${futsalId.value}`);
            return false;
        }
        return true;
    } catch (error) {
        console.error('Error checking existing bookings:', error);
        return false;
    }
};

const submitBooking = async () => {
    if (!termsAgreed.value) {
        alert('Please agree to the terms and conditions');
        return;
    }

    if (!userId.value) {
        alert('You must be logged in to book a slot.');
        router.push('/login');
        return;
    }

    isSubmitting.value = true;

    const [startHour] = bookingTime.value.split('-');
    const startTime = `${startHour.padStart(2, '0')}:00:00`;
    const endTime = `${(parseInt(startHour) + 1).toString().padStart(2, '0')}:00:00`;

    const bookingData = {
        booking_date: bookingDate.value,
        booking_start_time: startTime,
        booking_end_time: endTime,
        booking_status: false, // Initially pending
        futsal: futsalId.value,
        user: userId.value // Use the authenticated user's ID
    };

    try {
        // Check if slot is still available
        const isAvailable = await checkExistingBooking();
        if (!isAvailable) {
            isSubmitting.value = false;
            return;
        }

        // Create booking
        await apiClient.post('booking/create-booking/', bookingData);
        bookingSuccessModal.value = true;
    } catch (error) {
        console.error('Error creating booking:', error);
        alert('Failed to create booking. Please try again.');
    } finally {
        isSubmitting.value = false;
    }
};

// Watch for route changes to update booking details
watch(() => route.query, (newQuery) => {
    if (newQuery.date) bookingDate.value = newQuery.date;
    if (newQuery.time) bookingTime.value = newQuery.time;
}, { immediate: true });

onMounted(async () => {
    futsalId.value = route.params.id;

    if (!futsalId.value || !route.query.date || !route.query.time) {
        console.warn('Missing required parameters');
        router.push('/');
        return;
    }

    await Promise.all([
        fetchUserData(),
        fetchFutsalData(futsalId.value)
    ]);

    if (!bookingDate.value || !bookingTime.value) {
        router.push(`/futsals/${futsalId.value}`);
    }
});
</script>

<style scoped>
/* Booking Page Styles */
.booking-page {
    min-height: 100vh;
    background-color: #f8f9fa;
}

/* Page Header */
.page-header {
    background-color: #16a34a;
    color: white;
    padding: 2rem 0;
    margin-bottom: 2rem;
}

.page-title {
    font-size: 2rem;
    margin-bottom: 0.5rem;
    color: white;
}

.page-description {
    font-size: 1.125rem;
    opacity: 0.9;
}

/* Container */
.container {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

/* Booking Container */
.booking-container {
    display: flex;
    flex-direction: column;
    gap: 2rem;
    margin-bottom: 3rem;
    justify-content: center;
}

/* Booking Summary Section */
.booking-summary-section {
    max-width: 600px;
    margin: 0 auto;
    width: 100%;
}

.booking-summary-card {
    background-color: white;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    padding: 2rem;
}

.summary-title {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
    color: #2e7d32;
}

/* Futsal Summary */
.futsal-summary {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid #e0e0e0;
}

.futsal-image {
    width: 80px;
    height: 80px;
    border-radius: 8px;
    object-fit: cover;
}

.futsal-info {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
}

.futsal-name {
    font-size: 1.25rem;
    font-weight: 600;
    margin: 0;
    color: #333;
}

.futsal-location {
    display: flex;
    align-items: center;
    gap: 0.25rem;
    color: #666;
    font-size: 0.875rem;
}

.location-icon {
    color: #16a34a;
}

/* Booking Details */
.booking-details {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    margin-bottom: 1.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid #e0e0e0;
}

.detail-item {
    display: flex;
    justify-content: space-between;
}

.detail-label {
    color: #666;
}

.detail-value {
    font-weight: 500;
    color: #333;
}

/* Price Breakdown */
.price-breakdown {
    margin-bottom: 1.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid #e0e0e0;
}

.breakdown-title {
    font-size: 1.125rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: #2e7d32;
}

.breakdown-item {
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.5rem;
}

.breakdown-label {
    color: #666;
}

.breakdown-value {
    color: #333;
}

.breakdown-total {
    display: flex;
    justify-content: space-between;
    padding-top: 0.75rem;
    margin-top: 0.75rem;
    border-top: 1px dashed #e0e0e0;
    font-weight: 700;
}

.total-label {
    color: #333;
}

.total-value {
    color: #16a34a;
    font-size: 1.125rem;
}

/* Terms Agreement */
.terms-agreement {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    gap: 20px;
    margin-bottom: 1.5rem;
}

.terms-agreement input[type="checkbox"] {
    margin-top: 0.25rem;
    max-width: 20px;
    accent-color: #16a34a;
}

.terms-agreement label {
    font-size: 0.875rem;
    color: #666;
}

.terms-agreement a {
    color: #16a34a;
    text-decoration: none;
}

/* Submit Button */
.submit-booking-btn {
    padding: 1rem;
    margin-bottom: 30px;
    background-color: #16a34a;
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.2s;
    width: 100%;
}

.submit-booking-btn:hover:not(:disabled) {
    background-color: #15803d;
}

.submit-booking-btn:disabled {
    background-color: #9e9e9e;
    cursor: not-allowed;
}

/* Cancellation Policy */
.cancellation-policy {
    margin-bottom: 1.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid #e0e0e0;
}

.policy-title {
    font-size: 1.125rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: #2e7d32;
}

.policy-text {
    font-size: 0.875rem;
    color: #666;
    line-height: 1.5;
}

/* Need Help */
.need-help {
    text-align: center;
}

.help-title {
    font-size: 1.125rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: #2e7d32;
}

.help-text {
    font-size: 0.875rem;
    color: #666;
}

.help-text a {
    color: #16a34a;
    text-decoration: none;
}

/* Success Modal */
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 100;
}

.success-modal {
    background-color: white;
    border-radius: 12px;
    padding: 2rem;
    text-align: center;
    width: 90%;
    max-width: 500px;
}

.success-icon-container {
    width: 4rem;
    height: 4rem;
    background-color: #e8f5e9;
    border-radius: 9999px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1.5rem;
}

.success-icon {
    color: #16a34a;
}

.booking-details-text {
    margin: 1.5rem 0;
    line-height: 1.6;
}

.success-buttons {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
}

.view-bookings-btn {
    padding: 0.875rem 1.5rem;
    background-color: #16a34a;
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.2s;
    text-decoration: none;
    display: block;
}

.view-bookings-btn:hover {
    background-color: #15803d;
}

.close-success-btn {
    padding: 0.875rem 1.5rem;
    background-color: #f3f4f6;
    color: #4b5563;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    font-weight: 500;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.2s;
    text-decoration: none;
    display: block;
}

.close-success-btn:hover {
    background-color: #e5e7eb;
}

/* Media Queries */
@media (min-width: 768px) {
    .success-buttons {
        flex-direction: row;
        justify-content: center;
        gap: 1rem;
    }
}
</style>