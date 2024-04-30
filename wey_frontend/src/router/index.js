import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'
import SearchView from '@/views/SearchView.vue'
import FeedView from '@/views/FeedView.vue'
import MessagesView from '@/views/MessagesView.vue'
import ProfilView from '@/views/ProfilView.vue'
import FriendsView from '@/views/FriendsView.vue'
import ChatView from '@/views/ChatView.vue'
import DiscussionView from '@/views/DiscussionView.vue'
import NotificationView from '@/views/NotificationView.vue'
import PostDetailsView from '@/views/PostDetailsView.vue'





const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // {
    //   path: '/',
    //   name: 'home',
    //   component: HomeView
    // },

    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },

    {
      path: '/messages',
      name: 'messages',
      component: MessagesView
    },

    {
      path: '/',
      name: 'feed',
      component: FeedView
    },

    {
      path: '/chat',
      name: 'chat',
      component: ChatView
    },
   
    {
      path: '/discussion/:id',
      name: 'discussion',
      component: DiscussionView
    },
  
    {
      // path: '/details/:id',
      path: '/details/:id?',
      name: 'details',
      component: PostDetailsView
    },

    {
      path: '/profil/:id',
      name: 'profil',
      component: ProfilView
    },

    {
      path: '/friends',
      name: 'friends',
      component: FriendsView
    },


    {
      path: '/login',
      name: 'login',
      component: LoginView
    },

    {
      path: '/notification',
      name: 'notification',
      component: NotificationView
    },
    

    {
      path: '/search/:keyword',
      name: 'search',
      component: SearchView
    },

    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')   
    },
  ]
})

export default router
