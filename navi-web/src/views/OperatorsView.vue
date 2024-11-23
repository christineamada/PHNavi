<template>
  <div class="flex flex-row flex-wrap gap-3 w-full justify-center">
    <div
      class="w-full text-center p-4 bg-yellow-100 border border-yellow-400 rounded"
    >
      🚧 This page is still under construction 🚧
      <p>
        A possible feature of this page will be to fetch all nearby transits in
        your area, so the content will always change depending on your location.
      </p>
    </div>
    <Card
      v-for="operator in operators"
      :key="operator.companyName"
      class="w-[300px] h-[150px]"
    >
      <template #title>{{ operator.companyName }}</template>
      <template #content>
        <p>Vehicle Type: {{ getVehicleType(operator.vehicleType) }}</p>
        <p>
          Website:
          <a :href="operator.website" />
        </p>
      </template>
    </Card>
    <PlaceHolderComponent v-for="i in 5" :key="i" class="w-[300px] h-[150px]" />
  </div>
</template>

<script setup lang="ts">
import PlaceHolderComponent from '@/components/shared/PlaceholderComponent.vue'
import { ref } from 'vue'

enum VehicleTypes {
  BUS = 'Bus',
  FERRY = 'Ferry',
}

const getVehicleType = (type: VehicleTypes): string => {
  switch (type) {
    case VehicleTypes.BUS:
      return 'Bus'
    case VehicleTypes.FERRY:
      return 'Ferry'
    default:
      return 'UNKNOWN'
  }
}

type Operators = {
  companyName: string
  vehicleType: VehicleTypes
  website: string
}

const operators = ref<Operators[]>([
  {
    companyName: 'Ceres',
    vehicleType: VehicleTypes.BUS,
    website: 'https://ceresliner.com/',
  },
  {
    companyName: 'Montenegro',
    vehicleType: VehicleTypes.FERRY,
    website: 'https://montenegrolines.com.ph/landing.php',
  },
])
</script>
