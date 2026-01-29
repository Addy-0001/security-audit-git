<template>
    <div class="add-futsal-page">
        <div class="container">
            <div class="page-header">
                <h1>Add New Futsal</h1>
                <p>Fill in the details below to list your futsal on Booksall</p>
            </div>

            <!-- Form Progress -->
            <div class="form-progress">
                <div v-for="(step, index) in steps" :key="index" class="progress-step" :class="{
                    'active': currentStep === index,
                    'completed': currentStep > index
                }" @click="goToStep(index)">
                    <div class="step-indicator">
                        <span v-if="currentStep <= index">{{ index + 1 }}</span>
                        <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="20 6 9 17 4 12"></polyline>
                        </svg>
                    </div>
                    <span class="step-name">{{ step }}</span>
                </div>
            </div>

            <!-- Form Container -->
            <div class="form-container">
                <form @submit.prevent="submitForm">
                    <!-- Step 1: Basic Information -->
                    <div v-if="currentStep === 0" class="form-step">
                        <h2>Basic Information</h2>
                        <p>Let's start with the essential details about your futsal</p>

                        <div class="form-group">
                            <label for="futsal_name">Futsal Name <span class="required">*</span></label>
                            <input type="text" id="futsal_name" v-model="formData.futsal_name"
                                placeholder="Enter futsal name" @input="validateField('futsal_name')"
                                :class="{ 'input-error': errors.futsal_name }" />
                            <p class="error-message" v-if="errors.futsal_name">{{ errors.futsal_name }}</p>
                        </div>

                        <div class="form-group">
                            <label for="futsal_phone_number">Phone Number <span class="required">*</span></label>
                            <input type="tel" id="futsal_phone_number" v-model="formData.futsal_phone_number"
                                placeholder="Enter phone number (e.g., 9841234567)"
                                @input="validateField('futsal_phone_number')"
                                :class="{ 'input-error': errors.futsal_phone_number }" />
                            <p class="error-message" v-if="errors.futsal_phone_number">{{ errors.futsal_phone_number }}
                            </p>
                        </div>

                        <div class="form-group">
                            <label for="price_per_hour">Price Per Hour (NPR) <span class="required">*</span></label>
                            <input type="number" id="price_per_hour" v-model="formData.price_per_hour"
                                placeholder="Enter price per hour" min="0" @input="validateField('price_per_hour')"
                                :class="{ 'input-error': errors.price_per_hour }" />
                            <p class="error-message" v-if="errors.price_per_hour">{{ errors.price_per_hour }}</p>
                        </div>

                        <div class="form-group">
                            <label for="location">Location <span class="required">*</span></label>
                            <input type="text" id="location" v-model="formData.location"
                                placeholder="Enter location (e.g., Gyaneshwor, Kathmandu)"
                                @input="validateField('location')" :class="{ 'input-error': errors.location }" />
                            <p class="error-message" v-if="errors.location">{{ errors.location }}</p>
                        </div>

                        <div class="form-group">
                            <label for="google_maps_link">Google Maps Link <span class="required">*</span></label>
                            <input type="url" id="google_maps_link" v-model="formData.google_maps_link"
                                placeholder="Enter Google Maps link (e.g., https://goo.gl/maps/...)"
                                @input="validateField('google_maps_link')"
                                :class="{ 'input-error': errors.google_maps_link }" />
                            <p class="error-message" v-if="errors.google_maps_link">{{ errors.google_maps_link }}</p>
                            <p class="help-text">Paste the Google Maps link to your futsal location</p>
                        </div>
                    </div>

                    <!-- Step 2: Facilities & Features -->
                    <div v-if="currentStep === 1" class="form-step">
                        <h2>Facilities & Features</h2>
                        <p>Tell us about the facilities and features of your futsal</p>

                        <div class="form-row">
                            <div class="form-group half-width">
                                <label for="a_side">A-Side <span class="required">*</span></label>
                                <input type="number" id="a_side" v-model="formData.a_side"
                                    placeholder="Enter number of players per side" min="3" max="11"
                                    @input="validateField('a_side')" :class="{ 'input-error': errors.a_side }" />
                                <p class="error-message" v-if="errors.a_side">{{ errors.a_side }}</p>
                                <p class="help-text">Number of players per side (e.g., 5 for 5-a-side)</p>
                            </div>

                            <div class="form-group half-width">
                                <label for="grounds">Number of Grounds <span class="required">*</span></label>
                                <input type="number" id="grounds" v-model="formData.grounds"
                                    placeholder="Enter number of grounds" min="1" @input="validateField('grounds')"
                                    :class="{ 'input-error': errors.grounds }" />
                                <p class="error-message" v-if="errors.grounds">{{ errors.grounds }}</p>
                            </div>
                        </div>

                        <h3>Amenities</h3>
                        <div class="amenities-grid">
                            <div class="amenity-item">
                                <input type="checkbox" id="shower_facility" v-model="formData.shower_facility">
                                <label for="shower_facility">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                        stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round">
                                        <path
                                            d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z">
                                        </path>
                                        <line x1="12" y1="8" x2="12" y2="16"></line>
                                        <line x1="8" y1="12" x2="16" y2="12"></line>
                                    </svg>
                                    Shower Facility
                                </label>
                            </div>

                            <div class="amenity-item">
                                <input type="checkbox" id="parking_space" v-model="formData.parking_space">
                                <label for="parking_space">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                        stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round">
                                        <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                                        <path d="M9 17V7h4a3 3 0 0 1 0 6H9"></path>
                                    </svg>
                                    Parking Space
                                </label>
                            </div>

                            <div class="amenity-item">
                                <input type="checkbox" id="changing_room" v-model="formData.changing_room">
                                <label for="changing_room">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                        stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round">
                                        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                                    </svg>
                                    Changing Room
                                </label>
                            </div>

                            <div class="amenity-item">
                                <input type="checkbox" id="restaurant" v-model="formData.restaurant">
                                <label for="restaurant">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                        stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round">
                                        <path d="M7 2v4h10V2"></path>
                                        <path
                                            d="M17 8H7a5 5 0 0 0-5 5v6a1 1 0 0 0 1 1h18a1 1 0 0 0 1-1v-6a5 5 0 0 0-5-5z">
                                        </path>
                                    </svg>
                                    Restaurant
                                </label>
                            </div>

                            <div class="amenity-item">
                                <input type="checkbox" id="wifi" v-model="formData.wifi">
                                <label for="wifi">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                        stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round">
                                        <path d="M5 12.55a11 11 0 0 1 14.08 0"></path>
                                        <path d="M1.42 9a16 16 0 0 1 21.16 0"></path>
                                        <path d="M8.53 16.11a6 6 0 0 1 6.95 0"></path>
                                        <line x1="12" y1="20" x2="12.01" y2="20"></line>
                                    </svg>
                                    WiFi
                                </label>
                            </div>

                            <div class="amenity-item">
                                <input type="checkbox" id="open_ground" v-model="formData.open_ground">
                                <label for="open_ground">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                        stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round">
                                        <circle cx="12" cy="12" r="10"></circle>
                                        <path
                                            d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z">
                                        </path>
                                        <line x1="2" y1="12" x2="22" y2="12"></line>
                                    </svg>
                                    Open Ground
                                </label>
                            </div>
                        </div>
                    </div>

                    <!-- Step 3: Images Upload -->
                    <div v-if="currentStep === 2" class="form-step">
                        <h2>Upload Images</h2>
                        <p>Upload up to 5 high-quality images of your futsal</p>

                        <div class="image-upload-container">
                            <div v-for="n in 5" :key="n" class="image-upload-box"
                                :class="{ 'has-image': formData[`futsal_image_${n}`] }">
                                <div v-if="formData[`futsal_image_${n}`]" class="image-preview">
                                    <img :src="previewImages[n - 1]" :alt="`Futsal Image ${n}`" />
                                    <button type="button" class="remove-image-btn" @click="removeImage(n)">
                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                            stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                            stroke-linejoin="round">
                                            <line x1="18" y1="6" x2="6" y2="18"></line>
                                            <line x1="6" y1="6" x2="18" y2="18"></line>
                                        </svg>
                                    </button>
                                </div>
                                <label v-else :for="`futsal_image_${n}`" class="upload-label">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                        stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round">
                                        <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                                        <circle cx="8.5" cy="8.5" r="1.5"></circle>
                                        <polyline points="21 15 16 10 5 21"></polyline>
                                    </svg>
                                    <span>{{ n === 1 ? 'Upload Cover Image*' : `Upload Image ${n}` }}</span>
                                </label>
                                <input type="file" :id="`futsal_image_${n}`" @change="handleImageUpload($event, n)"
                                    accept="image/*" class="hidden-input" />
                            </div>
                        </div>
                        <p class="error-message" v-if="errors.futsal_image_1">{{ errors.futsal_image_1 }}</p>
                        <p class="help-text">First image will be used as the cover image. Recommended size: 1200x800
                            pixels.</p>
                    </div>

                    <!-- Step 4: Price Table -->
                    <div v-if="currentStep === 3" class="form-step">
                        <h2>Price Table</h2>
                        <p>Add different pricing options for your futsal</p>

                        <div class="price-table">
                            <div class="price-table-header">
                                <div class="price-name-header">Time Slot / Description</div>
                                <div class="price-value-header">Price (NPR)</div>
                                <div class="price-action-header"></div>
                            </div>

                            <div v-for="(price, index) in priceTable" :key="index" class="price-table-row">
                                <div class="price-name">
                                    <input type="text" v-model="price.name" placeholder="e.g., Morning (6AM-10AM)"
                                        @input="validatePriceTable" />
                                </div>
                                <div class="price-value">
                                    <input type="number" v-model="price.value" placeholder="Price" min="0"
                                        @input="validatePriceTable" />
                                </div>
                                <div class="price-action">
                                    <button type="button" class="remove-price-btn" @click="removePrice(index)">
                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                            stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                            stroke-linejoin="round">
                                            <line x1="18" y1="6" x2="6" y2="18"></line>
                                            <line x1="6" y1="6" x2="18" y2="18"></line>
                                        </svg>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <button type="button" class="add-price-btn" @click="addPrice">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <circle cx="12" cy="12" r="10"></circle>
                                <line x1="12" y1="8" x2="12" y2="16"></line>
                                <line x1="8" y1="12" x2="16" y2="12"></line>
                            </svg>
                            Add Price Option
                        </button>
                        <p class="error-message" v-if="errors.price_table">{{ errors.price_table }}</p>
                    </div>

                    <!-- Step 5: Description -->
                    <div v-if="currentStep === 4" class="form-step">
                        <h2>Description</h2>
                        <p>Provide a detailed description of your futsal</p>

                        <div class="form-group">
                            <label for="futsal_description">Futsal Description <span class="required">*</span></label>

                            <!-- Simple Rich Text Editor Toolbar -->
                            <div class="editor-toolbar">
                                <button type="button" @click="applyFormat('bold')" title="Bold">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                        stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round">
                                        <path d="M6 4h8a4 4 0 0 1 4 4 4 4 0 0 1-4 4H6z"></path>
                                        <path d="M6 12h9a4 4 0 0 1 4 4 4 4 0 0 1-4 4H6z"></path>
                                    </svg>
                                </button>
                                <button type="button" @click="applyFormat('italic')" title="Italic">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                        stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round">
                                        <line x1="19" y1="4" x2="10" y2="4"></line>
                                        <line x1="14" y1="20" x2="5" y2="20"></line>
                                        <line x1="15" y1="4" x2="9" y2="20"></line>
                                    </svg>
                                </button>
                                <button type="button" @click="applyFormat('underline')" title="Underline">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                        stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round">
                                        <path d="M6 3v7a6 6 0 0 0 6 6 6 6 0 0 0 6-6V3"></path>
                                        <line x1="4" y1="21" x2="20" y2="21"></line>
                                    </svg>
                                </button>
                                <span class="toolbar-divider"></span>
                                <button type="button" @click="applyFormat('h2')" title="Heading">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                        stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round">
                                        <path d="M4 12h8"></path>
                                        <path d="M4 18V6"></path>
                                        <path d="M12 18V6"></path>
                                        <path d="M16 12h4"></path>
                                        <path d="M16 18V6"></path>
                                        <path d="M20 18V6"></path>
                                    </svg>
                                </button>
                                <button type="button" @click="applyFormat('p')" title="Paragraph">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                        stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round">
                                        <path d="M13 4v16"></path>
                                        <path d="M19 4H8a4 4 0 0 0 0 8h5"></path>
                                    </svg>
                                </button>
                                <span class="toolbar-divider"></span>
                                <button type="button" @click="applyFormat('ul')" title="Bullet List">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                        stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round">
                                        <line x1="8" y1="6" x2="21" y2="6"></line>
                                        <line x1="8" y1="12" x2="21" y2="12"></line>
                                        <line x1="8" y1="18" x2="21" y2="18"></line>
                                        <line x1="3" y1="6" x2="3.01" y2="6"></line>
                                        <line x1="3" y1="12" x2="3.01" y2="12"></line>
                                        <line x1="3" y1="18" x2="3.01" y2="18"></line>
                                    </svg>
                                </button>
                                <button type="button" @click="applyFormat('ol')" title="Numbered List">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                        stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                        stroke-linejoin="round">
                                        <line x1="10" y1="6" x2="21" y2="6"></line>
                                        <line x1="10" y1="12" x2="21" y2="12"></line>
                                        <line x1="10" y1="18" x2="21" y2="18"></line>
                                        <path d="M4 6h1v4"></path>
                                        <path d="M4 10h2"></path>
                                        <path d="M6 18H4c0-1 2-2 2-3s-1-1.5-2-1"></path>
                                    </svg>
                                </button>
                            </div>

                            <div class="rich-text-editor" contenteditable="true" ref="editor" @input="updateDescription"
                                :class="{ 'input-error': errors.futsal_description }"></div>
                            <p class="error-message" v-if="errors.futsal_description">{{ errors.futsal_description }}
                            </p>
                            <p class="help-text">Describe your futsal, including special features, rules, and any other
                                important information.</p>
                        </div>

                        <div class="form-group">
                            <div class="preview-box">
                                <h3>Preview</h3>
                                <div class="description-preview" v-html="formData.futsal_description"></div>
                            </div>
                        </div>
                    </div>

                    <!-- Form Navigation -->
                    <div class="form-navigation">
                        <button type="button" class="back-btn" v-if="currentStep > 0" @click="prevStep">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <line x1="19" y1="12" x2="5" y2="12"></line>
                                <polyline points="12 19 5 12 12 5"></polyline>
                            </svg>
                            Back
                        </button>

                        <button type="button" class="next-btn" v-if="currentStep < steps.length - 1" @click="nextStep"
                            :disabled="!isStepValid">
                            Next
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <line x1="5" y1="12" x2="19" y2="12"></line>
                                <polyline points="12 5 19 12 12 19"></polyline>
                            </svg>
                        </button>

                        <button type="submit" class="submit-btn" v-if="currentStep === steps.length - 1"
                            :disabled="!isStepValid || isSubmitting">
                            <span v-if="!isSubmitting">Submit</span>
                            <div v-else class="spinner"></div>
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import apiClient from '@/axios';

const router = useRouter();
const editor = ref(null);

// State for user PK
const userPk = ref(null);

// Form steps
const steps = ['Basic Info', 'Facilities', 'Images', 'Pricing', 'Description'];
const currentStep = ref(0);

// Form data
const formData = reactive({
    futsal_name: '',
    futsal_phone_number: '',
    futsal_image_1: null,
    futsal_image_2: null,
    futsal_image_3: null,
    futsal_image_4: null,
    futsal_image_5: null,
    price_per_hour: '',
    price_table: null,
    location: '',
    google_maps_link: '',
    a_side: '',
    grounds: '',
    shower_facility: false,
    parking_space: false,
    changing_room: false,
    restaurant: false,
    wifi: false,
    open_ground: false,
    futsal_description: '',
    featured_futsal: false, // Added as per API spec
    futsal_owner: null // Will be set to userPk
});

// Price table data
const priceTable = ref([{ name: '', value: '' }]);

// Image previews
const previewImages = ref([null, null, null, null, null]);

// Form errors
const errors = reactive({
    futsal_name: '',
    futsal_phone_number: '',
    futsal_image_1: '',
    price_per_hour: '',
    price_table: '',
    location: '',
    google_maps_link: '',
    a_side: '',
    grounds: '',
    futsal_description: '',
    api_error: '' // For server-side errors
});

// Form submission state
const isSubmitting = ref(false);
const isLoading = ref(true);

// Computed property to check if current step is valid
const isStepValid = computed(() => {
    switch (currentStep.value) {
        case 0: // Basic Info
            return (
                formData.futsal_name &&
                formData.futsal_phone_number &&
                formData.price_per_hour &&
                formData.location &&
                formData.google_maps_link &&
                !errors.futsal_name &&
                !errors.futsal_phone_number &&
                !errors.price_per_hour &&
                !errors.location &&
                !errors.google_maps_link
            );
        case 1: // Facilities
            return (
                formData.a_side &&
                formData.grounds &&
                !errors.a_side &&
                !errors.grounds
            );
        case 2: // Images
            return formData.futsal_image_1 && !errors.futsal_image_1;
        case 3: // Pricing
            return !errors.price_table && isPriceTableValid();
        case 4: // Description
            return formData.futsal_description && !errors.futsal_description;
        default:
            return false;
    }
});

// Check if price table is valid
const isPriceTableValid = () => {
    if (priceTable.value.length === 0) return false;
    return priceTable.value.some(price => price.name && price.value);
};

// Check if user is authenticated
const isAuthenticated = () => {
    return !!localStorage.getItem('token');
};

// Fetch user PK
const fetchUserPk = async () => {
    try {
        const response = await apiClient.get('auth/user/');
        userPk.value = response.data.pk;
        formData.futsal_owner = userPk.value; // Set the owner PK
    } catch (err) {
        console.error('Error fetching user data:', err);
        if (err.response?.status === 401) {
            router.push('/login');
        }
        throw err;
    }
};

// Initialize the page
const initialize = async () => {
    if (!isAuthenticated()) {
        router.push('/login');
        return;
    }

    try {
        isLoading.value = true;
        await fetchUserPk();
    } catch (err) {
        errors.api_error = 'Failed to load user data. Please try again.';
    } finally {
        isLoading.value = false;
    }
};

// Navigation methods
const nextStep = () => {
    if (currentStep.value < steps.length - 1 && isStepValid.value) {
        if (currentStep.value === 3) {
            const priceObj = {};
            priceTable.value.forEach(price => {
                if (price.name && price.value) {
                    priceObj[price.name] = Number(price.value); // Ensure numeric values
                }
            });
            formData.price_table = Object.keys(priceObj).length ? priceObj : null;
        }
        currentStep.value++;
    }
};

const prevStep = () => {
    if (currentStep.value > 0) {
        currentStep.value--;
    }
};

const goToStep = (step) => {
    if (step <= currentStep.value) {
        currentStep.value = step;
    }
};

// Validation methods
const validateField = (field) => {
    errors[field] = '';

    switch (field) {
        case 'futsal_name':
            if (!formData.futsal_name) errors.futsal_name = 'Futsal name is required';
            else if (formData.futsal_name.length < 3) errors.futsal_name = 'Futsal name must be at least 3 characters';
            break;
        case 'futsal_phone_number':
            formData.futsal_phone_number = formData.futsal_phone_number.replace(/\D/g, '');
            if (!formData.futsal_phone_number) errors.futsal_phone_number = 'Phone number is required';
            else if (formData.futsal_phone_number.length !== 10) errors.futsal_phone_number = 'Phone number must be 10 digits';
            else if (!formData.futsal_phone_number.startsWith('9')) errors.futsal_phone_number = 'Phone number must start with 9';
            break;
        case 'price_per_hour':
            if (!formData.price_per_hour) errors.price_per_hour = 'Price per hour is required';
            else if (isNaN(formData.price_per_hour) || Number(formData.price_per_hour) <= 0) errors.price_per_hour = 'Price must be a positive number';
            break;
        case 'location':
            if (!formData.location) errors.location = 'Location is required';
            else if (formData.location.length < 5) errors.location = 'Please enter a more specific location';
            break;
        case 'google_maps_link':
            if (!formData.google_maps_link) errors.google_maps_link = 'Google Maps link is required';
            else if (!isValidGoogleMapsLink(formData.google_maps_link)) errors.google_maps_link = 'Please enter a valid Google Maps link';
            break;
        case 'a_side':
            if (!formData.a_side) errors.a_side = 'A-side is required';
            else if (isNaN(formData.a_side) || Number(formData.a_side) < 3 || Number(formData.a_side) > 11) errors.a_side = 'A-side must be between 3 and 11';
            break;
        case 'grounds':
            if (!formData.grounds) errors.grounds = 'Number of grounds is required';
            else if (isNaN(formData.grounds) || Number(formData.grounds) < 1) errors.grounds = 'Number of grounds must be at least 1';
            break;
    }
};

const isValidGoogleMapsLink = (url) => {
    return url.includes('google.com/maps') || url.includes('goo.gl/maps');
};

// Handle image upload
const handleImageUpload = (event, imageNumber) => {
    const file = event.target.files[0];
    if (!file) return;

    if (!file.type.startsWith('image/')) {
        errors.futsal_image_1 = 'Please upload only image files';
        return;
    }
    if (file.size > 5 * 1024 * 1024) {
        errors.futsal_image_1 = 'Image size should not exceed 5MB';
        return;
    }

    formData[`futsal_image_${imageNumber}`] = file;
    const reader = new FileReader();
    reader.onload = (e) => {
        previewImages.value[imageNumber - 1] = e.target.result;
    };
    reader.readAsDataURL(file);

    if (imageNumber === 1) errors.futsal_image_1 = '';
};

// Remove image
const removeImage = (imageNumber) => {
    formData[`futsal_image_${imageNumber}`] = null;
    previewImages.value[imageNumber - 1] = null;
    if (imageNumber === 1 && currentStep.value === 2) errors.futsal_image_1 = 'Cover image is required';
};

// Price table methods
const addPrice = () => {
    priceTable.value.push({ name: '', value: '' });
};

const removePrice = (index) => {
    priceTable.value.splice(index, 1);
    if (priceTable.value.length === 0) addPrice();
    validatePriceTable();
};

const validatePriceTable = () => {
    errors.price_table = '';
    const hasValidEntry = priceTable.value.some(price => price.name && price.value);
    if (!hasValidEntry) errors.price_table = 'Please add at least one valid price option';
};

// Rich text editor methods
const applyFormat = (format) => {
    if (!editor.value) return;
    document.execCommand('styleWithCSS', false, true);
    switch (format) {
        case 'bold': document.execCommand('bold', false, null); break;
        case 'italic': document.execCommand('italic', false, null); break;
        case 'underline': document.execCommand('underline', false, null); break;
        case 'h2': document.execCommand('formatBlock', false, '<h2>'); break;
        case 'p': document.execCommand('formatBlock', false, '<p>'); break;
        case 'ul': document.execCommand('insertUnorderedList', false, null); break;
        case 'ol': document.execCommand('insertOrderedList', false, null); break;
    }
    updateDescription();
};

const updateDescription = () => {
    if (editor.value) {
        formData.futsal_description = editor.value.innerHTML;
        validateDescription();
    }
};

const validateDescription = () => {
    errors.futsal_description = '';
    if (!formData.futsal_description) errors.futsal_description = 'Description is required';
    else if (formData.futsal_description.length < 50) errors.futsal_description = 'Description should be at least 50 characters';
};

// Form submission
const submitForm = async () => {
    validateField('futsal_name');
    validateField('futsal_phone_number');
    validateField('price_per_hour');
    validateField('location');
    validateField('google_maps_link');
    validateField('a_side');
    validateField('grounds');
    validateDescription();
    validatePriceTable();

    if (
        errors.futsal_name ||
        errors.futsal_phone_number ||
        errors.futsal_image_1 ||
        errors.price_per_hour ||
        errors.price_table ||
        errors.location ||
        errors.google_maps_link ||
        errors.a_side ||
        errors.grounds ||
        errors.futsal_description
    ) {
        return;
    }

    try {
        isSubmitting.value = true;
        errors.api_error = '';

        // Prepare FormData for API
        const submitData = new FormData();
        submitData.append('futsal_name', formData.futsal_name);
        submitData.append('futsal_phone_number', formData.futsal_phone_number);
        for (let i = 1; i <= 5; i++) {
            if (formData[`futsal_image_${i}`]) {
                submitData.append(`futsal_image_${i}`, formData[`futsal_image_${i}`]);
            }
        }
        submitData.append('price_per_hour', formData.price_per_hour);
        if (formData.price_table) {
            submitData.append('price_table', JSON.stringify(formData.price_table));
        }
        submitData.append('location', formData.location);
        submitData.append('google_maps_link', formData.google_maps_link);
        submitData.append('a_side', formData.a_side);
        submitData.append('grounds', formData.grounds);
        submitData.append('shower_facility', formData.shower_facility);
        submitData.append('parking_space', formData.parking_space);
        submitData.append('changing_room', formData.changing_room);
        submitData.append('restaurant', formData.restaurant);
        submitData.append('wifi', formData.wifi);
        submitData.append('open_ground', formData.open_ground);
        submitData.append('futsal_description', formData.futsal_description);
        submitData.append('featured_futsal', formData.featured_futsal);
        submitData.append('futsal_owner', formData.futsal_owner);

        const response = await apiClient.post('futsal/create-futsal/', submitData, {
            headers: { 'Content-Type': 'multipart/form-data' }
        });

        if (response.status === 201) {
            alert("Your request to add futsal has been sent to the admins and you will recieve a response shortly. Thank you for your patience.")
            router.push('/profile');
        }
    } catch (error) {
        console.error('Error submitting form:', error);
        errors.api_error = error.response?.data?.detail || 'An error occurred while submitting the form. Please try again.';
    } finally {
        isSubmitting.value = false;
    }
};

// Initialize editor and fetch user data
onMounted(async () => {
    await initialize();
    if (editor.value && formData.futsal_description) {
        editor.value.innerHTML = formData.futsal_description;
    }
});
</script>

<style scoped>
/* Existing styles unchanged */
.add-futsal-page {
    min-height: 100vh;
    background-color: #f8f9fa;
    font-family: 'Inter', 'Segoe UI', Roboto, sans-serif;
    color: #333;
    padding: 40px 0;
}

.container {
    width: 100%;
    max-width: 900px;
    margin: 0 auto;
    padding: 0 20px;
}

.page-header {
    text-align: center;
    margin-bottom: 40px;
}

.page-header h1 {
    font-size: 2.25rem;
    font-weight: 700;
    color: #2e7d32;
    margin: 0 0 10px;
}

.page-header p {
    font-size: 1.1rem;
    color: #666;
    margin: 0;
}

/* Form Progress */
.form-progress {
    display: flex;
    justify-content: space-between;
    margin-bottom: 30px;
    position: relative;
}

.form-progress::before {
    content: '';
    position: absolute;
    top: 14px;
    left: 0;
    right: 0;
    height: 2px;
    background-color: #e0e0e0;
    z-index: 1;
}

.progress-step {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    z-index: 2;
    cursor: pointer;
}

.step-indicator {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background-color: #fff;
    border: 2px solid #e0e0e0;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 8px;
    font-weight: 600;
    font-size: 0.9rem;
    color: #757575;
    transition: all 0.3s ease;
}

.step-name {
    font-size: 0.85rem;
    color: #757575;
    transition: all 0.3s ease;
}

.progress-step.active .step-indicator {
    background-color: #2e7d32;
    border-color: #2e7d32;
    color: white;
}

.progress-step.active .step-name {
    color: #2e7d32;
    font-weight: 600;
}

.progress-step.completed .step-indicator {
    background-color: #2e7d32;
    border-color: #2e7d32;
    color: white;
}

.progress-step.completed .step-name {
    color: #2e7d32;
}

.progress-step.completed .step-indicator svg {
    width: 16px;
    height: 16px;
    color: white;
}

/* Form Container */
.form-container {
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    padding: 30px;
}

.form-step {
    margin-bottom: 30px;
}

.form-step h2 {
    font-size: 1.5rem;
    font-weight: 700;
    color: #2e7d32;
    margin: 0 0 5px;
}

.form-step p {
    font-size: 1rem;
    color: #666;
    margin: 0 0 20px;
}

.form-step h3 {
    font-size: 1.1rem;
    font-weight: 600;
    color: #333;
    margin: 20px 0 15px;
}

/* Form Elements */
.form-group {
    margin-bottom: 20px;
}

.form-row {
    display: flex;
    gap: 20px;
    margin-bottom: 20px;
}

.half-width {
    flex: 1;
}

label {
    display: block;
    font-size: 0.95rem;
    font-weight: 600;
    color: #555;
    margin-bottom: 8px;
}

.required {
    color: #e53935;
}

input[type="text"],
input[type="tel"],
input[type="number"],
input[type="url"] {
    width: 100%;
    padding: 12px 15px;
    border: 2px solid #e0e0e0;
    border-radius: 8px;
    font-size: 1rem;
    color: #333;
    transition: all 0.3s ease;
}

input:focus {
    outline: none;
    border-color: #2e7d32;
    box-shadow: 0 0 0 3px rgba(46, 125, 50, 0.1);
}

input::placeholder {
    color: #aaa;
}

.input-error {
    border-color: #e53935 !important;
}

.error-message {
    color: #e53935;
    font-size: 0.85rem;
    margin: 5px 0 0;
}

.help-text {
    color: #757575;
    font-size: 0.85rem;
    margin: 5px 0 0;
}

/* Amenities Grid */
.amenities-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 15px;
    margin-top: 15px;
}

.amenity-item {
    display: flex;
    align-items: center;
}

.amenity-item input[type="checkbox"] {
    width: 18px;
    height: 18px;
    margin-right: 10px;
    accent-color: #2e7d32;
}

.amenity-item label {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.95rem;
    font-weight: 500;
    color: #555;
    cursor: pointer;
}

.amenity-item label svg {
    width: 18px;
    height: 18px;
    color: #2e7d32;
}

/* Image Upload */
.image-upload-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 15px;
    margin-bottom: 15px;
}

.image-upload-box {
    height: 150px;
    border: 2px dashed #e0e0e0;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
}

.image-upload-box:hover {
    border-color: #2e7d32;
}

.image-upload-box.has-image {
    border: none;
}

.upload-label {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100%;
    cursor: pointer;
    padding: 15px;
    text-align: center;
}

.upload-label svg {
    width: 30px;
    height: 30px;
    color: #757575;
    margin-bottom: 10px;
}

.upload-label span {
    font-size: 0.85rem;
    color: #757575;
}

.hidden-input {
    display: none;
}

.image-preview {
    width: 100%;
    height: 100%;
    position: relative;
}

.image-preview img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 8px;
}

.remove-image-btn {
    position: absolute;
    top: 5px;
    right: 5px;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background-color: rgba(0, 0, 0, 0.5);
    border: none;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s ease;
}

.remove-image-btn:hover {
    background-color: rgba(0, 0, 0, 0.7);
}

.remove-image-btn svg {
    width: 14px;
    height: 14px;
    color: white;
}

/* Price Table */
.price-table {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    overflow: hidden;
    margin-bottom: 20px;
}

.price-table-header {
    display: flex;
    background-color: #f5f5f5;
    padding: 12px 15px;
    font-weight: 600;
    color: #555;
}

.price-name-header {
    flex: 2;
}

.price-value-header {
    flex: 1;
}

.price-action-header {
    width: 50px;
}

.price-table-row {
    display: flex;
    border-top: 1px solid #e0e0e0;
    padding: 10px 15px;
}

.price-name {
    flex: 2;
    padding-right: 10px;
}

.price-value {
    flex: 1;
    padding-right: 10px;
}

.price-action {
    width: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.price-table-row input {
    width: 100%;
    padding: 8px 10px;
    border: 1px solid #e0e0e0;
    border-radius: 6px;
}

.remove-price-btn {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background-color: #ffebee;
    border: none;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s ease;
}

.remove-price-btn:hover {
    background-color: #ffcdd2;
}

.remove-price-btn svg {
    width: 16px;
    height: 16px;
    color: #e53935;
}

.add-price-btn {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 10px 15px;
    background-color: #e8f5e9;
    color: #2e7d32;
    border: none;
    border-radius: 8px;
    font-size: 0.95rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
}

.add-price-btn:hover {
    background-color: #c8e6c9;
}

.add-price-btn svg {
    width: 18px;
    height: 18px;
}

/* Rich Text Editor */
.editor-toolbar {
    display: flex;
    gap: 5px;
    padding: 8px;
    background-color: #f5f5f5;
    border-radius: 8px 8px 0 0;
    border: 1px solid #e0e0e0;
    border-bottom: none;
}

.editor-toolbar button {
    width: 32px;
    height: 32px;
    border-radius: 4px;
    background-color: transparent;
    border: none;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s ease;
}

.editor-toolbar button:hover {
    background-color: #e0e0e0;
}

.editor-toolbar button svg {
    width: 16px;
    height: 16px;
    color: #555;
}

.toolbar-divider {
    width: 1px;
    height: 24px;
    background-color: #e0e0e0;
    margin: 0 5px;
}

.rich-text-editor {
    min-height: 200px;
    padding: 15px;
    border: 1px solid #e0e0e0;
    border-radius: 0 0 8px 8px;
    font-size: 1rem;
    line-height: 1.5;
    color: #333;
    overflow-y: auto;
}

.rich-text-editor:focus {
    outline: none;
    border-color: #2e7d32;
    box-shadow: 0 0 0 3px rgba(46, 125, 50, 0.1);
}

.preview-box {
    margin-top: 20px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 15px;
}

.preview-box h3 {
    font-size: 1rem;
    font-weight: 600;
    color: #555;
    margin: 0 0 10px;
}

.description-preview {
    font-size: 0.95rem;
    line-height: 1.5;
    color: #333;
}

/* Form Navigation */
.form-navigation {
    display: flex;
    justify-content: space-between;
    margin-top: 30px;
}

.back-btn,
.next-btn,
.submit-btn {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 12px 20px;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
}

.back-btn {
    background-color: #f5f5f5;
    color: #555;
    border: none;
}

.back-btn:hover {
    background-color: #e0e0e0;
}

.next-btn,
.submit-btn {
    background-color: #2e7d32;
    color: white;
    border: none;
}

.next-btn:hover,
.submit-btn:hover {
    background-color: #1b5e20;
}

.next-btn:disabled,
.submit-btn:disabled {
    background-color: #9e9e9e;
    cursor: not-allowed;
}

.back-btn svg,
.next-btn svg {
    width: 18px;
    height: 18px;
}

.spinner {
    width: 20px;
    height: 20px;
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

/* Responsive Styles */
@media (max-width: 768px) {
    .form-row {
        flex-direction: column;
        gap: 15px;
    }

    .amenities-grid {
        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    }

    .image-upload-container {
        grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
    }

    .step-name {
        display: none;
    }
}

@media (max-width: 480px) {
    .form-container {
        padding: 20px 15px;
    }

    .page-header h1 {
        font-size: 1.75rem;
    }

    .form-step h2 {
        font-size: 1.25rem;
    }

    .amenities-grid {
        grid-template-columns: 1fr 1fr;
    }

    .image-upload-container {
        grid-template-columns: repeat(2, 1fr);
    }

    .form-navigation {
        flex-direction: column;
        gap: 15px;
    }

    .back-btn,
    .next-btn,
    .submit-btn {
        width: 100%;
        justify-content: center;
    }

    .back-btn {
        order: 2;
    }

    .next-btn,
    .submit-btn {
        order: 1;
    }
}
</style>