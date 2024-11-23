<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

const items = [
  {
    label: 'Map',
    icon: 'pi pi-map',
    command: () => {
      router.push('/map')
    },
  },
  {
    label: 'Schedules',
    icon: 'pi pi-map',
    command: () => {
      router.push('/schedules')
    },
  },
  {
    label: 'Feedback',
    icon: 'pi pi-comments',
    command: () => {
      router.push('/feedback')
    },
  },
  {
    label: 'Admin Login',
    icon: 'pi pi-lock',
    url: 'http://localhost:8000/admin',
  },
]
</script>

<template>
  <Menubar :model="items" class="rounded-none border-0">
    <template #start>
      <RouterLink to="/">
        <Button text class="logo-button">
          <Image
            src="/src/assets/images/logo.png"
            alt="Image"
            width="32"
            height="32"
          />
        </Button>
      </RouterLink>
    </template>
  </Menubar>
</template>
