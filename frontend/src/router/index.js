import { createRouter, createWebHistory } from 'vue-router'

//导入Vue组件
import MainVue from "@/views/MainVue.vue";
import AboutVue from "@/views/AboutVue.vue";
import ThreeVue from "@/views/ThreeVue.vue";
import UploadVue from "@/views/UploadVue.vue";
import Page from "@/views/Page.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
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
    { path: '/page/:id', name: 'Page', component: Page },
  ]
})

export default router