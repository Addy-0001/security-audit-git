<template>
    <div class="not-found-container">
        <!-- Background Elements -->
        <div class="field-lines"></div>

        <!-- Main Content -->
        <div class="content-container">
            <div class="error-content">
                <h1 class="error-title">
                    <span class="error-code">404</span>
                    <span class="error-text">Page Out of Bounds!</span>
                </h1>

                <p class="error-message">
                    Oops! Looks like this play went off the field. The page you're looking for doesn't exist.
                </p>

                <div class="search-container">
                    <input type="text" v-model="searchQuery" placeholder="Search for futsals..." class="search-input"
                        @keyup.enter="handleSearch" />
                    <button class="search-button" @click="handleSearch">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="11" cy="11" r="8"></circle>
                            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                        </svg>
                    </button>
                </div>

                <div class="action-buttons">
                    <router-link to="/" class="primary-button">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                            <polyline points="9 22 9 12 15 12 15 22"></polyline>
                        </svg>
                        Back to Home
                    </router-link>

                    <router-link to="/futsals" class="secondary-button">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="12" cy="12" r="10"></circle>
                            <path
                                d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z">
                            </path>
                            <line x1="2" y1="12" x2="22" y2="12"></line>
                        </svg>
                        Browse Futsals
                    </router-link>
                </div>
            </div>

            <!-- Interactive Football Element -->
            <div class="interactive-element">
                <div class="goal-post">
                    <div class="post left-post"></div>
                    <div class="crossbar"></div>
                    <div class="post right-post"></div>
                    <div class="net"></div>
                </div>

                <div ref="ball" class="football" @click="kickBall" :style="ballStyle">
                    <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="50" cy="50" r="48" fill="#ffffff" stroke="#000000" stroke-width="1" />
                        <path d="M50 2 L50 98 M2 50 L98 50" stroke="#000000" stroke-width="1" />
                        <path d="M26 2 C15 15, 15 35, 2 50" stroke="#000000" stroke-width="1" />
                        <path d="M74 2 C85 15, 85 35, 98 50" stroke="#000000" stroke-width="1" />
                        <path d="M2 50 C15 65, 15 85, 26 98" stroke="#000000" stroke-width="1" />
                        <path d="M98 50 C85 65, 85 85, 74 98" stroke="#000000" stroke-width="1" />
                    </svg>
                </div>

                <div class="instruction">Click the ball to score a goal!</div>
            </div>
        </div>

        <!-- Popular Links -->
        <div class="popular-links">
            <h3>Quick Links</h3>
            <div class="links-grid">
                <RouterLink to="/login" class="quick-link">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path>
                        <polyline points="10 17 15 12 10 7"></polyline>
                        <line x1="15" y1="12" x2="3" y2="12"></line>
                    </svg>
                    Login
                </RouterLink>

                <RouterLink to="/register" class="quick-link">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                        <circle cx="8.5" cy="7" r="4"></circle>
                        <line x1="20" y1="8" x2="20" y2="14"></line>
                        <line x1="23" y1="11" x2="17" y2="11"></line>
                    </svg>
                    Register
                </RouterLink>

                <RouterLink to="/blog" class="quick-link">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M12 20h9"></path>
                        <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
                    </svg>
                    Blog
                </RouterLink>

                <RouterLink to="/contact" class="quick-link">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path
                            d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z">
                        </path>
                    </svg>
                    Contact Us
                </RouterLink>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { RouterLink } from 'vue-router';

const router = useRouter();
const searchQuery = ref('');
const ball = ref(null);
const ballStyle = reactive({
    transform: 'translate(0, 0) rotate(0deg)',
    transition: 'none'
});

let goalScored = ref(false);
let goalCount = ref(0);

const handleSearch = () => {
    if (searchQuery.value.trim()) {
        // In a real app, you would navigate to search results
        router.push({
            path: '/futsals',
            query: { search: searchQuery.value }
        });
    }
};

const kickBall = () => {
    if (goalScored.value) {
        // Reset ball position
        ballStyle.transition = 'none';
        ballStyle.transform = 'translate(0, 0) rotate(0deg)';

        // Allow animation to take effect on next frame
        setTimeout(() => {
            goalScored.value = false;
        }, 10);
        return;
    }

    // Random rotation for the ball
    const rotation = Math.floor(Math.random() * 720) - 360;

    // Set ball animation
    ballStyle.transition = 'transform 1s cubic-bezier(0.2, 0.8, 0.3, 1)';
    ballStyle.transform = `translate(-50%, -200px) rotate(${rotation}deg)`;

    // Goal celebration
    setTimeout(() => {
        goalScored.value = true;
        goalCount.value++;

        // Show goal message
        const instruction = document.querySelector('.instruction');
        if (instruction) {
            instruction.textContent = goalCount.value === 1
                ? 'GOAL! Click the ball to try again!'
                : `GOAL! That's ${goalCount.value} goals! Click to continue.`;
        }
    }, 1000);
};

onMounted(() => {
    // Add some random movement to the ball on page load
    setTimeout(() => {
        ballStyle.transition = 'transform 0.5s ease-in-out';
        ballStyle.transform = 'translate(5px, -5px) rotate(5deg)';

        setTimeout(() => {
            ballStyle.transform = 'translate(0, 0) rotate(0deg)';
        }, 500);
    }, 1000);
});
</script>

<style scoped>
.not-found-container {
    min-height: 100vh;
    background-color: #f8f9fa;
    position: relative;
    overflow: hidden;
    padding: 2rem 1rem;
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* Field Lines Background */
.field-lines {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image:
        linear-gradient(to right, rgba(21, 128, 61, 0.05) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(21, 128, 61, 0.05) 1px, transparent 1px);
    background-size: 20px 20px;
    z-index: 0;
}

.field-lines::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 0;
    right: 0;
    height: 2px;
    background-color: rgba(21, 128, 61, 0.2);
    transform: translateY(-50%);
}

.field-lines::after {
    content: '';
    position: absolute;
    top: 0;
    left: 50%;
    bottom: 0;
    width: 2px;
    background-color: rgba(21, 128, 61, 0.2);
    transform: translateX(-50%);
}

/* Main Content */
.content-container {
    position: relative;
    z-index: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    max-width: 1200px;
    width: 100%;
    margin: 0 auto;
    padding: 2rem 0;
}

@media (min-width: 1024px) {
    .content-container {
        flex-direction: row;
        align-items: flex-start;
        gap: 4rem;
    }
}

.error-content {
    text-align: center;
    max-width: 600px;
}

.error-title {
    margin-bottom: 1.5rem;
    line-height: 1.2;
    display: flex;
    flex-direction: column;
}

.error-code {
    font-size: 8rem;
    font-weight: 800;
    color: #15803d;
    text-shadow:
        3px 3px 0 rgba(21, 128, 61, 0.2),
        -1px -1px 0 rgba(255, 255, 255, 0.7);
    line-height: 1;
}

.error-text {
    font-size: 2.5rem;
    font-weight: 700;
    color: #111827;
}

.error-message {
    font-size: 1.25rem;
    color: #4b5563;
    margin-bottom: 2rem;
}

/* Search Box */
.search-container {
    position: relative;
    max-width: 400px;
    margin: 0 auto 2rem;
}

.search-input {
    width: 100%;
    padding: 0.75rem 3rem 0.75rem 1.5rem;
    font-size: 1rem;
    border: 2px solid #d1d5db;
    border-radius: 50px;
    outline: none;
    transition: all 0.3s ease;
}

.search-input:focus {
    border-color: #15803d;
    box-shadow: 0 0 0 3px rgba(21, 128, 61, 0.2);
}

.search-button {
    position: absolute;
    right: 0.75rem;
    top: 50%;
    transform: translateY(-50%);
    background-color: #15803d;
    color: white;
    border: none;
    width: 2rem;
    height: 2rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: background-color 0.2s ease;
}

.search-button:hover {
    background-color: #166534;
}

.search-button svg {
    width: 1rem;
    height: 1rem;
}

/* Action Buttons */
.action-buttons {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 2rem;
}

.primary-button,
.secondary-button {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1.5rem;
    border-radius: 50px;
    font-weight: 600;
    font-size: 1rem;
    transition: all 0.2s ease;
    text-decoration: none;
}

.primary-button {
    background-color: #15803d;
    color: white;
    border: none;
}

.primary-button:hover {
    background-color: #166534;
    transform: translateY(-2px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.secondary-button {
    background-color: white;
    color: #15803d;
    border: 2px solid #15803d;
}

.secondary-button:hover {
    background-color: #f0fdf4;
    transform: translateY(-2px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.primary-button svg,
.secondary-button svg {
    width: 1.25rem;
    height: 1.25rem;
}

/* Interactive Football Element */
.interactive-element {
    position: relative;
    width: 300px;
    height: 300px;
    margin: 0 auto;
}

.goal-post {
    position: absolute;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 200px;
    height: 120px;
}

.post {
    position: absolute;
    width: 8px;
    height: 120px;
    background-color: white;
    border: 2px solid #d1d5db;
}

.left-post {
    left: 0;
}

.right-post {
    right: 0;
}

.crossbar {
    position: absolute;
    top: 0;
    left: 8px;
    right: 8px;
    height: 8px;
    background-color: white;
    border: 2px solid #d1d5db;
}

.net {
    position: absolute;
    top: 8px;
    left: 8px;
    right: 8px;
    height: 112px;
    background-image:
        linear-gradient(to right, rgba(209, 213, 219, 0.5) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(209, 213, 219, 0.5) 1px, transparent 1px);
    background-size: 10px 10px;
    border-bottom-left-radius: 20px;
    border-bottom-right-radius: 20px;
}

.football {
    position: absolute;
    bottom: 40px;
    left: 50%;
    transform: translateX(-50%);
    width: 60px;
    height: 60px;
    cursor: pointer;
    filter: drop-shadow(0 4px 3px rgba(0, 0, 0, 0.2));
    z-index: 2;
}

.football:hover {
    transform: translateX(-50%) scale(1.05);
}

.instruction {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    text-align: center;
    font-size: 1rem;
    color: #6b7280;
    font-weight: 500;
}

/* Popular Links */
.popular-links {
    margin-top: 2rem;
    width: 100%;
    max-width: 800px;
    text-align: center;
}

.popular-links h3 {
    font-size: 1.5rem;
    color: #111827;
    margin-bottom: 1.5rem;
    position: relative;
    display: inline-block;
}

.popular-links h3::after {
    content: '';
    position: absolute;
    bottom: -8px;
    left: 50%;
    transform: translateX(-50%);
    width: 60px;
    height: 3px;
    background-color: #15803d;
    border-radius: 3px;
}

.links-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
}

@media (min-width: 640px) {
    .links-grid {
        grid-template-columns: repeat(4, 1fr);
    }
}

.quick-link {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    padding: 1rem;
    background-color: white;
    border-radius: 8px;
    text-decoration: none;
    color: #4b5563;
    transition: all 0.2s ease;
    border: 1px solid #e5e7eb;
}

.quick-link:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    color: #15803d;
    border-color: #15803d;
}

.quick-link svg {
    width: 1.5rem;
    height: 1.5rem;
    color: #15803d;
}
</style>