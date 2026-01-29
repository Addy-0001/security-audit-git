<template>
    <div class="login-page">
        <div class="login-container">
            <!-- Logo and Header -->
            <div class="login-header">
                <div class="logo">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="logo-icon">
                        <circle cx="12" cy="12" r="10"></circle>
                        <polygon points="10 8 16 12 10 16 10 8"></polygon>
                    </svg>
                    <h1>Booksall</h1>
                </div>
                <h2>Welcome Back!</h2>
                <p>Sign in to your account to continue</p>
            </div>

            <!-- Login Form -->
            <form @submit.prevent="handleLogin" class="login-form">
                <!-- Phone Number Input -->
                <div class="form-group" :class="{ 'error': errors.phone }">
                    <label for="phone">Phone Number</label>
                    <div class="input-wrapper">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="input-icon">
                            <path
                                d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z">
                            </path>
                        </svg>
                        <input type="tel" id="phone" v-model="phone" placeholder="Enter your phone number"
                            @input="validatePhone" :class="{ 'input-error': errors.phone }" />
                    </div>
                    <p class="error-message" v-if="errors.phone">{{ errors.phone }}</p>
                </div>

                <!-- Password Input -->
                <div class="form-group" :class="{ 'error': errors.password }">
                    <label for="password">Password</label>
                    <div class="input-wrapper">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="input-icon">
                            <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                            <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                        </svg>
                        <input :type="showPassword ? 'text' : 'password'" id="password" v-model="password"
                            placeholder="Enter your password" @input="validatePassword"
                            :class="{ 'input-error': errors.password }" />
                        <button type="button" class="toggle-password" @click="togglePasswordVisibility" tabindex="-1">
                            <svg v-if="!showPassword" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                                <circle cx="12" cy="12" r="3"></circle>
                            </svg>
                            <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path
                                    d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24">
                                </path>
                                <line x1="1" y1="1" x2="23" y2="23"></line>
                            </svg>
                        </button>
                    </div>
                    <p class="error-message" v-if="errors.password">{{ errors.password }}</p>
                </div>

                <!-- Forgot Password Link -->
                <div class="forgot-password">
                    <a href="#" @click.prevent="forgotPassword">Forgot Password?</a>
                </div>

                <!-- Login Button -->
                <button type="submit" class="login-button" :disabled="isLoading || !isFormValid">
                    <span v-if="!isLoading">Login</span>
                    <div v-else class="spinner"></div>
                </button>

                <!-- Form Error -->
                <p class="form-error" v-if="formError">{{ formError }}</p>

                <!-- Register Link -->
                <div class="register-link">
                    <p>Don't have an account? <a href="#" @click.prevent="goToRegister">Register</a></p>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import apiClient from '@/axios';
import { useAuthStore } from '@/stores/auth';
const router = useRouter();

const authStore = useAuthStore();

// Form state
const phone = ref('');
const password = ref('');
const showPassword = ref(false);
const isLoading = ref(false);
const formError = ref('');
const errors = ref({
    phone: '',
    password: ''
});

// Computed property to check if form is valid
const isFormValid = computed(() => {
    return phone.value && password.value && !errors.value.phone && !errors.value.password;
});

// Toggle password visibility
const togglePasswordVisibility = () => {
    showPassword.value = !showPassword.value;
};

// Validate phone number
const validatePhone = () => {
    errors.value.phone = '';
    phone.value = phone.value.replace(/\D/g, '');
    if (!phone.value) {
        errors.value.phone = 'Phone number is required';
        return;
    }
    if (phone.value.length !== 10) {
        errors.value.phone = 'Phone number must be 10 digits';
        return;
    }
    if (!phone.value.startsWith('9')) {
        errors.value.phone = 'Phone number must start with 9';
        return;
    }
};

// Validate password
const validatePassword = () => {
    errors.value.password = '';
    if (!password.value) {
        errors.value.password = 'Password is required';
        return;
    }
    if (password.value.length < 6) {
        errors.value.password = 'Password must be at least 6 characters';
        return;
    }
};

// Handle login form submission
const handleLogin = async () => {
    // Validate form fields
    validatePhone();
    validatePassword();

    if (errors.value.phone || errors.value.password) {
        return;
    }

    try {
        isLoading.value = true;
        formError.value = '';

        // Prepare login data
        const loginData = {
            username: phone.value, // Using phone as username since that's what we collect
            password: password.value
        };

        // Make POST request to login endpoint
        const response = await apiClient.post('auth/login/', loginData).then((response) => {
            // Store the token in localStorage
            localStorage.setItem('token', response.data.key);
            authStore.login(response.data.key)
        });


        // Redirect to home page or dashboard
        router.push('/');
    } catch (error) {
        // Handle error
        if (error.response && error.response.data) {
            const errorData = error.response.data;
            if (errorData.non_field_errors) {
                formError.value = errorData.non_field_errors[0];
            } else if (errorData.username) {
                errors.value.phone = errorData.username[0];
            } else if (errorData.password) {
                errors.value.password = errorData.password[0];
            } else {
                formError.value = 'An error occurred. Please try again.';
            }
        } else {
            formError.value = 'An error occurred. Please try again.';
        }
        console.error('Login error:', error);
    } finally {
        isLoading.value = false;
    }
};

// Forgot password handler
const forgotPassword = () => {
    router.push('/password/reset');
};

// Go to register page
const goToRegister = () => {
    router.push('/register');
};
</script>

<style scoped>
/* Login Page Styles */
.login-page {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #f8f9fa;
    padding: 20px;
    font-family: 'Inter', 'Segoe UI', Roboto, sans-serif;
}

.login-container {
    width: 100%;
    max-width: 450px;
    background-color: white;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    padding: 40px;
    transition: transform 0.3s ease;
}

.login-container:hover {
    transform: translateY(-5px);
}

/* Header Styles */
.login-header {
    text-align: center;
    margin-bottom: 30px;
}

.logo {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
}

.logo-icon {
    width: 36px;
    height: 36px;
    color: #2e7d32;
    margin-right: 10px;
}

.logo h1 {
    font-size: 1.8rem;
    font-weight: 800;
    color: #2e7d32;
    margin: 0;
}

.login-header h2 {
    font-size: 1.5rem;
    font-weight: 700;
    color: #333;
    margin: 0 0 10px;
}

.login-header p {
    color: #666;
    font-size: 0.95rem;
    margin: 0;
}

/* Form Styles */
.login-form {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.form-group label {
    font-size: 0.9rem;
    font-weight: 600;
    color: #555;
}

.input-wrapper {
    position: relative;
    display: flex;
    align-items: center;
}

.input-icon {
    position: absolute;
    left: 14px;
    width: 20px;
    height: 20px;
    color: #757575;
}

.input-wrapper input {
    width: 100%;
    padding: 14px 14px 14px 44px;
    border: 2px solid #e0e0e0;
    border-radius: 10px;
    font-size: 1rem;
    color: #333;
    transition: all 0.3s ease;
}

.input-wrapper input:focus {
    outline: none;
    border-color: #2e7d32;
    box-shadow: 0 0 0 3px rgba(46, 125, 50, 0.1);
}

.input-wrapper input::placeholder {
    color: #aaa;
}

.input-wrapper input.input-error {
    border-color: #e53935;
}

.toggle-password {
    position: absolute;
    right: 14px;
    background: none;
    border: none;
    cursor: pointer;
    color: #757575;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0;
}

.toggle-password svg {
    width: 20px;
    height: 20px;
}

.error-message {
    color: #e53935;
    font-size: 0.8rem;
    margin: 4px 0 0;
}

.forgot-password {
    text-align: right;
}

.forgot-password a {
    color: #2e7d32;
    font-size: 0.9rem;
    text-decoration: none;
    transition: color 0.2s ease;
}

.forgot-password a:hover {
    color: #1b5e20;
    text-decoration: underline;
}

.login-button {
    padding: 16px;
    background-color: #2e7d32;
    color: white;
    border: none;
    border-radius: 10px;
    font-size: 1rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 52px;
}

.login-button:hover:not(:disabled) {
    background-color: #1b5e20;
    transform: translateY(-2px);
}

.login-button:disabled {
    background-color: #9e9e9e;
    cursor: not-allowed;
}

.spinner {
    width: 24px;
    height: 24px;
    border: 3px solid rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    border-top-color: white;
    animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
    to {
        transform: rotate(360deg);
    }
}

.form-error {
    color: #e53935;
    text-align: center;
    font-size: 0.9rem;
    margin: 0;
}

.register-link {
    text-align: center;
    margin-top: 10px;
}

.register-link p {
    color: #666;
    font-size: 0.9rem;
    margin: 0;
}

.register-link a {
    color: #2e7d32;
    font-weight: 600;
    text-decoration: none;
    transition: color 0.2s ease;
}

.register-link a:hover {
    color: #1b5e20;
    text-decoration: underline;
}

/* Responsive Styles */
@media (max-width: 500px) {
    .login-container {
        padding: 30px 20px;
    }

    .login-header {
        margin-bottom: 25px;
    }

    .logo-icon {
        width: 30px;
        height: 30px;
    }

    .logo h1 {
        font-size: 1.5rem;
    }

    .login-header h2 {
        font-size: 1.3rem;
    }

    .input-wrapper input {
        padding: 12px 12px 12px 40px;
        font-size: 0.95rem;
    }

    .login-button {
        padding: 14px;
        height: 48px;
    }
}
</style>