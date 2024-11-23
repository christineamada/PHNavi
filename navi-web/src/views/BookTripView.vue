<template>
  <div class="flex flex-row flex-wrap gap-3 w-full">
    <div
      class="w-full text-center p-4 bg-yellow-100 border border-yellow-400 rounded coming-soon"
    >
      <h1>Coming Soon</h1>
      <p>This page is about booking a trip. Stay tuned!</p>
      <p>🚧 We are working hard to bring this feature to you. 🚧</p>
      <p>🔨 Please check back later. 🔨</p>
    </div>
  </div>
</template>

<script lang="ts" setup></script>

<style scoped>
.coming-soon {
  text-align: center;
}

.coming-soon h1 {
  font-size: 2em;
  color: #333;
}

.coming-soon p {
  font-size: 1.2em;
  color: #666;
}
</style>
