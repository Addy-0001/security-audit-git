<template>
  <div class="admin-sidebar" :class="{ collapsed: isCollapsed }">
    <!-- Sidebar Header with Logo -->
    <div class="sidebar-header">
      <div class="logo-container">
        <span class="logo-text">Futsal Manager</span>
      </div>
      <button
        class="collapse-toggle"
        @click="toggleSidebar"
        :aria-label="isCollapsed ? 'Expand sidebar' : 'Collapse sidebar'"
      >
        <svg
          v-if="isCollapsed"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <polyline points="9 18 15 12 9 6"></polyline>
        </svg>
        <svg
          v-else
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
      </button>
    </div>

    <!-- Navigation Menu -->
    <nav class="sidebar-nav">
      <ul class="nav-list">
        <!-- Dashboard / Home -->
        <li class="nav-item" :class="{ active: currentRoute === '/' }">
          <router-link to="/" class="nav-link">
            <div class="nav-icon">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                <polyline points="9 22 9 12 15 12 15 22"></polyline>
              </svg>
            </div>
            <span class="nav-text">Home</span>
          </router-link>
        </li>

        <!-- Add Futsal -->
        <li class="nav-item" :class="{ active: currentRoute === '/add-futsal' }">
          <router-link to="/add-futsal" class="nav-link">
            <div class="nav-icon">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="12" y1="8" x2="12" y2="16"></line>
                <line x1="8" y1="12" x2="16" y2="12"></line>
              </svg>
            </div>
            <span class="nav-text">Add Futsal</span>
          </router-link>
        </li>

        <!-- Futsal List -->
        <li class="nav-item" :class="{ active: currentRoute === '/futsals' }">
          <router-link to="/futsals" class="nav-link">
            <div class="nav-icon">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <circle cx="12" cy="12" r="10"></circle>
                <path
                  d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"
                ></path>
                <line x1="2" y1="12" x2="22" y2="12"></line>
              </svg>
            </div>
            <span class="nav-text">My Futsals</span>
          </router-link>
        </li>

        <!-- Conditional section for when a futsal is selected -->
        <template v-if="selectedFutsalId">
          <li class="nav-divider"></li>
          <li class="nav-section-title">
            <span>Selected Futsal</span>
          </li>

          <!-- Edit Futsal -->
          <li
            class="nav-item"
            :class="{ active: currentRoute === `/futsal/${selectedFutsalId}/edit` }"
          >
            <router-link :to="`/futsal/${selectedFutsalId}/edit`" class="nav-link">
              <div class="nav-icon">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                  <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                </svg>
              </div>
              <span class="nav-text">Edit Futsal</span>
            </router-link>
          </li>

          <!-- Futsal Stats -->
          <li
            class="nav-item"
            :class="{ active: currentRoute === `/futsal/${selectedFutsalId}/stats` }"
          >
            <router-link :to="`/futsal/${selectedFutsalId}/stats`" class="nav-link">
              <div class="nav-icon">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <line x1="18" y1="20" x2="18" y2="10"></line>
                  <line x1="12" y1="20" x2="12" y2="4"></line>
                  <line x1="6" y1="20" x2="6" y2="14"></line>
                </svg>
              </div>
              <span class="nav-text">Stats</span>
            </router-link>
          </li>

          <!-- Regular Bookings -->
          <li
            class="nav-item"
            :class="{ active: currentRoute === `/futsal/${selectedFutsalId}/add-regular-booking` }"
          >
            <router-link :to="`/futsal/${selectedFutsalId}/add-regular-booking`" class="nav-link">
              <div class="nav-icon">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
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
              </div>
              <span class="nav-text">Regular Bookings</span>
            </router-link>
          </li>
        </template>

        <li class="nav-divider"></li>

        <!-- User Section -->
        <li class="nav-item" :class="{ active: currentRoute === '/profile' }">
          <router-link to="/profile" class="nav-link">
            <div class="nav-icon">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
              </svg>
            </div>
            <span class="nav-text">My Profile</span>
          </router-link>
        </li>

        <!-- Bookings -->
        <li class="nav-item" :class="{ active: currentRoute === '/bookings' }">
          <router-link to="/bookings" class="nav-link">
            <div class="nav-icon">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <path d="M12 8v4l3 3m6-3a9 9 0 1 1-18 0 9 9 0 0 1 18 0z"></path>
              </svg>
            </div>
            <span class="nav-text">My Bookings</span>
          </router-link>
        </li>

        <!-- Blog -->
        <li class="nav-item" :class="{ active: currentRoute === '/blog' }">
          <router-link to="/blog" class="nav-link">
            <div class="nav-icon">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <path d="M12 20h9"></path>
                <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
              </svg>
            </div>
            <span class="nav-text">Blog</span>
          </router-link>
        </li>
      </ul>
    </nav>

    <!-- Sidebar Footer -->
    <div class="sidebar-footer">
      <button class="logout-button" @click="logout">
        <div class="nav-icon">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          >
            <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
            <polyline points="16 17 21 12 16 7"></polyline>
            <line x1="21" y1="12" x2="9" y2="12"></line>
          </svg>
        </div>
        <span class="nav-text">Logout</span>
      </button>
    </div>

    <!-- Mobile Toggle Button (visible only on mobile) -->
    <button
      class="mobile-toggle"
      @click="toggleSidebar"
      :aria-label="isCollapsed ? 'Expand sidebar' : 'Collapse sidebar'"
    >
      <svg
        v-if="isCollapsed"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <line x1="3" y1="12" x2="21" y2="12"></line>
        <line x1="3" y1="6" x2="21" y2="6"></line>
        <line x1="3" y1="18" x2="21" y2="18"></line>
      </svg>
      <div v-else></div>
      <!-- <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg> -->
    </button>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const isCollapsed = ref(false)
const isMobile = ref(false)

// Get current route path for highlighting active menu item
const currentRoute = computed(() => route.path)

// Extract futsal ID from route if available
const selectedFutsalId = ref(null)

onMounted(() => {
  if (route.params.id) {
    selectedFutsalId.value = route.params.id
  }
})

watch(
  () => route.params.id,
  (newId) => {
    selectedFutsalId.value = newId || null
  }
)

// Toggle sidebar collapsed state
const toggleSidebar = () => {
  isCollapsed.value = !isCollapsed.value
  // Save preference to localStorage
  localStorage.setItem('futsalAdminSidebarCollapsed', isCollapsed.value)
}

// Logout function
const logout = () => {
  // Remove token from localStorage
  localStorage.removeItem('token')
  // Redirect to login page
  router.push('/login')
}

// Check screen size and set mobile state
const checkScreenSize = () => {
  isMobile.value = window.innerWidth < 768

  // Auto-collapse on mobile
  if (isMobile.value) {
    isCollapsed.value = true
  }
}

// Initialize sidebar state from localStorage or based on screen size
onMounted(() => {
  // Check if there's a saved preference
  const savedState = localStorage.getItem('futsalAdminSidebarCollapsed')

  if (savedState !== null) {
    isCollapsed.value = savedState === 'true'
  } else {
    // Default: collapsed on mobile, expanded on desktop
    checkScreenSize()
  }

  // Add resize listener
  window.addEventListener('resize', checkScreenSize)
})

// Auto-collapse sidebar when navigating on mobile
watch(currentRoute, () => {
  if (isMobile.value && !isCollapsed.value) {
    isCollapsed.value = true
  }
})
</script>

<style scoped>
/* Base Sidebar Styles */
.admin-sidebar {
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  background-color: #ffffff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  transition: width 0.3s ease;
  width: 250px;
  z-index: 1000;
  overflow-x: hidden;
  overflow-y: auto;
}

.admin-sidebar.collapsed {
  width: 70px;
}

/* Sidebar Header */
.sidebar-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  border-bottom: 1px solid #e5e7eb;
  height: 70px;
}

.logo-container {
  display: flex;
  align-items: center;
  overflow: hidden;
}

.logo-icon {
  width: 40px;
  height: 40px;
  flex-shrink: 0;
}

.logo-text {
  margin-left: 0.75rem;
  font-weight: 700;
  font-size: 1.125rem;
  color: #15803d;
  white-space: nowrap;
  opacity: 1;
  transition: opacity 0.3s ease;
}

.collapsed .logo-text {
  opacity: 0;
  width: 0;
  margin-left: 0;
}

.collapse-toggle {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 4px;
  border: none;
  background-color: #f3f4f6;
  color: #6b7280;
  cursor: pointer;
  transition: all 0.2s ease;
}

.collapse-toggle:hover {
  background-color: #e5e7eb;
  color: #15803d;
}

.collapse-toggle svg {
  width: 18px;
  height: 18px;
}

/* Navigation */
.sidebar-nav {
  flex: 1;
  padding: 1rem 0;
  overflow-y: auto;
}

.nav-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav-item {
  margin: 0.25rem 0;
}

.nav-section-title {
  padding: 0.5rem 1.5rem;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  color: #6b7280;
  letter-spacing: 0.05em;
}

.collapsed .nav-section-title {
  display: none;
}

.nav-link {
  display: flex;
  align-items: center;
  padding: 0.75rem 1rem;
  color: #4b5563;
  text-decoration: none;
  border-radius: 6px;
  margin: 0 0.5rem;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.nav-link:hover {
  background-color: #f9fafb;
  color: #15803d;
}

.nav-item.active .nav-link {
  background-color: #ecfdf5;
  color: #15803d;
  font-weight: 600;
}

.nav-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  flex-shrink: 0;
}

.nav-icon svg {
  width: 20px;
  height: 20px;
}

.nav-text {
  margin-left: 0.75rem;
  transition: opacity 0.2s ease;
  opacity: 1;
}

.collapsed .nav-text {
  opacity: 0;
  width: 0;
  margin-left: 0;
}

.nav-divider {
  height: 1px;
  background-color: #e5e7eb;
  margin: 0.75rem 1rem;
}

/* Sidebar Footer */
.sidebar-footer {
  padding: 1rem;
  border-top: 1px solid #e5e7eb;
}

.logout-button {
  display: flex;
  align-items: center;
  width: 100%;
  padding: 0.75rem 1rem;
  border: none;
  background-color: #fee2e2;
  color: #b91c1c;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.logout-button:hover {
  background-color: #fecaca;
}

.logout-button .nav-icon {
  color: #b91c1c;
}

/* Mobile Toggle Button */
.mobile-toggle {
  position: fixed;
  bottom: 1.5rem;
  left: 1.5rem;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: #15803d;
  color: white;
  border: none;
  display: none;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 1001;
  transition: all 0.2s ease;
}

.mobile-toggle:hover {
  background-color: #166534;
}

.mobile-toggle svg {
  width: 24px;
  height: 24px;
}

/* Responsive Styles */
@media (max-width: 767px) {
  .admin-sidebar {
    transform: translateX(0);
    transition: transform 0.3s ease, width 0.3s ease;
  }

  .admin-sidebar.collapsed {
    transform: translateX(-100%);
  }

  .mobile-toggle {
    display: flex;
  }

  .collapse-toggle {
    display: none;
  }
}

/* Tooltip for collapsed sidebar */
@media (min-width: 768px) {
  .collapsed .nav-link {
    position: relative;
  }

  .collapsed .nav-link:hover::after {
    content: attr(aria-label);
    position: absolute;
    left: 100%;
    top: 50%;
    transform: translateY(-50%);
    background-color: #374151;
    color: white;
    padding: 0.5rem 0.75rem;
    border-radius: 4px;
    font-size: 0.875rem;
    white-space: nowrap;
    z-index: 1000;
    margin-left: 10px;
  }

  .collapsed .nav-link:hover::before {
    content: '';
    position: absolute;
    left: 100%;
    top: 50%;
    transform: translateY(-50%);
    border-width: 6px;
    border-style: solid;
    border-color: transparent #374151 transparent transparent;
    margin-left: -2px;
    z-index: 1000;
  }
}
</style>