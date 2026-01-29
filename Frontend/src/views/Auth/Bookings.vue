<template>
  <div class="my-bookings-page">
    <div class="page-header">
      <div class="header-content">
        <h1 style="color: white;">My Bookings</h1>
        <p>View and manage all your futsal bookings</p>
      </div>
    </div>

    <!-- Booking Tabs -->
    <div class="booking-tabs">
      <button class="tab-button" :class="{ active: activeTab === 'upcoming' }" @click="activeTab = 'upcoming'">
        Upcoming Bookings
      </button>
      <button class="tab-button" :class="{ active: activeTab === 'past' }" @click="activeTab = 'past'">
        Past Bookings
      </button>
    </div>

    <!-- Filter and Search -->
    <div class="filter-section">
      <div class="search-bar">
        <input type="text" v-model="searchQuery" placeholder="Search by futsal name or location..." />
        <button class="search-button">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
            stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
        </button>
      </div>

      <div class="filter-dropdown">
        <button class="filter-button" @click="showFilters = !showFilters">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
            stroke-linecap="round" stroke-linejoin="round">
            <polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"></polygon>
          </svg>
          Filter
        </button>

        <div class="filter-menu" v-if="showFilters">
          <div class="filter-group">
            <label>Date Range</label>
            <div class="date-inputs">
              <input type="date" v-model="filters.dateFrom" />
              <span>to</span>
              <input type="date" v-model="filters.dateTo" />
            </div>
          </div>

          <div class="filter-group">
            <label>Status</label>
            <div class="checkbox-group">
              <label class="checkbox-label">
                <input type="checkbox" v-model="filters.statuses" value="confirmed" />
                Confirmed
              </label>
              <label class="checkbox-label">
                <input type="checkbox" v-model="filters.statuses" value="pending" />
                Pending
              </label>
              <label class="checkbox-label">
                <input type="checkbox" v-model="filters.statuses" value="cancelled" />
                Cancelled
              </label>
            </div>
          </div>

          <div class="filter-actions">
            <button class="reset-button" @click="resetFilters">Reset</button>
            <button class="apply-button" @click="applyFilters">Apply</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Bookings List -->
    <div class="bookings-container">
      <div v-if="loading" class="loading-state">
        <div class="spinner"></div>
        <p>Loading your bookings...</p>
      </div>

      <div v-else-if="filteredBookings.length === 0" class="empty-state">
        <div class="empty-icon">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
            stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
            <line x1="16" y1="2" x2="16" y2="6"></line>
            <line x1="8" y1="2" x2="8" y2="6"></line>
            <line x1="3" y1="10" x2="21" y2="10"></line>
          </svg>
        </div>
        <h3>No bookings found</h3>
        <p v-if="activeTab === 'upcoming'">You don't have any upcoming bookings.</p>
        <p v-else>You don't have any past bookings.</p>
        <button class="book-now-button" @click="navigateToFutsals">Book a Futsal Now</button>
      </div>

      <div v-else class="bookings-list">
        <div v-for="booking in filteredBookings" :key="booking.id" class="booking-card">
          <div class="booking-header">
            <div class="booking-date">
              <div class="date-badge">
                <span class="date-month">{{ formatDateMonth(booking.date) }}</span>
                <span class="date-day">{{ formatDateDay(booking.date) }}</span>
              </div>
              <div class="time-info">
                <span class="day-name">{{ formatDayName(booking.date) }}</span>
                <span class="time-range">{{ booking.timeSlot }}</span>
              </div>
            </div>
            <div class="booking-status" :class="booking.status">
              {{ formatStatus(booking.status) }}
            </div>
          </div>

          <div class="booking-content">
            <div class="futsal-info">
              <h3>{{ booking.futsalName }}</h3>
              <div class="location">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                  stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                  <circle cx="12" cy="10" r="3"></circle>
                </svg>
                <span>{{ booking.location }}</span>
              </div>
            </div>

            <div class="booking-details">
              <div class="detail-item">
                <span class="detail-label">Court:</span>
                <span class="detail-value">{{ booking.court }}</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Booking ID:</span>
                <span class="detail-value">{{ booking.id }}</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">Payment:</span>
                <span class="detail-value">NPR {{ formatNumber(booking.amount) }}</span>
              </div>
            </div>
          </div>

          <div class="booking-actions">
            <!-- <button 
                v-if="activeTab === 'upcoming' && booking.status !== 'cancelled'" 
                class="action-button cancel-button"
                @click="confirmCancelBooking(booking.id)"
              >
                Cancel Booking
              </button>
              <button 
                v-if="activeTab === 'upcoming' && booking.status !== 'cancelled'" 
                class="action-button reschedule-button"
                @click="rescheduleBooking(booking.id)"
              >
                Reschedule
              </button>
              <button 
                class="action-button details-button"
                @click="viewBookingDetails(booking.id)"
              >
                View Details
              </button> -->
          </div>
        </div>
      </div>

      <!-- Pagination -->
      <div v-if="filteredBookings.length > 0" class="pagination">
        <button class="pagination-button" :disabled="currentPage === 1" @click="currentPage--">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
            stroke-linecap="round" stroke-linejoin="round">
            <polyline points="15 18 9 12 15 6"></polyline>
          </svg>
          Previous
        </button>

        <div class="pagination-info">
          Page {{ currentPage }} of {{ totalPages }}
        </div>

        <button class="pagination-button" :disabled="currentPage === totalPages" @click="currentPage++">
          Next
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
            stroke-linecap="round" stroke-linejoin="round">
            <polyline points="9 18 15 12 9 6"></polyline>
          </svg>
        </button>
      </div>
    </div>

    <!-- Cancel Booking Modal -->
    <div v-if="showCancelModal" class="modal-overlay">
      <div class="modal-content">
        <div class="modal-header">
          <h3>Cancel Booking</h3>
          <button class="close-button" @click="showCancelModal = false">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
              stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </div>

        <div class="modal-body">
          <p>Are you sure you want to cancel this booking? This action cannot be undone.</p>

          <div class="cancellation-policy">
            <h4>Cancellation Policy</h4>
            <ul>
              <li>Full refund if cancelled 24 hours before the booking time</li>
              <li>50% refund if cancelled between 12-24 hours before the booking time</li>
              <li>No refund if cancelled less than 12 hours before the booking time</li>
            </ul>
          </div>

          <div class="reason-input">
            <label for="cancel-reason">Reason for cancellation (optional)</label>
            <textarea id="cancel-reason" v-model="cancellationReason" rows="3"
              placeholder="Please provide a reason for cancellation..."></textarea>
          </div>
        </div>

        <div class="modal-footer">
          <button class="secondary-button" @click="showCancelModal = false">
            Keep Booking
          </button>
          <button class="primary-button cancel-confirm-button" @click="cancelBooking" :disabled="cancelling">
            {{ cancelling ? 'Cancelling...' : 'Confirm Cancellation' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import apiClient from '@/axios';

const router = useRouter();

// State
const activeTab = ref('upcoming');
const searchQuery = ref('');
const showFilters = ref(false);
const loading = ref(false);
const error = ref(null);
const currentPage = ref(1);
const itemsPerPage = 5;
const showCancelModal = ref(false);
const bookingToCancel = ref(null);
const cancellationReason = ref('');
const cancelling = ref(false);
const upcomingBookings = ref([]);
const pastBookings = ref([]);

// Filters
const filters = reactive({
  dateFrom: '',
  dateTo: '',
  statuses: [],
});

// Get user ID and token from localStorage
const getAuthToken = () => localStorage.getItem('token');
const userId = ref("");

const getUserId = async () => {
  const response = await apiClient.get('auth/user/', {
    headers: {
      Authorization: 'Token ' + getAuthToken(),
    }
  }).then(
    (response) => {
      userId.value = response.data.pk;
      fetchBookings();
    }
  ).catch((error) => {
    console.error('Error fetching user ID:', error);
  });
}
// Normalize API data to ensure consistency
const normalizeBookingData = (booking) => {
  try {
    const bookingDate = new Date(booking.booking_date);
    if (isNaN(bookingDate)) {
      throw new Error('Invalid booking date');
    }

    const timeSlot = `${booking.booking_start_time.slice(0, 5)} - ${booking.booking_end_time.slice(0, 5)}`;

    return {
      id: booking.id || '',
      futsalName: booking.futsal?.futsal_name || 'Unknown Futsal',
      location: booking.futsal?.location || 'Unknown Location',
      date: booking.booking_date || '',
      timeSlot,
      court: booking.futsal?.grounds ? `Ground ${booking.futsal.grounds}` : 'N/A',
      amount: parseFloat(booking.futsal?.price_per_hour) || 0,
      status: booking.status || 'pending', // Assume pending if not provided
      paymentStatus: booking.payment_status || 'pending',
    };
  } catch (err) {
    console.error('Error normalizing booking:', booking.id, err);
    return null; // Skip invalid bookings
  }
};

// Fetch bookings from API
const fetchBookings = async () => {
  if (!userId) {
    error.value = 'Please log in to view your bookings.';
    router.push('/login');
    return;
  }

  try {
    loading.value = true;
    error.value = null;

    const response = await apiClient.get(`booking/list-bookings/user/${userId.value}/`, {
      headers: {
        Authorization: getAuthToken() ? `Bearer ${getAuthToken()}` : undefined,
      },
    });

    // Validate response
    if (!Array.isArray(response.data)) {
      throw new Error('Unexpected API response format');
    }

    const currentDate = new Date();
    const normalizedBookings = response.data
      .map(normalizeBookingData)
      .filter(booking => booking !== null); // Remove invalid bookings

    upcomingBookings.value = normalizedBookings.filter(
      booking => new Date(booking.date) >= currentDate
    );
    pastBookings.value = normalizedBookings.filter(
      booking => new Date(booking.date) < currentDate
    );
  } catch (err) {
    console.error('Error fetching bookings:', err);
    error.value = handleApiError(err);
    if (err.response?.status === 401) {
      router.push('/login');
    }
  } finally {
    loading.value = false;
  }
};

// Handle API errors
const handleApiError = (err) => {
  if (!navigator.onLine) {
    return 'No internet connection. Please check your network.';
  }
  if (err.response) {
    switch (err.response.status) {
      case 401:
        return 'Your session has expired. Please log in again.';
      case 403:
        return 'You are not authorized to view these bookings.';
      case 404:
        return 'No bookings found for your account.';
      case 500:
        return 'Something went wrong on our server. Please try again later.';
      default:
        return 'An unexpected error occurred. Please try again.';
    }
  }
  return 'Failed to load bookings. Please try again later.';
};

// Computed properties
const currentBookings = computed(() => {
  return activeTab.value === 'upcoming' ? upcomingBookings.value : pastBookings.value;
});

const filteredBookings = computed(() => {
  let result = [...currentBookings.value];

  // Apply search filter
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase().trim();
    result = result.filter(
      booking =>
        booking.futsalName?.toLowerCase().includes(query) ||
        booking.location?.toLowerCase().includes(query)
    );
  }

  // Apply date filters
  if (filters.dateFrom) {
    result = result.filter(booking => new Date(booking.date) >= new Date(filters.dateFrom));
  }
  if (filters.dateTo) {
    result = result.filter(booking => new Date(booking.date) <= new Date(filters.dateTo));
  }

  // Apply status filters
  if (filters.statuses.length > 0) {
    result = result.filter(booking => filters.statuses.includes(booking.status));
  }

  // Apply pagination
  const startIndex = (currentPage.value - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  return result.slice(startIndex, endIndex);
});

const totalPages = computed(() => {
  let filteredTotal = currentBookings.value.length;

  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase().trim();
    filteredTotal = currentBookings.value.filter(
      booking =>
        booking.futsalName?.toLowerCase().includes(query) ||
        booking.location?.toLowerCase().includes(query)
    ).length;
  }

  return Math.max(1, Math.ceil(filteredTotal / itemsPerPage));
});

// Methods
const formatDateMonth = (dateString) => {
  try {
    return new Date(dateString).toLocaleString('default', { month: 'short' }) || 'N/A';
  } catch {
    return 'N/A';
  }
};

const formatDateDay = (dateString) => {
  try {
    return new Date(dateString).getDate() || 'N/A';
  } catch {
    return 'N/A';
  }
};

const formatDayName = (dateString) => {
  try {
    return new Date(dateString).toLocaleString('default', { weekday: 'long' }) || 'N/A';
  } catch {
    return 'N/A';
  }
};

const formatStatus = (status) => {
  const statusMap = {
    confirmed: 'Confirmed',
    pending: 'Pending',
    completed: 'Completed',
    cancelled: 'Cancelled',
  };
  return statusMap[status] || status || 'Unknown';
};

const formatNumber = (number) => {
  try {
    return Number(number).toLocaleString('en-US') || '0';
  } catch {
    return '0';
  }
};

const resetFilters = () => {
  filters.dateFrom = '';
  filters.dateTo = '';
  filters.statuses = [];
  currentPage.value = 1;
};

const applyFilters = () => {
  currentPage.value = 1;
  showFilters.value = false;
};

const navigateToFutsals = () => {
  router.push('/futsals');
};

const confirmCancelBooking = (bookingId) => {
  bookingToCancel.value = bookingId;
  showCancelModal.value = true;
};

const cancelBooking = async () => {
  if (!bookingToCancel.value) return;

  try {
    cancelling.value = true;
    error.value = null;

    await apiClient.patch(`booking/${bookingToCancel.value}/`, {
      status: 'cancelled',
      cancellation_reason: cancellationReason.value || undefined,
    });

    // Update local state
    const bookingIndex = upcomingBookings.value.findIndex(b => b.id === bookingToCancel.value);
    if (bookingIndex !== -1) {
      upcomingBookings.value[bookingIndex].status = 'cancelled';
      upcomingBookings.value[bookingIndex].paymentStatus = 'refunded';
    }
  } catch (err) {
    console.error('Error cancelling booking:', err);
    error.value = handleApiError(err);
  } finally {
    cancelling.value = false;
    showCancelModal.value = false;
    cancellationReason.value = '';
    bookingToCancel.value = null;
  }
};

const rescheduleBooking = (bookingId) => {
  router.push(`/reschedule/${bookingId}`);
};

const viewBookingDetails = (bookingId) => {
  router.push(`/booking/${bookingId}`);
};

// Fetch bookings on mount
onMounted(() => {
  getUserId();

});
</script>

<style scoped>
.my-bookings-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.page-header {
  background-color: #2e7d32;
  color: white;
  padding: 2rem;
  border-radius: 0.5rem;
  margin-bottom: 2rem;
}

.page-header h1 {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.booking-tabs {
  display: flex;
  border-bottom: 1px solid #e5e7eb;
  margin-bottom: 1.5rem;
}

.tab-button {
  padding: 0.75rem 1.5rem;
  font-weight: 500;
  color: #4b5563;
  border: none;
  background: none;
  cursor: pointer;
  transition: all 0.2s;
}

.tab-button.active {
  color: #2e7d32;
  border-bottom: 2px solid #2e7d32;
}

.filter-section {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1.5rem;
}

.search-bar {
  display: flex;
  flex: 1;
  max-width: 500px;
  position: relative;
}

.search-bar input {
  width: 100%;
  padding: 0.75rem 1rem;
  padding-right: 3rem;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
}

.search-button {
  position: absolute;
  right: 0.5rem;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: #6b7280;
  cursor: pointer;
  padding: 0.25rem;
}

.search-button svg {
  width: 1.25rem;
  height: 1.25rem;
}

.filter-dropdown {
  position: relative;
}

.filter-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  background-color: white;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  cursor: pointer;
}

.filter-button svg {
  width: 1rem;
  height: 1rem;
}

.filter-menu {
  position: absolute;
  right: 0;
  top: 100%;
  margin-top: 0.5rem;
  background-color: white;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  padding: 1rem;
  width: 300px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  z-index: 10;
}

.filter-group {
  margin-bottom: 1rem;
}

.filter-group label {
  display: block;
  font-weight: 500;
  margin-bottom: 0.5rem;
}

.date-inputs {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.date-inputs input {
  flex: 1;
  padding: 0.5rem;
  border: 1px solid #d1d5db;
  border-radius: 0.25rem;
}

.checkbox-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
}

.filter-actions {
  display: flex;
  justify-content: flex-end;
  gap: 0.5rem;
  margin-top: 1rem;
}

.reset-button {
  padding: 0.5rem 1rem;
  background-color: white;
  border: 1px solid #d1d5db;
  border-radius: 0.25rem;
  cursor: pointer;
}

.apply-button {
  padding: 0.5rem 1rem;
  background-color: #2e7d32;
  color: white;
  border: none;
  border-radius: 0.25rem;
  cursor: pointer;
}

.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem 0;
}

.spinner {
  border: 4px solid rgba(0, 0, 0, 0.1);
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border-left-color: #2e7d32;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem 0;
  text-align: center;
}

.empty-icon {
  background-color: #f3f4f6;
  padding: 1.5rem;
  border-radius: 50%;
  margin-bottom: 1rem;
}

.empty-icon svg {
  width: 3rem;
  height: 3rem;
  color: #9ca3af;
}

.empty-state h3 {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.empty-state p {
  color: #6b7280;
  margin-bottom: 1.5rem;
}

.book-now-button {
  padding: 0.75rem 1.5rem;
  background-color: #2e7d32;
  color: white;
  border: none;
  border-radius: 0.375rem;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.2s;
}

.book-now-button:hover {
  background-color: #1b5e20;
}

.bookings-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.booking-card {
  background-color: white;
  border: 1px solid #e5e7eb;
  border-radius: 0.5rem;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.booking-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #f9fafb;
  border-bottom: 1px solid #e5e7eb;
}

.booking-date {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.date-badge {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #2e7d32;
  color: white;
  width: 3rem;
  height: 3rem;
  border-radius: 0.25rem;
  text-align: center;
}

.date-month {
  font-size: 0.75rem;
  text-transform: uppercase;
}

.date-day {
  font-size: 1.25rem;
  font-weight: 700;
}

.time-info {
  display: flex;
  flex-direction: column;
}

.day-name {
  font-weight: 500;
}

.time-range {
  color: #6b7280;
}

.booking-status {
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 500;
}

.booking-status.confirmed {
  background-color: #d1fae5;
  color: #065f46;
}

.booking-status.pending {
  background-color: #fef3c7;
  color: #92400e;
}

.booking-status.completed {
  background-color: #e0e7ff;
  color: #4338ca;
}

.booking-status.cancelled {
  background-color: #fee2e2;
  color: #b91c1c;
}

.booking-content {
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

@media (min-width: 768px) {
  .booking-content {
    flex-direction: row;
    justify-content: space-between;
  }

  .futsal-info {
    flex: 1;
  }

  .booking-details {
    flex: 1;
  }
}

.futsal-info h3 {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.location {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #6b7280;
}

.location svg {
  width: 1rem;
  height: 1rem;
}

.booking-details {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.75rem;
}

.detail-item {
  display: flex;
  flex-direction: column;
}

.detail-label {
  font-size: 0.875rem;
  color: #6b7280;
}

.detail-value {
  font-weight: 500;
}

.payment-status {
  display: inline-block;
  padding: 0.125rem 0.5rem;
  border-radius: 9999px;
  font-size: 0.75rem;
}

.payment-status.paid {
  background-color: #d1fae5;
  color: #065f46;
}

.payment-status.pending {
  background-color: #fef3c7;
  color: #92400e;
}

.payment-status.refunded {
  background-color: #e0e7ff;
  color: #4338ca;
}

.booking-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  padding: 1.5rem;
  border-top: 1px solid #e5e7eb;
  background-color: #f9fafb;
}

.action-button {
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.cancel-button {
  background-color: #fee2e2;
  color: #b91c1c;
  border: 1px solid #fecaca;
}

.cancel-button:hover {
  background-color: #fecaca;
}

.reschedule-button {
  background-color: #e0f2fe;
  color: #0369a1;
  border: 1px solid #bae6fd;
}

.reschedule-button:hover {
  background-color: #bae6fd;
}

.details-button {
  background-color: white;
  color: #4b5563;
  border: 1px solid #d1d5db;
}

.details-button:hover {
  background-color: #f3f4f6;
}

.pagination {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 2rem;
  padding-top: 1rem;
  border-top: 1px solid #e5e7eb;
}

.pagination-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background-color: white;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  cursor: pointer;
}

.pagination-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination-button svg {
  width: 1rem;
  height: 1rem;
}

.pagination-info {
  color: #6b7280;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 50;
}

.modal-content {
  background-color: white;
  border-radius: 0.5rem;
  width: 100%;
  max-width: 500px;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid #e5e7eb;
}

.modal-header h3 {
  font-size: 1.25rem;
  font-weight: 600;
}

.close-button {
  background: none;
  border: none;
  cursor: pointer;
  color: #6b7280;
}

.close-button svg {
  width: 1.25rem;
  height: 1.25rem;
}

.modal-body {
  padding: 1.5rem;
}

.cancellation-policy {
  margin-top: 1rem;
  padding: 1rem;
  background-color: #f3f4f6;
  border-radius: 0.375rem;
}

.cancellation-policy h4 {
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.cancellation-policy ul {
  padding-left: 1.5rem;
  list-style-type: disc;
}

.cancellation-policy li {
  margin-bottom: 0.25rem;
  font-size: 0.875rem;
}

.reason-input {
  margin-top: 1.5rem;
}

.reason-input label {
  display: block;
  font-weight: 500;
  margin-bottom: 0.5rem;
}

.reason-input textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  resize: vertical;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 0.75rem;
  padding: 1rem 1.5rem;
  border-top: 1px solid #e5e7eb;
}

.secondary-button {
  padding: 0.5rem 1rem;
  background-color: white;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  font-weight: 500;
  cursor: pointer;
}

.primary-button {
  padding: 0.5rem 1rem;
  background-color: #2e7d32;
  color: white;
  border: none;
  border-radius: 0.375rem;
  font-weight: 500;
  cursor: pointer;
}

.cancel-confirm-button {
  background-color: #dc2626;
}

.cancel-confirm-button:hover {
  background-color: #b91c1c;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .booking-details {
    grid-template-columns: 1fr;
  }

  .filter-section {
    flex-direction: column;
    gap: 1rem;
  }

  .search-bar {
    max-width: none;
  }

  .booking-actions {
    flex-direction: column;
  }

  .action-button {
    width: 100%;
    text-align: center;
  }
}
</style>