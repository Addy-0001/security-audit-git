<template>
  <div class="futsal-list-page" style="margin-bottom: 50px">
    <!-- Header Section -->
    <div class="page-header">
      <div class="container">
        <h1 class="page-title">Find Futsals</h1>
        <p class="page-description">Discover and book the best futsal courts in your area</p>
      </div>
    </div>

    <div class="container">
      <div class="search-section">
        <div class="search-bar">
          <input
            type="text"
            v-model="searchQuery"
            placeholder="Search by name or location..."
            class="search-input"
          />
          <button class="search-button" @click="fetchFutsals">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
            Search
          </button>
        </div>
      </div>

      <div class="content-wrapper">
        <!-- Filters Sidebar -->
        <aside class="filters-sidebar" :class="{ active: showFilters }">
          <div class="filters-header">
            <h2>Filters</h2>
            <button class="close-filters-btn" @click="toggleFilters">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
              </svg>
            </button>
          </div>

          <div class="filter-group">
            <h3>Price Range</h3>
            <div class="price-range">
              <input
                type="range"
                v-model="priceRange"
                min="500"
                max="5000"
                step="100"
                class="price-slider"
              />
              <div class="price-values">
                <span>Rs. 500</span>
                <span>Rs. {{ priceRange }}</span>
              </div>
            </div>
          </div>

          <div class="filter-group">
            <h3>Amenities</h3>
            <div class="checkbox-group">
              <label class="checkbox-label">
                <input type="checkbox" v-model="filters.shower_facility" />
                <span>Shower Facility</span>
              </label>
              <label class="checkbox-label">
                <input type="checkbox" v-model="filters.parking_space" />
                <span>Parking Space</span>
              </label>
              <label class="checkbox-label">
                <input type="checkbox" v-model="filters.changing_room" />
                <span>Changing Room</span>
              </label>
              <label class="checkbox-label">
                <input type="checkbox" v-model="filters.restaurant" />
                <span>Restaurant</span>
              </label>
              <label class="checkbox-label">
                <input type="checkbox" v-model="filters.wifi" />
                <span>WiFi</span>
              </label>
              <label class="checkbox-label">
                <input type="checkbox" v-model="filters.open_ground" />
                <span>Open Ground</span>
              </label>
            </div>
          </div>

          <div class="filter-group">
            <h3>Players per Side</h3>
            <div class="checkbox-group">
              <label class="checkbox-label">
                <input type="checkbox" v-model="filters.a_side_5" />
                <span>5-a-side</span>
              </label>
              <label class="checkbox-label">
                <input type="checkbox" v-model="filters.a_side_6" />
                <span>6-a-side</span>
              </label>
              <label class="checkbox-label">
                <input type="checkbox" v-model="filters.a_side_7" />
                <span>7-a-side</span>
              </label>
            </div>
          </div>

          <div class="filter-actions">
            <button class="apply-filters-btn" @click="applyFilters">Apply Filters</button>
            <button class="reset-filters-btn" @click="resetFilters">Reset</button>
          </div>
        </aside>

        <!-- Main Content -->
        <main class="main-content">
          <div class="list-header">
            <div class="results-count">{{ filteredFutsals.length }} futsals found</div>
            <div class="sort-controls">
              <label for="sort-select">Sort by:</label>
              <select id="sort-select" v-model="sortBy" class="sort-select">
                <option value="price_asc">Price: Low to High</option>
                <option value="price_desc">Price: High to Low</option>
                <option value="name_asc">Name: A to Z</option>
                <option value="name_desc">Name: Z to A</option>
              </select>
            </div>
            <button class="filter-toggle-btn" @click="toggleFilters">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <line x1="4" y1="21" x2="4" y2="14"></line>
                <line x1="4" y1="10" x2="4" y2="3"></line>
                <line x1="12" y1="21" x2="12" y2="12"></line>
                <line x1="12" y1="8" x2="12" y2="3"></line>
                <line x1="20" y1="21" x2="20" y2="16"></line>
                <line x1="20" y1="12" x2="20" y2="3"></line>
                <line x1="1" y1="14" x2="7" y2="14"></line>
                <line x1="9" y1="8" x2="15" y2="8"></line>
                <line x1="17" y1="16" x2="23" y2="16"></line>
              </svg>
              Filters
            </button>
          </div>

          <div v-if="loading" class="loading-state">
            <div class="spinner"></div>
            <p>Loading futsals...</p>
          </div>

          <div v-else-if="filteredFutsals.length === 0" class="empty-state">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="48"
              height="48"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="12" y1="8" x2="12" y2="12"></line>
              <line x1="12" y1="16" x2="12.01" y2="16"></line>
            </svg>
            <h3>No futsals found</h3>
            <p>Try adjusting your filters or search query</p>
            <button class="reset-search-btn" @click="resetSearch">Reset Search</button>
          </div>

          <div v-else class="futsal-grid">
            <div v-for="futsal in paginatedFutsals" :key="futsal.id" class="futsal-card">
              <div class="futsal-image">
                <img :src="futsal.futsal_image_1 || '/placeholder.jpg'" :alt="futsal.futsal_name" />
              </div>
              <div class="futsal-content">
                <div class="futsal-info">
                  <h3 class="futsal-name">{{ futsal.futsal_name }}</h3>
                  <div class="futsal-location">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="16"
                      height="16"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      stroke-width="2"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    >
                      <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                      <circle cx="12" cy="10" r="3"></circle>
                    </svg>
                    <span>{{ futsal.location }}</span>
                  </div>
                  <div class="futsal-details">
                    <div class="detail-item">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="16"
                        height="16"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        stroke-width="2"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                      >
                        <circle cx="12" cy="12" r="10"></circle>
                        <polygon points="10 8 16 12 10 16 10 8"></polygon>
                      </svg>
                      <span>{{ futsal.a_side }}-a-side</span>
                    </div>
                    <div class="detail-item">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="16"
                        height="16"
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
                      <span>Available Today</span>
                    </div>
                  </div>
                  <div class="amenities">
                    <div v-if="futsal.parking_space" class="amenity-tag">Parking</div>
                    <div v-if="futsal.changing_room" class="amenity-tag">Changing Room</div>
                    <div v-if="futsal.shower_facility" class="amenity-tag">Shower</div>
                    <div v-if="futsal.restaurant" class="amenity-tag">Restaurant</div>
                    <div v-if="futsal.wifi" class="amenity-tag">WiFi</div>
                    <div v-if="futsal.open_ground" class="amenity-tag">Open Ground</div>
                  </div>
                </div>
                <div class="futsal-actions">
                  <div class="futsal-price">
                    <span class="price-amount">Rs. {{ formatPrice(futsal.price_per_hour) }}</span>
                    <span class="price-unit">per hour</span>
                  </div>
                  <div class="action-buttons">
                    <router-link :to="`/futsals/${futsal.id}`" class="view-details-btn"
                      >View Details</router-link
                    >
                    <!-- <router-link :to="`/futsals/${futsal.id}/book`" class="book-now-btn">Book
                                            Now</router-link> -->
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="pagination">
            <button class="pagination-btn prev" :disabled="currentPage === 1" @click="prevPage">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <polyline points="15 18 9 12 15 6"></polyline>
              </svg>
              Previous
            </button>
            <div class="page-numbers">
              <button
                v-for="page in totalPages"
                :key="page"
                class="page-number"
                :class="{ active: currentPage === page }"
                @click="goToPage(page)"
              >
                {{ page }}
              </button>
            </div>
            <button
              class="pagination-btn next"
              :disabled="currentPage === totalPages"
              @click="nextPage"
            >
              Next
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <polyline points="9 18 15 12 9 6"></polyline>
              </svg>
            </button>
          </div>
        </main>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import apiClient from '@/axios' // Assuming this is your axios instance

// State
const futsals = ref([])
const loading = ref(true)
const searchQuery = ref('')
const priceRange = ref(5000)
const showFilters = ref(false)
const sortBy = ref('price_asc')
const currentPage = ref(1)
const itemsPerPage = 6

// Filters
const filters = ref({
  shower_facility: false,
  parking_space: false,
  changing_room: false,
  restaurant: false,
  wifi: false,
  open_ground: false,
  a_side_5: false,
  a_side_6: false,
  a_side_7: false,
})

// Fetch futsals from API
const fetchFutsals = async () => {
  loading.value = true
  try {
    const response = await apiClient.get('futsal/list-futsals/', {
      params: {
        search: searchQuery.value || undefined,
        price_per_hour__lte: priceRange.value,
        shower_facility: filters.value.shower_facility || undefined,
        parking_space: filters.value.parking_space || undefined,
        changing_room: filters.value.changing_room || undefined,
        restaurant: filters.value.restaurant || undefined,
        wifi: filters.value.wifi || undefined,
        open_ground: filters.value.open_ground || undefined,
        a_side:
          [
            filters.value.a_side_5 ? '5' : null,
            filters.value.a_side_6 ? '6' : null,
            filters.value.a_side_7 ? '7' : null,
          ]
            .filter(Boolean)
            .join(',') || undefined,
      },
    })
    futsals.value = response.data
  } catch (error) {
    console.error('Error fetching futsals:', error)
    futsals.value = [] // Clear futsals on error
  } finally {
    loading.value = false
  }
}

// Filter futsals client-side (if API doesn't fully support all filters)
const filteredFutsals = computed(() => {
  let result = futsals.value

  // Client-side search fallback (if API search is insufficient)
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    result = result.filter(
      (futsal) =>
        futsal.futsal_name.toLowerCase().includes(query) ||
        futsal.location.toLowerCase().includes(query)
    )
  }

  // Client-side price filter fallback
  result = result.filter((futsal) => parseFloat(futsal.price_per_hour) <= priceRange.value)

  // Client-side amenities filter
  if (filters.value.shower_facility) result = result.filter((futsal) => futsal.shower_facility)
  if (filters.value.parking_space) result = result.filter((futsal) => futsal.parking_space)
  if (filters.value.changing_room) result = result.filter((futsal) => futsal.changing_room)
  if (filters.value.restaurant) result = result.filter((futsal) => futsal.restaurant)
  if (filters.value.wifi) result = result.filter((futsal) => futsal.wifi)
  if (filters.value.open_ground) result = result.filter((futsal) => futsal.open_ground)

  // Client-side a-side filter
  const aSideFilters = []
  if (filters.value.a_side_5) aSideFilters.push('5')
  if (filters.value.a_side_6) aSideFilters.push('6')
  if (filters.value.a_side_7) aSideFilters.push('7')
  if (aSideFilters.length > 0) {
    result = result.filter((futsal) => aSideFilters.includes(futsal.a_side))
  }

  // Sort futsals
  result = sortFutsals(result)

  return result
})

// Sort futsals based on selected sort option
const sortFutsals = (futsalList) => {
  switch (sortBy.value) {
    case 'price_asc':
      return [...futsalList].sort(
        (a, b) => parseFloat(a.price_per_hour) - parseFloat(b.price_per_hour)
      )
    case 'price_desc':
      return [...futsalList].sort(
        (a, b) => parseFloat(b.price_per_hour) - parseFloat(a.price_per_hour)
      )
    case 'name_asc':
      return [...futsalList].sort((a, b) => a.futsal_name.localeCompare(b.futsal_name))
    case 'name_desc':
      return [...futsalList].sort((a, b) => b.futsal_name.localeCompare(a.futsal_name))
    default:
      return futsalList
  }
}

// Pagination
const paginatedFutsals = computed(() => {
  const startIndex = (currentPage.value - 1) * itemsPerPage
  const endIndex = startIndex + itemsPerPage
  return filteredFutsals.value.slice(startIndex, endIndex)
})

const totalPages = computed(() => {
  return Math.ceil(filteredFutsals.value.length / itemsPerPage)
})

// Methods
const toggleFilters = () => {
  showFilters.value = !showFilters.value
}

const applyFilters = () => {
  currentPage.value = 1
  fetchFutsals()
  if (window.innerWidth < 768) {
    showFilters.value = false
  }
}

const resetFilters = () => {
  searchQuery.value = ''
  priceRange.value = 3000
  Object.keys(filters.value).forEach((key) => {
    filters.value[key] = false
  })
  currentPage.value = 1
  fetchFutsals()
}

const resetSearch = () => {
  resetFilters()
}

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--
  }
}

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
  }
}

const goToPage = (page) => {
  currentPage.value = page
}

const formatPrice = (price) => {
  return parseFloat(price).toLocaleString()
}

// Watch for changes in sort options (fetch only on filter apply)
watch(sortBy, () => {
  currentPage.value = 1
})

// Fetch futsals on component mount
onMounted(() => {
  fetchFutsals()
})
</script>

<style scoped>
/* Styles remain unchanged from your original code */
.futsal-list-page {
  min-height: 100vh;
  background-color: var(--gray-50);
}

/* Page Header */
.page-header {
  background-color: var(--primary-600);
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

/* Search Section */
.search-section {
  margin-bottom: 2rem;
}

.search-bar {
  display: flex;
  max-width: 800px;
  margin: 0 auto;
  box-shadow: var(--shadow-md);
  border-radius: var(--radius);
  overflow: hidden;
}

.search-input {
  flex: 1;
  padding: 1rem;
  border: none;
  font-size: 1rem;
}

.search-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0 1.5rem;
  background-color: var(--primary-600);
  color: white;
  border: none;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s;
}

.search-button:hover {
  background-color: var(--primary-700);
}

/* Content Layout */
.content-wrapper {
  display: flex;
  gap: 2rem;
  position: relative;
}

/* Filters Sidebar */
.filters-sidebar {
  width: 280px;
  background-color: white;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow);
  padding: 1.5rem;
  position: sticky;
  top: 2rem;
  height: fit-content;
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.filters-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.filters-header h2 {
  font-size: 1.25rem;
  margin: 0;
}

.close-filters-btn {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  color: var(--gray-500);
}

.filter-group {
  margin-bottom: 1.5rem;
}

.filter-group h3 {
  font-size: 1rem;
  margin-bottom: 1rem;
  color: var(--gray-800);
}

.price-range {
  margin-bottom: 0.5rem;
}

.price-slider {
  width: 100%;
  margin-bottom: 0.5rem;
  accent-color: var(--primary-600);
}

.price-values {
  display: flex;
  justify-content: space-between;
  font-size: 0.875rem;
  color: var(--gray-600);
}

.checkbox-group {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  font-size: 0.95rem;
}

.checkbox-label input {
  width: auto;
  accent-color: var(--primary-600);
}

.filter-actions {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.apply-filters-btn {
  padding: 0.75rem;
  background-color: var(--primary-600);
  color: white;
  border: none;
  border-radius: var(--radius);
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s;
}

.apply-filters-btn:hover {
  background-color: var(--primary-700);
}

.reset-filters-btn {
  padding: 0.75rem;
  background-color: var(--gray-100);
  color: var(--gray-700);
  border: 1px solid var(--gray-200);
  border-radius: var(--radius);
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.2s;
}

.reset-filters-btn:hover {
  background-color: var(--gray-200);
}

/* Main Content */
.main-content {
  flex: 1;
}

.list-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.results-count {
  font-weight: 500;
  color: var(--gray-700);
}

.sort-controls {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.sort-select {
  padding: 0.5rem;
  border: 1px solid var(--gray-200);
  border-radius: var(--radius);
  background-color: white;
  color: var(--gray-800);
  font-size: 0.95rem;
}

.filter-toggle-btn {
  display: none;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background-color: white;
  border: 1px solid var(--gray-200);
  border-radius: var(--radius);
  font-weight: 500;
  cursor: pointer;
}

/* Futsal Cards */
.futsal-grid {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.futsal-card {
  display: flex;
  background-color: white;
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: transform 0.2s, box-shadow 0.2s;
}

.futsal-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}

.futsal-image {
  width: 280px;
  height: 200px;
  flex-shrink: 0;
}

.futsal-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.futsal-content {
  flex: 1;
  display: flex;
  padding: 1.5rem;
}

.futsal-info {
  flex: 1;
}

.futsal-name {
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
  color: var(--gray-900);
}

.futsal-location {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  color: var(--gray-600);
  margin-bottom: 1rem;
}

.futsal-details {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}

.detail-item {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  color: var(--gray-700);
  font-size: 0.95rem;
}

.amenities {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.amenity-tag {
  padding: 0.25rem 0.5rem;
  background-color: var(--gray-100);
  border-radius: var(--radius);
  font-size: 0.75rem;
  color: var(--gray-700);
}

.futsal-actions {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-end;
  min-width: 180px;
}

.futsal-price {
  text-align: right;
  margin-bottom: 1rem;
}

.price-amount {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary-600);
  display: block;
}

.price-unit {
  font-size: 0.875rem;
  color: var(--gray-500);
}

.action-buttons {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  width: 100%;
}

.view-details-btn,
.book-now-btn {
  padding: 0.75rem 1rem;
  border-radius: var(--radius);
  font-weight: 600;
  text-align: center;
  transition: all 0.2s;
}

.view-details-btn {
  background-color: var(--gray-100);
  color: var(--gray-700);
  border: 1px solid var(--gray-200);
}

.view-details-btn:hover {
  background-color: var(--gray-200);
}

.book-now-btn {
  background-color: var(--primary-600);
  color: white;
  border: none;
}

.book-now-btn:hover {
  background-color: var(--primary-700);
}

/* Loading and Empty States */
.loading-state,
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  text-align: center;
  background-color: white;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow);
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(22, 163, 74, 0.1);
  border-left-color: var(--primary-600);
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.empty-state svg {
  color: var(--gray-400);
  margin-bottom: 1rem;
}

.empty-state h3 {
  margin-bottom: 0.5rem;
  color: var(--gray-800);
}

.empty-state p {
  color: var(--gray-600);
  margin-bottom: 1.5rem;
}

.reset-search-btn {
  padding: 0.75rem 1.5rem;
  background-color: var(--primary-600);
  color: white;
  border: none;
  border-radius: var(--radius);
  font-weight: 600;
  cursor: pointer;
}

/* Pagination */
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.5rem;
  margin-top: 2rem;
}

.pagination-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background-color: white;
  border: 1px solid var(--gray-200);
  border-radius: var(--radius);
  font-weight: 500;
  cursor: pointer;
}

.pagination-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.page-numbers {
  display: flex;
  gap: 0.25rem;
}

.page-number {
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius);
  background-color: white;
  border: 1px solid var(--gray-200);
  font-weight: 500;
  cursor: pointer;
}

.page-number.active {
  background-color: var(--primary-600);
  color: white;
  border-color: var(--primary-600);
}

/* Responsive Styles */
@media (max-width: 1024px) {
  .futsal-image {
    width: 220px;
  }
}

@media (max-width: 768px) {
  .content-wrapper {
    flex-direction: column;
  }

  .filters-sidebar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 100;
    border-radius: 0;
    transform: translateX(-100%);
    opacity: 0;
    pointer-events: none;
    overflow-y: auto;
  }

  .filters-sidebar.active {
    transform: translateX(0);
    opacity: 1;
    pointer-events: auto;
  }

  .close-filters-btn {
    display: block;
  }

  .filter-toggle-btn {
    display: flex;
  }

  .futsal-card {
    flex-direction: column;
  }

  .futsal-image {
    width: 100%;
    height: 200px;
  }

  .futsal-content {
    flex-direction: column;
  }

  .futsal-actions {
    align-items: stretch;
    margin-top: 1.5rem;
    min-width: auto;
  }

  .action-buttons {
    flex-direction: row;
  }

  .view-details-btn,
  .book-now-btn {
    flex: 1;
  }
}

@media (max-width: 640px) {
  .list-header {
    flex-wrap: wrap;
    gap: 1rem;
  }

  .results-count {
    width: 100%;
    order: 3;
  }

  .sort-controls {
    flex: 1;
  }

  .action-buttons {
    flex-direction: column;
  }

  .page-numbers {
    display: none;
  }
}
</style>