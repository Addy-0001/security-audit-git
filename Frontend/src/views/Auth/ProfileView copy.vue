<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import apiClient from '@/axios'
import { notificationService } from '@/services/notificationService'

const router = useRouter()

// State for user data
const user = ref({
  pk: null,
  username: '',
  email: '',
  first_name: '',
  last_name: '',
})

// State for user profile
const userProfile = ref({
  bio: '',
  address: '',
  city: '',
  country: '',
  zip_code: '',
  profile_picture: '',
  is_verified: false,
  is_futsal_admin: false,
})

// State for editing profile
const isEditing = ref(false)
const formData = ref({
  bio: '',
  address: '',
  profile_picture: null,
})
const formError = ref('')
const isSaving = ref(false)

// State for settings popup
const showSettingsPopup = ref(false)
const passwordForm = ref({
  old_password: '',
  new_password1: '',
  new_password2: '',
})
const passwordError = ref('')
const isPasswordSaving = ref(false)

// State for futsals
const futsals = ref([])

// State for notifications
const isNotificationEnabled = ref(false)
const notificationError = ref('')

// State for bookings
const bookings = ref([])
const loadingBookings = ref(false)
const bookingError = ref(null)

// Loading and error states
const isLoading = ref(true)
const error = ref(null)

// Check if user is authenticated
const isAuthenticated = () => {
  return !!localStorage.getItem('token')
}

// Fetch user data
const fetchUserData = async () => {
  try {
    const response = await apiClient.get('auth/user/')
    user.value = response.data
    return user.value.pk
  } catch (err) {
    console.error('Error fetching user data:', err)
    if (err.response?.status === 401) {
      router.push('/login')
    }
    throw err
  }
}

// Fetch user profile
const fetchUserProfile = async (userPk) => {
  try {
    const response = await apiClient.get(`user/profile/retrieve-user-profile/${userPk}/`)
    userProfile.value = {
      bio: response.data.bio,
      address: response.data.address,
      city: response.data.city,
      country: response.data.country,
      zip_code: response.data.zip_code,
      profile_picture: response.data.profile_picture,
      is_verified: response.data.is_verified,
      is_futsal_admin: response.data.is_futsal_admin,
    }
    formData.value.bio = response.data.bio || ''
    formData.value.address = response.data.address || ''
    formData.value.profile_picture = null
  } catch (err) {
    if (err.response?.status === 404) {
      router.push('/profile/create')
    } else {
      console.error('Error fetching user profile:', err)
      throw err
    }
  }
}

// Fetch user's futsals
const fetchFutsals = async (userPk) => {
  try {
    const response = await apiClient.get('futsal/list-futsals/')
    futsals.value = response.data.filter((futsal) => futsal.futsal_owner === userPk)
  } catch (err) {
    console.error('Error fetching futsals:', err)
    throw err
  }
}

// Fetch last 10 bookings
const fetchBookings = async (userPk) => {
  try {
    loadingBookings.value = true
    bookingError.value = null

    const response = await apiClient.get(`booking/list-bookings/user/${userPk}/`)

    if (!Array.isArray(response.data)) {
      throw new Error('Unexpected API response format')
    }

    const normalizedBookings = response.data
      .map((booking) => ({
        id: booking.id || '',
        futsalName: booking.futsal?.futsal_name || 'Unknown Futsal',
        location: booking.futsal?.location || 'Unknown Location',
        date: booking.booking_date || '',
        timeSlot: `${booking.booking_start_time?.slice(0, 5)} - ${booking.booking_end_time?.slice(
          0,
          5
        )}`,
        status: booking.status || 'pending',
      }))
      .filter((booking) => booking !== null)
      .sort((a, b) => new Date(b.date) - new Date(a.date))
      .slice(0, 10)

    bookings.value = normalizedBookings
  } catch (err) {
    console.error('Error fetching bookings:', err)
    bookingError.value = handleApiError(err)
  } finally {
    loadingBookings.value = false
  }
}

// Handle API errors
const handleApiError = (err) => {
  if (!navigator.onLine) {
    return 'No internet connection. Please check your network.'
  }
  if (err.response) {
    switch (err.response.status) {
      case 401:
        return 'Your session has expired. Please log in again.'
      case 403:
        return 'You are not authorized to view these bookings.'
      case 404:
        return 'No bookings found for your account.'
      case 500:
        return 'Something went wrong on our server. Please try again later.'
      default:
        return 'An unexpected error occurred. Please try again.'
    }
  }
  return 'Failed to load bookings. Please try again later.'
}

// Initialize profile data
const initializeProfile = async () => {
  if (!isAuthenticated()) {
    router.push('/login')
    return
  }

  try {
    isLoading.value = true
    error.value = null

    const userPk = await fetchUserData()
    await fetchUserProfile(userPk)
    await fetchFutsals(userPk)
    await fetchBookings(userPk)

    // Check notification status for futsal admins
    if (userProfile.value.is_futsal_admin) {
      isNotificationEnabled.value = Notification.permission === 'granted'
      notificationService.setupForegroundNotifications()
    }
  } catch (err) {
    error.value = 'Failed to load profile data. Please try again.'
  } finally {
    isLoading.value = false
  }
}

// Toggle notifications
const toggleNotifications = async () => {
  if (isNotificationEnabled.value) {
    // Disable notifications (clear token in backend)
    try {
      await apiClient.post(
        'user/update-fcm-token/',
        { fcm_token: null },
        {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`,
          },
        }
      )
      isNotificationEnabled.value = false
    } catch (err) {
      console.error('Error disabling notifications:', err)
      notificationError.value = 'Failed to disable notifications.'
    }
  } else {
    // Enable notifications
    try {
      const token = await notificationService.initializeNotifications()
      if (token) {
        isNotificationEnabled.value = true
        notificationError.value = ''
      } else {
        notificationError.value = 'Notifications not enabled. Please allow permissions.'
      }
    } catch (err) {
      console.error('Error enabling notifications:', err)
      notificationError.value = 'Failed to enable notifications.'
    }
  }
}

// Toggle edit mode for profile
const toggleEdit = () => {
  isEditing.value = !isEditing.value
  if (!isEditing.value) {
    formData.value.bio = userProfile.value.bio || ''
    formData.value.address = userProfile.value.address || ''
    formData.value.profile_picture = null
    formError.value = ''
  }
}

// Handle profile update
const handleUpdate = async () => {
  try {
    isSaving.value = true
    formError.value = ''

    const updateData = new FormData()
    updateData.append('user', user.value.pk)
    if (formData.value.bio !== userProfile.value.bio) {
      updateData.append('bio', formData.value.bio)
    }
    if (formData.value.address !== userProfile.value.address) {
      updateData.append('address', formData.value.address)
    }
    if (formData.value.profile_picture) {
      updateData.append('profile_picture', formData.value.profile_picture)
    }

    if (updateData.has('bio') || updateData.has('address') || updateData.has('profile_picture')) {
      const response = await apiClient.patch(
        `/user/profile/update-user-profile/${user.value.pk}/`,
        updateData,
        { headers: { 'Content-Type': 'multipart/form-data' } }
      )
      userProfile.value.bio = response.data.bio
      userProfile.value.address = response.data.address
      userProfile.value.profile_picture = response.data.profile_picture
    }

    toggleEdit()
  } catch (err) {
    console.error('Error updating profile:', err)
    formError.value = err.response?.data?.non_field_errors?.[0] || 'Failed to update profile.'
  } finally {
    isSaving.value = false
  }
}

// Handle settings popup and password update
const openSettings = () => {
  showSettingsPopup.value = true
  passwordError.value = ''
  passwordForm.value = { old_password: '', new_password1: '', new_password2: '' }
}

const closeSettingsPopup = () => {
  showSettingsPopup.value = false
}

const updatePassword = async () => {
  if (passwordForm.value.new_password1 !== passwordForm.value.new_password2) {
    passwordError.value = 'New passwords do not match.'
    return
  }

  try {
    isPasswordSaving.value = true
    passwordError.value = ''

    const response = await apiClient.post('/auth/password/change/', {
      old_password: passwordForm.value.old_password,
      new_password1: passwordForm.value.new_password1,
      new_password2: passwordForm.value.new_password2,
    })

    if (response.status === 200 || response.status === 204) {
      closeSettingsPopup()
      alert('Password updated successfully!')
    }
  } catch (err) {
    console.error('Error updating password:', err)
    passwordError.value =
      err.response?.data?.detail ||
      err.response?.data?.old_password?.[0] ||
      'Failed to update password.'
  } finally {
    isPasswordSaving.value = false
  }
}

// Methods for profile actions
const editProfilePicture = () => {
  toggleEdit()
}

const editProfile = () => {
  router.push('/profile/edit')
}

const editUserDetails = () => {
  toggleEdit()
}

const addNewFutsal = () => {
  router.push('/add-futsal')
}

const viewFutsal = (id) => {
  router.push(`/futsals/${id}`)
}

const editFutsal = (id) => {
  router.push(`/futsal/${id}/edit`)
}

const viewStats = (id) => {
  router.push(`/futsal/${id}/stats`)
}

const viewAllBookings = () => {
  router.push('/bookings')
}

const viewBooking = (id) => {
  router.push(`/bookings`)
}

// Mount the component and fetch data
onMounted(() => {
  initializeProfile()
})
</script>

<template>
  <div class="profile-page">
    <!-- Loading State -->
    <div v-if="isLoading" style="margin: auto; padding-top: 50vh">
      <div class="spinner-profile" style="margin: auto"></div>
    </div>
    <!-- Error State -->
    <div v-else-if="error" class="error">{{ error }}</div>

    <!-- Profile Content -->
    <div v-else>
      <!-- Profile Header -->
      <div class="profile-header">
        <div class="container">
          <div class="profile-header-content">
            <div class="profile-avatar-wrapper">
              <img :src="userProfile.profile_picture || 'https://via.placeholder.com/150'" alt="Profile Picture"
                class="profile-avatar" />
              <div class="edit-avatar-button" @click="editProfilePicture">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                  stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                  <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                </svg>
              </div>
            </div>

            <div class="profile-info">
              <div class="profile-name-wrapper">
                <h1 class="profile-name">{{ user.first_name }} {{ user.last_name }}</h1>
                <div v-if="userProfile.is_verified" class="verified-badge" title="Verified Account">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                    <polyline points="22 4 12 14.01 9 11.01"></polyline>
                  </svg>
                </div>
              </div>

              <div class="profile-contact">
                <div class="contact-item">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                    <polyline points="22,6 12,13 2,6"></polyline>
                  </svg>
                  <span>{{ user.email }}</span>
                </div>

                <div class="contact-item">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                    <circle cx="12" cy="7" r="4"></circle>
                  </svg>
                  <span>ID: {{ user.pk }}</span>
                </div>
              </div>

              <div class="profile-actions">
                <button class="edit-profile-btn" @click="editProfile">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                    <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                  </svg>
                  Edit User
                </button>
                <button class="settings-btn" @click="openSettings">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="3"></circle>
                    <path
                      d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l-.06-.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z">
                    </path>
                  </svg>
                  Change Password
                </button>
                <button v-if="userProfile.is_futsal_admin" class="notification-btn" @click="toggleNotifications">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                    <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
                  </svg>
                  {{ isNotificationEnabled ? 'Disable Notifications' : 'Enable Notifications' }}
                </button>
              </div>
              <p v-if="notificationError" class="notification-error">{{ notificationError }}</p>
            </div>
          </div>
        </div>
      </div>

      <div class="container">
        <div class="profile-content">
          <!-- User Details Section -->
          <section class="profile-section user-details-section">
            <div class="section-header">
              <h2>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                  stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
                User Details
              </h2>
              <button class="edit-section-btn" @click="editUserDetails">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                  stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                  <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                </svg>
              </button>
            </div>

            <div class="user-details-content">
              <div class="detail-item">
                <div class="detail-label">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                    <circle cx="12" cy="7" r="4"></circle>
                  </svg>
                  Username
                </div>
                <div class="detail-value">{{ user.username }}</div>
              </div>

              <div class="detail-item">
                <div class="detail-label">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                    <polyline points="22,6 12,13 2,6"></polyline>
                  </svg>
                  Email
                </div>
                <div class="detail-value">{{ user.email }}</div>
              </div>

              <div class="detail-item">
                <div class="detail-label">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="10"></circle>
                    <path d="M12 8v8"></path>
                    <path d="M8 12h8"></path>
                  </svg>
                  Bio
                </div>
                <div class="detail-value" v-if="!isEditing">
                  {{ userProfile.bio || 'Not set' }}
                </div>
                <textarea v-else v-model="formData.bio" class="edit-input" placeholder="Enter your bio"
                  rows="3"></textarea>
              </div>

              <div class="detail-item">
                <div class="detail-label">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                    <circle cx="12" cy="10" r="3"></circle>
                  </svg>
                  Address
                </div>
                <div class="detail-value" v-if="!isEditing">
                  {{
                    userProfile.address
                      ? `${userProfile.address}, ${userProfile.city},
                  ${userProfile.country} ${userProfile.zip_code}`
                      : 'Not set'
                  }}
                </div>
                <div v-else>
                  <input type="text" v-model="formData.address" class="edit-input" placeholder="Enter your address" />
                  <div class="address-note">City, country, and zip code remain unchanged here.</div>
                </div>
              </div>

              <div class="detail-item" v-if="isEditing">
                <div class="detail-label">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                    <circle cx="8.5" cy="8.5" r="1.5"></circle>
                    <polyline points="21 15 16 10 5 21"></polyline>
                  </svg>
                  Profile Picture
                </div>
                <input type="file" @change="formData.profile_picture = $event.target.files[0]" class="edit-file-input"
                  accept="image/*" />
              </div>

              <div class="detail-item" v-if="userProfile.is_futsal_admin">
                <div class="detail-label">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                    <circle cx="12" cy="7" r="4"></circle>
                  </svg>
                  Role
                </div>
                <div class="detail-value">Futsal Admin</div>
              </div>

              <div v-if="isEditing" class="form-actions">
                <button class="save-btn" @click="handleUpdate" :disabled="isSaving">
                  <span v-if="!isSaving">Save Changes</span>
                  <div v-else class="spinner"></div>
                </button>
                <button class="cancel-btn" @click="toggleEdit" :disabled="isSaving">Cancel</button>
                <p v-if="formError" class="form-error">{{ formError }}</p>
              </div>
            </div>
          </section>

          <!-- Your Futsals Section -->
          <section class="profile-section futsals-section" v-if="userProfile.is_futsal_admin">
            <div class="section-header">
              <h2>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                  stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"></circle>
                  <polygon points="10 8 16 12 10 16 10 8"></polygon>
                </svg>
                Your Futsals
              </h2>
              <button class="add-futsal-btn" @click="addNewFutsal">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                  stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"></circle>
                  <line x1="12" y1="8" x2="12" y2="16"></line>
                  <line x1="8" y1="12" x2="16" y2="12"></line>
                </svg>
                Add New
              </button>
            </div>

            <div class="futsals-grid">
              <div v-for="futsal in futsals" :key="futsal.id" class="futsal-card">
                <div class="futsal-image-container">
                  <img :src="futsal.futsal_image_1 || 'https://via.placeholder.com/300x200'" :alt="futsal.name"
                    class="futsal-image" />
                  <div class="futsal-status" :class="{ active: futsal.is_active }">
                    {{ futsal.is_active ? 'Active' : 'Inactive' }}
                  </div>
                </div>

                <div class="futsal-content">
                  <h3 class="futsal-name">{{ futsal.futsal_name }}</h3>
                  <p class="futsal-description" v-html="futsal.futsal_description || 'No description available'"></p>

                  <div class="futsal-meta">
                    <div class="futsal-meta-item">
                      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                        <circle cx="12" cy="10" r="3"></circle>
                      </svg>
                      <span>{{ futsal.location || 'Not specified' }}</span>
                    </div>

                    <div class="futsal-meta-item">
                      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="16" y1="2" x2="16" y2="6"></line>
                        <line x1="8" y1="2" x2="8" y2="6"></line>
                        <line x1="3" y1="10" x2="21" y2="10"></line>
                      </svg>
                      <span>{{ new Date(futsal.date_created).toLocaleDateString() }}</span>
                    </div>
                  </div>

                  <div class="futsal-id">ID: {{ futsal.id }}</div>

                  <div class="futsal-actions">
                    <!-- <button class="futsal-action-btn view-btn" @click="viewFutsal(futsal.id)">
                                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                                stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                stroke-linejoin="round">
                                                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                                                <circle cx="12" cy="12" r="3"></circle>
                                            </svg>
                                            View
                                        </button>

                                        <button class="futsal-action-btn edit-btn" @click="editFutsal(futsal.id)">
                                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                                stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                stroke-linejoin="round">
                                                <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7">
                                                </path>
                                                <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z">
                                                </path>
                                            </svg>
                                            Edit
                                        </button> -->

                    <button class="futsal-action-btn stats-btn" @click="viewStats(futsal.id)">
                      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="18" y1="20" x2="18" y2="10"></line>
                        <line x1="12" y1="20" x2="12" y2="4"></line>
                        <line x1="6" y1="20" x2="6" y2="14"></line>
                      </svg>
                      Admin
                    </button>

                    <router-link :to="`/futsal/${futsal.id}/add-regular-booking`"
                      class="futsal-action-btn regular-booking-btn">
                      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="16" y1="2" x2="16" y2="6"></line>
                        <line x1="8" y1="2" x2="8" y2="6"></line>
                        <line x1="3" y1="10" x2="21" y2="10"></line>
                      </svg>
                      Regular Bookings
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
          </section>
          <section style="text-align: center" v-else>
            <h1 class="profile-name" style="margin-bottom: 20px">
              Are you a futsal owner? Register your own futsal here.
            </h1>
            <RouterLink to="/add-futsal">
              <button class="add-futsal-btn" style="margin: 0 auto">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                  stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"></circle>
                  <line x1="12" y1="8" x2="12" y2="16"></line>
                  <line x1="8" y1="12" x2="16" y2="12"></line>
                </svg>
                Add Futsal
              </button>
            </RouterLink>
          </section>

          <!-- Recent Bookings Section -->
          <section class="profile-section bookings-section">
            <div class="section-header">
              <h2>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                  stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                  <line x1="16" y1="2" x2="16" y2="6"></line>
                  <line x1="8" y1="2" x2="8" y2="6"></line>
                  <line x1="3" y1="10" x2="21" y2="10"></line>
                </svg>
                Recent Bookings
              </h2>
              <button class="view-all-btn" @click="viewAllBookings">
                View All
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                  stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="9 18 15 12 9 6"></polyline>
                </svg>
              </button>
            </div>

            <div class="bookings-table-container">
              <div v-if="loadingBookings" class="spinner-profile" style="margin: 20px auto"></div>
              <div v-else-if="bookingError" class="error">{{ bookingError }}</div>
              <table v-else class="bookings-table">
                <thead>
                  <tr>
                    <th>Futsal</th>
                    <th>Date</th>
                    <th>Time</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-if="bookings.length === 0">
                    <td colspan="4">No bookings found.</td>
                  </tr>
                  <tr v-for="booking in bookings" :key="booking.id" @click="viewBooking(booking.id)"
                    style="cursor: pointer">
                    <td>{{ booking.futsalName }}</td>
                    <td>{{ new Date(booking.date).toLocaleDateString() }}</td>
                    <td>{{ booking.timeSlot }}</td>
                    <td>{{ booking.status.charAt(0).toUpperCase() + booking.status.slice(1) }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </section>
        </div>
      </div>

      <!-- Settings Popup -->
      <div v-if="showSettingsPopup" class="modal-overlay" @click.self="closeSettingsPopup">
        <div class="modal">
          <div class="modal-header">
            <h2>Change Password</h2>
            <button class="close-btn" @click="closeSettingsPopup">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
              </svg>
            </button>
          </div>
          <div class="modal-body">
            <div class="form-group">
              <label for="current-password">Current Password</label>
              <input type="password" id="current-password" v-model="passwordForm.old_password" class="modal-input"
                placeholder="Enter current password" />
            </div>
            <div class="form-group">
              <label for="new-password">New Password</label>
              <input type="password" id="new-password" v-model="passwordForm.new_password1" class="modal-input"
                placeholder="Enter new password" />
            </div>
            <div class="form-group">
              <label for="confirm-password">Confirm New Password</label>
              <input type="password" id="confirm-password" v-model="passwordForm.new_password2" class="modal-input"
                placeholder="Confirm new password" />
            </div>
            <p v-if="passwordError" class="form-error">{{ passwordError }}</p>
          </div>
          <div class="modal-footer">
            <button class="save-btn" @click="updatePassword" :disabled="isPasswordSaving">
              <span v-if="!isPasswordSaving">Save</span>
              <div v-else class="spinner"></div>
            </button>
            <button class="cancel-btn" @click="closeSettingsPopup" :disabled="isPasswordSaving">
              Cancel
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.profile-page {
  min-height: 100vh;
  background-color: #f8f9fa;
  font-family: 'Inter', 'Segoe UI', Roboto, sans-serif;
  color: #333;
}

.profile-header {
  background-color: #ffffff;
  padding: 40px 0;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  margin-bottom: 30px;
}

.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.profile-header-content {
  display: flex;
  align-items: center;
  gap: 30px;
}

.profile-avatar-wrapper {
  position: relative;
}

.profile-avatar {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid #ffffff;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.edit-avatar-button {
  position: absolute;
  bottom: 5px;
  right: 5px;
  width: 36px;
  height: 36px;
  background-color: #2e7d32;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  transition: all 0.2s ease;
}

.edit-avatar-button:hover {
  background-color: #1b5e20;
  transform: scale(1.1);
}

.edit-avatar-button svg {
  width: 18px;
  height: 18px;
  color: white;
}

.profile-info {
  flex: 1;
}

.profile-name-wrapper {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}

.profile-name {
  font-size: 2.25rem;
  font-weight: 700;
  color: #2e7d32;
  margin: 0;
}

.verified-badge {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  background-color: #2e7d32;
  border-radius: 50%;
}

.verified-badge svg {
  width: 16px;
  height: 16px;
  color: white;
}

.profile-contact {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #666;
}

.contact-item svg {
  width: 16px;
  height: 16px;
  color: #2e7d32;
}

.profile-actions {
  display: flex;
  gap: 15px;
}

.edit-profile-btn,
.settings-btn,
.notification-btn,
.add-futsal-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 16px;
  border: none;
  border-radius: 8px;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.edit-profile-btn,
.add-futsal-btn {
  background-color: #2e7d32;
  color: white;
}

.edit-profile-btn:hover {
  background-color: #1b5e20;
}

.settings-btn,
.notification-btn {
  background-color: #f1f8e9;
  color: #2e7d32;
}

.settings-btn:hover,
.notification-btn:hover {
  background-color: #e8f5e9;
}

.edit-profile-btn svg,
.settings-btn svg,
.notification-btn svg {
  width: 16px;
  height: 16px;
}

.notification-error {
  font-size: 0.9rem;
  color: #c62828;
  margin-top: 10px;
}

.profile-content {
  display: flex;
  flex-direction: column;
  gap: 30px;
  padding-bottom: 60px;
}

.profile-section {
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  overflow: hidden;
}

.section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
  border-bottom: 1px solid #f0f0f0;
}

.section-header h2 {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 1.25rem;
  font-weight: 700;
  color: #2e7d32;
  margin: 0;
}

.section-header h2 svg {
  width: 20px;
  height: 20px;
  color: #2e7d32;
}

.edit-section-btn,
.add-futsal-btn,
.view-all-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border: none;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.edit-section-btn {
  background-color: transparent;
  color: #2e7d32;
  padding: 8px;
}

.edit-section-btn:hover {
  background-color: #f1f8e9;
}

.add-futsal-btn {
  background-color: #2e7d32;
  color: white;
}

.add-futsal-btn:hover {
  background-color: #1b5e20;
}

.view-all-btn {
  background-color: transparent;
  color: #2e7d32;
}

.view-all-btn:hover {
  text-decoration: underline;
}

.edit-section-btn svg,
.add-futsal-btn svg,
.view-all-btn svg {
  width: 16px;
  height: 16px;
}

.user-details-content {
  padding: 20px;
}

.detail-item {
  display: flex;
  margin-bottom: 16px;
}

.detail-item:last-child {
  margin-bottom: 0;
}

.detail-label {
  display: flex;
  align-items: center;
  gap: 8px;
  width: 150px;
  font-size: 0.95rem;
  font-weight: 600;
  color: #666;
}

.detail-label svg {
  width: 16px;
  height: 16px;
  color: #2e7d32;
}

.detail-value {
  flex: 1;
  font-size: 0.95rem;
  color: #333;
}

.edit-input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 0.95rem;
  color: #333;
  transition: border-color 0.2s ease;
}

.edit-input:focus {
  outline: none;
  border-color: #2e7d32;
  box-shadow: 0 0 0 2px rgba(46, 125, 50, 0.1);
}

.edit-file-input {
  font-size: 0.9rem;
  color: #333;
}

.address-note {
  font-size: 0.85rem;
  color: #999;
  margin-top: 5px;
}

.form-actions {
  display: flex;
  gap: 15px;
  margin-top: 20px;
}

.save-btn,
.cancel-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 16px;
  border: none;
  border-radius: 8px;
  font-size: 0.95rem;
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

.save-btn:disabled {
  background-color: #b0bec5;
  cursor: not-allowed;
}

.cancel-btn {
  background-color: #f1f8e9;
  color: #2e7d32;
}

.cancel-btn:hover:not(:disabled) {
  background-color: #e8f5e9;
}

.spinner {
  width: 20px;
  height: 20px;
  border: 3px solid #ffffff;
  border-top: 3px solid transparent;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.spinner-profile {
  width: 50px;
  height: 50px;
  border: 3px solid #2e7d32;
  border-top: 3px solid transparent;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.form-error {
  font-size: 0.9rem;
  color: #c62828;
  margin-top: 10px;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

.futsals-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 20px;
  padding: 20px;
}

.futsal-card {
  border: 1px solid #f0f0f0;
  border-radius: 10px;
  overflow: hidden;
  transition: all 0.3s ease;
}

.futsal-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.futsal-image-container {
  position: relative;
  height: 180px;
}

.futsal-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.futsal-status {
  position: absolute;
  top: 10px;
  right: 10px;
  padding: 5px 10px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
}

.futsal-status.active {
  background-color: #e8f5e9;
  color: #2e7d32;
}

.futsal-status.inactive {
  background-color: #ffebee;
  color: #c62828;
}

.futsal-content {
  padding: 20px;
}

.futsal-name {
  font-size: 1.25rem;
  font-weight: 700;
  color: #2e7d32;
  margin: 0 0 10px;
}

.futsal-description {
  font-size: 0.95rem;
  color: #666;
  margin: 0 0 15px;
  line-height: 1.5;
}

.futsal-meta {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 15px;
}

.futsal-meta-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.9rem;
  color: #666;
}

.futsal-meta-item svg {
  width: 16px;
  height: 16px;
  color: #2e7d32;
}

.futsal-id {
  font-size: 0.8rem;
  color: #999;
  margin-bottom: 15px;
  font-family: monospace;
}

.futsal-actions {
  display: flex;
  gap: 10px;
}

.futsal-action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
  padding: 8px 12px;
  border: none;
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
}

.futsal-action-btn svg {
  width: 14px;
  height: 14px;
}

.view-btn {
  background-color: #e8f5e9;
  color: #2e7d32;
}

.view-btn:hover {
  background-color: #c8e6c9;
}

.edit-btn {
  background-color: #e3f2fd;
  color: #1976d2;
}

.edit-btn:hover {
  background-color: #bbdefb;
}

.stats-btn {
  background-color: #fff3e0;
  color: #f57c00;
}

.stats-btn:hover {
  background-color: #ffe0b2;
}

.regular-booking-btn {
  background-color: #e1f5fe;
  color: #0277bd;
}

.regular-booking-btn:hover {
  background-color: #b3e5fc;
}

.bookings-table-container {
  padding: 0 20px 20px;
  overflow-x: auto;
}

.bookings-table {
  width: 100%;
  border-collapse: collapse;
}

.bookings-table th,
.bookings-table td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid #f0f0f0;
}

.bookings-table th {
  font-size: 0.9rem;
  font-weight: 600;
  color: #666;
}

.bookings-table td {
  font-size: 0.95rem;
  color: #333;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal {
  background-color: #ffffff;
  border-radius: 12px;
  width: 100%;
  max-width: 500px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  overflow: hidden;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  border-bottom: 1px solid #f0f0f0;
}

.modal-header h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #2e7d32;
  margin: 0;
}

.close-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 5px;
}

.close-btn svg {
  width: 20px;
  height: 20px;
  color: #666;
}

.close-btn:hover svg {
  color: #333;
}

.modal-body {
  padding: 20px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  font-size: 0.95rem;
  font-weight: 600;
  color: #666;
  margin-bottom: 8px;
}

.modal-input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 0.95rem;
  color: #333;
  transition: border-color 0.2s ease;
}

.modal-input:focus {
  outline: none;
  border-color: #2e7d32;
  box-shadow: 0 0 0 2px rgba(46, 125, 50, 0.1);
}

.modal-footer {
  padding: 20px;
  border-top: 1px solid #f0f0f0;
  display: flex;
  gap: 15px;
  justify-content: flex-end;
}

.error {
  color: #c62828;
  text-align: center;
  padding: 20px;
}

@media (max-width: 768px) {
  .profile-header-content {
    flex-direction: column;
    text-align: center;
  }

  .profile-contact {
    justify-content: center;
  }

  .profile-actions {
    justify-content: center;
    flex-wrap: wrap;
  }

  .detail-item {
    flex-direction: column;
    gap: 5px;
  }

  .detail-label {
    width: 100%;
  }

  .futsals-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .profile-name {
    font-size: 1.75rem;
  }

  .profile-avatar {
    width: 120px;
    height: 120px;
  }

  .contact-item {
    font-size: 0.9rem;
  }

  .section-header {
    flex-direction: column;
    gap: 15px;
    align-items: flex-start;
  }

  .futsal-actions {
    flex-wrap: wrap;
  }

  .futsal-action-btn {
    flex: 1;
  }

  .form-actions {
    flex-direction: column;
  }

  .save-btn,
  .cancel-btn {
    width: 100%;
  }

  .modal {
    width: 90%;
    margin: 0 20px;
  }

  .modal-header h2 {
    font-size: 1.25rem;
  }
}
</style>