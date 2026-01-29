<template>
  <div class="stats-page" :class="{ loading: isLoading }">
    <!-- Loading Overlay -->
    <transition name="fade">
      <div v-if="isLoading" class="loading-overlay">
        <div class="loading-spinner"></div>
        <p>Loading Stats...</p>
      </div>
    </transition>

    <!-- Unauthorized Message -->
    <div v-if="!isAuthorized" class="unauthorized-message">
      <h1>Access Denied</h1>
      <p>
        You don't have permission to view these statistics. Only the futsal owner can access this
        page.
      </p>
      <router-link to="/" class="back-home-btn">Back to Home</router-link>
    </div>

    <!-- Stats Content -->
    <div v-else class="stats-container">
      <h1 class="page-title">{{ futsal.futsal_name }} Statistics</h1>

      <!-- Date Selection -->
      <div class="date-selection">
        <label for="stats-date">Select Date:</label>
        <div class="date-input-wrapper">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="date-icon"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          >
            <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
            <line x1="16" y1="2" x2="16" y2="6"></line>
            <line x1="8" y1="2" x2="8" y2="6"></line>
            <line x1="3" y1="10" x2="21" y2="10"></line>
          </svg>
          <input id="stats-date" type="date" v-model="selectedDate" class="date-input" />
        </div>
      </div>

      <!-- Time Slots -->
      <div class="time-slots">
        <label>Bookings for {{ formatDate(selectedDate) }}:</label>
        <div class="time-slots-grid">
          <button
            v-for="slot in timeSlots"
            :key="slot.time"
            :class="[
              'time-slot',
              {
                available: slot.available && !slot.isPast,
                confirmed: slot.status === 'confirmed',
                pending: slot.status === 'pending',
                past: slot.isPast,
                selected: selectedSlot === slot.time,
              },
            ]"
            @click="selectSlot(slot)"
          >
            {{ slot.time }}
          </button>
        </div>
      </div>

      <!-- Booking Details Modal -->
      <div v-if="selectedSlot && selectedSlotData" class="modal-overlay">
        <div class="booking-modal">
          <h2>{{ selectedSlotData.booking ? 'Booking Details' : 'Create Booking' }}</h2>
          <div class="booking-details">
            <!-- Edit Existing Booking -->
            <div v-if="selectedSlotData.booking">
              <p><strong>Username:</strong> {{ bookingUser?.username || 'Not Booked' }}</p>
              <div class="time-edit">
                <label>Edit Time:</label>
                <select v-model="editedTime" class="time-select">
                  <option
                    v-for="timeOption in availableTimeOptions"
                    :key="timeOption.time"
                    :value="timeOption.time"
                  >
                    {{ timeOption.time }}
                  </option>
                </select>
              </div>
              <div class="status-edit">
                <label>Booking Status:</label>
                <select v-model="editedStatus" class="status-select">
                  <option :value="true">Confirmed</option>
                  <option :value="false">Pending</option>
                </select>
              </div>
              <div class="notes-edit">
                <label>Booking Notes:</label>
                <textarea
                  v-model="editedNotes"
                  class="notes-input"
                  placeholder="Add any notes about this booking"
                ></textarea>
              </div>
            </div>
            <!-- Create New Booking -->
            <div v-else>
              <p><strong>Time:</strong> {{ selectedSlot }}</p>
              <p><strong>User:</strong> {{ currentUser.username }}</p>
              <div class="status-edit">
                <label>Booking Status:</label>
                <select v-model="editedStatus" class="status-select">
                  <option :value="true">Confirmed</option>
                  <option :value="false">Pending</option>
                </select>
              </div>
              <div class="notes-edit">
                <label>Booking Notes:</label>
                <textarea
                  v-model="editedNotes"
                  class="notes-input"
                  placeholder="Add any notes about this booking"
                ></textarea>
              </div>
            </div>
          </div>
          <div class="booking-actions">
            <div class="action-buttons">
              <button
                v-if="selectedSlotData.booking"
                class="save-btn"
                @click="updateBooking"
                :disabled="isSubmitting"
              >
                {{ isSubmitting ? 'Saving...' : 'Save Changes' }}
              </button>
              <button v-else class="save-btn" @click="createBooking" :disabled="isSubmitting">
                {{ isSubmitting ? 'Creating...' : 'Create Booking' }}
              </button>
              <button
                v-if="selectedSlotData.booking"
                class="delete-btn"
                @click="deleteBooking"
                :disabled="isSubmitting"
              >
                {{ isSubmitting ? 'Deleting...' : 'Delete Booking' }}
              </button>
              <button class="close-btn" @click.self="closeModal">Close</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import AdminSidebar from '@/components/AdminSidebar.vue'
import { ref, computed, onMounted, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import apiClient from '@/axios'
import AdminSidebarVue from '@/components/AdminSidebar.vue'

const router = useRouter()
const route = useRoute()

// State
const isLoading = ref(true)
const isAuthorized = ref(false)
const futsal = ref({})
const currentUser = ref({})
const bookings = ref([])
const selectedDate = ref('')
const selectedSlot = ref(null)
const selectedSlotData = ref(null)
const bookingUser = ref(null)
const editedTime = ref('')
const editedStatus = ref(null)
const editedNotes = ref('')
const isSubmitting = ref(false)
const today = ref('')
const currentNepalTime = ref(null)

// Computed properties
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
    { time: '20-21', start: '20:00:00', end: '21:00:00' },
  ]

  if (!currentNepalTime.value || !selectedDate.value) return slots

  const nepalOffset = 5.75 // UTC+5:45 in hours
  const now = new Date(currentNepalTime.value.getTime())
  const selected = new Date(selectedDate.value)

  return slots.map((slot) => {
    const booking = bookings.value.find(
      (b) =>
        b.booking_date === selectedDate.value &&
        b.booking_start_time === slot.start &&
        b.booking_end_time === slot.end
    )

    const slotStartTime = new Date(selected)
    const [startHour, startMinute] = slot.start.split(':').map(Number)
    slotStartTime.setHours(startHour, startMinute, 0, 0)

    const isPast = selectedDate.value === today.value && now > slotStartTime

    if (booking) {
      return {
        ...slot,
        available: false,
        status: booking.booking_status ? 'confirmed' : 'pending',
        isPast,
        booking,
      }
    }
    return {
      ...slot,
      available: true,
      status: 'available',
      isPast,
    }
  })
})

const availableTimeOptions = computed(() => {
  return timeSlots.value.filter(
    (slot) =>
      slot.available || (selectedSlotData.value && slot.time === selectedSlotData.value.time)
  )
})

// Methods
const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
}

const fetchFutsalData = async () => {
  const futsalId = route.params.id
  try {
    const response = await apiClient.get(`futsal/retrieve-futsal/${futsalId}/`)
    futsal.value = response.data
  } catch (error) {
    console.error('Error fetching futsal:', error)
  }
}

const fetchUserData = async () => {
  try {
    const response = await apiClient.get('auth/user/')
    currentUser.value = response.data
    isAuthorized.value = futsal.value.futsal_owner === currentUser.value.pk
  } catch (error) {
    console.error('Error fetching user:', error)
    isAuthorized.value = false
  }
}

const fetchBookings = async () => {
  const futsalId = route.params.id
  try {
    const response = await apiClient.get(`booking/list-bookings/${futsalId}/`)
    bookings.value = response.data
  } catch (error) {
    console.error('Error fetching bookings:', error)
    bookings.value = []
  }
}

const updateNepalTime = () => {
  const now = new Date()
  const nepalOffset = 5.75 * 60 * 60 * 1000 // UTC+5:45 in milliseconds
  currentNepalTime.value = new Date(now.getTime())
}

const selectSlot = (slot) => {
  selectedSlot.value = slot.time
  selectedSlotData.value = slot
  editedTime.value = slot.time
  editedNotes.value = slot.booking?.booking_notes || ''
  if (slot.booking) {
    bookingUser.value = slot.booking.user
    editedStatus.value = slot.booking.booking_status
  } else {
    bookingUser.value = null
    editedStatus.value = true // Default to confirmed for new bookings
  }
}

const closeModal = () => {
  selectedSlot.value = null
  selectedSlotData.value = null
  bookingUser.value = null
  editedTime.value = ''
  editedStatus.value = null
  editedNotes.value = ''
}

const updateBooking = async () => {
  if (!selectedSlotData.value?.booking) return

  isSubmitting.value = true
  const bookingId = selectedSlotData.value.booking.id
  const [startHour] = editedTime.value.split('-')
  const bookingData = {
    booking_start_time: `${startHour.padStart(2, '0')}:00:00`,
    booking_end_time: `${(parseInt(startHour) + 1).toString().padStart(2, '0')}:00:00`,
    booking_status: editedStatus.value,
    booking_notes: editedNotes.value || null,
  }

  try {
    await apiClient.patch(`booking/update-booking/${bookingId}/`, bookingData)
    await fetchBookings()
    closeModal()
    alert('Booking updated successfully!')
  } catch (error) {
    console.error('Error updating booking:', error)
    alert('Failed to update booking')
  } finally {
    isSubmitting.value = false
  }
}

const createBooking = async () => {
  isSubmitting.value = true
  const [startHour] = selectedSlot.value.split('-')
  const bookingData = {
    user: currentUser.value.pk,
    booking_date: selectedDate.value,
    booking_start_time: `${startHour.padStart(2, '0')}:00:00`,
    booking_end_time: `${(parseInt(startHour) + 1).toString().padStart(2, '0')}:00:00`,
    booking_status: editedStatus.value,
    booking_notes: editedNotes.value || null,
    futsal: route.params.id,
  }

  try {
    await apiClient.post('booking/create-booking/', bookingData)
    await fetchBookings()
    closeModal()
    alert('Booking created successfully!')
  } catch (error) {
    console.error('Error creating booking:', error)
    alert('Failed to create booking')
  } finally {
    isSubmitting.value = false
  }
}

const deleteBooking = async () => {
  if (!selectedSlotData.value?.booking || !confirm('Are you sure you want to delete this booking?'))
    return

  isSubmitting.value = true
  const bookingId = selectedSlotData.value.booking.id
  try {
    await apiClient.delete(`booking/delete-booking/${bookingId}/`)
    await fetchBookings()
    closeModal()
    alert('Booking deleted successfully!')
  } catch (error) {
    console.error('Error deleting booking:', error)
    alert('Failed to delete booking')
  } finally {
    isSubmitting.value = false
  }
}

// Watch for date changes
watch(selectedDate, () => {
  selectedSlot.value = null
  selectedSlotData.value = null
  bookingUser.value = null
  fetchBookings()
})

onMounted(async () => {
  const now = new Date()
  today.value = now.toISOString().split('T')[0]
  selectedDate.value = today.value

  updateNepalTime()
  const timeUpdateInterval = setInterval(updateNepalTime, 60000)

  try {
    // Fetch futsal data first
    await fetchFutsalData()
    // Then fetch user data and check authorization
    await fetchUserData()
    // Finally fetch bookings
    await fetchBookings()
  } catch (error) {
    console.error('Error during initialization:', error)
    isAuthorized.value = false // Fallback to unauthorized if any fetch fails
  } finally {
    isLoading.value = false
  }

  return () => {
    clearInterval(timeUpdateInterval)
  }
})
</script>

<style scoped>
.stats-page {
  min-height: 100vh;
  background-color: #f8f9fa;
  padding: 40px 20px;
  font-family: 'Inter', 'Segoe UI', Roboto, sans-serif;
  color: #333333;
}

.stats-container {
  max-width: 1200px;
  margin: 0 auto;
}

.page-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #2e7d32;
  margin-bottom: 40px;
  text-align: center;
}

.date-selection {
  margin-bottom: 20px;
  max-width: 300px;
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
  opacity: 0.8;
}

.time-slot.pending {
  background-color: #fff9c4;
  color: #f9a825;
  opacity: 0.8;
}

.time-slot.past {
  background-color: #e0e0e0;
  color: #757575;
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

.booking-modal {
  background-color: white;
  border-radius: 12px;
  padding: 24px;
  width: 90%;
  max-width: 500px;
}

.booking-details p {
  margin: 10px 0;
  color: #333;
}

.booking-actions {
  margin-top: 20px;
}

.time-edit,
.status-edit,
.notes-edit {
  margin-bottom: 20px;
}

.time-edit label,
.status-edit label,
.notes-edit label {
  display: block;
  font-weight: 600;
  margin-bottom: 8px;
  color: #555;
}

.time-select,
.status-select {
  width: 100%;
  padding: 10px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 1rem;
}

.notes-input {
  width: 100%;
  padding: 10px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 1rem;
  min-height: 100px;
  resize: vertical;
}

.action-buttons {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.save-btn,
.delete-btn,
.close-btn {
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.save-btn {
  background-color: #2e7d32;
  color: white;
}

.save-btn:hover:not(:disabled) {
  background-color: #1b5e20;
}

.delete-btn {
  background-color: #c62828;
  color: white;
}

.delete-btn:hover:not(:disabled) {
  background-color: #b71c1c;
}

.close-btn {
  background-color: #e0e0e0;
  color: #333;
}

.close-btn:hover {
  background-color: #d0d0d0;
}

.unauthorized-message {
  text-align: center;
  padding: 40px;
  max-width: 600px;
  margin: 0 auto;
}

.unauthorized-message h1 {
  color: #c62828;
  font-size: 2rem;
  margin-bottom: 20px;
}

.back-home-btn {
  display: inline-block;
  padding: 12px 24px;
  background-color: #2e7d32;
  color: white;
  text-decoration: none;
  border-radius: 8px;
  margin-top: 20px;
}

.back-home-btn:hover {
  background-color: #1b5e20;
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

@media (max-width: 600px) {
  .time-slots-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>