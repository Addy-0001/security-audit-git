<template>
  <div class="about-page">
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="container">
        <h1>About Booksall</h1>
        <p class="tagline">Revolutionizing futsal bookings in Nepal</p>
      </div>
    </section>

    <!-- Our Story Section -->
    <section class="story-section">
      <div class="container">
        <div class="section-grid">
          <div class="content-block">
            <h2>Our Story</h2>
            <p>
              Booksall was born out of frustration and passion. As avid futsal players ourselves, we experienced
              firsthand the challenges of booking courts in Nepal. The endless phone calls, the uncertainty of
              availability, and the lack of a streamlined booking process were problems we faced every week.
            </p>
            <p>
              We'd spend hours calling different futsal venues just to check if they had an available slot. Often, by
              the time we confirmed one venue, another would have been a better option. We knew there had to be a better
              way.
            </p>
            <p>
              That's when the idea for Booksall struck – a platform that brings all futsal venues together, allowing
              players to check availability, compare prices, and book courts instantly. No more endless calls, no more
              uncertainty – just more time to enjoy the beautiful game.
            </p>
          </div>
          <div class="image-block">
            <div class="image-container">
              <img src="@/assets/images/player.jpg" alt="Futsal players enjoying a game" class="story-image" />
              <div class="image-caption">The passion that drives us</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Problem Solution Section -->
    <section class="problem-solution-section">
      <div class="container">
        <h2>The Problem We're Solving</h2>

        <div class="cards-container">
          <div class="problem-card">
            <div class="card-icon problem-icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path
                  d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z">
                </path>
                <path d="M14.05 2a9 9 0 0 1 8 7.94"></path>
                <path d="M14.05 6A5 5 0 0 1 18 10"></path>
                <line x1="2" y1="2" x2="22" y2="22"></line>
              </svg>
            </div>
            <h3>Multiple Calls</h3>
            <p>Players had to call numerous venues just to check availability, often waiting on hold or getting
              incomplete information.</p>
          </div>

          <div class="problem-card">
            <div class="card-icon problem-icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="12" y1="6" x2="12" y2="12"></line>
                <line x1="12" y1="16" x2="12.01" y2="16"></line>
              </svg>
            </div>
            <h3>Uncertain Availability</h3>
            <p>No way to know which courts were available without directly contacting each venue, leading to wasted time
              and missed opportunities.</p>
          </div>

          <div class="problem-card">
            <div class="card-icon problem-icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="16" y1="2" x2="16" y2="6"></line>
                <line x1="8" y1="2" x2="8" y2="6"></line>
                <line x1="3" y1="10" x2="21" y2="10"></line>
              </svg>
            </div>
            <h3>Manual Scheduling</h3>
            <p>Booking and payment processes were manual and inefficient, with no way to easily manage or reschedule
              bookings.</p>
          </div>
        </div>

        <div class="solution-block">
          <div class="solution-content">
            <h3>Our Solution: Booksall</h3>
            <ul class="solution-list">
              <li>
                <span class="check-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="20 6 9 17 4 12"></polyline>
                  </svg>
                </span>
                <span>Instant visibility of all available futsal courts in your area</span>
              </li>
              <li>
                <span class="check-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="20 6 9 17 4 12"></polyline>
                  </svg>
                </span>
                <span>Online booking and payment system that eliminates the need for calls</span>
              </li>
              <li>
                <span class="check-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="20 6 9 17 4 12"></polyline>
                  </svg>
                </span>
                <span>User profiles to track booking history and favorite venues</span>
              </li>
              <li>
                <span class="check-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="20 6 9 17 4 12"></polyline>
                  </svg>
                </span>
                <span>Venue management tools for futsal owners to optimize their business</span>
              </li>
              <li>
                <span class="check-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="20 6 9 17 4 12"></polyline>
                  </svg>
                </span>
                <span>Community features to connect players and organize matches</span>
              </li>
            </ul>
          </div>
          <div class="solution-image">
            <img src="@/assets/images/interface.png" alt="Booksall app interface" />
          </div>
        </div>
      </div>
    </section>

    <!-- Team Section -->
    <section class="team-section">
      <div class="container">
        <h2>Meet Our Team</h2>
        <p class="section-subtitle">The passionate minds behind Booksall</p>

        <div class="team-grid">
          <div class="team-member">
            <div class="member-photo">
              <img src="@/assets/images/adamya.png" alt="Adamya Neupane" />
            </div>
            <h3>Adamya Neupane</h3>
            <p class="member-role">Backend Developer</p>
            <p class="member-bio">Adamya brings robust backend architecture to Booksall, ensuring our platform handles
              bookings efficiently and securely.</p>
            <div class="member-social">
              <a href="https://github.com/Addy-0001" class="social-link" aria-label="GitHub">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                  stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path
                    d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22">
                  </path>
                </svg>
              </a>
              <a href="#" class="social-link" aria-label="LinkedIn">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                  stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                  <rect x="2" y="9" width="4" height="12"></rect>
                  <circle cx="4" cy="4" r="2"></circle>
                </svg>
              </a>
            </div>
          </div>

          <div class="team-member">
            <div class="member-photo">
              <img src="@/assets/images/rassu.jpeg" alt="Ayush Bishwokarma" />
            </div>
            <h3>Ayush Bishwokarma</h3>
            <p class="member-role">Frontend Developer</p>
            <p class="member-bio">Ayush crafts the intuitive user interfaces that make Booksall a joy to use, focusing
              on
              user experience and accessibility.</p>
            <div class="member-social">
              <a href="#" class="social-link" aria-label="GitHub">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                  stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path
                    d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22">
                  </path>
                </svg>
              </a>
              <a href="#" class="social-link" aria-label="LinkedIn">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                  stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                  <rect x="2" y="9" width="4" height="12"></rect>
                  <circle cx="4" cy="4" r="2"></circle>
                </svg>
              </a>
            </div>
          </div>

          <div class="team-member">
            <div class="member-photo">
              <img src="@/assets/images/sudipti.jpg" alt="Sudipti Upreti" />
            </div>
            <h3>Sudipti Upreti</h3>
            <p class="member-role">Graphic Designer</p>
            <p class="member-bio">Sudipti specializes in creating responsive designs and interactive elements that make
              the Booksall experience seamless across all devices.</p>
            <div class="member-social">
              <a href="#" class="social-link" aria-label="GitHub">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                  stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path
                    d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22">
                  </path>
                </svg>
              </a>
              <a href="#" class="social-link" aria-label="LinkedIn">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                  stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                  <rect x="2" y="9" width="4" height="12"></rect>
                  <circle cx="4" cy="4" r="2"></circle>
                </svg>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Company Info Section -->
    <section class="company-section">
      <div class="container">
        <div class="company-info">
          <div class="company-logo">
            <img src="@/assets/images/GS-logo.png" alt="Getintoto Software Logo" style="width: 200px;" />
          </div>
          <div class="company-details">
            <h2>Developed by</h2>
            <h3>Getintoto Software Pvt. Ltd.</h3>
            <p>A tech company dedicated to solving real-world problems through innovative software solutions.</p>
            <div class="company-meta">
              <div class="meta-item">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                  stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                  <line x1="16" y1="2" x2="16" y2="6"></line>
                  <line x1="8" y1="2" x2="8" y2="6"></line>
                  <line x1="3" y1="10" x2="21" y2="10"></line>
                </svg>
                <span>Developed in: April 2025</span>
              </div>
              <div class="meta-item">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                  stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                  <circle cx="12" cy="10" r="3"></circle>
                </svg>
                <span>Kathmandu, Nepal</span>
              </div>
              <div class="meta-item">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                  stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                  <polyline points="22,6 12,13 2,6"></polyline>
                </svg>
                <span>info@getintoto.com</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Timeline Section -->
    <section class="timeline-section">
      <div class="container">
        <h2>Our Journey</h2>
        <div class="timeline">
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
              <h3>January 2025</h3>
              <p>Concept Development</p>
              <p>The idea for Booksall was born during a frustrating evening trying to book a futsal court.</p>
            </div>
          </div>

          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
              <h3>February 2025</h3>
              <p>Market Research</p>
              <p>We surveyed over 100 futsal venues and 30 venue owners along with multiple regular futsal players to
                understand the pain points.</p>
            </div>
          </div>

          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
              <h3>March 2025</h3>
              <p>Design & Development</p>
              <p>Our team began designing and developing the platform with a focus on user experience.</p>
            </div>
          </div>

          <div class="timeline-item active">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
              <h3>April 2025</h3>
              <p>Launch</p>
              <p>Booksall officially launched, revolutionizing how futsal courts are booked in Nepal.</p>
            </div>
          </div>

          <div class="timeline-item future">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
              <h3>The Future</h3>
              <p>Expansion</p>
              <p>We're working on expanding to more cities and adding new features to enhance the futsal community.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Call to Action -->
    <section class="cta-section">
      <div class="container">
        <div class="cta-content">
          <h2>Ready to experience hassle-free futsal bookings?</h2>
          <p>Join thousands of players who have already simplified their futsal experience with Booksall.</p>
          <div class="cta-buttons">
            <router-link to="/register" class="cta-button primary">
              Sign Up Now
            </router-link>
            <router-link to="/futsals" class="cta-button secondary">
              Browse Futsals
            </router-link>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
// No specific script functionality needed for this page
</script>

<style scoped>
/* Base Styles */
.about-page {
  color: #374151;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

section {
  padding: 5rem 0;
}

h1,
h2,
h3 {
  color: #111827;
}

/* Hero Section */
.hero-section {
  background-color: #15803d;
  color: white;
  text-align: center;
  padding: 8rem 0;
  position: relative;
  overflow: hidden;
}

.hero-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.1'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
  opacity: 0.2;
}

.hero-section h1 {
  font-size: 3.5rem;
  font-weight: 800;
  margin-bottom: 1rem;
  color: white;
}

.tagline {
  font-size: 1.5rem;
  font-weight: 300;
  max-width: 600px;
  margin: 0 auto;
}

/* Story Section */
.story-section {
  background-color: #f9fafb;
}

.section-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 3rem;
}

@media (min-width: 768px) {
  .section-grid {
    grid-template-columns: 1fr 1fr;
    align-items: center;
  }
}

.content-block h2 {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  color: #15803d;
}

.content-block p {
  margin-bottom: 1.5rem;
  line-height: 1.7;
  font-size: 1.1rem;
}

.image-container {
  position: relative;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

.story-image {
  width: 100%;
  height: auto;
  display: block;
}

.image-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(21, 128, 61, 0.8);
  color: white;
  padding: 1rem;
  text-align: center;
  font-weight: 500;
}

/* Problem Solution Section */
.problem-solution-section {
  background-color: white;
}

.problem-solution-section h2 {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 3rem;
  text-align: center;
  color: #15803d;
}

.cards-container {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
  margin-bottom: 4rem;
}

@media (min-width: 768px) {
  .cards-container {
    grid-template-columns: repeat(3, 1fr);
  }
}

.problem-card {
  background-color: #f9fafb;
  border-radius: 8px;
  padding: 2rem;
  text-align: center;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.problem-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

.card-icon {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1.5rem;
}

.problem-icon {
  background-color: #fee2e2;
  color: #b91c1c;
}

.problem-icon svg {
  width: 32px;
  height: 32px;
}

.problem-card h3 {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.problem-card p {
  color: #6b7280;
  line-height: 1.6;
}

.solution-block {
  background-color: #ecfdf5;
  border-radius: 12px;
  padding: 3rem;
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

@media (min-width: 768px) {
  .solution-block {
    grid-template-columns: 2fr 1fr;
    align-items: center;
  }
}

.solution-content h3 {
  font-size: 1.75rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  color: #15803d;
}

.solution-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.solution-list li {
  display: flex;
  align-items: flex-start;
  margin-bottom: 1rem;
}

.check-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  background-color: #15803d;
  border-radius: 50%;
  margin-right: 1rem;
  flex-shrink: 0;
}

.check-icon svg {
  width: 16px;
  height: 16px;
  color: white;
}

.solution-image img {
  width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

/* Team Section */
.team-section {
  background-color: #f9fafb;
  text-align: center;
}

.team-section h2 {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: #15803d;
}

.section-subtitle {
  font-size: 1.25rem;
  color: #6b7280;
  margin-bottom: 3rem;
}

.team-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 3rem;
  max-width: 1000px;
  margin: 0 auto;
}

@media (min-width: 768px) {
  .team-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

.team-member {
  background-color: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.team-member:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

.member-photo {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  overflow: hidden;
  margin: 0 auto 1.5rem;
  border: 4px solid #15803d;
}

.member-photo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.team-member h3 {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.member-role {
  color: #15803d;
  font-weight: 600;
  margin-bottom: 1rem;
}

.member-bio {
  color: #6b7280;
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.member-social {
  display: flex;
  justify-content: center;
  gap: 1rem;
}

.social-link {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: #f3f4f6;
  color: #4b5563;
  transition: all 0.2s ease;
}

.social-link:hover {
  background-color: #15803d;
  color: white;
}

.social-link svg {
  width: 20px;
  height: 20px;
}

/* Company Section */
.company-section {
  background-color: white;
}

.company-info {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

@media (min-width: 768px) {
  .company-info {
    flex-direction: row;
    text-align: left;
    align-items: flex-start;
  }
}

.company-logo {
  margin-bottom: 2rem;
}

@media (min-width: 768px) {
  .company-logo {
    margin-right: 3rem;
    margin-bottom: 0;
  }
}

.company-logo img {
  border-radius: 12px;
}

.company-details h2 {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #6b7280;
}

.company-details h3 {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: #15803d;
}

.company-details p {
  margin-bottom: 2rem;
  font-size: 1.1rem;
  line-height: 1.7;
  max-width: 600px;
}

.company-meta {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

@media (min-width: 640px) {
  .company-meta {
    flex-direction: row;
    flex-wrap: wrap;
  }
}

.meta-item {
  display: flex;
  align-items: center;
  color: #6b7280;
  margin-right: 2rem;
}

.meta-item svg {
  width: 20px;
  height: 20px;
  margin-right: 0.75rem;
  color: #15803d;
}

/* Timeline Section */
.timeline-section {
  background-color: #f9fafb;
  text-align: center;
}

.timeline-section h2 {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 3rem;
  color: #15803d;
}

.timeline {
  position: relative;
  max-width: 800px;
  margin: 0 auto;
}

.timeline::before {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  left: 50%;
  width: 4px;
  background-color: #e5e7eb;
  transform: translateX(-50%);
}

.timeline-item {
  position: relative;
  margin-bottom: 3rem;
}

.timeline-dot {
  position: absolute;
  top: 0;
  left: 50%;
  width: 20px;
  height: 20px;
  background-color: #e5e7eb;
  border-radius: 50%;
  transform: translateX(-50%);
  z-index: 1;
}

.timeline-item.active .timeline-dot {
  background-color: #15803d;
  box-shadow: 0 0 0 4px rgba(21, 128, 61, 0.2);
}

.timeline-item.future .timeline-dot {
  background-color: #9ca3af;
}

.timeline-content {
  position: relative;
  width: calc(50% - 30px);
  padding: 1.5rem;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.timeline-item:nth-child(odd) .timeline-content {
  margin-left: auto;
}

.timeline-item:nth-child(even) .timeline-content {
  margin-right: auto;
}

.timeline-content h3 {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #15803d;
}

.timeline-content p {
  margin-bottom: 0.5rem;
}

.timeline-content p:first-of-type {
  font-weight: 600;
}

/* Call to Action */
.cta-section {
  background-color: #15803d;
  color: white;
  text-align: center;
  padding: 5rem 0;
}

.cta-content {
  max-width: 800px;
  margin: 0 auto;
}

.cta-content h2 {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: white;
}

.cta-content p {
  font-size: 1.25rem;
  margin-bottom: 2rem;
  opacity: 0.9;
}

.cta-buttons {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  justify-content: center;
}

@media (min-width: 640px) {
  .cta-buttons {
    flex-direction: row;
  }
}

.cta-button {
  display: inline-block;
  padding: 1rem 2rem;
  border-radius: 50px;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.3s ease;
}

.cta-button.primary {
  background-color: white;
  color: #15803d;
}

.cta-button.primary:hover {
  background-color: #f3f4f6;
  transform: translateY(-2px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.cta-button.secondary {
  background-color: transparent;
  color: white;
  border: 2px solid white;
}

.cta-button.secondary:hover {
  background-color: rgba(255, 255, 255, 0.1);
  transform: translateY(-2px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* Responsive adjustments */
@media (max-width: 640px) {
  .hero-section h1 {
    font-size: 2.5rem;
  }

  .tagline {
    font-size: 1.25rem;
  }

  .content-block h2,
  .problem-solution-section h2,
  .team-section h2,
  .timeline-section h2,
  .cta-content h2 {
    font-size: 2rem;
  }

  .timeline::before {
    left: 20px;
  }

  .timeline-dot {
    left: 20px;
  }

  .timeline-content {
    width: calc(100% - 50px);
    margin-left: 50px !important;
  }
}
</style>