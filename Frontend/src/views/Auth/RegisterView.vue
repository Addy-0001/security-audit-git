<template>
    <div class="signup-page">
        <div class="signup-container">
            <!-- Logo and Header -->
            <div class="signup-header">
                <div class="logo">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="logo-icon">
                        <circle cx="12" cy="12" r="10"></circle>
                        <polygon points="10 8 16 12 10 16 10 8"></polygon>
                    </svg>
                    <h1>Booksall</h1>
                </div>
                <h2>Create an Account</h2>
                <p>Sign up to start booking futsal courts</p>
            </div>

            <!-- Signup Form -->
            <form @submit.prevent="handleSignup" class="signup-form">
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

                <!-- Email Input -->
                <div class="form-group" :class="{ 'error': errors.email }">
                    <label for="email">Email Address</label>
                    <div class="input-wrapper">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="input-icon">
                            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z">
                            </path>
                            <polyline points="22,6 12,13 2,6"></polyline>
                        </svg>
                        <input type="email" id="email" v-model="email" placeholder="Enter your email address"
                            @input="validateEmail" :class="{ 'input-error': errors.email }" />
                    </div>
                    <p class="error-message" v-if="errors.email">{{ errors.email }}</p>
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
                            placeholder="Create a password" @input="validatePassword"
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
                    <div class="password-strength" v-if="password && !errors.password">
                        <div class="strength-meter">
                            <div class="strength-bar" :style="{ width: passwordStrength + '%' }"
                                :class="passwordStrengthClass"></div>
                        </div>
                        <span class="strength-text" :class="passwordStrengthClass">{{ passwordStrengthText }}</span>
                    </div>
                </div>

                <!-- Confirm Password Input -->
                <div class="form-group" :class="{ 'error': errors.confirmPassword }">
                    <label for="confirmPassword">Confirm Password</label>
                    <div class="input-wrapper">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="input-icon">
                            <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                            <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                        </svg>
                        <input :type="showConfirmPassword ? 'text' : 'password'" id="confirmPassword"
                            v-model="confirmPassword" placeholder="Confirm your password"
                            @input="validateConfirmPassword" :class="{ 'input-error': errors.confirmPassword }" />
                        <button type="button" class="toggle-password" @click="toggleConfirmPasswordVisibility"
                            tabindex="-1">
                            <svg v-if="!showConfirmPassword" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                                fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                stroke-linejoin="round">
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
                    <p class="error-message" v-if="errors.confirmPassword">{{ errors.confirmPassword }}</p>
                </div>

                <!-- Terms and Conditions -->
                <div class="form-group terms-group" :class="{ 'error': errors.terms }">
                    <div class="checkbox-wrapper">
                        <input type="checkbox" id="terms" v-model="termsAccepted" @change="validateTerms" />
                        <label for="terms">I agree to the <a href="#" @click.prevent="showTerms">Terms and
                                Conditions</a></label>
                    </div>
                    <p class="error-message" v-if="errors.terms">{{ errors.terms }}</p>
                </div>

                <!-- Signup Button -->
                <button type="submit" class="signup-button" :disabled="isLoading || !isFormValid">
                    <span v-if="!isLoading">Create Account</span>
                    <div v-else class="spinner"></div>
                </button>

                <!-- Form Error -->
                <p class="form-error" v-if="formError">{{ formError }}</p>

                <!-- Login Link -->
                <div class="login-link">
                    <p>Already have an account? <a href="#" @click.prevent="goToLogin">Login</a></p>
                </div>
            </form>
        </div>
    </div>
</template>
<script setup>
import { ref, computed, watch } from 'vue';
import { useRouter } from 'vue-router';
import apiClient from '@/axios';

const router = useRouter();

// Form state
const phone = ref('');
const email = ref('');
const password = ref('');
const confirmPassword = ref('');
const termsAccepted = ref(false);
const showPassword = ref(false);
const showConfirmPassword = ref(false);
const isLoading = ref(false);
const formError = ref('');
const errors = ref({
    phone: '',
    email: '',
    password: '',
    confirmPassword: '',
    terms: ''
});

// Toggle password visibility
const togglePasswordVisibility = () => {
    showPassword.value = !showPassword.value;
};

const toggleConfirmPasswordVisibility = () => {
    showConfirmPassword.value = !showConfirmPassword.value;
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

// Validate email
const validateEmail = () => {
    errors.value.email = '';
    if (!email.value) {
        errors.value.email = 'Email address is required';
        return;
    }
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email.value)) {
        errors.value.email = 'Please enter a valid email address';
        return;
    }
};

// Password strength calculation
const calculatePasswordStrength = (pwd) => {
    if (!pwd) return 0;
    let strength = 0;
    if (pwd.length >= 8) strength += 25;
    if (/[a-z]/.test(pwd)) strength += 25;
    if (/[A-Z]/.test(pwd)) strength += 25;
    if (/[0-9!@#$%^&*(),.?":{}|<>]/.test(pwd)) strength += 25;
    return strength;
};

const passwordStrength = computed(() => {
    return calculatePasswordStrength(password.value);
});

const passwordStrengthClass = computed(() => {
    if (passwordStrength.value <= 25) return 'weak';
    if (passwordStrength.value <= 50) return 'fair';
    if (passwordStrength.value <= 75) return 'good';
    return 'strong';
});

const passwordStrengthText = computed(() => {
    if (passwordStrength.value <= 25) return 'Weak';
    if (passwordStrength.value <= 50) return 'Fair';
    if (passwordStrength.value <= 75) return 'Good';
    return 'Strong';
});

// Validate password
const validatePassword = () => {
    errors.value.password = '';
    if (!password.value) {
        errors.value.password = 'Password is required';
        return;
    }
    if (password.value.length < 8) {
        errors.value.password = 'Password must be at least 8 characters';
        return;
    }
    if (!/[a-zA-Z]/.test(password.value) || !/[0-9]/.test(password.value)) {
        errors.value.password = 'Password must contain at least one letter and one number';
        return;
    }
    if (confirmPassword.value) {
        validateConfirmPassword();
    }
};

// Validate confirm password
const validateConfirmPassword = () => {
    errors.value.confirmPassword = '';
    if (!confirmPassword.value) {
        errors.value.confirmPassword = 'Please confirm your password';
        return;
    }
    if (password.value !== confirmPassword.value) {
        errors.value.confirmPassword = 'Passwords do not match';
        return;
    }
};

// Validate terms
const validateTerms = () => {
    errors.value.terms = '';
    if (!termsAccepted.value) {
        errors.value.terms = 'You must accept the terms and conditions';
        return;
    }
};

const isFormValid = computed(() => {
    return (
        phone.value &&
        email.value &&
        password.value &&
        confirmPassword.value &&
        termsAccepted.value &&
        !errors.value.phone &&
        !errors.value.email &&
        !errors.value.password &&
        !errors.value.confirmPassword &&
        !errors.value.terms
    );
});

// Handle signup form submission
const handleSignup = async () => {
    // Validate all form fields
    validatePhone();
    validateEmail();
    validatePassword();
    validateConfirmPassword();
    validateTerms();

    if (
        errors.value.phone ||
        errors.value.email ||
        errors.value.password ||
        errors.value.confirmPassword ||
        errors.value.terms
    ) {
        return;
    }

    try {
        isLoading.value = true;
        formError.value = '';

        // Prepare the data in the format expected by the server
        const signupData = {
            username: phone.value, // Using phone as username since it's required
            email: email.value,
            password1: password.value,
            password2: confirmPassword.value
        };

        // Make POST request to registration endpoint
        const response = await apiClient.post('auth/registration/', signupData);

        // Store the token in localStorage
        localStorage.setItem('token', response.data.key);

        // Redirect to login page or dashboard
        router.push('/login'); // You might want to redirect to dashboard instead
    } catch (error) {
        // Handle specific error responses
        if (error.response && error.response.data) {
            const errorData = error.response.data;
            if (errorData.username) {
                errors.value.phone = errorData.username[0];
            }
            if (errorData.email) {
                errors.value.email = errorData.email[0];
            }
            if (errorData.password1) {
                errors.value.password = errorData.password1[0];
            }
            if (errorData.password2) {
                errors.value.confirmPassword = errorData.password2[0];
            }
            if (errorData.non_field_errors) {
                formError.value = errorData.non_field_errors[0];
            }
        } else {
            formError.value = 'An error occurred during registration. Please try again.';
        }
        console.error('Signup error:', error);
    } finally {
        isLoading.value = false;
    }
};

// Show terms and conditions
const showTerms = () => {
    router.push('/terms')
};

// Go to login page
const goToLogin = () => {
    router.push('/login');
};

watch(password, () => {
    if (confirmPassword.value) {
        validateConfirmPassword();
    }
});
</script>

<style scoped>
/* Signup Page Styles */
.signup-page {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #f8f9fa;
    padding: 20px;
    font-family: 'Inter', 'Segoe UI', Roboto, sans-serif;
}

.signup-container {
    width: 100%;
    max-width: 500px;
    background-color: white;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    padding: 40px;
    transition: transform 0.3s ease;
}

.signup-container:hover {
    transform: translateY(-5px);
}

/* Header Styles */
.signup-header {
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

.signup-header h2 {
    font-size: 1.5rem;
    font-weight: 700;
    color: #333;
    margin: 0 0 10px;
}

.signup-header p {
    color: #666;
    font-size: 0.95rem;
    margin: 0;
}

/* Form Styles */
.signup-form {
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

/* Password Strength Meter */
.password-strength {
    margin-top: 8px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.strength-meter {
    flex-grow: 1;
    height: 4px;
    background-color: #e0e0e0;
    border-radius: 2px;
    overflow: hidden;
}

.strength-bar {
    height: 100%;
    transition: width 0.3s ease, background-color 0.3s ease;
}

.strength-bar.weak {
    background-color: #f44336;
}

.strength-bar.fair {
    background-color: #ff9800;
}

.strength-bar.good {
    background-color: #4caf50;
}

.strength-bar.strong {
    background-color: #2e7d32;
}

.strength-text {
    font-size: 0.8rem;
    font-weight: 600;
}

.strength-text.weak {
    color: #f44336;
}

.strength-text.fair {
    color: #ff9800;
}

.strength-text.good {
    color: #4caf50;
}

.strength-text.strong {
    color: #2e7d32;
}

/* Terms and Conditions */
.terms-group {
    margin-top: 10px;
}

.checkbox-wrapper {
    display: flex;
    align-items: center;
    gap: 10px;
}

.checkbox-wrapper input[type="checkbox"] {
    width: 18px;
    height: 18px;
    accent-color: #2e7d32;
}

.checkbox-wrapper label {
    font-size: 0.9rem;
    color: #555;
    font-weight: 400;
}

.checkbox-wrapper a {
    color: #2e7d32;
    text-decoration: none;
    font-weight: 600;
}

.checkbox-wrapper a:hover {
    text-decoration: underline;
}

/* Signup Button */
.signup-button {
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
    margin-top: 10px;
}

.signup-button:hover:not(:disabled) {
    background-color: #1b5e20;
    transform: translateY(-2px);
}

.signup-button:disabled {
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

.login-link {
    text-align: center;
    margin-top: 10px;
}

.login-link p {
    color: #666;
    font-size: 0.9rem;
    margin: 0;
}

.login-link a {
    color: #2e7d32;
    font-weight: 600;
    text-decoration: none;
    transition: color 0.2s ease;
}

.login-link a:hover {
    color: #1b5e20;
    text-decoration: underline;
}

/* Responsive Styles */
@media (max-width: 550px) {
    .signup-container {
        padding: 30px 20px;
    }

    .signup-header {
        margin-bottom: 25px;
    }

    .logo-icon {
        width: 30px;
        height: 30px;
    }

    .logo h1 {
        font-size: 1.5rem;
    }

    .signup-header h2 {
        font-size: 1.3rem;
    }

    .input-wrapper input {
        padding: 12px 12px 12px 40px;
        font-size: 0.95rem;
    }

    .signup-button {
        padding: 14px;
        height: 48px;
    }
}
</style>