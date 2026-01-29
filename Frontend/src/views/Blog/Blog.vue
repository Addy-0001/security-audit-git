<template>
  <section class="blog-section">

    <div class="section-header">
      <div class="container">
        <h2>Futsal Blogs</h2>
        <p>Detailed information about the best futsal facilities in the area</p>
      </div>
    </div>

    <div class="container">


      <!-- Search and Filter Bar -->
      <div class="search-filter-container">
        <!-- Search Input -->
        <div class="search-wrapper">
          <div class="search-input-wrapper">
            <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
              stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
            <input id="search-input" v-model="searchQuery" type="text" placeholder="Search blogs..."
              aria-label="Search blogs" />
            <button v-if="searchQuery" @click="clearSearch" class="clear-button" aria-label="Clear search">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
              </svg>
            </button>
          </div>
        </div>

        <!-- Filter Dropdown -->
        <div class="filter-wrapper">
          <div class="filter-select-wrapper">
            <svg class="filter-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
              stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"></polygon>
            </svg>
            <select id="location-filter" v-model="selectedLocation" aria-label="Filter by location">
              <option value="">All Locations</option>
              <option v-for="location in availableLocations" :key="location" :value="location">
                {{ location }}
              </option>
            </select>
          </div>
          <button v-if="selectedLocation" @click="clearFilter" class="clear-filter-button"
            aria-label="Clear location filter">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
              stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </div>


      </div>

      <!-- Loading State -->
      <div v-if="isLoading" class="loading-state">
        <div class="spinner"></div>
        <p>Loading blogs...</p>
      </div>

      <!-- Error Message -->
      <div v-else-if="errorMessage" class="error-message-container">
        <p>{{ errorMessage }}</p>
        <button @click="fetchBlogPosts" class="retry-btn">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
            stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 2v6h-6"></path>
            <path d="M3 12a9 9 0 0 1 15-6.7L21 8"></path>
            <path d="M3 22v-6h6"></path>
            <path d="M21 12a9 9 0 0 1-15 6.7L3 16"></path>
          </svg>
          Try Again
        </button>
      </div>

      <!-- Empty State -->
      <div v-else-if="filteredPosts.length === 0" class="empty-state">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"
          class="empty-icon">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
        </svg>
        <h3>No blogs found</h3>
        <p>Try adjusting your filters or search query</p>
        <button @click="clearAllFilters" class="reset-btn">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
            stroke-linecap="round" stroke-linejoin="round" class="reset-icon">
            <path d="M2.5 2v6h6M21.5 22v-6h-6"></path>
            <path d="M22 11.5A10 10 0 0 0 3.2 7.2M2 12.5a10 10 0 0 0 18.8 4.2"></path>
          </svg>
          Reset Filters
        </button>
      </div>

      <!-- Blog Grid -->
      <div v-else class="blog-grid-wrapper">
        <div class="blog-grid">
          <!-- Blog Card -->
          <article v-for="(post, index) in filteredPosts" :key="index" class="blog-card">
            <div class="card-content">
              <!-- Category and Location Tags -->
              <div class="tags">
                <span class="category-tag">{{ post.category }}</span>
                <span class="location-tag">{{ post.location }}</span>
              </div>

              <!-- Date and Read Time -->
              <div class="meta">
                <span class="date">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="meta-icon">
                    <path fill-rule="evenodd"
                      d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z"
                      clip-rule="evenodd" />
                  </svg>
                  {{ post.date }}
                </span>
                <span class="read-time">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="meta-icon">
                    <path fill-rule="evenodd"
                      d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z"
                      clip-rule="evenodd" />
                  </svg>
                  {{ post.readTime }} min read
                </span>
              </div>

              <!-- Title -->
              <h3 class="blog-title">{{ post.title }}</h3>

              <!-- Excerpt -->
              <p class="excerpt">{{ post.excerpt }}</p>

              <!-- Read More Link -->
              <router-link v-if="post.id" :to="`/blog/${post.id}`" class="read-more">
                Read Full Review
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                </svg>
              </router-link>
            </div>
          </article>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';
import axios from 'axios';

// State variables
const selectedLocation = ref('');
const searchQuery = ref('');
const blogPosts = ref([]);
const isLoading = ref(false);
const errorMessage = ref('');

// Fetch blog posts from API
const fetchBlogPosts = async () => {
  isLoading.value = true;
  errorMessage.value = '';

  try {
    const response = await axios.get('https://apibooksal.getintoto.com/api/v1/blog/list-blogs/');
    const data = response.data;

    blogPosts.value = data.map(post => ({
      id: post.id,
      title: post.title,
      excerpt: post.meta_description || 'No description available.',
      date: new Date(post.created_at).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      }),
      category: post.category?.name || 'Uncategorized',
      location: post.meta_tags?.split(',')[1]?.trim() || 'Unknown',
      readTime: calculateReadTime(post.meta_description || '')
    }));
  } catch (error) {
    console.error('Failed to fetch blog posts:', error);
    errorMessage.value = 'Could not load blogs. Please try again later.';
  } finally {
    isLoading.value = false;
  }
};

// Calculate estimated read time based on content length
const calculateReadTime = (content) => {
  const wordsPerMinute = 200;
  const wordCount = content.split(/\s+/).length;
  const readTime = Math.ceil(wordCount / wordsPerMinute);
  return readTime < 1 ? 1 : readTime;
};

// Computed properties
const availableLocations = computed(() => {
  const locations = blogPosts.value.map(post => post.location);
  return [...new Set(locations)].filter(Boolean).sort();
});

const filteredPosts = computed(() => {
  let filtered = blogPosts.value;

  if (selectedLocation.value) {
    filtered = filtered.filter(post => post.location === selectedLocation.value);
  }

  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase();
    filtered = filtered.filter(post =>
      post.title.toLowerCase().includes(query) ||
      post.excerpt.toLowerCase().includes(query)
    );
  }

  return filtered;
});

// Methods
const clearFilter = () => {
  selectedLocation.value = '';
};

const clearSearch = () => {
  searchQuery.value = '';
};

const clearAllFilters = () => {
  selectedLocation.value = '';
  searchQuery.value = '';
};

// Lifecycle hooks
onMounted(() => {
  fetchBlogPosts();
});

// Add debounced search for better performance
let searchTimeout;
watch(searchQuery, () => {
  clearTimeout(searchTimeout);
  searchTimeout = setTimeout(() => {
    // This would be where you might want to trigger a search API call
    // if you're implementing server-side search
  }, 300);
});
</script>

<style scoped>
/* Base Styles */
.blog-section {
  background-color: #f8f9fa;
  padding: 60px 16px;
  min-height: 100vh;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

/* Section Header */
.section-header {
  background-color: var(--primary-600);
  /* Using green color from the theme */
  color: white;
  padding: 3rem 2rem;
  margin: -60px -16px 0px -16px;
  text-align: start;
  border-radius: 0 0 10px 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.section-header h2 {
  font-size: 2.8rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: #ffffff;
}

.section-header p {
  color: rgba(255, 255, 255, 0.85);
  max-width: 672px;
  font-size: 1.1rem;
}

/* Search and Filter Container */
.search-filter-container {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  margin: 0 auto 2rem;
  max-width: 800px;
  flex-wrap: wrap;
  margin-top: 50px;
}

@media (min-width: 640px) {
  .search-filter-container {
    flex-wrap: nowrap;
    margin-top: 50px;
  }
}

/* Search Bar */
.search-wrapper {
  flex: 1;
  min-width: 200px;
}

.search-input-wrapper {
  position: relative;
  width: 100%;
}

.search-icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #6b7280;
}

.search-input-wrapper input {
  width: 100%;
  padding: 12px 40px 12px 40px;
  font-size: 1rem;
  border: 2px solid #d1d5db;
  border-radius: 50px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  outline: none;
  transition: all 0.3s ease;
}

.search-input-wrapper input:focus {
  border-color: #15803d;
  box-shadow: 0 0 0 3px rgba(21, 128, 61, 0.2);
}

.clear-button {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  cursor: pointer;
  color: #6b7280;
  padding: 0;
  border-radius: 50%;
  transition: all 0.2s ease;
}

.clear-button:hover {
  background-color: #f3f4f6;
  color: #15803d;
}

.clear-button svg {
  width: 16px;
  height: 16px;
}

/* Filter Dropdown */
.filter-wrapper {
  position: relative;
  width: 180px;
  display: flex;
  align-items: center;
}

.filter-select-wrapper {
  position: relative;
  width: 100%;
}

.filter-icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  width: 18px;
  height: 18px;
  color: #6b7280;
  pointer-events: none;
}

.filter-wrapper select {
  width: 100%;
  padding: 12px 40px 12px 40px;
  font-size: 1rem;
  border: 2px solid #d1d5db;
  border-radius: 50px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  outline: none;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='%236b7280'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M19 9l-7 7-7-7'%3E%3C/path%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 12px center;
  background-size: 16px;
  transition: all 0.3s ease;
  cursor: pointer;
}

.filter-wrapper select:focus {
  border-color: #15803d;
  box-shadow: 0 0 0 3px rgba(21, 128, 61, 0.2);
}

.clear-filter-button {
  position: absolute;
  right: -36px;
  top: 50%;
  transform: translateY(-50%);
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  cursor: pointer;
  color: #6b7280;
  padding: 0;
  border-radius: 50%;
  transition: all 0.2s ease;
  z-index: 2;
}

.clear-filter-button:hover {
  background-color: #f3f4f6;
  color: #15803d;
}

.clear-filter-button svg {
  width: 30px;
  height: 30px;
}

/* Reset All Button */
.reset-all-button {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background-color: #15803d;
  color: white;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.reset-all-button:hover {
  background-color: #166534;
  transform: rotate(45deg);
}

.reset-all-button svg {
  width: 30px;
  height: 30px;
}

/* Loading, Error, and Empty States */
.loading-state,
.error-message-container,
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem 1rem;
  text-align: center;
}

.spinner {
  border: 4px solid rgba(21, 128, 61, 0.1);
  border-radius: 50%;
  border-top: 4px solid #15803d;
  width: 40px;
  height: 40px;
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

.error-message-container p {
  color: #b91c1c;
  margin-bottom: 1rem;
}

.retry-btn,
.reset-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background-color: #15803d;
  color: white;
  border: none;
  border-radius: 6px;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.retry-btn:hover,
.reset-btn:hover {
  background-color: #166534;
}

.retry-btn svg,
.reset-btn svg {
  width: 18px;
  height: 18px;
}

.empty-icon {
  width: 60px;
  height: 60px;
  color: #9ca3af;
  margin-bottom: 1rem;
}

.empty-state h3 {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #374151;
}

.empty-state p {
  color: #6b7280;
  margin-bottom: 1rem;
}

/* Blog Grid */
.blog-grid-wrapper {
  display: flex;
  justify-content: center;
}

.blog-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 32px;
  width: 100%;
  max-width: 1024px;
}

/* Blog Card */
.blog-card {
  background-color: #fff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 1px solid #e5e7eb;
}

.blog-card:hover {
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
  transform: translateY(-4px);
}

.card-content {
  padding: 24px;
}

/* Tags */
.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 16px;
}

.category-tag {
  background-color: #15803d;
  color: #fff;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 50px;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

.location-tag {
  background-color: #f3f4f6;
  color: #4b5563;
  font-size: 0.75rem;
  font-weight: 500;
  padding: 4px 12px;
  border-radius: 50px;
}

/* Meta Information */
.meta {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  color: #6b7280;
  font-size: 0.875rem;
  margin-bottom: 12px;
  gap: 16px;
}

.date,
.read-time {
  display: flex;
  align-items: center;
}

.meta-icon {
  width: 16px;
  height: 16px;
  margin-right: 6px;
}

/* Blog Content */
.blog-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 12px;
  color: #111827;
  line-height: 1.3;
}

.excerpt {
  color: #4b5563;
  margin-bottom: 20px;
  line-height: 1.6;
}

/* Read More Link */
.read-more {
  display: inline-flex;
  align-items: center;
  color: #15803d;
  font-weight: 600;
  font-size: 0.95rem;
  text-decoration: none;
  transition: color 0.2s ease;
}

.read-more:hover {
  color: #166534;
  text-decoration: underline;
}

.read-more svg {
  width: 18px;
  height: 18px;
  margin-left: 6px;
  transition: transform 0.2s ease;
}

.read-more:hover svg {
  transform: translateX(4px);
}

/* Responsive Styles */
@media (min-width: 640px) {
  .section-header {
    padding: 4rem 2rem;
  }

  .search-wrapper {
    padding: 2rem 0;
  }
}

@media (min-width: 768px) {
  .blog-section {
    padding: 60px 32px;
  }

  .section-header {
    margin: -60px -48px 10px -49px;
  }

  .filter-controls {
    flex-direction: row;
    justify-content: center;
    gap: 24px;
  }

  .blog-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .blog-section {
    padding: 60px 48px;
  }

  .section-header {
    margin-bottom: 2rem;
  }

  .search-wrapper {
    max-width: 600px;
  }
}
</style>