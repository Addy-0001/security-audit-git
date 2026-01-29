<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import apiClient from '@/axios';

const router = useRouter();

// State for user data
const userPk = ref(null);

// Form data for profile creation
const formData = ref({
    profile_picture: null,
    bio: '',
    address: '',
    city: '',
    country: '',
    zip_code: ''
});

// Loading and error states
const isLoading = ref(true);
const isSubmitting = ref(false);
const error = ref(null);
const formError = ref('');

// Check if user is authenticated
const isAuthenticated = () => {
    return !!localStorage.getItem('token');
};

// Fetch user PK
const fetchUserPk = async () => {
    try {
        const response = await apiClient.get('auth/user/');
        userPk.value = response.data.pk;
    } catch (err) {
        console.error('Error fetching user data:', err);
        if (err.response?.status === 401) {
            router.push('/login');
        }
        throw err;
    }
};

// Initialize page
const initialize = async () => {
    if (!isAuthenticated()) {
        router.push('/login');
        return;
    }

    try {
        isLoading.value = true;
        error.value = null;
        await fetchUserPk();
    } catch (err) {
        error.value = 'Failed to load user data. Please try again.';
    } finally {
        isLoading.value = false;
    }
};

// Handle profile creation
const createProfile = async () => {
    try {
        isSubmitting.value = true;
        formError.value = '';

        const profileData = new FormData();
        profileData.append('user', userPk.value);
        profileData.append('first_name', ''); // Required but not editable here
        profileData.append('last_name', '');  // Required but not editable here
        profileData.append('email_address', ''); // Required but not editable here
        if (formData.value.profile_picture) {
            profileData.append('profile_picture', formData.value.profile_picture);
        }
        profileData.append('bio', formData.value.bio || '');
        profileData.append('address', formData.value.address || '');
        profileData.append('city', formData.value.city || '');
        profileData.append('country', formData.value.country || '');
        profileData.append('zip_code', formData.value.zip_code || '');
        profileData.append('is_verified', false);
        profileData.append('is_futsal_admin', false);

        const response = await apiClient.post(
            'user/profile/create-user-profile/',
            profileData,
            { headers: { 'Content-Type': 'multipart/form-data' } }
        );

        if (response.status === 201) {
            router.push('/profile'); // Redirect to profile page on success
        }
    } catch (err) {
        console.error('Error creating profile:', err);
        formError.value = err.response?.data?.non_field_errors?.[0] || 'Failed to create profile. Please try again.';
    } finally {
        isSubmitting.value = false;
    }
};

// Handle file input change
const handleFileChange = (event) => {
    formData.value.profile_picture = event.target.files[0];
};

// Mount the component and fetch user data
onMounted(() => {
    initialize();
});
</script>

<template>
    <div class="profile-create-page">
        <!-- Loading State -->
        <div v-if="isLoading" class="loading">Loading...</div>

        <!-- Error State -->
        <div v-else-if="error" class="error">{{ error }}</div>

        <!-- Profile Creation Form -->
        <div v-else class="container">
            <h1 class="page-title">Create Your Profile</h1>
            <p class="page-subtitle">Please fill in the details below to create your profile.</p>

            <form @submit.prevent="createProfile" class="profile-form">
                <div class="form-group">
                    <label for="profile-picture">Profile Picture</label>
                    <input type="file" id="profile-picture" @change="handleFileChange" accept="image/*"
                        class="form-input file-input" />
                    <div v-if="formData.profile_picture" class="file-preview">
                        Selected: {{ formData.profile_picture.name }}
                    </div>
                </div>

                <div class="form-group">
                    <label for="bio">Bio</label>
                    <textarea v-model="formData.bio" id="bio" class="form-input" placeholder="Tell us about yourself"
                        rows="4"></textarea>
                </div>

                <div class="form-group">
                    <label for="address">Address</label>
                    <input type="text" v-model="formData.address" id="address" class="form-input"
                        placeholder="Street address" />
                </div>

                <div class="form-group">
                    <label for="city">City</label>
                    <input type="text" v-model="formData.city" id="city" class="form-input" placeholder="City" />
                </div>

                <div class="form-group">
                    <label for="country">Country</label>
                    <input type="text" v-model="formData.country" id="country" class="form-input"
                        placeholder="Country" />
                </div>

                <div class="form-group">
                    <label for="zip-code">Zip Code</label>
                    <input type="text" v-model="formData.zip_code" id="zip-code" class="form-input"
                        placeholder="Zip code" />
                </div>

                <div class="form-actions">
                    <button type="submit" class="submit-btn" :disabled="isSubmitting">
                        <span v-if="!isSubmitting">Create Profile</span>
                        <div v-else class="spinner"></div>
                    </button>
                    <p v-if="formError" class="form-error">{{ formError }}</p>
                </div>
            </form>
        </div>
    </div>
</template>

<style scoped>
.profile-create-page {
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

.page-title {
    font-size: 2rem;
    font-weight: 700;
    color: #2e7d32;
    margin-bottom: 10px;
    text-align: center;
}

.page-subtitle {
    font-size: 1rem;
    color: #666;
    margin-bottom: 30px;
    text-align: center;
}

.profile-form {
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    padding: 30px;
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    font-size: 0.95rem;
    font-weight: 600;
    color: #666;
    margin-bottom: 8px;
}

.form-input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 6px;
    font-size: 0.95rem;
    color: #333;
    transition: border-color 0.2s ease;
}

.form-input:focus {
    outline: none;
    border-color: #2e7d32;
    box-shadow: 0 0 0 2px rgba(46, 125, 50, 0.1);
}

.file-input {
    padding: 5px;
    /* Adjusted for file input */
}

.file-preview {
    font-size: 0.85rem;
    color: #999;
    margin-top: 5px;
}

.form-actions {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 15px;
}

.submit-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 12px 24px;
    border: none;
    border-radius: 8px;
    background-color: #2e7d32;
    color: white;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
}

.submit-btn:hover:not(:disabled) {
    background-color: #1b5e20;
}

.submit-btn:disabled {
    background-color: #b0bec5;
    cursor: not-allowed;
}

.spinner {
    width: 20px;
    height: 20px;
    border: 3px solid #ffffff;
    border-top: 3px solid transparent;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}

.form-error {
    font-size: 0.9rem;
    color: #c62828;
    text-align: center;
}

.loading,
.error {
    text-align: center;
    font-size: 1.25rem;
    color: #666;
    margin-top: 50px;
}

.error {
    color: #c62828;
}

/* Responsive Styles */
@media (max-width: 480px) {
    .page-title {
        font-size: 1.75rem;
    }

    .profile-form {
        padding: 20px;
    }

    .submit-btn {
        width: 100%;
    }
}
</style>