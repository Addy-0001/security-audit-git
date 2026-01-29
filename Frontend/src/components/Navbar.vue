<template>
  <nav class="navbar">
    <div class="container">
      <div class="navbar-content">
        <!-- Logo -->
        <div class="logo">
          <router-link to="/" class="logo-link">
            <span
              class="logo-text"
              style="font-family: 'Bungee Shade sans-serif'; font-weight: 400; font-style: normal"
              >Booksall</span
            >
          </router-link>
        </div>

        <!-- Desktop Navigation -->
        <div class="desktop-nav">
          <router-link to="/" class="nav-link">Home</router-link>
          <router-link to="/futsals" class="nav-link">Find Futsals</router-link>
          <router-link to="/blog" class="nav-link">Blog</router-link>
          <router-link to="/profile" class="nav-link" v-if="authStore.isLoggedIn"
            >Profile</router-link
          >
          <router-link to="/login" class="nav-link" v-if="!authStore.isLoggedIn">Login</router-link>
          <router-link to="/register" class="signup-btn" v-if="!authStore.isLoggedIn"
            >Sign Up</router-link
          >
          <button @click="handleLogout" class="signup-btn" v-if="authStore.isLoggedIn">
            Logout
          </button>
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
        <router-link to="/blog" class="mobile-nav-link">Blog</router-link>
        <router-link
          to="/profile"
          class="mobile-nav-link"
          v-if="authStore.isLoggedIn"
          @click="closeMobileMenu"
          >Profile</router-link
        >
        <router-link
          to="/login"
          class="mobile-nav-link"
          v-if="!authStore.isLoggedIn"
          @click="closeMobileMenu"
          >Login</router-link
        >
        <router-link
          to="/signup"
          class="mobile-signup-btn"
          v-if="!authStore.isLoggedIn"
          @click="closeMobileMenu"
          >Sign Up</router-link
        >
        <button @click="handleLogout" class="mobile-signup-btn" v-if="authStore.isLoggedIn">
          Logout
        </button>
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

// Toggle mobile menu
const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}

// Close mobile menu
const closeMobileMenu = () => {
  isMobileMenuOpen.value = false
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
  /* Makes it stick to the top */
  top: 0;
  /* Aligns it to the top */
  left: 0;
  /* Ensures it spans full width */
  right: 0;
  /* Ensures it spans full width */
  z-index: 1000;
  /* Keeps it above other content */
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
}

.signup-btn:hover {
  background-color: #dcfce7;
}

.logout-btn {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 0.875rem;
  font-weight: 500;
  padding: 0;
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
}

.mobile-signup-btn:hover {
  background-color: #dcfce7;
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