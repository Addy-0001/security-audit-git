// Custom JavaScript for Futsal Booking System

document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Confirm before deleting/cancelling
    const confirmButtons = document.querySelectorAll('[data-confirm]');
    confirmButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            const message = this.getAttribute('data-confirm');
            if (!confirm(message)) {
                e.preventDefault();
            }
        });
    });

    // Add loading state to forms
    const forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(e) {
            const submitButton = this.querySelector('button[type="submit"]');
            if (submitButton && !submitButton.hasAttribute('data-no-loading')) {
                submitButton.disabled = true;
                const originalText = submitButton.innerHTML;
                submitButton.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Processing...';
                
                // Re-enable if form validation fails
                setTimeout(function() {
                    submitButton.disabled = false;
                    submitButton.innerHTML = originalText;
                }, 3000);
            }
        });
    });

    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href !== '#!') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // Add fade-in animation to cards
    const cards = document.querySelectorAll('.card');
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    cards.forEach(card => {
        observer.observe(card);
    });

    // Phone number formatting
    const phoneInputs = document.querySelectorAll('input[type="tel"], input[name="contact_number"]');
    phoneInputs.forEach(function(input) {
        input.addEventListener('input', function(e) {
            // Remove all non-numeric characters except +, -, (, ), and spaces
            let value = this.value.replace(/[^\d+\-\s()]/g, '');
            this.value = value;
        });
    });

    // Date input validation
    const dateInputs = document.querySelectorAll('input[type="date"]');
    dateInputs.forEach(function(input) {
        input.addEventListener('change', function() {
            const selectedDate = new Date(this.value);
            const today = new Date();
            today.setHours(0, 0, 0, 0);
            
            if (selectedDate < today) {
                alert('Please select a future date');
                this.value = '';
            }
        });
    });

    // Add current year to footer
    const yearElement = document.getElementById('current-year');
    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }

    // Prevent double form submission
    let isSubmitting = false;
    forms.forEach(function(form) {
        form.addEventListener('submit', function(e) {
            if (isSubmitting) {
                e.preventDefault();
                return false;
            }
            isSubmitting = true;
            
            // Reset after 3 seconds as a safety measure
            setTimeout(function() {
                isSubmitting = false;
            }, 3000);
        });
    });

    // Add loading indicator for AJAX requests
    window.showLoading = function(message = 'Loading...') {
        const loadingHtml = `
            <div class="position-fixed top-50 start-50 translate-middle" style="z-index: 9999;" id="loadingIndicator">
                <div class="spinner-border text-success" role="status">
                    <span class="visually-hidden">${message}</span>
                </div>
                <p class="mt-2 text-center">${message}</p>
            </div>
            <div class="position-fixed top-0 start-0 w-100 h-100 bg-dark opacity-50" style="z-index: 9998;" id="loadingOverlay"></div>
        `;
        document.body.insertAdjacentHTML('beforeend', loadingHtml);
    };

    window.hideLoading = function() {
        const indicator = document.getElementById('loadingIndicator');
        const overlay = document.getElementById('loadingOverlay');
        if (indicator) indicator.remove();
        if (overlay) overlay.remove();
    };

    // CSRF token for AJAX requests
    window.getCsrfToken = function() {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]');
        return csrfToken ? csrfToken.value : '';
    };

    // Utility function to format currency
    window.formatCurrency = function(amount) {
        return 'NPR ' + parseFloat(amount).toFixed(2);
    };

    // Utility function to format date
    window.formatDate = function(dateString) {
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        return new Date(dateString).toLocaleDateString('en-US', options);
    };

    // Console welcome message
    console.log('%cFutsal Booking System', 'color: #198754; font-size: 20px; font-weight: bold;');
    console.log('%cBuilt with Django & Bootstrap', 'color: #6c757d; font-size: 12px;');
});

// Service Worker registration (for PWA functionality - optional)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        // Uncomment to enable service worker
        // navigator.serviceWorker.register('/sw.js').then(function(registration) {
        //     console.log('ServiceWorker registration successful');
        // }, function(err) {
        //     console.log('ServiceWorker registration failed: ', err);
        // });
    });
}
