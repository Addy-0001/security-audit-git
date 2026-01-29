<template>
    <div class="edit-profile-page">
        <div class="container">
            <!-- Header -->
            <div class="edit-profile-header">
                <h1>
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                        <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                    </svg>
                    Edit Profile
                </h1>
                <p>Update your personal information below</p>
            </div>

            <!-- Loading State -->
            <div v-if="isLoading" class="loading">Loading...</div>

            <!-- Error State -->
            <div v-else-if="error" class="error">{{ error }}</div>

            <!-- Edit Form -->
            <form v-else @submit.prevent="handleUpdate" class="edit-profile-form">
                <!-- Username (Read-only) -->
                <div class="form-group">
                    <label for="username">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                            <circle cx="12" cy="7" r="4"></circle>
                        </svg>
                        Username
                    </label>
                    <input type="text" id="username" v-model="formData.username" disabled />
                </div>

                <!-- First Name -->
                <div class="form-group" :class="{ 'error': errors.first_name }">
                    <label for="first_name">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                            <circle cx="12" cy="7" r="4"></circle>
                        </svg>
                        First Name
                    </label>
                    <input type="text" id="first_name" v-model="formData.first_name" placeholder="Enter your first name"
                        @input="validateFirstName" :class="{ 'input-error': errors.first_name }" />
                    <p class="error-message" v-if="errors.first_name">{{ errors.first_name }}</p>
                </div>

                <!-- Last Name -->
                <div class="form-group" :class="{ 'error': errors.last_name }">
                    <label for="last_name">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                            <circle cx="12" cy="7" r="4"></circle>
                        </svg>
                        Last Name
                    </label>
                    <input type="text" id="last_name" v-model="formData.last_name" placeholder="Enter your last name"
                        @input="validateLastName" :class="{ 'input-error': errors.last_name }" />
                    <p class="error-message" v-if="errors.last_name">{{ errors.last_name }}</p>
                </div>

                <!-- Form Error -->
                <p class="form-error" v-if="formError">{{ formError }}</p>

                <!-- Buttons -->
                <div class="form-actions">
                    <button type="submit" class="save-btn" :disabled="isSaving || !isFormValid">
                        <span v-if="!isSaving">Save Changes</span>
                        <div v-else class="spinner"></div>
                    </button>
                    <button type="button" class="cancel-btn" @click="cancelEdit" :disabled="isSaving">
                        Cancel
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import apiClient from '@/axios';

const router = useRouter();

// Form state
const formData = ref({
    username: '',
    first_name: '',
    last_name: ''
});

const errors = ref({
    first_name: '',
    last_name: ''
});

const isLoading = ref(true);
const isSaving = ref(false);
const error = ref(null);
const formError = ref('');

// Check if user is authenticated
const isAuthenticated = () => {
    return !!localStorage.getItem('token');
};

// Fetch current user data
const fetchUserData = async () => {
    try {
        const response = await apiClient.get('auth/user/');
        formData.value = {
            username: response.data.username,
            first_name: response.data.first_name,
            last_name: response.data.last_name
        };
    } catch (err) {
        console.error('Error fetching user data:', err);
        if (err.response?.status === 401) {
            router.push('/login');
        } else {
            error.value = 'Failed to load user data. Please try again.';
        }
        throw err;
    }
};

// Validation functions
const validateFirstName = () => {
    errors.value.first_name = '';
    if (formData.value.first_name && formData.value.first_name.length < 2) {
        errors.value.first_name = 'First name must be at least 2 characters';
    }
};

const validateLastName = () => {
    errors.value.last_name = '';
    if (formData.value.last_name && formData.value.last_name.length < 2) {
        errors.value.last_name = 'Last name must be at least 2 characters';
    }
};

// Computed property to check if form is valid
const isFormValid = computed(() => {
    return (
        !errors.value.first_name &&
        !errors.value.last_name
    );
});

// Handle form submission
const handleUpdate = async () => {
    validateFirstName();
    validateLastName();

    if (!isFormValid.value) {
        return;
    }

    try {
        isSaving.value = true;
        formError.value = '';

        // Prepare data for PATCH request (exclude username)
        const updateData = {};
        if (formData.value.first_name !== undefined) updateData.first_name = formData.value.first_name;
        if (formData.value.last_name !== undefined) updateData.last_name = formData.value.last_name;

        // Send PATCH request to update user data
        await apiClient.patch('auth/user/', updateData);

        // Redirect back to profile page on success
        router.push('/profile');
    } catch (err) {
        console.error('Error updating user:', err);
        if (err.response?.data) {
            const errorData = err.response.data;
            if (errorData.first_name) errors.value.first_name = errorData.first_name[0];
            if (errorData.last_name) errors.value.last_name = errorData.last_name[0];
            if (errorData.non_field_errors) formError.value = errorData.non_field_errors[0];
            else formError.value = 'An error occurred while updating your profile.';
        } else {
            formError.value = 'An error occurred. Please try again.';
        }
    } finally {
        isSaving.value = false;
    }
};

// Cancel editing
const cancelEdit = () => {
    router.push('/profile');
};

// Initialize form with current user data
onMounted(async () => {
    if (!isAuthenticated()) {
        router.push('/login');
        return;
    }

    try {
        isLoading.value = true;
        await fetchUserData();
    } finally {
        isLoading.value = false;
    }
});
</script>

<style scoped>
.edit-profile-page {
    min-height: 100vh;
    background-color: #f8f9fa;
    font-family: 'Inter', 'Segoe UI', Roboto, sans-serif;
    color: #333;
    padding: 40px 0;
}

.container {
    width: 100%;
    max-width: 600px;
    margin: 0 auto;
    padding: 0 20px;
}

.edit-profile-header {
    text-align: center;
    margin-bottom: 30px;
}

.edit-profile-header h1 {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    font-size: 2rem;
    font-weight: 700;
    color: #2e7d32;
    margin: 0 0 10px;
}

.edit-profile-header svg {
    width: 24px;
    height: 24px;
    color: #2e7d32;
}

.edit-profile-header p {
    font-size: 1rem;
    color: #666;
    margin: 0;
}

.edit-profile-form {
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    padding: 30px;
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.95rem;
    font-weight: 600;
    color: #666;
    margin-bottom: 8px;
}

.form-group label svg {
    width: 16px;
    height: 16px;
    color: #2e7d32;
}

.form-group input {
    width: 100%;
    padding: 12px 16px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 0.95rem;
    color: #333;
    transition: border-color 0.2s ease;
}

.form-group input:focus {
    outline: none;
    border-color: #2e7d32;
    box-shadow: 0 0 0 3px rgba(46, 125, 50, 0.1);
}

.form-group input:disabled {
    background-color: #f5f5f5;
    color: #999;
    cursor: not-allowed;
}

.form-group.error input {
    border-color: #c62828;
}

.error-message {
    font-size: 0.85rem;
    color: #c62828;
    margin-top: 5px;
}

.form-error {
    font-size: 0.9rem;
    color: #c62828;
    text-align: center;
    margin-bottom: 20px;
}

.form-actions {
    display: flex;
    gap: 15px;
    justify-content: center;
}

.save-btn,
.cancel-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 10px 20px;
    border: none;
    border-radius: 8px;
    font-size: 0.95rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
}

.save-btn {
    background-color: #2e7d32;
    color: white;
}

.save-btn:hover:not(:disabled) {
    background-color: #1b5e20;
}

.save-btn:disabled {
    background-color: #b0bec5;
    cursor: not-allowed;
}

.cancel-btn {
    background-color: #f1f8e9;
    color: #2e7d32;
}

.cancel-btn:hover:not(:disabled) {
    background-color: #e8f5e9;
}

.spinner {
    width: 20px;
    height: 20px;
    border: 3px solid #ffffff;
    border-top: 3px solid transparent;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

.loading,
.error {
    text-align: center;
    padding: 20px;
    font-size: 1rem;
    color: #666;
}

.error {
    color: #c62828;
}

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}

@media (max-width: 480px) {
    .edit-profile-header h1 {
        font-size: 1.75rem;
    }

    .edit-profile-form {
        padding: 20px;
    }

    .form-actions {
        flex-direction: column;
    }

    .save-btn,
    .cancel-btn {
        width: 100%;
    }
}
</style>