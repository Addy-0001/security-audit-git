<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue'
import FutsalAdminNavbar from './components/FutsalAdminNavbar.vue'
import Footer from './components/Footer.vue'
import { useAuthStore } from '@/stores/auth'
import { ref, onMounted } from 'vue'
import apiClient from '@/axios'

const authStore = useAuthStore()
const isFutsalAdmin = ref(false)
const user = ref(null)
const userProfile = ref(null)

const fetchUserData = async () => {
  try {
    const response = await apiClient.get('auth/user/')
    user.value = response.data
    return user.value.pk
  } catch (err) {
    console.error('Error fetching user data:', err)
    if (err.response?.status === 401) {
      authStore.logout()
    }
    throw err
  }
}

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
    isFutsalAdmin.value = userProfile.value.is_futsal_admin
  } catch (err) {
    if (err.response?.status === 404) {
      isFutsalAdmin.value = false
    } else {
      console.error('Error fetching user profile:', err)
      throw err
    }
  }
}

const verifyToken = async () => {
  try {
    await authStore.verifyAuth()
    if (authStore.isLoggedIn) {
      const userPk = await fetchUserData()
      if (userPk) {
        await fetchUserProfile(userPk)
      }
    }
  } catch (error) {
    authStore.logout()
    isFutsalAdmin.value = false
  }
}

onMounted(() => {
  verifyToken()
})

window.addEventListener('storage', () => {
  authStore.checkAuth()
})
</script>

<template>
  <div class="main">
    <Navbar />
    <div>
      <RouterView />
    </div>
    <Footer />
  </div>
</template>

<style>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* CSS Reset and Base Styles */
:root {
  /* Primary Colors */
  --primary-50: #f0fdf4;
  --primary-100: #dcfce7;
  --primary-200: #bbf7d0;
  --primary-300: #86efac;
  --primary-400: #4ade80;
  --primary-500: #22c55e;
  --primary-600: #16a34a;
  --primary-700: #15803d;
  --primary-800: #166534;
  --primary-900: #14532d;

  /* Gray Colors */
  --gray-50: #f9fafb;
  --gray-100: #f3f4f6;
  --gray-200: #e5e7eb;
  --gray-300: #d1d5db;
  --gray-400: #9ca3af;
  --gray-500: #6b7280;
  --gray-600: #4b5563;
  --gray-700: #374151;
  --gray-800: #1f2937;
  --gray-900: #111827;

  /* Other Colors */
  --red-500: #ef4444;
  --yellow-500: #f59e0b;
  --blue-500: #3b82f6;

  /* Shadows */
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);

  /* Border Radius */
  --radius-sm: 0.25rem;
  --radius: 0.375rem;
  --radius-md: 0.5rem;
  --radius-lg: 0.75rem;
  --radius-xl: 1rem;
  --radius-full: 9999px;
}

/* Global Reset */
*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-size: 16px;
  -webkit-text-size-adjust: 100%;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu,
    Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  line-height: 1.5;
  color: var(--gray-900);
  background-color: #ffffff;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  padding-top: 4rem;
}

#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Typography */
h1,
h2,
h3,
h4,
h5,
h6 {
  font-weight: 700;
  line-height: 1.2;
  margin-bottom: 0.5rem;
  color: var(--gray-900);
}

h1 {
  font-size: 2rem;
}

h2 {
  font-size: 1.5rem;
}

h3 {
  font-size: 1.25rem;
}

h4 {
  font-size: 1.125rem;
}

p {
  margin-bottom: 1rem;
}

a {
  color: var(--primary-600);
  text-decoration: none;
  transition: color 0.2s;
}

a:hover {
  color: var(--primary-700);
}

/* Form Elements */
input,
textarea,
select,
button {
  font-family: inherit;
  font-size: 1rem;
}

input,
textarea,
select {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid var(--gray-200);
  border-radius: var(--radius);
  background-color: white;
  color: var(--gray-900);
  transition: border-color 0.2s, box-shadow 0.2s;
}

input:focus,
textarea:focus,
select:focus {
  outline: none;
  border-color: var(--primary-500);
  box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.2);
}

button {
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.75rem 1.5rem;
  font-weight: 600;
  border-radius: var(--radius);
  transition: all 0.2s;
  border: none;
}

button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

/* Button Variants */
.btn-primary {
  background-color: var(--primary-600);
  color: white;
}

.btn-primary:hover:not(:disabled) {
  background-color: var(--primary-700);
}

.btn-secondary {
  background-color: var(--gray-100);
  color: var(--gray-700);
  border: 1px solid var(--gray-200);
}

.btn-secondary:hover:not(:disabled) {
  background-color: var(--gray-200);
}

.btn-danger {
  background-color: var(--red-500);
  color: white;
}

.btn-danger:hover:not(:disabled) {
  background-color: #dc2626;
}

/* Card Styles */
.card {
  background-color: white;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow);
  overflow: hidden;
}

.card-header {
  padding: 1.25rem 1.5rem;
  border-bottom: 1px solid var(--gray-200);
}

.card-body {
  padding: 1.5rem;
}

.card-footer {
  padding: 1.25rem 1.5rem;
  border-top: 1px solid var(--gray-200);
}

/* Utility Classes */
.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.text-center {
  text-align: center;
}

.text-right {
  text-align: right;
}

.flex {
  display: flex;
}

.flex-col {
  flex-direction: column;
}

.items-center {
  align-items: center;
}

.justify-center {
  justify-content: center;
}

.justify-between {
  justify-content: space-between;
}

.gap-1 {
  gap: 0.25rem;
}

.gap-2 {
  gap: 0.5rem;
}

.gap-4 {
  gap: 1rem;
}

.gap-8 {
  gap: 2rem;
}

.mt-1 {
  margin-top: 0.25rem;
}

.mt-2 {
  margin-top: 0.5rem;
}

.mt-4 {
  margin-top: 1rem;
}

.mt-8 {
  margin-top: 2rem;
}

.mb-1 {
  margin-bottom: 0.25rem;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.mb-4 {
  margin-bottom: 1rem;
}

.mb-8 {
  margin-bottom: 2rem;
}

.p-2 {
  padding: 0.5rem;
}

.p-4 {
  padding: 1rem;
}

.p-6 {
  padding: 1.5rem;
}

.rounded {
  border-radius: var(--radius);
}

.rounded-lg {
  border-radius: var(--radius-lg);
}

.rounded-full {
  border-radius: var(--radius-full);
}

.shadow {
  box-shadow: var(--shadow);
}

.shadow-md {
  box-shadow: var(--shadow-md);
}

.shadow-lg {
  box-shadow: var(--shadow-lg);
}

.text-sm {
  font-size: 0.875rem;
}

.text-lg {
  font-size: 1.125rem;
}

.text-xl {
  font-size: 1.25rem;
}

.text-2xl {
  font-size: 1.5rem;
}

.font-medium {
  font-weight: 500;
}

.font-semibold {
  font-weight: 600;
}

.font-bold {
  font-weight: 700;
}

.text-primary {
  color: var(--primary-600);
}

.text-gray {
  color: var(--gray-500);
}

.text-error {
  color: var(--red-500);
}

.bg-primary {
  background-color: var(--primary-600);
}

.bg-light {
  background-color: var(--gray-50);
}

.bg-white {
  background-color: white;
}

.border {
  border: 1px solid var(--gray-200);
}

.border-primary {
  border-color: var(--primary-600);
}

/* Responsive Utilities */
@media (min-width: 640px) {
  .sm\:flex {
    display: flex;
  }

  .sm\:grid-cols-2 {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 768px) {
  .md\:flex {
    display: flex;
  }

  .md\:grid-cols-3 {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (min-width: 1024px) {
  .lg\:flex {
    display: flex;
  }

  .lg\:grid-cols-4 {
    grid-template-columns: repeat(4, 1fr);
  }
}

/* Animation Utilities */
.transition {
  transition-property: background-color, border-color, color, fill, stroke, opacity, box-shadow,
    transform;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

.hover\:shadow-md:hover {
  box-shadow: var(--shadow-md);
}

.hover\:scale-105:hover {
  transform: scale(1.05);
}

/* Specific Component Styles */
.futsal-badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  padding: 0.375rem 0.75rem;
  border-radius: var(--radius);
  font-size: 0.75rem;
  font-weight: 600;
  color: white;
}

.futsal-badge-popular {
  background-color: var(--primary-600);
}

.futsal-badge-new {
  background-color: var(--blue-500);
}

.futsal-badge-hot {
  background-color: var(--red-500);
}

.star-icon.filled {
  color: var(--yellow-500);
}

.star-icon.empty {
  color: var(--gray-300);
}

/* Fix for SVG icons */
svg {
  display: inline-block;
  vertical-align: middle;
}
</style>
