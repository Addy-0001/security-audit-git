<template>
    <div class="futsal-detail-page" :class="{ 'loading': isLoading }">
        <!-- Loading Overlay -->
        <transition name="fade">
            <div v-if="isLoading" class="loading-overlay">
                <div class="loading-spinner"></div>
                <p>Loading Futsal Details...</p>
            </div>
        </transition>

        <!-- Hero Section with Carousel -->
        <section class="hero-section">
            <div class="carousel-container">
                <div class="carousel-slides" :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
                    <div v-for="(image, index) in futsalImages" :key="index" class="carousel-slide">
                        <img :src="image || '/placeholder.jpg'" :alt="`${futsal.futsal_name} - image ${index + 1}`"
                            class="carousel-image">
                    </div>
                </div>

                <div class="carousel-overlay">
                    <h1 class="futsal-name" style="color: #86efac;">{{ futsal.futsal_name }}</h1>
                    <div class="futsal-location">
                        <svg xmlns="http://www.w3.org/2000/svg" class="location-icon" viewBox="0 0 24 24" fill="none"
                            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                            <circle cx="12" cy="10" r="3"></circle>
                        </svg>
                        {{ futsal.location }}
                    </div>
                </div>

                <button class="carousel-control prev" @click="prevSlide" v-if="futsalImages.length > 1">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <polyline points="15 18 9 12 15 6"></polyline>
                    </svg>
                </button>

                <button class="carousel-control next" @click="nextSlide" v-if="futsalImages.length > 1">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <polyline points="9 18 15 12 9 6"></polyline>
                    </svg>
                </button>

                <div class="carousel-indicators" v-if="futsalImages.length > 1">
                    <button v-for="(image, index) in futsalImages" :key="index"
                        :class="['carousel-indicator', { active: currentSlide === index }]"
                        @click="goToSlide(index)"></button>
                </div>
            </div>
        </section>

        <div class="content-container">
            <!-- Booking Section (Left Side) -->
            <div class="booking-section">
                <div class="booking-card">
                    <div class="card-header">
                        <h2>Book Your Slot</h2>
                        <div class="price-tag">
                            <span class="price-amount">NRs. {{ formatPrice(futsal.price_per_hour) }}</span>
                            <span class="price-unit">/hour</span>
                        </div>
                    </div>

                    <!-- Date Selection -->
                    <div class="date-selection">
                        <label for="booking-date">Select Date:</label>
                        <div class="date-input-wrapper">
                            <svg xmlns="http://www.w3.org/2000/svg" class="date-icon" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                                <line x1="16" y1="2" x2="16" y2="6"></line>
                                <line x1="8" y1="2" x2="8" y2="6"></line>
                                <line x1="3" y1="10" x2="21" y2="10"></line>
                            </svg>
                            <input id="booking-date" type="date" v-model="selectedDate" class="date-input" :min="today"
                                :max="maxDate">
                        </div>
                        <p v-if="dateError" class="date-error">{{ dateError }}</p>
                    </div>

                    <!-- Time Slots -->
                    <div class="time-slots">
                        <label>Select Time:</label>
                        <div class="time-slots-grid">
                            <button v-for="slot in timeSlots" :key="slot.time" :class="['time-slot', {
                                'available': slot.available && !slot.isPast,
                                'confirmed': slot.status === 'confirmed',
                                'pending': slot.status === 'pending',
                                'past': slot.isPast,
                                'selected': selectedTimeSlot === slot.time && slot.available && !slot.isPast
                            }]" :disabled="!slot.available || slot.isPast" @click="selectTimeSlot(slot)">
                                {{ slot.time }}
                            </button>
                        </div>
                    </div>

                    <!-- Book Now Button -->
                    <div class="action-area">
                        <button class="book-now-btn" @click="proceedToBooking" :disabled="!selectedTimeSlot">
                            Book Now
                        </button>
                        <p class="slot-message" v-if="!selectedTimeSlot">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <circle cx="12" cy="12" r="10"></circle>
                                <line x1="12" y1="8" x2="12" y2="12"></line>
                                <line x1="12" y1="16" x2="12.01" y2="16"></line>
                            </svg>
                            Select a time slot to continue
                        </p>
                    </div>
                </div>
            </div>

            <!-- Details Section (Right Side) -->
            <div class="details-section">
                <!-- Description Card -->
                <div class="detail-card description-card">
                    <h2>About This Futsal</h2>
                    <p>{{ futsal.short_description }}</p>
                    <div class="full-description" v-html="futsal.futsal_description"></div>
                </div>

                <!-- Features & Amenities Card -->
                <div class="detail-card features-card">
                    <h2>Features & Amenities</h2>
                    <div class="features-grid">
                        <div v-if="futsal.a_side" class="feature-item">
                            <svg xmlns="http://www.w3.org/2000/svg" class="feature-icon" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <circle cx="12" cy="12" r="10"></circle>
                                <polygon points="10 8 16 12 10 16 10 8"></polygon>
                            </svg>
                            <span>{{ futsal.a_side }}-a-side</span>
                        </div>
                        <div v-if="futsal.parking_space" class="feature-item">
                            <svg xmlns="http://www.w3.org/2000/svg" class="feature-icon" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <rect x="3" y="5" width="18" height="14" rx="2" ry="2"></rect>
                                <line x1="3" y1="10" x2="21" y2="10"></line>
                            </svg>
                            <span>Parking</span>
                        </div>
                        <div v-if="futsal.shower_facility" class="feature-item">
                            <svg xmlns="http://www.w3.org/2000/svg" class="feature-icon" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M4 4v16"></path>
                                <path d="M4 8h12a4 4 0 0 1 4 4 4 4 0 0 1-4 4H4"></path>
                            </svg>
                            <span>Shower</span>
                        </div>
                        <div v-if="futsal.changing_room" class="feature-item">
                            <svg xmlns="http://www.w3.org/2000/svg" class="feature-icon" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                                <circle cx="9" cy="7" r="4"></circle>
                                <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                                <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                            </svg>
                            <span>Changing Room</span>
                        </div>
                        <div v-if="futsal.restaurant" class="feature-item">
                            <svg xmlns="http://www.w3.org/2000/svg" class="feature-icon" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M18 8h1a4 4 0 0 1 0 8h-1"></path>
                                <path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"></path>
                                <line x1="6" y1="1" x2="6" y2="4"></line>
                                <line x1="10" y1="1" x2="10" y2="4"></line>
                                <line x1="14" y1="1" x2="14" y2="4"></line>
                            </svg>
                            <span>Restaurant</span>
                        </div>
                        <div v-if="futsal.wifi" class="feature-item">
                            <svg xmlns="http://www.w3.org/2000/svg" class="feature-icon" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M5 12.55a11 11 0 0 1 14.08 0"></path>
                                <path d="M1.42 9a16 16 0 0 1 21.16 0"></path>
                                <path d="M8.53 16.11a6 6 0 0 1 6.95 0"></path>
                                <line x1="12" y1="20" x2="12.01" y2="20"></line>
                            </svg>
                            <span>WiFi</span>
                        </div>
                    </div>
                </div>

                <!-- Pricing Details Card -->
                <div class="detail-card pricing-card">
                    <h2>Pricing Details</h2>
                    <table class="pricing-table">
                        <thead>
                            <tr>
                                <th>Day</th>
                                <th>Price (NRs./hour)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(price, day) in futsal.price_table" :key="day">
                                <td>{{ day.trim() }}</td>
                                <td>{{ formatPrice(price) }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- Contact Card -->
                <div class="detail-card contact-card">
                    <h2>Contact Information</h2>
                    <div class="contact-items">
                        <a :href="`tel:${futsal.futsal_phone_number}`" class="contact-item">
                            <svg xmlns="http://www.w3.org/2000/svg" class="contact-icon" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path
                                    d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z">
                                </path>
                            </svg>
                            <div>
                                <strong>Phone:</strong>
                                <span>{{ formatPhoneNumber(futsal.futsal_phone_number) }}</span>
                            </div>
                        </a>

                        <a :href="futsal.google_maps_link" target="_blank" class="contact-item">
                            <svg xmlns="http://www.w3.org/2000/svg" class="contact-icon" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polygon points="3 11 22 2 13 21 11 13 3 11"></polygon>
                            </svg>
                            <div>
                                <strong>Location:</strong>
                                <span>{{ futsal.location }}</span>
                            </div>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import apiClient from '@/axios';

// Router and Route
const router = useRouter();
const route = useRoute();

// State
const selectedDate = ref('');
const selectedTimeSlot = ref('');
const today = ref('');
const maxDate = ref('');
const currentSlide = ref(0);
const isLoading = ref(true);
const futsal = ref({});
const bookings = ref([]);
const currentNepalTime = ref(null);
const dateError = ref(''); // New state for error message

// Computed properties
const futsalImages = computed(() => {
    return [
        futsal.value.futsal_image_1,
        futsal.value.futsal_image_2,
        futsal.value.futsal_image_3,
        futsal.value.futsal_image_4,
        futsal.value.futsal_image_5
    ].filter(image => image !== null);
});

const timeSlots = computed(() => {
    const slots = [
        { time: '6-7', start: '06:00:00', end: '07:00:00' },
        { time: '7-8', start: '07:00:00', end: '08:00:00' },
        { time: '8-9', start: '08:00:00', end: '09:00:00' },
        { time: '9-10', start: '09:00:00', end: '10:00:00' },
        { time: '10-11', start: '10:00:00', end: '11:00:00' },
        { time: '11-12', start: '11:00:00', end: '12:00:00' },
        { time: '12-13', start: '12:00:00', end: '13:00:00' },
        { time: '13-14', start: '13:00:00', end: '14:00:00' },
        { time: '14-15', start: '14:00:00', end: '15:00:00' },
        { time: '15-16', start: '15:00:00', end: '16:00:00' },
        { time: '16-17', start: '16:00:00', end: '17:00:00' },
        { time: '17-18', start: '17:00:00', end: '18:00:00' },
        { time: '18-19', start: '18:00:00', end: '19:00:00' },
        { time: '19-20', start: '19:00:00', end: '20:00:00' },
        { time: '20-21', start: '20:00:00', end: '21:00:00' }
    ];

    if (!currentNepalTime.value || !selectedDate.value) return slots;

    const nepalOffset = 5.75; // UTC+5:45 in hours
    const now = new Date(currentNepalTime.value.getTime());
    const selected = new Date(selectedDate.value);

    return slots.map(slot => {
        const booking = bookings.value.find(b =>
            b.booking_date === selectedDate.value &&
            b.booking_start_time === slot.start &&
            b.booking_end_time === slot.end
        );

        const slotStartTime = new Date(selected);
        const [startHour, startMinute] = slot.start.split(':').map(Number);
        slotStartTime.setHours(startHour, startMinute, 0, 0);

        const isPast = selectedDate.value === today.value && now > slotStartTime;

        if (booking) {
            return {
                ...slot,
                available: false,
                status: booking.booking_status ? 'confirmed' : 'pending',
                isPast
            };
        }
        return {
            ...slot,
            available: true,
            status: 'available',
            isPast
        };
    });
});

// Fetch futsal data from API
const fetchFutsal = async () => {
    isLoading.value = true;
    const futsalId = route.params.id;

    try {
        const response = await apiClient.get(`futsal/retrieve-futsal/${futsalId}/`);
        await new Promise(resolve => setTimeout(resolve, 1000));
        futsal.value = response.data;
    } catch (error) {
        console.error('Error fetching futsal:', error);
        futsal.value = {};
    } finally {
        isLoading.value = false;
    }
};

// Fetch bookings for the selected date
const fetchBookings = async () => {
    const futsalId = route.params.id;
    try {
        const response = await apiClient.get(`booking/list-bookings/${futsalId}`);
        bookings.value = response.data;
    } catch (error) {
        console.error('Error fetching bookings:', error);
        bookings.value = [];
    }
};

// Update current Nepal time
const updateNepalTime = () => {
    const now = new Date();
    const nepalOffset = 5.75 * 60 * 60 * 1000; // UTC+5:45 in milliseconds
    currentNepalTime.value = new Date(now.getTime());
};

// New validation method
const validateDate = () => {
    const selected = new Date(selectedDate.value);
    const minDate = new Date(today.value);
    const max = new Date(maxDate.value);

    if (selected < minDate) {
        dateError.value = 'Cannot book a date in the past.';
        selectedDate.value = today.value; // Reset to today
        return false;
    } else if (selected > max) {
        dateError.value = 'Bookings are only allowed up to 7 days in advance.';
        selectedDate.value = today.value; // Reset to today
        return false;
    } else {
        dateError.value = ''; // Clear error if valid
        return true;
    }
};

// Methods
const formatPrice = (price) => {
    return price ? parseFloat(price).toLocaleString() : 'N/A';
};

const formatPhoneNumber = (phone) => {
    return phone || 'N/A';
};

const selectTimeSlot = (slot) => {
    if (slot.available && !slot.isPast) {
        selectedTimeSlot.value = slot.time;
    }
};

const proceedToBooking = () => {
    if (!selectedTimeSlot.value || !validateDate()) return;

    router.push({
        path: `/futsals/${futsal.value.id}/book`,
        query: {
            date: selectedDate.value,
            time: selectedTimeSlot.value
        }
    });
};

// Carousel methods
const nextSlide = () => {
    if (currentSlide.value < futsalImages.value.length - 1) {
        currentSlide.value++;
    } else {
        currentSlide.value = 0;
    }
};

const prevSlide = () => {
    if (currentSlide.value > 0) {
        currentSlide.value--;
    } else {
        currentSlide.value = futsalImages.value.length - 1;
    }
};

const goToSlide = (index) => {
    currentSlide.value = index;
};

// Watch for date changes to validate and update bookings
watch(selectedDate, (newDate) => {
    if (newDate) {
        validateDate(); // Validate on change
        if (!dateError.value) {
            fetchBookings();
            selectedTimeSlot.value = '';
        }
    }
});

onMounted(() => {
    const now = new Date();
    const nepalOffset = 5.75 * 60 * 60 * 1000; // UTC+5:45 in milliseconds
    const nepalNow = new Date(now.getTime() + nepalOffset);

    today.value = nepalNow.toISOString().split('T')[0];
    selectedDate.value = today.value;

    // Set max date to 7 days from today
    const max = new Date(nepalNow);
    max.setDate(max.getDate() + 7);
    maxDate.value = max.toISOString().split('T')[0];

    updateNepalTime();
    const timeUpdateInterval = setInterval(updateNepalTime, 60000);

    fetchFutsal();
    fetchBookings();

    const autoPlayInterval = setInterval(() => {
        if (document.visibilityState === 'visible' && !isLoading.value) {
            nextSlide();
        }
    }, 5000);

    return () => {
        clearInterval(timeUpdateInterval);
        clearInterval(autoPlayInterval);
    };
});
</script>



<style scoped>
.time-slot {
    padding: 12px 8px;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    text-align: center;
    cursor: pointer;
    transition: all 0.2s ease;
}

.time-slot.available {
    background-color: #e8f5e9;
    color: #2e7d32;
}

.time-slot.available:hover {
    background-color: #c8e6c9;
    transform: translateY(-2px);
}

.time-slot.confirmed {
    background-color: #ffebee;
    color: #c62828;
    cursor: not-allowed;
    opacity: 0.8;
}

.time-slot.pending {
    background-color: #fff9c4;
    color: #f9a825;
    cursor: not-allowed;
    opacity: 0.8;
}

.time-slot.past {
    background-color: #e0e0e0;
    color: #757575;
    cursor: not-allowed;
    opacity: 0.8;
}

.time-slot.selected {
    background-color: #2e7d32;
    color: white;
    box-shadow: 0 4px 8px rgba(46, 125, 50, 0.3);
    transform: translateY(-2px);
    position: relative;
}

.time-slot.selected::after {
    content: '✓';
    position: absolute;
    top: 2px;
    right: 6px;
    font-size: 10px;
}

.futsal-detail-page {
    min-height: 100vh;
    background-color: #f8f9fa;
    font-family: 'Inter', 'Segoe UI', Roboto, sans-serif;
    color: #333333;
    position: relative;
    opacity: 1;
    transition: opacity 0.3s ease;
}

.futsal-detail-page.loading {
    opacity: 0.5;
}

.loading-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    color: white;
}

.loading-spinner {
    width: 50px;
    height: 50px;
    border: 5px solid #ffffff;
    border-top: 5px solid #2e7d32;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin-bottom: 20px;
}

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}

.hero-section {
    position: relative;
    width: 100%;
    height: 50vh;
    min-height: 400px;
    overflow: hidden;
}

.carousel-container {
    height: 100%;
    width: 100%;
    position: relative;
}

.carousel-slides {
    display: flex;
    height: 100%;
    transition: transform 0.5s ease;
}

.carousel-slide {
    min-width: 100%;
    height: 100%;
}

.carousel-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.carousel-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(to top, rgba(0, 0, 0, 0.8) 0%, rgba(0, 0, 0, 0) 100%);
    color: white;
    padding: 2rem;
    z-index: 2;
}

.futsal-name {
    font-size: 2.75rem;
    font-weight: 800;
    margin: 0;
    line-height: 1.1;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.futsal-location {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 1.1rem;
    margin-top: 0.5rem;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.location-icon {
    width: 16px;
    height: 16px;
}

.carousel-control {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 48px;
    height: 48px;
    background-color: #86efac;
    border: none;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 10;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}

.carousel-control svg {
    width: 24px;
    height: 24px;
}

.carousel-control:hover {
    background-color: white;
    transform: translateY(-50%) scale(1.1);
}

.carousel-control.prev {
    left: 20px;
}

.carousel-control.next {
    right: 20px;
}

.carousel-indicators {
    position: absolute;
    bottom: 100px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 6px;
    z-index: 10;
}

.carousel-indicator {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background-color: rgba(255, 255, 255, 0.5);
    border: none;
    padding: 0;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.3s ease;
}

.carousel-indicator.active {
    background-color: #86efac;
    transform: scale(1.3);
}

.content-container {
    max-width: 1200px;
    margin: -60px auto 0;
    padding: 0 20px 60px;
    position: relative;
    z-index: 10;
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
}

.booking-section {
    flex: 1;
    min-width: 330px;
    order: 2;
}

.booking-card {
    background-color: white;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    padding: 24px;
    height: fit-content;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.booking-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 16px;
    border-bottom: 1px solid #e0e0e0;
    margin-bottom: 20px;
}

.card-header h2 {
    font-size: 1.5rem;
    font-weight: 700;
    margin: 0;
    color: #2e7d32;
}

.price-tag {
    display: flex;
    align-items: baseline;
}

.price-amount {
    font-size: 1.5rem;
    font-weight: 800;
    color: #2e7d32;
}

.price-unit {
    font-size: 0.9rem;
    color: #757575;
    margin-left: 2px;
}

.date-selection {
    margin-bottom: 20px;
}

.date-selection label {
    display: block;
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 8px;
    color: #555;
}

.date-input-wrapper {
    position: relative;
}

.date-icon {
    position: absolute;
    left: 12px;
    top: 50%;
    transform: translateY(-50%);
    color: #757575;
    width: 20px;
    height: 20px;
}

.date-input {
    width: 100%;
    padding: 12px 12px 12px 40px;
    border: 2px solid #e0e0e0;
    border-radius: 10px;
    font-size: 1rem;
    color: #333;
    transition: all 0.3s ease;
}

.date-input:focus {
    outline: none;
    border-color: #2e7d32;
    box-shadow: 0 0 0 3px rgba(46, 125, 50, 0.1);
}

.date-error {
    color: #c62828;
    font-size: 0.85rem;
    margin-top: 8px;
    display: flex;
    align-items: center;
    gap: 6px;
}

.date-error::before {
    content: '⚠';
    font-size: 1rem;
}

.time-slots {
    margin-bottom: 20px;
}

.time-slots label {
    display: block;
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 12px;
    color: #555;
}

.time-slots-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
}

.action-area {
    margin-top: 24px;
}

.book-now-btn {
    width: 100%;
    padding: 16px;
    background-color: #2e7d32;
    color: white;
    border: none;
    border-radius: 10px;
    font-size: 1rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(46, 125, 50, 0.3);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.book-now-btn:hover:not(:disabled) {
    background-color: #1b5e20;
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(46, 125, 50, 0.4);
}

.book-now-btn:active:not(:disabled) {
    transform: translateY(0);
}

.book-now-btn:disabled {
    background-color: #9e9e9e;
    box-shadow: none;
    cursor: not-allowed;
}

.slot-message {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    margin-top: 12px;
    color: #757575;
    font-size: 0.9rem;
    text-align: center;
}

.slot-message svg {
    width: 16px;
    height: 16px;
}

.details-section {
    flex: 2;
    min-width: 330px;
    order: 1;
    display: flex;
    flex-direction: column;
    gap: 24px;
}

.detail-card {
    background-color: white;
    border-radius: 16px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    padding: 24px;
    transition: transform 0.3s ease;
}

.detail-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
}

.detail-card h2 {
    font-size: 1.3rem;
    font-weight: 700;
    color: #2e7d32;
    margin-top: 0;
    margin-bottom: 16px;
    position: relative;
}

.detail-card h2::after {
    content: '';
    position: absolute;
    bottom: -8px;
    left: 0;
    width: 60px;
    height: 3px;
    background-color: #2e7d32;
    border-radius: 3px;
}

.description-card p {
    line-height: 1.8;
    color: #555;
    margin-top: 20px;
    margin-bottom: 10px;
}

.full-description {
    margin-top: 20px;
}

.full-description p {
    margin-top: 0;
    color: #666;
}

.features-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    margin-top: 24px;
}

.feature-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 16px;
    background-color: #f5f9f5;
    border-radius: 10px;
    transition: all 0.2s ease;
}

.feature-item:hover {
    background-color: #e8f5e9;
    transform: translateY(-2px);
}

.feature-icon {
    width: 24px;
    height: 24px;
    color: #2e7d32;
}

.feature-item span {
    font-size: 0.95rem;
    font-weight: 500;
    color: #333;
}

.pricing-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

.pricing-table th,
.pricing-table td {
    padding: 12px 16px;
    text-align: left;
    border-bottom: 1px solid #e0e0e0;
}

.pricing-table th {
    background-color: #f5f9f5;
    font-weight: 600;
    color: #2e7d32;
}

.pricing-table td {
    color: #333;
}

.pricing-table tr:hover {
    background-color: #e8f5e9;
}

.contact-items {
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin-top: 20px;
}

.contact-item {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 14px 16px;
    background-color: #f5f9f5;
    border-radius: 10px;
    text-decoration: none;
    color: inherit;
    transition: all 0.2s ease;
}

.contact-item:hover {
    background-color: #e8f5e9;
    transform: translateX(5px);
}

.contact-icon {
    width: 24px;
    height: 24px;
    color: #2e7d32;
    flex-shrink: 0;
}

.contact-item div {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.contact-item strong {
    font-size: 0.8rem;
    color: #555;
}

.contact-item span {
    font-size: 1rem;
    color: #333;
}

@media (max-width: 900px) {
    .content-container {
        flex-direction: column;
    }

    .booking-section {
        order: 1;
    }

    .details-section {
        order: 2;
    }

    .hero-section {
        height: 40vh;
    }

    .carousel-overlay {
        padding: 1.5rem;
    }

    .futsal-name {
        font-size: 2.25rem;
    }

    .carousel-indicators {
        bottom: 15px;
    }
}

@media (max-width: 600px) {
    .hero-section {
        height: 30vh;
        min-height: 250px;
    }

    .futsal-name {
        font-size: 1.75rem;
    }

    .futsal-location {
        font-size: 0.9rem;
    }

    .carousel-control {
        width: 40px;
        height: 40px;
    }

    .carousel-control svg {
        width: 20px;
        height: 20px;
    }

    .features-grid {
        grid-template-columns: 1fr;
    }

    .time-slots-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .carousel-indicators {
        bottom: 10px;
    }

    .carousel-overlay {
        padding: 10px;
    }

    .content-container {
        margin-top: -40px;
        padding: 0 15px 40px;
    }

    .pricing-table th,
    .pricing-table td {
        padding: 10px 12px;
    }
}
</style>