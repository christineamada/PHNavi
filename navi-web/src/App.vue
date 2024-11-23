<script lang="ts" setup>
import { RouterLink, RouterView, useRoute } from 'vue-router'
import NavBar from '@/components/Navbar.vue'
import { computed } from 'vue'

const route = useRoute()
const isHomeRoute = computed(() => route.path === '/')
const isMapRoute = computed(() => route.path === '/map')
</script>

<template>
  <NavBar />
  <div>
    <main
      :class="{
        'm-8': !isHomeRoute && !isMapRoute,
        'flex flex-col items-center justify-center': isHomeRoute,
      }"
    >
      <RouterView />
    </main>
  </div>
  <footer
    v-if="isHomeRoute"
    class="fixed bottom-0 w-full text-center p-4 bg-gray-800 text-white"
  >
    Created with ❤️ by the BASS Team
  </footer>
</template>

<style>
body {
  background-image: url('@/assets/images/background.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  height: 100vh;
  margin: 0;
  padding: 0;
}
</style>
