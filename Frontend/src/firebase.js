// src/firebase.js
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getMessaging } from "firebase/messaging";

// Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyCrEq8RvWyCCa8dLfmuCR_9ViF_DivkR7g",
    authDomain: "booksall-a0fb3.firebaseapp.com",
    projectId: "booksall-a0fb3",
    storageBucket: "booksall-a0fb3.firebasestorage.app",
    messagingSenderId: "913686080361",
    appId: "1:913686080361:web:6f7da9ddbf85bd5d6a6bf8",
    measurementId: "G-8YNY2VPXV0"
};

// VAPID key
const vapidPublicKey = "BETWsJJTRfAxDFkHSM7mxlg4X8T7AZiAPjc807WUvyCkISDQmCJaPZXuWOQ_NZyDZeb_ZlJgqObS_WpaSkkclWM";

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const messaging = getMessaging(app);

export { app, analytics, messaging, vapidPublicKey };