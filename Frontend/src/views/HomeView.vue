<template>
  <div class="home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-overlay"></div>
      <div class="container hero-container">
        <div class="hero-content">
          <h1 class="hero-title" style="color: white">Book Your Perfect Futsal Court in Seconds</h1>
          <p class="hero-subtitle">
            Find and book the best futsal courts near you. No hassle, no waiting.
          </p>
          <div class="hero-buttons">
            <router-link to="/futsals" class="btn btn-primary"> Find Futsals Now </router-link>
            <router-link :to="isLoggedIn ? '/profile' : '/register'" class="btn btn-outline">
              {{ isLoggedIn ? 'Profile' : 'Create Account' }}
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section class="features-section">
      <div class="container">
        <h2 class="section-title">Why Choose Booksall?</h2>
        <div class="features-grid">
          <div class="feature-card">
            <div class="feature-icon-wrapper">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="feature-icon"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>
            </div>
            <h3 class="feature-title">Quick Booking</h3>
            <p class="feature-description">
              Book your favorite futsal court in less than a minute. No phone calls needed.
            </p>
          </div>
          <div class="feature-card">
            <div class="feature-icon-wrapper">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="feature-icon"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
                />
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
                />
              </svg>
            </div>
            <h3 class="feature-title">Find Nearby Courts</h3>
            <p class="feature-description">
              Discover the best futsal courts near your location with real-time availability.
            </p>
          </div>
          <div class="feature-card">
            <div class="feature-icon-wrapper">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="feature-icon"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>
            </div>
            <h3 class="feature-title">Verified Venues</h3>
            <p class="feature-description">
              All futsal courts are verified for quality and facilities. Play with confidence.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Futsals Section -->
    <section class="featured-section">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">Featured Futsals</h2>
          <router-link to="/futsals" class="view-all-link">
            View All
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="view-all-icon"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                clip-rule="evenodd"
              />
            </svg>
          </router-link>
        </div>

        <div class="futsal-grid" v-if="!isLoading">
          <div class="futsal-card" v-for="futsal in featuredFutsals" :key="futsal.id">
            <div class="futsal-image-container">
              <img
                :src="futsal.futsal_image_1 || 'https://via.placeholder.com/600x400'"
                :alt="futsal.futsal_name"
                class="futsal-image"
              />
              <div class="futsal-badge futsal-badge-popular" v-if="futsal.rating >= 4.8">
                Popular
              </div>
              <div class="futsal-badge futsal-badge-new" v-else-if="futsal.is_new">New</div>
              <div class="futsal-badge futsal-badge-hot" v-else-if="futsal.rating >= 4.5">Hot</div>
            </div>
            <div class="futsal-content">
              <div class="futsal-header">
                <h3 class="futsal-title">{{ futsal.futsal_name }}</h3>
                <div class="futsal-rating">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="rating-icon"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3 .921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784 .57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81 .588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                    />
                  </svg>
                  <span class="rating-text">{{ futsal.rating || 'N/A' }}</span>
                </div>
              </div>
              <p class="futsal-location">{{ futsal.location }}</p>
              <div class="futsal-footer">
                <span class="futsal-price">NRs. {{ formatPrice(futsal.price_per_hour) }}/hour</span>
                <router-link :to="`/futsals/${futsal.id}`" class="futsal-details-btn">
                  View Details
                </router-link>
              </div>
            </div>
          </div>
        </div>
        <div v-else class="loading-text">Loading featured futsals...</div>

        <div class="section-cta">
          <router-link to="/futsals" class="btn btn-primary"> Explore All Futsals </router-link>
        </div>
      </div>
    </section>

    <!-- How It Works Section -->
    <section class="how-it-works-section">
      <div class="container">
        <h2 class="section-title">How Booksall Works</h2>

        <div class="steps-grid">
          <div class="step-item">
            <div class="step-number">1</div>
            <h3 class="step-title">Find a Futsal Court</h3>
            <p class="step-description">
              Browse through our extensive list of futsal courts and filter by location, price, or
              facilities.
            </p>
          </div>

          <div class="step-item">
            <div class="step-number">2</div>
            <h3 class="step-title">Choose Your Time Slot</h3>
            <p class="step-description">
              Select from available time slots that fit your schedule and see real-time
              availability.
            </p>
          </div>

          <div class="step-item">
            <div class="step-number">3</div>
            <h3 class="step-title">Book & Play</h3>
            <p class="step-description">
              Complete your booking with secure payment and receive instant confirmation. Just show
              up and play!
            </p>
          </div>
        </div>

        <div class="section-cta">
          <router-link to="/futsals" class="btn btn-primary"> Find a Court Now </router-link>
        </div>
      </div>
    </section>

    <!-- Testimonials Section -->
    <section class="testimonials-section">
      <div class="container">
        <h2 class="section-title">What Our Users Say</h2>

        <div class="testimonials-grid">
          <!-- Testimonial 1 -->
          <div class="testimonial-card">
            <div class="testimonial-header">
              <div class="testimonial-avatar"></div>
              <div class="testimonial-user">
                <h4 class="testimonial-name">Sakshyam Parajuli</h4>
                <div class="testimonial-rating">
                  <svg
                    v-for="n in 5"
                    :key="n"
                    xmlns="http://www.w3.org/2000/svg"
                    class="star-icon"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24 .588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3 .921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784 .57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81 .588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                    />
                  </svg>
                </div>
              </div>
            </div>
            <p class="testimonial-text">
              "Booksall has completely changed how our team books futsal courts. No more calling
              around to check availability. Just a few clicks and we're set!"
            </p>
          </div>

          <!-- Testimonial 2 -->
          <div class="testimonial-card">
            <div class="testimonial-header">
              <div class="testimonial-avatar"></div>
              <div class="testimonial-user">
                <h4 class="testimonial-name">Aayash Dwa</h4>
                <div class="testimonial-rating">
                  <svg
                    v-for="n in 5"
                    :key="n"
                    xmlns="http://www.w3.org/2000/svg"
                    class="star-icon"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24 .588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3 .921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784 .57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81 .588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                    />
                  </svg>
                </div>
              </div>
            </div>
            <p class="testimonial-text">
              "I love the detailed information about each futsal court. The photos and easy maps
              location helped me find the perfect venue for our weekly games. The booking process
              was super simple and smooth too!"
            </p>
          </div>

          <!-- Testimonial 3 -->
          <div class="testimonial-card">
            <div class="testimonial-header">
              <div class="testimonial-avatar"></div>
              <div class="testimonial-user">
                <h4 class="testimonial-name">Imperial Rulz Futsal</h4>
                <div class="testimonial-rating">
                  <svg
                    v-for="n in 5"
                    :key="n"
                    xmlns="http://www.w3.org/2000/svg"
                    class="star-icon"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24 .588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3 .921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784 .57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81 .588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                    />
                  </svg>
                </div>
              </div>
            </div>
            <p class="testimonial-text">
              "As a futsal venue owner, partnering with Booksall has increased our bookings by 40%.
              The platform is easy to use and their customer service is excellent."
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Final CTA Section -->
    <section class="final-cta-section">
      <div class="container">
        <h2 class="cta-title" style="color: white">Ready to Find Your Perfect Futsal Court?</h2>
        <p class="cta-subtitle">
          Join thousands of futsal players who book courts through Booksall every day. Fast, easy,
          and reliable.
        </p>
        <div class="cta-buttons">
          <router-link to="/futsals" class="btn btn-primary"> Browse Futsals </router-link>
          <router-link :to="isLoggedIn ? '/profile' : '/register'" class="btn btn-outline-light">
            {{ isLoggedIn ? 'Profile' : 'Create Free Account' }}
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import apiClient from '@/axios'

// State
const featuredFutsals = ref([])
const isLoading = ref(true)
const isLoggedIn = ref(false)

// Methods
const fetchFeaturedFutsals = async () => {
  try {
    isLoading.value = true
    const response = await apiClient.get('futsal/list-futsals/')
    // Filter futsals where featured_futsal is true
    featuredFutsals.value = response.data.filter((futsal) => futsal.featured_futsal === true)
  } catch (error) {
    console.error('Error fetching featured futsals:', error)
    featuredFutsals.value = []
  } finally {
    isLoading.value = false
  }
}

const checkUserLogin = async () => {
  try {
    await apiClient.get('auth/user/')
    isLoggedIn.value = true // If request succeeds, user is logged in
  } catch (error) {
    console.error('User not logged in:', error)
    isLoggedIn.value = false // If request fails (e.g., 401), user is not logged in
  }
}

const formatPrice = (price) => {
  return price ? parseFloat(price).toLocaleString() : 'N/A'
}

onMounted(async () => {
  await Promise.all([fetchFeaturedFutsals(), checkUserLogin()])
})
</script>

<style scoped>
/* General Styles */
.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.section-title {
  font-size: 1.875rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 3rem;
}

.section-cta {
  text-align: center;
  margin-top: 3rem;
}

.btn {
  display: inline-block;
  padding: 1rem 2rem;
  border-radius: 0.5rem;
  font-weight: 700;
  font-size: 1.125rem;
  text-decoration: none;
  transition: all 0.2s;
  cursor: pointer;
}

.btn-primary {
  background-color: #16a34a;
  color: white;
}

.btn-primary:hover {
  background-color: #15803d;
}

.btn-outline {
  background-color: transparent;
  border: 2px solid white;
  color: white;
}

.btn-outline:hover {
  background-color: white;
  color: #16a34a;
}

.btn-outline-light {
  background-color: transparent;
  border: 2px solid white;
  color: white;
}

.btn-outline-light:hover {
  background-color: white;
  color: #16a34a;
}

/* Hero Section */
.hero {
  position: relative;
  background-color: #16a34a;
  color: white;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background-color: black;
  opacity: 0.3;
}

.hero-container {
  position: relative;
  z-index: 10;
  padding: 5rem 1rem;
}

.hero-content {
  max-width: 48rem;
}

.hero-title {
  font-size: 2.25rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  line-height: 1.2;
}

.hero-subtitle {
  font-size: 1.25rem;
  margin-bottom: 2rem;
  color: #bbf7d0;
}

.hero-buttons {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

/* Features Section */
.features-section {
  padding: 4rem 0;
  background-color: #f9fafb;
}

.features-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
}

.feature-card {
  background-color: white;
  padding: 1.5rem;
  border-radius: 0.5rem;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
  text-align: center;
}

.feature-icon-wrapper {
  background-color: #dcfce7;
  width: 4rem;
  height: 4rem;
  border-radius: 9999px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1rem;
}

.feature-icon {
  width: 2rem;
  height: 2rem;
  color: #16a34a;
}

.feature-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.feature-description {
  color: #4b5563;
  font-size: 0.875rem;
}

/* Featured Futsals Section */
.featured-section {
  padding: 4rem 0;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 3rem;
}

.view-all-link {
  color: #16a34a;
  font-weight: 600;
  display: flex;
  align-items: center;
  text-decoration: none;
  transition: color 0.2s;
}

.view-all-link:hover {
  color: #15803d;
}

.view-all-icon {
  width: 1.25rem;
  height: 1.25rem;
  margin-left: 0.25rem;
}

.futsal-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
}

.futsal-card {
  background-color: white;
  border-radius: 0.5rem;
  overflow: hidden;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
  transition: box-shadow 0.2s;
}

.futsal-card:hover {
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

.futsal-image-container {
  position: relative;
  height: 12rem;
  background-color: #e5e7eb;
}

.futsal-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.futsal-badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  font-size: 0.875rem;
  font-weight: 500;
  color: white;
}

.futsal-badge-popular {
  background-color: #16a34a;
}

.futsal-badge-new {
  background-color: #3b82f6;
}

.futsal-badge-hot {
  background-color: #ef4444;
}

.futsal-content {
  padding: 1.5rem;
}

.futsal-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 0.5rem;
}

.futsal-title {
  font-size: 1.25rem;
  font-weight: 700;
}

.futsal-rating {
  display: flex;
  align-items: center;
}

.rating-icon {
  width: 1.25rem;
  height: 1.25rem;
  color: #f59e0b;
}

.rating-text {
  margin-left: 0.25rem;
  color: #4b5563;
}

.futsal-location {
  color: #6b7280;
  margin-bottom: 1rem;
}

.futsal-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.futsal-price {
  color: #16a34a;
  font-weight: 700;
}

.futsal-details-btn {
  background-color: #dcfce7;
  color: #16a34a;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-weight: 500;
  text-decoration: none;
  transition: background-color 0.2s;
}

.futsal-details-btn:hover {
  background-color: #bbf7d0;
}

/* How It Works Section */
.how-it-works-section {
  padding: 4rem 0;
  background-color: #f9fafb;
}

.steps-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
}

.step-item {
  text-align: center;
}

.step-number {
  background-color: #16a34a;
  width: 4rem;
  height: 4rem;
  border-radius: 9999px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1.5rem;
  color: white;
  font-size: 1.5rem;
  font-weight: 700;
}

.step-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
}

.step-description {
  color: #4b5563;
}

/* Testimonials Section */
.testimonials-section {
  padding: 4rem 0;
}

.testimonials-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
}

.testimonial-card {
  background-color: white;
  padding: 1.5rem;
  border-radius: 0.5rem;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
}

.testimonial-header {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.testimonial-avatar {
  width: 3rem;
  height: 3rem;
  border-radius: 9999px;
  background-color: #e5e7eb;
  margin-right: 1rem;
}

.testimonial-name {
  font-weight: 600;
}

.testimonial-rating {
  display: flex;
  color: #f59e0b;
}

.star-icon {
  width: 1rem;
  height: 1rem;
}

.testimonial-text {
  color: #4b5563;
}

/* Final CTA Section */
.final-cta-section {
  padding: 4rem 0;
  background-color: #16a34a;
  color: white;
  text-align: center;
}

.cta-title {
  font-size: 1.875rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
}

.cta-subtitle {
  font-size: 1.25rem;
  color: #bbf7d0;
  margin-bottom: 2rem;
  max-width: 48rem;
  margin-left: auto;
  margin-right: auto;
}

.cta-buttons {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  justify-content: center;
}

/* Loading Text */
.loading-text {
  text-align: center;
  color: #6b7280;
  font-size: 1rem;
  margin: 2rem 0;
}

/* Media Queries */
@media (min-width: 640px) {
  .hero-title {
    font-size: 3rem;
  }

  .hero-buttons {
    flex-direction: row;
  }

  .cta-buttons {
    flex-direction: row;
    justify-content: center;
  }
}

@media (min-width: 768px) {
  .hero-container {
    padding: 8rem 1rem;
  }

  .features-grid {
    grid-template-columns: repeat(3, 1fr);
  }

  .futsal-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .steps-grid {
    grid-template-columns: repeat(3, 1fr);
  }

  .testimonials-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .futsal-grid {
    grid-template-columns: repeat(3, 1fr);
  }

  .testimonials-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
</style>