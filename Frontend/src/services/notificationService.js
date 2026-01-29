import { messaging, vapidPublicKey } from '@/firebase';
import { getToken, onMessage } from 'firebase/messaging';
import axios from 'axios';

const API_URL = 'https://apibooksal.getintoto.com/api/v1/';

export const notificationService = {
    // Request permission and get/save FCM token
    async initializeNotifications() {
        try {
            // Request permission
            const permission = await Notification.requestPermission();
            if (permission !== 'granted') {
                console.warn('Notification permission denied');
                return null;
            }

            // Get FCM token
            const token = await getToken(messaging, { vapidKey: vapidPublicKey });
            console.log('FCM token:', token);

            // Send token to Django backend
            const response = await axios.post(
                `${API_URL}user/update-fcm-token/`,
                { fcm_token: token },
                {
                    headers: {
                        Authorization: `Token ${localStorage.getItem('token')}`
                    }
                }
            );
            console.log('Token saved:', response.data);
            return token;
        } catch (error) {
            console.error('Error initializing notifications:', error);
            return null;
        }
    },

    // Handle foreground notifications
    setupForegroundNotifications() {
        onMessage(messaging, (payload) => {
            console.log('Foreground notification:', payload);
            const { title, body } = payload.notification || {};
            if (title && body) {
                // Show browser notification
                new Notification(title, {
                    body,
                    icon: '/favicon.ico' // Customize as needed
                });
            }
        });
    }
};