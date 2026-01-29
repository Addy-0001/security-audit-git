import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import FutsalList from '@/views/FutsalList.vue'
import FutsalDetailView from '@/views/FutsalDetailView.vue'
import BookFutsalView from '@/views/BookFutsalView.vue'
import LoginView from '@/views/Auth/LoginView.vue'
import RegisterView from '@/views/Auth/RegisterView.vue'
import ProfileView from '@/views/Auth/ProfileView.vue'
import AddFutsal from '@/views/FutsalAdmin/AddFutsal.vue'
import EditProfileView from '@/views/Auth/EditProfileView.vue'
import CreateProfileView from '@/views/Auth/CreateProfileView.vue'
import EditFutsal from '@/views/FutsalAdmin/EditFutsal.vue'
import FutsalStats from '@/views/FutsalAdmin/FutsalStats.vue'
import TermsAndConditions from '@/views/TermsAndConditions.vue'
import PrivacyPolicy from '@/views/PrivacyPolicy.vue'
import Bookings from '@/views/Auth/Bookings.vue'
import Blog from '@/views/Blog/Blog.vue'
import BlogView from '@/views/Blog/BlogView.vue'
import RegularBookings from '@/views/FutsalAdmin/RegularBookings.vue'
import NotFoundView from '@/views/NotFoundView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/futsals',
      name: 'futsals',
      component: FutsalList
    },
    {
      path: '/futsals/:id',
      name: 'futsalDetails',
      component: FutsalDetailView
    },
    {
      path: '/futsals/:id/book',
      name: 'book-futsal',
      component: BookFutsalView,
      props: true,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      meta: {
        requiresGuest: true,
      }
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView,
      meta: {
        requiresGuest: true,
      }
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/bookings',
      name: 'bookings',
      component: Bookings,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/profile/create',
      name: 'create-profile',
      component: CreateProfileView,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/add-futsal',
      name: 'add-futsal',
      component: AddFutsal,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/futsal/:id/stats',
      name: 'futsal-stats',
      component: FutsalStats,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/futsal/:id/add-regular-booking',
      name: 'add-regular-booking',
      component: RegularBookings,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/blog',
      name: 'blog',
      component: Blog,

    },
    {
      path: '/blog/:blogid',
      name: 'blog-detail',
      component: BlogView
    },
    {
      path: '/futsal/:id/edit',
      name: 'edit-futsal',
      component: EditFutsal,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/profile/edit',
      name: 'profile-edit',
      component: EditProfileView,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/terms',
      name: 'terms',
      component: TermsAndConditions,
    },
    {
      path: '/privacy-policy',
      name: 'privacy-policy',
      component: PrivacyPolicy
    },
    {
      path: '/:notFound',
      name: 'notFound',
      component: NotFoundView
    }
  ],
  scrollBehavior(to, from, savedPosition) {
    // Always scroll to top
    return { top: 0 }
  }
})


function checkIfAuthenticated() {
  const store = localStorage.getItem('token')
  if (!store) {
    return false;
  } else {
    return true
  }
}

// Navigation Guard
router.beforeEach((to, from, next) => {
  const isAuthenticated = checkIfAuthenticated();

  // Redirect unauthenticated users trying to access protected routes
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login');
  }
  // Prevent authenticated users from accessing Sign In or Sign Up
  else if (to.meta.requiresGuest && isAuthenticated) {
    next('/profile');
  }
  else {
    next();
  }
});
export default router
