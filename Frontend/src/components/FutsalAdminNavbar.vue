<template>
  <nav class="navbar">
    <div class="container">
      <div class="navbar-content">
        <!-- Sidebar Toggle Button (Visible on all screens) -->
        <button @click="toggleSidebar" class="sidebar-toggle-btn">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="hamburger-icon"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"
            />
          </svg>
        </button>

        <!-- Logo -->
        <div class="logo">
          <router-link to="/" class="logo-link">
            <span class="logo-text">Booksall</span>
          </router-link>
        </div>

        <!-- Desktop Navigation -->
        <div class="desktop-nav">
          <router-link to="/" class="nav-link">Home</router-link>
          <router-link to="/futsals" class="nav-link">Find Futsals</router-link>
          <router-link to="/blog" class="nav-link">Blog</router-link>
          <router-link to="/profile" class="nav-link">Profile</router-link>
          <button @click="handleLogout" class="signup-btn">Logout</button>
        </div>

        <!-- Mobile menu button -->
        <div class="mobile-menu-btn">
          <button @click="toggleMobileMenu" class="hamburger-btn">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="hamburger-icon"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                v-if="!isMobileMenuOpen"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              />
              <path
                v-else
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
      </div>

      <!-- Mobile Navigation -->
      <div v-if="isMobileMenuOpen" class="mobile-nav">
        <router-link to="/" class="mobile-nav-link" @click="closeMobileMenu">Home</router-link>
        <router-link to="/futsals" class="mobile-nav-link" @click="closeMobileMenu"
          >Find Futsals</router-link
        >
        <router-link to="/blog" class="mobile-nav-link" @click="closeMobileMenu">Blog</router-link>
        <router-link to="/profile" class="mobile-nav-link" @click="closeMobileMenu"
          >Profile</router-link
        >
        <button @click="handleLogout" class="mobile-signup-btn">Logout</button>
      </div>
    </div>

    <!-- Sidebar -->
    <div v-if="isSidebarOpen" class="sidebar">
      <div class="sidebar-header">
        <h2 class="sidebar-title" style="color: white">Futsal Admin</h2>
        <button @click="toggleSidebar" class="close-sidebar-btn">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="close-icon"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
        </button>
      </div>
      <div class="sidebar-content">
        <router-link to="/admin/bookings" class="sidebar-link" @click="toggleSidebar"
          >Manage Bookings</router-link
        >
        <router-link to="/admin/reports" class="sidebar-link" @click="toggleSidebar"
          >Reports</router-link
        >
        <router-link to="/admin/settings" class="sidebar-link" @click="toggleSidebar"
          >Settings</router-link
        >
      </div>
    </div>
  </nav>
</template>
  
  <script setup>
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import apiClient from '@/axios'
import { useAuthStore } from '../stores/auth'

const router = useRouter()
const authStore = useAuthStore()
const isMobileMenuOpen = ref(false)
const isSidebarOpen = ref(false)

// Toggle mobile menu
const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}

// Close mobile menu
const closeMobileMenu = () => {
  isMobileMenuOpen.value = false
}

// Toggle sidebar
const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value
}

// Handle logout
const handleLogout = async () => {
  try {
    await apiClient.post('auth/logout/')
    authStore.logout()
    closeMobileMenu()
    router.push('/')
  } catch (error) {
    console.error('Logout error:', error)
    authStore.logout()
    closeMobileMenu()
    router.push('/')
  }
}
</script>
  
  <style scoped>
.navbar {
  background-color: #16a34a;
  color: white;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
}

.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.navbar-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 4rem;
}

.sidebar-toggle-btn {
  color: white;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
  margin-right: 1rem;
}

.sidebar-toggle-btn .hamburger-icon {
  width: 1.5rem;
  height: 1.5rem;
}

.logo-link {
  display: flex;
  align-items: center;
  text-decoration: none;
  color: white;
}

.logo-text {
  font-size: 1.25rem;
  font-weight: 700;
}

.desktop-nav {
  display: none;
}

.nav-link {
  color: white;
  text-decoration: none;
  margin-left: 2rem;
  font-size: 0.875rem;
  font-weight: 500;
  transition: color 0.2s;
}

.nav-link:hover {
  color: #bbf7d0;
}

.signup-btn {
  background-color: white;
  color: #16a34a;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-weight: 500;
  font-size: 0.875rem;
  text-decoration: none;
  margin-left: 2rem;
  transition: background-color 0.2s;
  border: none;
  cursor: pointer;
}

.signup-btn:hover {
  background-color: #dcfce7;
}

.mobile-menu-btn {
  display: block;
}

.hamburger-btn {
  color: white;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
}

.hamburger-btn:focus {
  outline: none;
}

.hamburger-icon {
  width: 1.5rem;
  height: 1.5rem;
}

.mobile-nav {
  display: flex;
  flex-direction: column;
  padding-bottom: 1rem;
  min-height: 100vh;
}

.mobile-nav-link {
  color: white;
  text-decoration: none;
  padding: 0.75rem 0;
  transition: color 0.2s;
}

.mobile-nav-link:hover {
  color: #bbf7d0;
}

.mobile-signup-btn {
  background-color: white;
  color: #16a34a;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-weight: 500;
  text-decoration: none;
  display: inline-block;
  margin-top: 0.5rem;
  width: fit-content;
  transition: background-color 0.2s;
  border: none;
  cursor: pointer;
}

.mobile-signup-btn:hover {
  background-color: #dcfce7;
}

/* Sidebar Styles */
.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  width: 250px;
  height: 100vh;
  background-color: #ffffff;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
  z-index: 1001;
  transform: translateX(0);
  transition: transform 0.3s ease-in-out;
}

.sidebar-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #16a34a;
  color: white;
}

.sidebar-title {
  font-size: 1.25rem;
  font-weight: 600;
}

.close-sidebar-btn {
  background: none;
  border: none;
  color: white;
  cursor: pointer;
}

.close-icon {
  width: 1.5rem;
  height: 1.5rem;
}

.sidebar-content {
  padding: 1rem;
  display: flex;
  flex-direction: column;
}

.sidebar-link {
  color: #16a34a;
  text-decoration: none;
  padding: 0.75rem 0;
  font-size: 1rem;
  font-weight: 500;
  transition: color 0.2s;
}

.sidebar-link:hover {
  color: #15803d;
}

@media (min-width: 768px) {
  .desktop-nav {
    display: flex;
    align-items: center;
  }

  .mobile-menu-btn {
    display: none;
  }

  .mobile-nav {
    display: none;
  }
}
</style>