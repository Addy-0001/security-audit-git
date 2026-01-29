import axios from 'axios';
import { format } from 'date-fns';


const apiClient = axios.create({
    baseURL: 'https://apibooksal.getintoto.com/api/v1/',
    withCredentials: true, // Make sure the cookies are sent with the request
});

// Add token to each request if it's available
apiClient.interceptors.request.use(config => {
    const token = localStorage.getItem('token');
    if (token) {
        config.headers['Authorization'] = `Token ${token}`;
    }
    return config;
}, error => Promise.reject(error));

export default apiClient;
