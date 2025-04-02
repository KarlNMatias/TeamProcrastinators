import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue'; // Ensure this file exists

const routes = [
  { path: '/', component: Home },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

