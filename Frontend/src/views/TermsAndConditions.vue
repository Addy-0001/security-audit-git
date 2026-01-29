<template>
    <div class="terms-page">
        <div class="container">
            <div class="terms-header">
                <h1>Terms and Conditions</h1>
                <p class="last-updated">Last Updated: April 4, 2023</p>
            </div>

            <!-- Table of Contents -->
            <div class="toc-container">
                <div class="toc-header" @click="toggleToc">
                    <h2>Table of Contents</h2>
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round" :class="{ 'rotate': showToc }">
                        <polyline points="6 9 12 15 18 9"></polyline>
                    </svg>
                </div>
                <div class="toc-content" v-show="showToc">
                    <ul>
                        <li v-for="(section, index) in sections" :key="index">
                            <a href="#" @click.prevent="scrollToSection(section.id)">{{ section.title }}</a>
                        </li>
                    </ul>
                </div>
            </div>

            <!-- Terms Content -->
            <div class="terms-content">
                <!-- Introduction -->
                <section id="introduction" class="terms-section">
                    <h2>1. Introduction</h2>
                    <p>Welcome to Booksall ("we," "our," or "us"). By accessing or using our website, mobile
                        application,
                        or any other services provided by Booksall (collectively, the "Services"), you agree to be bound
                        by these Terms and Conditions ("Terms").</p>
                    <p>Please read these Terms carefully before using our Services. If you do not agree to these Terms,
                        you may not access or use our Services.</p>
                    <div class="info-box">
                        <div class="info-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <circle cx="12" cy="12" r="10"></circle>
                                <line x1="12" y1="16" x2="12" y2="12"></line>
                                <line x1="12" y1="8" x2="12.01" y2="8"></line>
                            </svg>
                        </div>
                        <div class="info-content">
                            <p>l is a platform that connects futsal court owners with individuals looking to book
                                futsal courts. These Terms govern your use of our platform, whether you are a futsal
                                court owner or a user booking courts.</p>
                        </div>
                    </div>
                </section>

                <!-- Definitions -->
                <section id="definitions" class="terms-section">
                    <h2>2. Definitions</h2>
                    <p>Throughout these Terms, we use certain defined terms:</p>
                    <ul class="definitions-list">
                        <li><strong>"User"</strong> refers to any individual who accesses or uses our Services,
                            including futsal court owners and individuals booking courts.</li>
                        <li><strong>"Futsal Owner"</strong> refers to any User who lists their futsal court(s) on our
                            platform.</li>
                        <li><strong>"Booking"</strong> refers to the reservation of a futsal court through our platform.
                        </li>
                        <li><strong>"Content"</strong> refers to all information, text, images, videos, and other
                            materials uploaded, posted, or otherwise made available through our Services.</li>
                    </ul>
                </section>

                <!-- Account Registration -->
                <section id="account-registration" class="terms-section">
                    <h2>3. Account Registration and User Responsibilities</h2>
                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('accountRegistration')">
                            <h3>3.1 Account Registration</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.accountRegistration }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.accountRegistration">
                            <p>To use certain features of our Services, you may need to create an account. When
                                registering for an account, you agree to provide accurate, current, and complete
                                information. You are responsible for maintaining the confidentiality of your account
                                credentials and for all activities that occur under your account.</p>
                            <p>You must be at least 18 years old to create an account. By creating an account, you
                                represent and warrant that you are at least 18 years old.</p>
                        </div>
                    </div>

                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('userResponsibilities')">
                            <h3>3.2 User Responsibilities</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.userResponsibilities }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.userResponsibilities">
                            <p>As a User, you agree to:</p>
                            <ul>
                                <li>Comply with all applicable laws and regulations</li>
                                <li>Respect the rights of other Users</li>
                                <li>Not engage in any activity that may interfere with the proper functioning of our
                                    Services</li>
                                <li>Not attempt to access any part of our Services by any means other than through the
                                    interfaces provided by us</li>
                                <li>Not use our Services for any illegal or unauthorized purpose</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Futsal Owner Terms -->
                <section id="futsal-owner-terms" class="terms-section">
                    <h2>4. Futsal Owner Terms</h2>
                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('listingRequirements')">
                            <h3>4.1 Listing Requirements</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.listingRequirements }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.listingRequirements">
                            <p>As a Futsal Owner, you are responsible for ensuring that all information provided about
                                your futsal court(s) is accurate, complete, and up-to-date. This includes, but is not
                                limited to:</p>
                            <ul>
                                <li>Futsal court name, location, and contact information</li>
                                <li>Pricing information</li>
                                <li>Availability</li>
                                <li>Amenities and facilities</li>
                                <li>Images of the futsal court</li>
                            </ul>
                            <p>You represent and warrant that you have the legal right to list your futsal court(s) on
                                our platform and that your listing does not violate any applicable laws, regulations, or
                                third-party rights.</p>
                        </div>
                    </div>

                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('ownerObligations')">
                            <h3>4.2 Futsal Owner Obligations</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.ownerObligations }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.ownerObligations">
                            <p>As a Futsal Owner, you agree to:</p>
                            <ul>
                                <li>Honor all bookings made through our platform</li>
                                <li>Maintain your futsal court(s) in a safe and clean condition</li>
                                <li>Provide the amenities and facilities as described in your listing</li>
                                <li>Respond promptly to booking requests and inquiries</li>
                                <li>Comply with all applicable laws and regulations, including health and safety
                                    regulations</li>
                                <li>Obtain and maintain all necessary licenses, permits, and insurance for operating
                                    your futsal court(s)</li>
                            </ul>
                        </div>
                    </div>

                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('commissionFees')">
                            <h3>4.3 Commission and Fees</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.commissionFees }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.commissionFees">
                            <p>In consideration for the use of our platform, Futsal Owners agree to pay us a commission
                                on each booking made through our Services. The commission rate will be specified in a
                                separate agreement between us and the Futsal Owner.</p>
                            <p>We reserve the right to change our commission rates from time to time. Any changes to
                                commission rates will be communicated to Futsal Owners in advance and will apply to
                                bookings made after the effective date of the change.</p>
                        </div>
                    </div>
                </section>

                <!-- Booking Terms -->
                <section id="booking-terms" class="terms-section">
                    <h2>5. Booking Terms</h2>
                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('bookingProcess')">
                            <h3>5.1 Booking Process</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.bookingProcess }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.bookingProcess">
                            <p>Users may book futsal courts through our platform based on the availability provided by
                                Futsal Owners. A booking is confirmed once the User has completed the booking process
                                and received a confirmation from us.</p>
                            <p>By making a booking, Users agree to pay the specified price for the futsal court at the
                                time and date selected. Users also agree to comply with any rules or requirements
                                specified by the Futsal Owner in the listing.</p>
                        </div>
                    </div>

                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('cancellationPolicy')">
                            <h3>5.2 Cancellation Policy</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.cancellationPolicy }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.cancellationPolicy">
                            <p>Cancellation policies may vary depending on the Futsal Owner. The specific cancellation
                                policy applicable to a booking will be displayed at the time of booking.</p>
                            <p>In general, cancellations made more than 24 hours before the scheduled booking time may
                                be eligible for a full or partial refund, while cancellations made less than 24 hours
                                before the scheduled booking time may not be eligible for a refund.</p>
                            <p>We reserve the right to cancel a booking in exceptional circumstances, such as if we have
                                reason to believe that the booking violates our Terms or if the futsal court becomes
                                unavailable due to unforeseen circumstances. In such cases, we will provide a full
                                refund to the User.</p>
                        </div>
                    </div>

                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('paymentTerms')">
                            <h3>5.3 Payment Terms</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.paymentTerms }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.paymentTerms">
                            <p>Users agree to pay the full amount specified at the time of booking. Payments may be made
                                through the payment methods available on our platform.</p>
                            <p>We use third-party payment processors to process payments. By making a payment through
                                our Services, you agree to the terms and conditions of these payment processors.</p>
                            <p>Futsal Owners will receive payment for bookings according to the payment schedule
                                specified in a separate agreement between us and the Futsal Owner, less our commission
                                and any applicable fees.</p>
                        </div>
                    </div>
                </section>

                <!-- Content and Intellectual Property -->
                <section id="content-ip" class="terms-section">
                    <h2>6. Content and Intellectual Property</h2>
                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('userContent')">
                            <h3>6.1 User Content</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.userContent }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.userContent">
                            <p>By uploading, posting, or otherwise making available any Content through our Services,
                                you grant us a non-exclusive, worldwide, royalty-free, sublicensable, and transferable
                                license to use, reproduce, modify, adapt, publish, translate, create derivative works
                                from, distribute, and display such Content in connection with providing and promoting
                                our Services.</p>
                            <p>You represent and warrant that:</p>
                            <ul>
                                <li>You own or have the necessary rights to the Content you post</li>
                                <li>The Content does not violate the privacy rights, publicity rights, copyright,
                                    contractual rights, or any other rights of any person or entity</li>
                                <li>The Content does not contain any material that is defamatory, obscene, indecent,
                                    abusive, offensive, harassing, violent, hateful, inflammatory, or otherwise
                                    objectionable</li>
                            </ul>
                            <p>We reserve the right to remove any Content that violates these Terms or that we otherwise
                                find objectionable.</p>
                        </div>
                    </div>

                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('intellectualProperty')">
                            <h3>6.2 Intellectual Property Rights</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.intellectualProperty }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.intellectualProperty">
                            <p>Our Services and all content, features, and functionality thereof, including but not
                                limited to all information, software, text, displays, images, video, and audio, and the
                                design, selection, and arrangement thereof, are owned by us, our licensors, or other
                                providers of such material and are protected by copyright, trademark, patent, trade
                                secret, and other intellectual property or proprietary rights laws.</p>
                            <p>These Terms do not grant you any right, title, or interest in our Services or any
                                content, features, or functionality thereof.</p>
                        </div>
                    </div>
                </section>

                <!-- Data Privacy -->
                <section id="data-privacy" class="terms-section">
                    <h2>7. Data Privacy</h2>
                    <p>We collect, use, and share your personal information in accordance with our Privacy Policy, which
                        is incorporated by reference into these Terms. By using our Services, you consent to the
                        collection, use, and sharing of your personal information as described in our Privacy Policy.
                    </p>

                    <div class="info-box">
                        <div class="info-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M18 8h1a4 4 0 0 1 0 8h-1"></path>
                                <path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"></path>
                                <line x1="6" y1="1" x2="6" y2="4"></line>
                                <line x1="10" y1="1" x2="10" y2="4"></line>
                                <line x1="14" y1="1" x2="14" y2="4"></line>
                            </svg>
                        </div>
                        <div class="info-content">
                            <p><strong>Important:</strong> For Futsal Owners, we collect and process information about
                                your futsal court(s), including location data, images, pricing information, and
                                amenities. This information is necessary to provide our Services and will be displayed
                                publicly on our platform.</p>
                        </div>
                    </div>

                    <p>We implement appropriate technical and organizational measures to protect your personal
                        information. However, no method of transmission over the Internet or electronic storage is 100%
                        secure, and we cannot guarantee absolute security.</p>
                </section>

                <!-- Limitation of Liability -->
                <section id="limitation-liability" class="terms-section">
                    <h2>8. Limitation of Liability</h2>
                    <p>To the maximum extent permitted by law, we shall not be liable for any indirect, incidental,
                        special, consequential, or punitive damages, or any loss of profits or revenues, whether
                        incurred directly or indirectly, or any loss of data, use, goodwill, or other intangible losses,
                        resulting from:</p>
                    <ul>
                        <li>Your access to or use of or inability to access or use our Services</li>
                        <li>Any conduct or content of any third party on our Services</li>
                        <li>Any content obtained from our Services</li>
                        <li>Unauthorized access, use, or alteration of your transmissions or content</li>
                    </ul>
                    <p>In no event shall our aggregate liability exceed the greater of one hundred dollars ($100) or the
                        amount you have paid us in the past twelve months.</p>
                </section>

                <!-- Indemnification -->
                <section id="indemnification" class="terms-section">
                    <h2>9. Indemnification</h2>
                    <p>You agree to defend, indemnify, and hold harmless us, our affiliates, licensors, and service
                        providers, and our and their respective officers, directors, employees, contractors, agents,
                        licensors, suppliers, successors, and assigns from and against any claims, liabilities, damages,
                        judgments, awards, losses, costs, expenses, or fees (including reasonable attorneys' fees)
                        arising out of or relating to your violation of these Terms or your use of our Services.</p>
                </section>

                <!-- Termination -->
                <section id="termination" class="terms-section">
                    <h2>10. Termination</h2>
                    <p>We may terminate or suspend your account and access to our Services immediately, without prior
                        notice or liability, for any reason whatsoever, including without limitation if you breach these
                        Terms.</p>
                    <p>Upon termination, your right to use our Services will immediately cease. If you wish to terminate
                        your account, you may simply discontinue using our Services or contact us to request account
                        deletion.</p>
                </section>

                <!-- Governing Law -->
                <section id="governing-law" class="terms-section">
                    <h2>11. Governing Law and Dispute Resolution</h2>
                    <p>These Terms shall be governed by and construed in accordance with the laws of Nepal, without
                        regard to its conflict of law provisions.</p>
                    <p>Any dispute arising out of or relating to these Terms or our Services shall be resolved through
                        binding arbitration in accordance with the rules of the Nepal Council of Arbitration. The
                        arbitration shall take place in Kathmandu, Nepal, and shall be conducted in the English
                        language.</p>
                </section>

                <!-- Changes to Terms -->
                <section id="changes-terms" class="terms-section">
                    <h2>12. Changes to Terms</h2>
                    <p>We reserve the right to modify or replace these Terms at any time. If a revision is material, we
                        will provide at least 30 days' notice prior to any new terms taking effect. What constitutes a
                        material change will be determined at our sole discretion.</p>
                    <p>By continuing to access or use our Services after any revisions become effective, you agree to be
                        bound by the revised terms. If you do not agree to the new terms, you are no longer authorized
                        to use our Services.</p>
                </section>

                <!-- Contact Us -->
                <section id="contact-us" class="terms-section">
                    <h2>13. Contact Us</h2>
                    <p>If you have any questions about these Terms, please contact us at:</p>
                    <div class="contact-info">
                        <p><strong>Email:</strong> support@booksall.com</p>
                        <p><strong>Phone:</strong> +977 9841234567</p>
                        <p><strong>Address:</strong> Kathmandu, Nepal</p>
                    </div>
                </section>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const showToc = ref(true);
const termsAccepted = ref(false);

// Sections for table of contents
const sections = [
    { id: 'introduction', title: '1. Introduction' },
    { id: 'definitions', title: '2. Definitions' },
    { id: 'account-registration', title: '3. Account Registration and User Responsibilities' },
    { id: 'futsal-owner-terms', title: '4. Futsal Owner Terms' },
    { id: 'booking-terms', title: '5. Booking Terms' },
    { id: 'content-ip', title: '6. Content and Intellectual Property' },
    { id: 'data-privacy', title: '7. Data Privacy' },
    { id: 'limitation-liability', title: '8. Limitation of Liability' },
    { id: 'indemnification', title: '9. Indemnification' },
    { id: 'termination', title: '10. Termination' },
    { id: 'governing-law', title: '11. Governing Law and Dispute Resolution' },
    { id: 'changes-terms', title: '12. Changes to Terms' },
    { id: 'contact-us', title: '13. Contact Us' }
];

// Track open/closed state of collapsible sections
const openSections = reactive({
    accountRegistration: false,
    userResponsibilities: false,
    listingRequirements: false,
    ownerObligations: false,
    commissionFees: false,
    bookingProcess: false,
    cancellationPolicy: false,
    paymentTerms: false,
    userContent: false,
    intellectualProperty: false
});

// Toggle table of contents
const toggleToc = () => {
    showToc.value = !showToc.value;
};

// Toggle collapsible sections
const toggleSection = (section) => {
    openSections[section] = !openSections[section];
};

// Scroll to section
const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
    }
};

// Accept terms and continue
const acceptTerms = () => {
    if (termsAccepted.value) {
        // In a real app, you would store this acceptance
        // For demo purposes, we'll just go back to the add futsal page
        router.push('/add-futsal');
    }
};
</script>

<style scoped>
/* Terms and Conditions Page Styles */
.terms-page {
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

/* Header Styles */
.terms-header {
    text-align: center;
    margin-bottom: 30px;
}

.terms-header h1 {
    font-size: 2.25rem;
    font-weight: 700;
    color: #2e7d32;
    margin: 0 0 10px;
}

.last-updated {
    font-size: 0.9rem;
    color: #666;
    margin: 0;
}

/* Table of Contents */
.toc-container {
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    margin-bottom: 30px;
    overflow: hidden;
}

.toc-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 20px;
    cursor: pointer;
    border-bottom: 1px solid #f0f0f0;
}

.toc-header h2 {
    font-size: 1.25rem;
    font-weight: 700;
    color: #2e7d32;
    margin: 0;
}

.toc-header svg {
    width: 20px;
    height: 20px;
    color: #2e7d32;
    transition: transform 0.3s ease;
}

.toc-header svg.rotate {
    transform: rotate(180deg);
}

.toc-content {
    padding: 20px;
}

.toc-content ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
}

.toc-content li {
    margin-bottom: 10px;
}

.toc-content li:last-child {
    margin-bottom: 0;
}

.toc-content a {
    color: #2e7d32;
    text-decoration: none;
    font-size: 0.95rem;
    transition: color 0.2s ease;
}

.toc-content a:hover {
    color: #1b5e20;
    text-decoration: underline;
}

/* Terms Content */
.terms-content {
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    padding: 30px;
    margin-bottom: 30px;
}

.terms-section {
    margin-bottom: 40px;
    scroll-margin-top: 20px;
}

.terms-section:last-child {
    margin-bottom: 0;
}

.terms-section h2 {
    font-size: 1.5rem;
    font-weight: 700;
    color: #2e7d32;
    margin: 0 0 20px;
    padding-bottom: 10px;
    border-bottom: 1px solid #e0e0e0;
}

.terms-section p {
    font-size: 0.95rem;
    line-height: 1.6;
    color: #333;
    margin: 0 0 15px;
}

.terms-section ul {
    padding-left: 20px;
    margin: 0 0 15px;
}

.terms-section li {
    font-size: 0.95rem;
    line-height: 1.6;
    color: #333;
    margin-bottom: 8px;
}

/* Collapsible Sections */
.collapsible-section {
    margin-bottom: 15px;
}

.collapsible-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 15px;
    background-color: #f1f8e9;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.2s ease;
}

.collapsible-header:hover {
    background-color: #e8f5e9;
}

.collapsible-header h3 {
    font-size: 1.1rem;
    font-weight: 600;
    color: #333;
    margin: 0;
}

.collapsible-header svg {
    width: 16px;
    height: 16px;
    color: #2e7d32;
    transition: transform 0.3s ease;
}

.collapsible-header svg.rotate {
    transform: rotate(180deg);
}

.collapsible-content {
    padding: 15px;
}

/* Info Box */
.info-box {
    display: flex;
    gap: 15px;
    padding: 15px;
    background-color: #e8f5e9;
    border-radius: 8px;
    margin: 20px 0;
}

.info-icon {
    display: flex;
    align-items: flex-start;
}

.info-icon svg {
    width: 24px;
    height: 24px;
    color: #2e7d32;
}

.info-content p {
    margin: 0;
}

/* Definitions List */
.definitions-list {
    list-style-type: none;
    padding: 0;
}

.definitions-list li {
    margin-bottom: 12px;
    padding-left: 20px;
    position: relative;
}

.definitions-list li:before {
    content: "•";
    position: absolute;
    left: 0;
    color: #2e7d32;
}

/* Contact Info */
.contact-info {
    background-color: #f5f5f5;
    border-radius: 8px;
    padding: 15px;
    margin-top: 15px;
}

.contact-info p {
    margin: 0 0 8px;
}

.contact-info p:last-child {
    margin-bottom: 0;
}

/* Terms Acceptance */
.terms-acceptance {
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.acceptance-checkbox {
    display: flex;
    align-items: center;
    gap: 10px;
}

.acceptance-checkbox input[type="checkbox"] {
    width: 18px;
    height: 18px;
    accent-color: #2e7d32;
}

.acceptance-checkbox label {
    font-size: 0.95rem;
    color: #333;
}

.accept-button {
    padding: 12px 20px;
    background-color: #2e7d32;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    align-self: flex-end;
}

.accept-button:hover:not(:disabled) {
    background-color: #1b5e20;
}

.accept-button:disabled {
    background-color: #9e9e9e;
    cursor: not-allowed;
}

/* Responsive Styles */
@media (max-width: 768px) {
    .terms-header h1 {
        font-size: 1.75rem;
    }

    .terms-content {
        padding: 20px;
    }

    .terms-section h2 {
        font-size: 1.3rem;
    }

    .collapsible-header h3 {
        font-size: 1rem;
    }

    .terms-acceptance {
        flex-direction: column;
        align-items: stretch;
    }

    .accept-button {
        align-self: stretch;
    }
}

@media (max-width: 480px) {
    .terms-header h1 {
        font-size: 1.5rem;
    }

    .terms-content {
        padding: 15px;
    }

    .collapsible-header {
        padding: 10px;
    }

    .info-box {
        flex-direction: column;
        gap: 10px;
    }
}
</style>