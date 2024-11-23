<template>
  <Card class="w-[400px]" v-auto-animate>
    <template #title>
      <h2>Routes List</h2>
    </template>
    <template #content>
      <div class="flex flex-col gap-3">
        <!-- Origin Input -->
        <MapSearchBarComponent
          v-model="selectedOrigin"
          placeholder="Enter your origin"
        />
        <!-- Destination Input -->
        <MapSearchBarComponent
          v-model="selectedDestination"
          placeholder="Enter your destination"
        />
        <!-- Air-conditioned Checkbox & Passenger Type Selection -->
        <div class="flex flex-row gap-4 items-center">
          <Checkbox
            v-model="isRideWithAircon"
            inputId="rideWithAircon"
            name="rideWithAircon"
            binary
            label="Ride with aircon"
          />
          <label for="rideWithAircon" class="ml-2">Ride with aircon</label>

          <label for="passengerType" class="ml-4">Passenger Type:</label>
          <select v-model="passengerType" id="passengerType">
            <option value="regular">Regular</option>
            <option value="senior">Senior Citizen</option>
            <option value="student">Student</option>
          </select>
        </div>
        <!-- Button to Fetch Routes -->
        <Button
          label="Fetch routes"
          icon="pi pi-search"
          iconPos="right"
          @click="handleFetchRoutesClick"
        />
        <!-- Display Fetched Routes -->
        <div class="flex flex-col gap-2">
          <DataTable :value="routes" class="p-datatable-sm">
            <Column field="from_location" header="From" />
            <Column field="to_location" header="To" />
            <Column field="fare" header="Estimated Fare (₱)" />
            <Column field="duration" header="Estimated Duration (mins)" />
          </DataTable>
          <!-- Link to Schedule Page -->
          <RouterLink to="/schedules">
            <Button
              label="See schedule"
              icon="pi pi-arrow-right"
              iconPos="right"
            />
          </RouterLink>
        </div>
      </div>
    </template>
  </Card>
</template>

<script setup lang="ts">
import { ref, onMounted, defineEmits } from 'vue'
import MapSearchBarComponent from './MapSearchBarComponent.vue'
import { getDirections, getPlaceDetails, findNearbyPlaces } from '@/services/googleMapsServices'
import { BACKEND_API_URL } from '@/config'
import axios from 'axios'
import type { IRoute } from '@/interfaces'

const emit = defineEmits(['routeSelected'])

interface BusStation {
  name: string
  address: string
  location: {
    lat: number
    lng: number
  }
}

// State Variables
const busStations = ref<BusStation[]>([])
const selectedOrigin = ref<Record<string, any> | undefined>(undefined)
const selectedDestination = ref<Record<string, any> | undefined>(undefined)
const routesOnMap = ref<any[]>([])
const bestRoute = ref<any | undefined>(undefined)
const routes = ref<IRoute[]>([])
const isRideWithAircon = ref(false)
const passengerType = ref('regular') // Default is 'regular'

// Function to calculate fare based on passenger type and aircon option
const calculateFare = (distanceInMeters: number, isRideWithAircon: boolean, passengerType: string): number => {
  // Fare rates
  const farePerKm = isRideWithAircon ? 2.3 : 1.9
  const distanceInKm = distanceInMeters / 1000

  // Calculate base fare
  let totalFare = distanceInKm * farePerKm

  // Apply discount based on passenger type
  let discountRate = 0
  if (passengerType === 'senior' || passengerType === 'student') {
    discountRate = 0.3 // 30% discount for senior citizens and students
  }

  totalFare = totalFare * (1 - discountRate)

  // Return fare rounded to two decimal places
  return parseFloat(totalFare.toFixed(0))
}

// Function to calculate duration based on aircon option
const calculateDuration = (distanceInMeters: number, isRideWithAircon: boolean): number => {
  const distanceInKm = distanceInMeters / 1000
  const speedKmPerHour = isRideWithAircon ? 55 : 50 // Speed for aircon vs non-aircon
  const durationInHours = distanceInKm / speedKmPerHour

  return parseFloat((durationInHours * 60).toFixed(2)) // Convert hours to minutes
}

// Fetch Routes and Apply Calculations
const fetchRoutes = async () => {
  if (!selectedOrigin.value || !selectedDestination.value) {
    console.error('Both origin and destination must be selected')
    return
  }
  const { lat: originLat, lng: originLng } = selectedOrigin.value.coordinates
  const { lat: destLat, lng: destLng } = selectedDestination.value.coordinates
  const origin = `${originLat},${originLng}`
  const destination = `${destLat},${destLng}`

  try {
    const data = await getDirections(origin, destination)
    routesOnMap.value = data.routes
    if (data.routes.length > 0) {
      bestRoute.value = data.routes[0].summary
    }
    // Process the routes to add fare and duration information
    routes.value = data.routes.map((route: any) => {
      const distanceInMeters = route.legs[0].distance.value
      const fare = calculateFare(distanceInMeters, isRideWithAircon.value, passengerType.value)
      const duration = calculateDuration(distanceInMeters, isRideWithAircon.value)

      return {
        from_location: selectedOrigin.value?.address ?? 'Unknown',
        to_location: selectedDestination.value?.address ?? 'Unknown',
        fare,
        duration,
      }
    })
    emit('routeSelected', {
      to: {
        lat: destLat,
        lng: destLng,
      },
      from: {
        lat: originLat,
        lng: originLng,
      },
      routes: routes.value, // Emit routes for route information
    })
  } catch (error) {
    console.error('Error fetching routes:', error)
  }
}

// Handle Fetch Routes Click Event
const handleFetchRoutesClick = () => {
  fetchRoutes()
}

// Fetch Bus Stations (example function)
const fetchBusStations = async () => {
  const query = 'Ceres Bus Terminal'
  try {
    const data = await findNearbyPlaces('bus_station', query)
    busStations.value = await Promise.all(
      data.results.map(async (result: any) => {
        const placeDetails = await getPlaceDetails(result.place_id)
        return {
          name: `${placeDetails.result.name} - ${placeDetails.result.vicinity}`,
          address: placeDetails.result.vicinity,
          location: {
            lat: placeDetails.result.geometry.location.lat,
            lng: placeDetails.result.geometry.location.lng,
          },
        }
      }),
    )
  } catch (error) {
    console.error('Error fetching bus stations:', error)
  }
}

// Run on Component Mount
onMounted(() => {
  fetchBusStations()
  fetchRoutesFromApi()
})

// Fetch Routes from API (example function)
const fetchRoutesFromApi = async () => {
  try {
    const response = await axios.get(`${BACKEND_API_URL}/api/routes/route-list`)
    routes.value = response.data.map((route: any) => ({
      ...route,
      to: {
        lat: route.to_coords.lat,
        lng: route.to_coords.lng,
      },
      from: {
        lat: route.from_coords.lat,
        lng: route.from_coords.lng,
      },
    }))
  } catch (err) {
    console.error('Error fetching routes from API', err)
  }
}
</script>