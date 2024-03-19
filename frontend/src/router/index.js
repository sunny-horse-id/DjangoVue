import { createRouter, createWebHistory } from 'vue-router'

//导入Vue组件
import IndexVue from "@/views/IndexVue.vue";
import AboutVue from "@/views/AboutVue.vue";
import ThreeVue from "@/views/ThreeVue.vue";
import UploadVue from "@/views/UploadVue.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      children: [
        {
          path: '',
          component: IndexVue,
        },
        {
          path: '/about',
          component: AboutVue,
        },
        {
          path: '/three',
          component: ThreeVue,
        },
        {
          path: '/upload',
          component: UploadVue,
        },
      ],
    },
  ]
})

export default router