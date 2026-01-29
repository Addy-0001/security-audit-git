<template>
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <!-- Company Info -->
                <div class="footer-section">
                    <h2 class="footer-title" style="color: white;">Booksall</h2>
                    <p class="footer-description">
                        The easiest way to book futsal courts near you. Play more, worry less.
                    </p>
                    <div class="social-links">
                        <a href="#" class="social-link">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                                fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" class="social-icon">
                                <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
                            </svg>
                        </a>
                        <a href="#" class="social-link">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                                fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" class="social-icon">
                                <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                                <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                                <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
                            </svg>
                        </a>
                        <a href="#" class="social-link">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                                fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round" class="social-icon">
                                <path
                                    d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z">
                                </path>
                            </svg>
                        </a>
                    </div>
                </div>

                <!-- Quick Links -->
                <div class="footer-section">
                    <h3 class="footer-subtitle" style="color: white;">Quick Links</h3>
                    <ul class="footer-links">
                        <li><router-link to="/" class="footer-link">Home</router-link></li>
                        <li><router-link to="/futsals" class="footer-link">Find Futsals</router-link></li>
                        <li><router-link to="/about" class="footer-link">About Us</router-link></li>
                        <li><router-link to="/contact" class="footer-link">Contact</router-link></li>
                    </ul>
                </div>

                <!-- Account -->
                <!-- <div class="footer-section">
                    <h3 class="footer-subtitle" style="color: white;">Account</h3>
                    <ul class="footer-links">
                        <li><router-link to="/login" class="footer-link">Login</router-link></li>
                        <li><router-link to="/signup" class="footer-link">Sign Up</router-link></li>
                        <li><router-link to="/profile" class="footer-link">My Profile</router-link></li>
                        <li><router-link to="/bookings" class="footer-link">My Bookings</router-link></li>
                    </ul>
                </div> -->

                <!-- Contact -->
                <div class="footer-section">
                    <h3 class="footer-subtitle" style="color: white;">Contact Us</h3>
                    <ul class="footer-links">
                        <li class="contact-item">
                            <svg xmlns="http://www.w3.org/2000/svg" class="contact-icon" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                            </svg>
                            <span class="contact-text">Bhaktapur, Nepal</span>
                        </li>
                        <li class="contact-item">
                            <svg xmlns="http://www.w3.org/2000/svg" class="contact-icon" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                            </svg>
                            <span class="contact-text">info@booksall.app</span>
                        </li>
                        <li class="contact-item">
                            <svg xmlns="http://www.w3.org/2000/svg" class="contact-icon" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                            </svg>
                            <span class="contact-text">+977 9767649598</span>
                        </li>
                    </ul>
                </div>
            </div>

            <!-- Divider -->
            <div class="footer-bottom">
                <div class="footer-bottom-content">
                    <p class="copyright">
                        &copy; {{ new Date().getFullYear() }} Booksall. All rights reserved.
                    </p>
                    <div class="legal-links">
                        <ul class="legal-links-list">
                            <li>
                                <RouterLink to="/privacy-policy" class="legal-link">Privacy Policy</RouterLink>
                            </li>
                            <li>
                                <RouterLink to="/terms" class="legal-link">Terms of Service</RouterLink>
                            </li>

                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </footer>
</template>

<script setup>
import { RouterLink } from 'vue-router';

// No additional script needed for the footer
</script>

<style scoped>
.footer {
    background-color: #166534;
    /* green-800 equivalent */
    color: white;
    padding-top: 2.5rem;
    padding-bottom: 1.5rem;
}

.container {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

.footer-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2rem;
}

.footer-section {
    margin-bottom: 1.5rem;
}

.footer-title {
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.footer-description {
    color: #bbf7d0;
    /* green-200 equivalent */
    margin-bottom: 1rem;
}

.social-links {
    display: flex;
    gap: 1rem;
}

.social-link {
    color: white;
    transition: color 0.2s;
}

.social-link:hover {
    color: #bbf7d0;
    /* green-200 equivalent */
}

.social-icon {
    width: 1.5rem;
    height: 1.5rem;
}

.footer-subtitle {
    font-size: 1.125rem;
    font-weight: 600;
    margin-bottom: 1rem;
}

.footer-links {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.footer-link {
    color: #bbf7d0;
    /* green-200 equivalent */
    text-decoration: none;
    transition: color 0.2s;
}

.footer-link:hover {
    color: white;
}

.contact-item {
    display: flex;
    align-items: flex-start;
    margin-bottom: 0.5rem;
}

.contact-icon {
    width: 1.25rem;
    height: 1.25rem;
    margin-right: 0.5rem;
    margin-top: 0.125rem;
}

.contact-text {
    color: #bbf7d0;
    /* green-200 equivalent */
}

.footer-bottom {
    border-top: 1px solid #15803d;
    /* green-700 equivalent */
    margin-top: 2rem;
    padding-top: 1.5rem;
}

.footer-bottom-content {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.copyright {
    font-size: 0.875rem;
    color: #86efac;
    /* green-300 equivalent */
}

.legal-links {
    margin-top: 1rem;
}

.legal-links-list {
    display: flex;
    gap: 1rem;
    list-style: none;
    padding: 0;
    margin: 0;
}

.legal-link {
    color: #86efac;
    /* green-300 equivalent */
    font-size: 0.875rem;
    text-decoration: none;
    transition: color 0.2s;
}

.legal-link:hover {
    color: white;
}

/* Media query for desktop */
@media (min-width: 768px) {
    .footer-grid {
        grid-template-columns: repeat(4, 1fr);
        gap: 2rem;
    }

    .footer-bottom-content {
        flex-direction: row;
        justify-content: space-between;
    }

    .legal-links {
        margin-top: 0;
    }
}
</style>