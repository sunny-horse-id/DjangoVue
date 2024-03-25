<template>
  <div>
    <button @click="goToPage1">访问页面1</button>
    <button @click="goToPage2">访问页面2</button>
  </div>
</template>

<script setup>
  import { useRouter } from 'vue-router';

  const router = useRouter();

  const goToPage1 = () => {
    router.push({ name: 'Page', params: { id: 1 } });
  };

  const goToPage2 = () => {
    router.push({ name: 'Page', params: { id: 2 } });
  };
</script>


<style scoped>
/* 可选：添加样式 */
</style>
