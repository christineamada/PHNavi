<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import { GoogleMap, Marker } from 'vue3-google-map'
import { GOOGLE_MAPS_API_KEY, GOOGLE_MAPS_ID } from '@/config'
import RoutesListComponent from '@/components/RoutesListComponent.vue'
import type { LatLng } from '@/interfaces'
import InformationBox from './shared/InformationBox.vue'
import RouteInformationComponent from './RouteInformationComponent.vue'


type CalculateRouteInput = {
  to: LatLng
  from: LatLng
}


export type RouteInformation = {
  distance: string
  duration: string
  fare: number
  summary: string
}


const mapAPIKey = GOOGLE_MAPS_API_KEY
const mapId = GOOGLE_MAPS_ID
const center = ref<google.maps.LatLngLiteral | null>(null)
const mapRef = ref<InstanceType<typeof GoogleMap> | null>(null)
const directionsRenderer = ref<google.maps.DirectionsRenderer | null>(null)
const mapInstance = ref<google.maps.Map | null>(null)
const dumagueteCoords: google.maps.LatLngLiteral = {
  lat: 9.3068,
  lng: 123.3054,
}
const isRouteChosen = ref(false)
const currentRouteInformation = ref<RouteInformation | null>(null)
const selectedLocation = ref<LatLng | null>(null)


const clearRoute = () => {
  if (directionsRenderer.value) {
    directionsRenderer.value.setMap(null)
    isRouteChosen.value = false
  }
}


const getCurrentLocation = () => {
  navigator.geolocation.getCurrentPosition(
    (position: GeolocationPosition) => {
      const pos: google.maps.LatLngLiteral = {
        lat: position.coords.latitude,
        lng: position.coords.longitude,
      }
      center.value = pos
      if (mapInstance.value) {
        mapInstance.value.setCenter(pos)
      }
    },
    () => {
      // If unable to get current location, default to Dumaguete
      center.value = dumagueteCoords
    }
  )
}


const calculateRoute = (
  input: CalculateRouteInput,
  isRideWithAircon: boolean,
) => {
  console.log('Calculating route...')
  console.log('Getting input:', input)
  if (!mapInstance.value) {
    alert('Map is not ready yet')
    return
  }


  // Clear previous directions
  if (directionsRenderer.value) {
    directionsRenderer.value.setMap(null)
    isRouteChosen.value = false
  }


  isRouteChosen.value = true


  const request = {
    origin: input.from,
    destination: input.to,
    travelMode: google.maps.TravelMode.DRIVING,
  }


  const directionsService = new google.maps.DirectionsService()
  directionsRenderer.value = new google.maps.DirectionsRenderer()
  directionsRenderer.value.setMap(mapInstance.value)


  directionsService.route(request, (response, status) => {
    if (status === google.maps.DirectionsStatus.OK) {
      if (directionsRenderer.value && response) {
        directionsRenderer.value.setDirections(response)
        isRouteChosen.value = true


        // Extract route information
        const route = response.routes[0]
        console.log('Route:', route)
        const leg = route.legs[0]
        const distance = leg.distance?.text || 'N/A'
        const duration = leg.duration?.text || 'N/A'
        const fare = calculateFare(leg.distance?.value || 0, isRideWithAircon)
        const summary = route.summary || 'N/A'
        currentRouteInformation.value = {
          distance,
          duration,
          fare,
          summary,
        }
        console.log(`Distance: ${distance}`)
        console.log(`Duration: ${duration}`)
        console.log(`Estimated Fare: ${fare}`)
      }
    } else {
      alert('Directions request failed, status=' + status)
    }
  })
}


const calculateFare = (
  distanceInMeters: number,
  isRideWithAircon: boolean,
): number => {
  const farePerKm = isRideWithAircon ? 2.3 : 1.9;
  const baseFare = isRideWithAircon ? 40 : 30;
  const distanceInKm = distanceInMeters / 1000;


  let totalFare = baseFare + farePerKm * distanceInKm;


  // Apply discount for long distances
  const discountThresholdKm = 500;
  const discountRate = 0.1; // 10% discount


  if (distanceInKm > discountThresholdKm) {
    totalFare -= totalFare * discountRate;
  }


  return totalFare;
}


const handleMapClick = (event: google.maps.MapMouseEvent) => {
  if (event.latLng) {
    const clickedLocation: LatLng = {
      lat: event.latLng.lat(),
      lng: event.latLng.lng(),
    }
    selectedLocation.value = clickedLocation
    center.value = clickedLocation
  }
}


onMounted(() => {
  center.value = dumagueteCoords // Set a default value initially
  getCurrentLocation()
})


watch(
  () => mapRef.value?.ready,
  ready => {
    if (ready && mapRef.value?.map) {
      mapInstance.value = mapRef.value.map;

      // Ensure mapInstance is defined before using it
      if (mapInstance.value) {
        mapInstance.value.addListener('click', handleMapClick);

        // Set center if center has a valid value
        if (center.value) {
          mapInstance.value.setCenter(center.value);
        }
      }
    }
  },
);
</script>


<template>
  <div style="position: relative; width: 100%; height: 91.5vh">
    <GoogleMap
      ref="mapRef"
      :api-key="mapAPIKey"
      :map-id="mapId"
      style="width: 100%; height: 100%"
      :center="center || dumagueteCoords"
      :zoom="15"
      :clickable-icons="false"
      :disable-double-click-zoom="true"
      :map-type-control="false"
      :fullscreen-control="false"
      :street-view-control="false"
      :keyboard-shortcuts="false"
      :min-zoom="12"
      :zoom-control="false"
    >
      <Marker
        v-if="!isRouteChosen && center"
        :options="{
          position: center || dumagueteCoords, // Provide fallback value
        }"
      />
    </GoogleMap>
    <div
      style="
        position: absolute;
        top: 10px;
        left: 10px;
        z-index: 1;
        width: 300px;
      "
    >
      <div class="flex flex-col gap-2">
        <InformationBox class="w-full" />
        <RouteInformationComponent
          v-show="isRouteChosen"
          :route="currentRouteInformation"
        />
      </div>
    </div>
    <div
      class="flex flex-col gap-2"
      style="position: absolute; top: 10px; right: 10px; z-index: 1"
    >
      <RoutesListComponent
        :selected-location="selectedLocation"
        @route-selected="calculateRoute($event, $event.isRideWithAircon)"
      />
      <div class="flex flex-row-reverse gap-2">
        <Button
          @click="getCurrentLocation"
          icon="pi pi-map-marker"
          iconPos="right"
          class="fixed-height"
          severity="danger"
        />
        <Button
          v-if="isRouteChosen"
          @click="clearRoute"
          label="Clear Route"
          icon="pi pi-times"
          iconPos="right"
          class="fixed-height"
          severity="warn"
        />
      </div>
    </div>
  </div>
</template>
