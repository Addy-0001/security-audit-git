<template>
    <div class="privacy-page">
        <div class="container">
            <div class="privacy-header">
                <h1>Privacy Policy</h1>
                <p class="last-updated">Last Updated: April 4, 2023</p>
            </div>

            <!-- Introduction Banner -->
            <div class="intro-banner">
                <div class="intro-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                        <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                    </svg>
                </div>
                <div class="intro-content">
                    <p>At l, we take your privacy seriously. This Privacy Policy explains how we collect, use,
                        disclose, and safeguard your information when you use our futsal booking platform.</p>
                    <p>Please read this Privacy Policy carefully. If you do not agree with the terms of this Privacy
                        Policy, please do not access our platform.</p>
                </div>
            </div>

            <!-- Quick Links -->
            <div class="quick-links">
                <h2>Quick Links</h2>
                <div class="links-grid">
                    <a href="#information-collection" @click.prevent="scrollToSection('information-collection')">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                            <polyline points="14 2 14 8 20 8"></polyline>
                            <line x1="16" y1="13" x2="8" y2="13"></line>
                            <line x1="16" y1="17" x2="8" y2="17"></line>
                            <polyline points="10 9 9 9 8 9"></polyline>
                        </svg>
                        Information We Collect
                    </a>
                    <a href="#information-use" @click.prevent="scrollToSection('information-use')">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="12" cy="12" r="10"></circle>
                            <polyline points="12 6 12 12 16 14"></polyline>
                        </svg>
                        How We Use Your Information
                    </a>
                    <a href="#information-sharing" @click.prevent="scrollToSection('information-sharing')">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                            <circle cx="9" cy="7" r="4"></circle>
                            <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                            <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                        </svg>
                        Information Sharing
                    </a>
                    <a href="#data-security" @click.prevent="scrollToSection('data-security')">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                        </svg>
                        Data Security
                    </a>
                    <a href="#your-rights" @click.prevent="scrollToSection('your-rights')">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
                            <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
                        </svg>
                        Your Rights
                    </a>
                    <a href="#cookies" @click.prevent="scrollToSection('cookies')">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="12" cy="12" r="10"></circle>
                            <circle cx="12" cy="12" r="4"></circle>
                            <line x1="21.17" y1="8" x2="12" y2="8"></line>
                            <line x1="3.95" y1="6.06" x2="8.54" y2="14"></line>
                            <line x1="10.88" y1="21.94" x2="15.46" y2="14"></line>
                        </svg>
                        Cookies Policy
                    </a>
                </div>
            </div>

            <!-- Privacy Content -->
            <div class="privacy-content">
                <!-- Information Collection -->
                <section id="information-collection" class="privacy-section">
                    <h2>1. Information We Collect</h2>

                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('personalInfo')">
                            <h3>1.1 Personal Information</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.personalInfo }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.personalInfo">
                            <p>We may collect the following types of personal information:</p>
                            <ul>
                                <li><strong>Contact Information:</strong> Name, email address, phone number, and
                                    address.</li>
                                <li><strong>Account Information:</strong> Username, password, and account preferences.
                                </li>
                                <li><strong>Profile Information:</strong> Profile picture, bio, and other information
                                    you choose to provide.</li>
                                <li><strong>Payment Information:</strong> Credit card details, billing address, and
                                    other payment details. Note that we use third-party payment processors and do not
                                    store complete payment information on our servers.</li>
                            </ul>
                            <div class="info-callout">
                                <p><strong>For Futsal Owners:</strong> We collect additional information such as futsal
                                    court details, business information, and tax identification numbers where
                                    applicable.</p>
                            </div>
                        </div>
                    </div>

                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('futsalInfo')">
                            <h3>1.2 Futsal Court Information</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.futsalInfo }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.futsalInfo">
                            <p>For futsal courts listed on our platform, we collect:</p>
                            <ul>
                                <li><strong>Basic Details:</strong> Futsal court name, description, and pricing
                                    information.</li>
                                <li><strong>Location Data:</strong> Address, geographic coordinates, and Google Maps
                                    links.</li>
                                <li><strong>Amenities and Features:</strong> Information about facilities, court size,
                                    and available services.</li>
                                <li><strong>Images:</strong> Photographs of the futsal court and its facilities.</li>
                                <li><strong>Availability:</strong> Operating hours and booking availability.</li>
                            </ul>
                            <p>This information is necessary to provide our core services and will be displayed publicly
                                on our platform to users looking to book futsal courts.</p>
                        </div>
                    </div>

                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('automaticInfo')">
                            <h3>1.3 Automatically Collected Information</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.automaticInfo }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.automaticInfo">
                            <p>When you access our platform, we automatically collect certain information, including:
                            </p>
                            <ul>
                                <li><strong>Device Information:</strong> Device type, operating system, browser type,
                                    and mobile network information.</li>
                                <li><strong>Log Data:</strong> IP address, access times, pages viewed, and activities on
                                    our platform.</li>
                                <li><strong>Location Data:</strong> General location information based on IP address or
                                    more precise location if you grant permission.</li>
                                <li><strong>Usage Data:</strong> How you interact with our platform, including search
                                    queries, bookings made, and features used.</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Information Use -->
                <section id="information-use" class="privacy-section">
                    <h2>2. How We Use Your Information</h2>

                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('serviceProvision')">
                            <h3>2.1 Providing and Improving Our Services</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.serviceProvision }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.serviceProvision">
                            <p>We use your information to:</p>
                            <ul>
                                <li>Create and manage your account</li>
                                <li>Process bookings and payments</li>
                                <li>Connect futsal court owners with potential customers</li>
                                <li>Provide customer support</li>
                                <li>Improve and optimize our platform</li>
                                <li>Develop new features and services</li>
                                <li>Ensure the security and integrity of our platform</li>
                            </ul>
                        </div>
                    </div>

                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('communications')">
                            <h3>2.2 Communications</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.communications }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.communications">
                            <p>We may use your information to communicate with you about:</p>
                            <ul>
                                <li>Booking confirmations and updates</li>
                                <li>Responses to your inquiries and requests</li>
                                <li>Important updates about our platform</li>
                                <li>Marketing and promotional materials (with your consent)</li>
                                <li>Surveys and feedback requests</li>
                            </ul>
                            <p>You can opt out of marketing communications at any time by following the unsubscribe
                                instructions in our emails or contacting us directly.</p>
                        </div>
                    </div>

                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('analytics')">
                            <h3>2.3 Analytics and Research</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.analytics }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.analytics">
                            <p>We use data analytics to:</p>
                            <ul>
                                <li>Understand how users interact with our platform</li>
                                <li>Identify usage trends and preferences</li>
                                <li>Measure the effectiveness of our marketing campaigns</li>
                                <li>Improve user experience</li>
                                <li>Develop new features based on user behavior</li>
                            </ul>
                            <p>For these purposes, we may use third-party analytics providers who may use cookies and
                                similar technologies to collect information about your use of our platform.</p>
                        </div>
                    </div>

                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('legalCompliance')">
                            <h3>2.4 Legal Compliance and Protection</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.legalCompliance }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.legalCompliance">
                            <p>We may use your information to:</p>
                            <ul>
                                <li>Comply with applicable laws and regulations</li>
                                <li>Respond to legal requests and prevent harm</li>
                                <li>Detect and prevent fraud, abuse, and security incidents</li>
                                <li>Enforce our Terms and Conditions</li>
                                <li>Protect the rights, property, or safety of our users, ourselves, or others</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Information Sharing -->
                <section id="information-sharing" class="privacy-section">
                    <h2>3. Information Sharing and Disclosure</h2>

                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('userSharing')">
                            <h3>3.1 Sharing Between Users</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.userSharing }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.userSharing">
                            <p>Our platform facilitates connections between futsal court owners and users looking to
                                book courts. As part of this service:</p>
                            <ul>
                                <li>Futsal court information (including location, amenities, images, and availability)
                                    is publicly visible to all users.</li>
                                <li>When you make a booking, we share your name and contact information with the futsal
                                    court owner.</li>
                                <li>Futsal owners can see booking history and patterns for their courts.</li>
                            </ul>
                            <div class="info-callout">
                                <p><strong>Note:</strong> While we facilitate communication between users and futsal
                                    court owners, we advise against sharing sensitive personal or payment information
                                    directly with other users outside our platform.</p>
                            </div>
                        </div>
                    </div>

                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('serviceProviders')">
                            <h3>3.2 Service Providers</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.serviceProviders }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.serviceProviders">
                            <p>We may share your information with third-party service providers who help us operate our
                                platform, including:</p>
                            <ul>
                                <li><strong>Payment Processors:</strong> To process bookings and payments.</li>
                                <li><strong>Cloud Service Providers:</strong> For data storage and hosting.</li>
                                <li><strong>Analytics Providers:</strong> To help us understand user behavior and
                                    improve our services.</li>
                                <li><strong>Customer Support Services:</strong> To assist with user inquiries and
                                    issues.</li>
                                <li><strong>Marketing Services:</strong> To help us promote our platform (with your
                                    consent).</li>
                            </ul>
                            <p>These service providers are contractually obligated to use your information only as
                                directed by us and in accordance with this Privacy Policy.</p>
                        </div>
                    </div>

                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('legalDisclosure')">
                            <h3>3.3 Legal Disclosure</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.legalDisclosure }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.legalDisclosure">
                            <p>We may disclose your information if required to do so by law or in response to valid
                                requests by public authorities (e.g., a court or government agency). We may also
                                disclose your information to:</p>
                            <ul>
                                <li>Enforce our Terms and Conditions</li>
                                <li>Protect and defend our rights or property</li>
                                <li>Prevent or investigate possible wrongdoing in connection with our services</li>
                                <li>Protect the personal safety of users of our services or the public</li>
                                <li>Protect against legal liability</li>
                            </ul>
                        </div>
                    </div>

                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('businessTransfers')">
                            <h3>3.4 Business Transfers</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.businessTransfers }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.businessTransfers">
                            <p>If we are involved in a merger, acquisition, or sale of all or a portion of our assets,
                                your information may be transferred as part of that transaction. We will notify you via
                                email and/or a prominent notice on our platform of any change in ownership or uses of
                                your information, as well as any choices you may have regarding your information.</p>
                        </div>
                    </div>
                </section>

                <!-- Data Security -->
                <section id="data-security" class="privacy-section">
                    <h2>4. Data Security</h2>
                    <p>We implement appropriate technical and organizational measures to protect your personal
                        information against unauthorized or unlawful processing, accidental loss, destruction, or
                        damage.</p>

                    <div class="security-measures">
                        <div class="security-item">
                            <div class="security-icon">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                    stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round">
                                    <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                                    <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                                </svg>
                            </div>
                            <div class="security-content">
                                <h4>Encryption</h4>
                                <p>We use industry-standard encryption to protect your data in transit and at rest.</p>
                            </div>
                        </div>

                        <div class="security-item">
                            <div class="security-icon">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                    stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round">
                                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                                </svg>
                            </div>
                            <div class="security-content">
                                <h4>Access Controls</h4>
                                <p>We restrict access to personal information to employees, contractors, and agents who
                                    need to know that information to process it for us.</p>
                            </div>
                        </div>

                        <div class="security-item">
                            <div class="security-icon">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                    stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round">
                                    <path
                                        d="M21 2l-2 2m-7.61 7.61a5.5 5.5 0 1 1-7.778 7.778 5.5 5.5 0 0 1 7.777-7.777zm0 0L15.5 7.5m0 0l3 3L22 7l-3-3m-3.5 3.5L19 4">
                                    </path>
                                </svg>
                            </div>
                            <div class="security-content">
                                <h4>Regular Audits</h4>
                                <p>We conduct regular security audits and vulnerability assessments to identify and
                                    address potential security risks.</p>
                            </div>
                        </div>
                    </div>

                    <div class="info-callout warning">
                        <p><strong>Important:</strong> While we take reasonable measures to protect your information, no
                            method of transmission over the Internet or electronic storage is 100% secure. We cannot
                            guarantee absolute security of your data.</p>
                    </div>

                    <p>In the event of a data breach that affects your personal information, we will notify you in
                        accordance with applicable laws.</p>
                </section>

                <!-- Data Retention -->
                <section id="data-retention" class="privacy-section">
                    <h2>5. Data Retention</h2>
                    <p>We retain your personal information for as long as necessary to fulfill the purposes outlined in
                        this Privacy Policy, unless a longer retention period is required or permitted by law.</p>

                    <div class="retention-details">
                        <div class="retention-item">
                            <h4>Account Information</h4>
                            <p>We retain your account information for as long as your account is active. If you close
                                your account, we will retain certain information as necessary to comply with our legal
                                obligations, resolve disputes, and enforce our agreements.</p>
                        </div>

                        <div class="retention-item">
                            <h4>Booking Information</h4>
                            <p>We retain booking information for a period of 5 years to comply with tax and accounting
                                requirements, handle disputes, and provide customer support.</p>
                        </div>

                        <div class="retention-item">
                            <h4>Futsal Court Information</h4>
                            <p>Information about futsal courts is retained for as long as the court is listed on our
                                platform and for a reasonable period afterward to handle any related inquiries or
                                disputes.</p>
                        </div>
                    </div>

                    <p>When we no longer need your personal information, we will securely delete or anonymize it.</p>
                </section>

                <!-- Your Rights -->
                <section id="your-rights" class="privacy-section">
                    <h2>6. Your Rights</h2>
                    <p>Depending on your location, you may have certain rights regarding your personal information.
                        These may include:</p>

                    <div class="rights-grid">
                        <div class="right-item">
                            <div class="right-icon">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                    stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round">
                                    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                                    <circle cx="12" cy="12" r="3"></circle>
                                </svg>
                            </div>
                            <h4>Right to Access</h4>
                            <p>You can request a copy of the personal information we hold about you.</p>
                        </div>

                        <div class="right-item">
                            <div class="right-icon">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                    stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round">
                                    <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                                    <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                                </svg>
                            </div>
                            <h4>Right to Rectification</h4>
                            <p>You can request that we correct inaccurate or incomplete information about you.</p>
                        </div>

                        <div class="right-item">
                            <div class="right-icon">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                    stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round">
                                    <polyline points="3 6 5 6 21 6"></polyline>
                                    <path
                                        d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2">
                                    </path>
                                </svg>
                            </div>
                            <h4>Right to Erasure</h4>
                            <p>In certain circumstances, you can request that we delete your personal information.</p>
                        </div>

                        <div class="right-item">
                            <div class="right-icon">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                    stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round">
                                    <line x1="22" y1="2" x2="11" y2="13"></line>
                                    <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                                </svg>
                            </div>
                            <h4>Right to Restriction</h4>
                            <p>You can request that we restrict the processing of your personal information.</p>
                        </div>

                        <div class="right-item">
                            <div class="right-icon">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                    stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round">
                                    <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                                    <path d="M5 15H4a2 2 0 0 1-2" y="9" width="13" height="13" rx="2" ry="2">
                                    </path>
                                    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9"></path>
                                </svg>
                            </div>
                            <h4>Right to Data Portability</h4>
                            <p>You can request a copy of your personal information in a structured, commonly used, and
                                machine-readable format.</p>
                        </div>

                        <div class="right-item">
                            <div class="right-icon">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                    stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round">
                                    <circle cx="12" cy="12" r="10"></circle>
                                    <line x1="4.93" y1="4.93" x2="19.07" y2="19.07"></line>
                                </svg>
                            </div>
                            <h4>Right to Object</h4>
                            <p>You can object to the processing of your personal information in certain circumstances.
                            </p>
                        </div>
                    </div>

                    <p>To exercise any of these rights, please contact us using the information provided in the "Contact
                        Us" section. We will respond to your request within a reasonable timeframe and in accordance
                        with applicable laws.</p>
                </section>

                <!-- Cookies -->
                <section id="cookies" class="privacy-section">
                    <h2>7. Cookies and Similar Technologies</h2>
                    <p>We use cookies and similar tracking technologies to collect and use information about you and
                        your interaction with our platform.</p>

                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('cookieTypes')">
                            <h3>7.1 Types of Cookies We Use</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.cookieTypes }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.cookieTypes">
                            <div class="cookie-types">
                                <div class="cookie-type">
                                    <h4>Essential Cookies</h4>
                                    <p>These cookies are necessary for the platform to function and cannot be switched
                                        off. They are usually set in response to actions made by you, such as setting
                                        your privacy preferences, logging in, or filling in forms.</p>
                                </div>

                                <div class="cookie-type">
                                    <h4>Performance Cookies</h4>
                                    <p>These cookies allow us to count visits and traffic sources so we can measure and
                                        improve the performance of our platform. They help us know which pages are the
                                        most and least popular and see how visitors move around the site.</p>
                                </div>

                                <div class="cookie-type">
                                    <h4>Functionality Cookies</h4>
                                    <p>These cookies enable the platform to provide enhanced functionality and
                                        personalization. They may be set by us or by third-party providers whose
                                        services we have added to our pages.</p>
                                </div>

                                <div class="cookie-type">
                                    <h4>Targeting Cookies</h4>
                                    <p>These cookies may be set through our platform by our advertising partners. They
                                        may be used by those companies to build a profile of your interests and show you
                                        relevant advertisements on other sites.</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="collapsible-section">
                        <div class="collapsible-header" @click="toggleSection('cookieControl')">
                            <h3>7.2 Your Cookie Choices</h3>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                :class="{ 'rotate': openSections.cookieControl }">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="collapsible-content" v-show="openSections.cookieControl">
                            <p>You can control cookies through your browser settings. Most browsers allow you to refuse
                                or accept cookies, delete cookies, or be notified when a cookie is being sent. However,
                                if you disable cookies, some features of our platform may not function properly.</p>
                            <p>When you first visit our platform, you will be presented with a cookie banner that allows
                                you to accept or decline non-essential cookies.</p>
                        </div>
                    </div>
                </section>

                <!-- Children's Privacy -->
                <section id="childrens-privacy" class="privacy-section">
                    <h2>8. Children's Privacy</h2>
                    <p>Our platform is not intended for children under the age of 18. We do not knowingly collect
                        personal information from children under 18. If you are a parent or guardian and believe that
                        your child has provided us with personal information, please contact us, and we will delete such
                        information from our systems.</p>
                </section>

                <!-- International Data Transfers -->
                <section id="international-transfers" class="privacy-section">
                    <h2>9. International Data Transfers</h2>
                    <p>We may transfer your personal information to countries other than the one in which you reside.
                        When we transfer your personal information internationally, we take appropriate safeguards to
                        ensure that your information receives an adequate level of protection.</p>
                    <p>By using our platform, you acknowledge that your personal information may be transferred to and
                        processed in countries outside of your country of residence, which may have different data
                        protection rules than those of your country.</p>
                </section>

                <!-- Changes to Privacy Policy -->
                <section id="policy-changes" class="privacy-section">
                    <h2>10. Changes to This Privacy Policy</h2>
                    <p>We may update this Privacy Policy from time to time. We will notify you of any changes by posting
                        the new Privacy Policy on this page and updating the "Last Updated" date at the top of this
                        page.</p>
                    <p>We encourage you to review this Privacy Policy periodically for any changes. Changes to this
                        Privacy Policy are effective when they are posted on this page.</p>
                </section>

                <!-- Contact Us -->
                <section id="contact-us" class="privacy-section">
                    <h2>11. Contact Us</h2>
                    <p>If you have any questions about this Privacy Policy or our data practices, please contact us at:
                    </p>
                    <div class="contact-info">
                        <p><strong>Email:</strong> privacy@booksall.app</p>
                        <p><strong>Phone:</strong> +977 9841234567</p>
                        <p><strong>Address:</strong> Kathmandu, Nepal</p>
                    </div>
                    <p>We will respond to your inquiry within a reasonable timeframe.</p>
                </section>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const privacyAccepted = ref(false);

// Track open/closed state of collapsible sections
const openSections = reactive({
    personalInfo: false,
    futsalInfo: false,
    automaticInfo: false,
    serviceProvision: false,
    communications: false,
    analytics: false,
    legalCompliance: false,
    userSharing: false,
    serviceProviders: false,
    legalDisclosure: false,
    businessTransfers: false,
    cookieTypes: false,
    cookieControl: false
});

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

// Accept privacy policy and continue
const acceptPrivacy = () => {
    if (privacyAccepted.value) {
        // In a real app, you would store this acceptance
        // For demo purposes, we'll just go back to the add futsal page
        router.push('/add-futsal');
    }
};
</script>

<style scoped>
/* Privacy Policy Page Styles */
.privacy-page {
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
.privacy-header {
    text-align: center;
    margin-bottom: 30px;
}

.privacy-header h1 {
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

/* Introduction Banner */
.intro-banner {
    display: flex;
    gap: 20px;
    background-color: #e8f5e9;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 30px;
}

.intro-icon {
    display: flex;
    align-items: flex-start;
}

.intro-icon svg {
    width: 40px;
    height: 40px;
    color: #2e7d32;
}

.intro-content p {
    margin: 0 0 10px;
    font-size: 1rem;
    line-height: 1.6;
}

.intro-content p:last-child {
    margin-bottom: 0;
}

/* Quick Links */
.quick-links {
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    padding: 20px;
    margin-bottom: 30px;
}

.quick-links h2 {
    font-size: 1.25rem;
    font-weight: 700;
    color: #2e7d32;
    margin: 0 0 15px;
}

.links-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 15px;
}

.links-grid a {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 12px 15px;
    background-color: #f1f8e9;
    border-radius: 8px;
    color: #2e7d32;
    text-decoration: none;
    font-size: 0.95rem;
    font-weight: 500;
    transition: all 0.2s ease;
}

.links-grid a:hover {
    background-color: #e8f5e9;
    transform: translateY(-2px);
}

.links-grid a svg {
    width: 18px;
    height: 18px;
    color: #2e7d32;
}

/* Privacy Content */
.privacy-content {
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    padding: 30px;
    margin-bottom: 30px;
}

.privacy-section {
    margin-bottom: 40px;
    scroll-margin-top: 20px;
}

.privacy-section:last-child {
    margin-bottom: 0;
}

.privacy-section h2 {
    font-size: 1.5rem;
    font-weight: 700;
    color: #2e7d32;
    margin: 0 0 20px;
    padding-bottom: 10px;
    border-bottom: 1px solid #e0e0e0;
}

.privacy-section p {
    font-size: 0.95rem;
    line-height: 1.6;
    color: #333;
    margin: 0 0 15px;
}

.privacy-section ul {
    padding-left: 20px;
    margin: 0 0 15px;
}

.privacy-section li {
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

/* Info Callout */
.info-callout {
    padding: 15px;
    background-color: #e8f5e9;
    border-left: 4px solid #2e7d32;
    border-radius: 4px;
    margin: 15px 0;
}

.info-callout.warning {
    background-color: #fff8e1;
    border-left-color: #ffa000;
}

.info-callout p {
    margin: 0;
}

/* Security Measures */
.security-measures {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
    margin: 20px 0;
}

.security-item {
    display: flex;
    gap: 15px;
    padding: 15px;
    background-color: #f5f5f5;
    border-radius: 8px;
}

.security-icon {
    display: flex;
    align-items: flex-start;
}

.security-icon svg {
    width: 24px;
    height: 24px;
    color: #2e7d32;
}

.security-content h4 {
    font-size: 1rem;
    font-weight: 600;
    color: #333;
    margin: 0 0 5px;
}

.security-content p {
    font-size: 0.9rem;
    margin: 0;
}

/* Retention Details */
.retention-details {
    margin: 20px 0;
}

.retention-item {
    margin-bottom: 15px;
    padding-bottom: 15px;
    border-bottom: 1px solid #f0f0f0;
}

.retention-item:last-child {
    margin-bottom: 0;
    padding-bottom: 0;
    border-bottom: none;
}

.retention-item h4 {
    font-size: 1rem;
    font-weight: 600;
    color: #333;
    margin: 0 0 5px;
}

.retention-item p {
    margin: 0;
}

/* Rights Grid */
.rights-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
    margin: 20px 0;
}

.right-item {
    padding: 15px;
    background-color: #f5f5f5;
    border-radius: 8px;
}

.right-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    background-color: #e8f5e9;
    border-radius: 50%;
    margin-bottom: 10px;
}

.right-icon svg {
    width: 20px;
    height: 20px;
    color: #2e7d32;
}

.right-item h4 {
    font-size: 1rem;
    font-weight: 600;
    color: #333;
    margin: 0 0 5px;
}

.right-item p {
    font-size: 0.9rem;
    margin: 0;
}

/* Cookie Types */
.cookie-types {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 15px;
}

.cookie-type {
    padding: 15px;
    background-color: #f5f5f5;
    border-radius: 8px;
}

.cookie-type h4 {
    font-size: 1rem;
    font-weight: 600;
    color: #333;
    margin: 0 0 5px;
}

.cookie-type p {
    font-size: 0.9rem;
    margin: 0;
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

/* Privacy Acceptance */
.privacy-acceptance {
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
    .privacy-header h1 {
        font-size: 1.75rem;
    }

    .intro-banner {
        flex-direction: column;
        gap: 15px;
    }

    .privacy-content {
        padding: 20px;
    }

    .privacy-section h2 {
        font-size: 1.3rem;
    }

    .collapsible-header h3 {
        font-size: 1rem;
    }

    .security-measures,
    .rights-grid,
    .cookie-types {
        grid-template-columns: 1fr;
    }

    .privacy-acceptance {
        flex-direction: column;
        align-items: stretch;
    }

    .accept-button {
        align-self: stretch;
    }
}

@media (max-width: 480px) {
    .privacy-header h1 {
        font-size: 1.5rem;
    }

    .links-grid {
        grid-template-columns: 1fr;
    }

    .privacy-content {
        padding: 15px;
    }

    .collapsible-header {
        padding: 10px;
    }
}
</style>