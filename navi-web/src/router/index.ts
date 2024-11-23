import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import OperatorsView from '@/views/OperatorsView.vue'
import FeedbackView from '@/views/FeedbackView.vue'
import BookTripView from '../views/BookTripView.vue'
import SchedulesView from '@/views/SchedulesView.vue'
import MapComponent from '@/components/MapComponent.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/map',
    name: 'map',
    component: MapComponent,
  },
  {
    path: '/operators',
    name: 'operators',
    component: OperatorsView,
  },
  {
    path: '/schedules',
    name: 'schedules',
    component: SchedulesView,
  },
  {
    path: '/book-trip',
    name: 'book-trip',
    component: BookTripView,
  },
  {
    path: '/feedback',
    name: 'feedback',
    component: FeedbackView,
  },
]
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
