import { createRouter, createWebHistory } from 'vue-router'

//导入Vue组件
import IndexView from "@/views/IndexView.vue";
import AboutView from "@/views/AboutView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: IndexView,
    },
    {
      path: '/about',
      component: AboutView,
    },
  ]
})

export default router