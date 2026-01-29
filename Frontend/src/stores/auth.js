import { defineStore } from 'pinia';
import apiClient from '@/axios'; // Import your custom axios instance

export const useAuthStore = defineStore('auth', {
    state: () => ({
        isLoggedIn: !!localStorage.getItem('token')
    }),
    actions: {
        login(token) {
            localStorage.setItem('token', token);
            this.isLoggedIn = true;
        },
        logout() {
            localStorage.removeItem('token');
            this.isLoggedIn = false;
        },
        checkAuth() {
            this.isLoggedIn = !!localStorage.getItem('token');
        },
        async verifyAuth() {
            const token = localStorage.getItem('token');
            if (!token) {
                this.isLoggedIn = false;
                return;
            }

            try {
                const response = await apiClient.get('auth/user/');
                this.isLoggedIn = true;
                return response.data;
            } catch (error) {
                this.logout();
                throw error;
            }
        }
    }
});