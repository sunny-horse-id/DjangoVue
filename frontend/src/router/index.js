import { createRouter, createWebHistory } from 'vue-router'

//导入Vue组件
import IndexView from "@/views/IndexVue.vue";
import AboutView from "@/views/AboutVue.vue";
import ThreeVue from "@/views/ThreeVue.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      children: [
        {
          path: '/',
          component: IndexView,
        },
        {
          path: '/about',
          component: AboutView,
        },
        {
          path: '/three',
          component: ThreeVue,
        },
      ],
    },
  ]
})

export default router