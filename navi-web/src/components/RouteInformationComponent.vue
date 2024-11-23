<template>
  <Card>
    <template #title>Route Information</template>
    <template #content>
      <div class="flex flex-col gap-2">
        <p>
          <i class="pi pi-map mr-1" style="font-size: 1.25rem"></i>Distance:
          {{ adjustedDistance }}
        </p>
        <p>
          <i class="pi pi-money-bill mr-1" style="font-size: 1.25rem"></i
          >Estimated Fare: ₱{{ adjustedFare }}
        </p>
        <p>
          <i class="pi pi-clock mr-1" style="font-size: 1.25rem"></i>Duration:
          {{ adjustedDuration }}
        </p>
      </div>
    </template>
    <template #footer>
      <div>
        <p class="mb-3">Journey at {{ percentageOfJourney }}%</p>
        <Slider v-model="percentageOfJourney" :step="10" class="w-56" />
      </div>
    </template>
  </Card>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue';
import type { RouteInformation } from './MapComponent.vue';

const props = defineProps<{
  route: RouteInformation | null;
}>();

const percentageOfJourney = ref<number>(100);

const extractNumber = (value: string) => {
  const match = value.match(/[\d.]+/);
  return match ? parseFloat(match[0]) : 0;
};

// Adjusted distance calculation
const adjustedDistance = computed(() => {
  return props.route
    ? (
        (extractNumber(props.route.distance) * percentageOfJourney.value) /
        100
      ).toFixed(2) + ' km'
    : 'N/A';
});

// Adjusted fare calculation
const adjustedFare = computed(() => {
  if (!props.route) {
    return 'N/A';
  }

  const distanceInKm = extractNumber(props.route.distance);
  const isRideWithAircon = props.route.isRideWithAircon ?? false;
  const passengerType = props.route.passengerType ?? 'regular';

  // Fare calculation
  const farePerKm = isRideWithAircon ? 2.3 : 1.9;
  let totalFare = Math.ceil(distanceInKm * farePerKm * 100) / 100; // Match `RouteList` precision and rounding

  // Apply discount
  let discountRate = 0;
  if (passengerType === 'senior' || passengerType === 'student') {
    discountRate = 0.3;
  }

  totalFare *= 1 - discountRate;

  // Adjust based on the percentage of the journey
  return ((totalFare * percentageOfJourney.value) / 100).toFixed(0);
});

// Adjusted duration calculation
const adjustedDuration = computed(() => {
  if (!props.route) {
    return 'N/A';
  }

  const distanceInKm = extractNumber(props.route.distance);
  const isRideWithAircon = props.route.isRideWithAircon ?? false;

  // Duration calculation
  const speedKmPerHour = isRideWithAircon ? 55 : 50; // Adjusted for aircon
  const fullDurationInHours = distanceInKm / speedKmPerHour;
  const adjustedDurationInMinutes = (fullDurationInHours * 60 * percentageOfJourney.value) / 100;

  const hours = Math.floor(adjustedDurationInMinutes / 60);
  const minutes = adjustedDurationInMinutes % 60;

  if (hours > 0) {
    return `${hours}h ${minutes.toFixed(0)}m`;
  } else {
    return `${minutes.toFixed(0)} mins`;
  }
});
</script>