import { createRouter, createWebHistory } from 'vue-router'

//导入Vue组件
import MainVue from "@/views/MainVue.vue";
import AboutVue from "@/views/AboutVue.vue";
import ThreeVue from "@/views/ThreeVue.vue";
import UploadVue from "@/views/UploadVue.vue";
import TestVue from "@/views/TestVue.vue";
import IndexVue from "@/views/IndexVue.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      children: [
        {
          path: '',
          component: MainVue,
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
        {
          path: '/test',
          component: TestVue,
        },
        {
          path: '/index',
          component: IndexVue,
        }
      ],
    },
  ]
})

export default router