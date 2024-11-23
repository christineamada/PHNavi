<template>
  <div class="flex flex-col gap-2">
    <div class="flex flex-row gap-2">
      <h1 class="text-2xl font-bold text-white">Select Transporation:</h1>
      <TransportationDropdown v-model="selectedTransportationType" />
    </div>
    <div>
      <div v-if="selectedTransportationType == transportationTypes.Bus">
        <DataTable
          :value="busSchedulesOptions"
          stripedRows
          showGridlines
          sortable
          :paginator="true"
          :rows="10"
        >
          <template #header>
            <div class="flex flex-wrap items-center justify-between gap-2">
              <span class="text-xl font-bold">Bus Schedules</span>
              <div class="flex gap-2">
                <Dropdown placeholder="Company" :options="uniqueBusCompanies" />
                <InputText
                  v-model="fromLocationSearch"
                  placeholder="Type from location..."
                  class="p-inputtext-sm"
                />
                <InputText
                  v-model="toLocationSearch"
                  placeholder="Type destination..."
                  class="p-inputtext-sm"
                />
                <Button
                  icon="pi pi-refresh"
                  rounded
                  raised
                  @click="fetchBusSchedules"
                />
              </div>
            </div>
          </template>
          <Column field="company_name" header="Company"></Column>
          <Column field="route" header="Route"></Column>
          <Column field="departure_time" header="Departure Time"></Column>
          <Column field="arrival_time" header="Arrival Time"></Column>
          <Column field="travel_days" header="Travel Days"></Column>
          <Column field="fare" header="Fare"></Column>
        </DataTable>
      </div>
      <div v-else>
        <DataTable
          :value="ferrySchedulesOptions"
          stripedRows
          showGridlines
          sortable
          :paginator="true"
          :rows="10"
        >
          <template #header>
            <div class="flex flex-wrap items-center justify-between gap-2">
              <span class="text-xl font-bold">Ferry Schedules</span>
              <div class="flex gap-2">
                <Dropdown
                  placeholder="Company"
                  :options="uniqueFerryCompanies"
                  v-model="selectedCompany"
                />
                <InputText
                  v-model="fromLocationSearch"
                  placeholder="Type from location..."
                  class="p-inputtext-sm"
                />
                <InputText
                  v-model="toLocationSearch"
                  placeholder="Type destination..."
                  class="p-inputtext-sm"
                />
                <Button
                  icon="pi pi-refresh"
                  rounded
                  raised
                  @click="fetchFerrySchedules"
                />
              </div>
            </div>
          </template>
          <Column field="company_name" header="Company"></Column>
          <Column field="route" header="Route"></Column>
          <Column field="vessel" header="Vessel Name"></Column>
          <Column field="departure_time" header="Departure Time"></Column>
          <Column field="arrival_time" header="Arrival Time"></Column>
          <Column field="day_of_departure" header="Day of Departure"></Column>
          <Column field="day_of_arrival" header="Day of Arrival"></Column>
          <Column field="fare" header="Fare"></Column>
        </DataTable>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, watch } from 'vue'
import { BACKEND_API_URL } from '@/config'
import axios from 'axios'
import type { ISchedule } from '@/interfaces'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import InputText from 'primevue/inputtext'
import Button from 'primevue/button'
import TransportationTypes from '@/enums/transportationTypes'
import { uniq } from '@vueuse/core/metadata.cjs'

const loading = ref(true)
const error = ref('')
let busSchedules: ISchedule[] = []
const busSchedulesOptions = ref<ISchedule[]>([])
let ferrySchedules: ISchedule[] = []
const ferrySchedulesOptions = ref<ISchedule[]>([])
const searchQuery = ref('')
const transportationTypes = TransportationTypes
const selectedTransportationType = ref(transportationTypes.Bus)
const selectedCompany = ref('')
const uniqueBusCompanies = ref<string[]>([])
const uniqueFerryCompanies = ref<string[]>([])

// form
const toLocationSearch = ref('')
const fromLocationSearch = ref('')

const daysOfWeek = [
  'Monday',
  'Tuesday',
  'Wednesday',
  'Thursday',
  'Friday',
  'Saturday',
  'Sunday',
]

const convertDaysString = (daysString: string): string => {
  if (!daysString) {
    return 'TBA'
  }
  const daysArray = daysString
    .split(',')
    .map(day => day.trim())
    .map(Number)
  const daysNames = daysArray.map(day => daysOfWeek[day - 1])
  return daysNames.join(', ')
}

const titleCaseString = (str: string): string =>
  str
    .split(' ')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join(' ')

const fetchBusSchedules = async () => {
  loading.value = true
  try {
    const response = await axios.get(
      `${BACKEND_API_URL}/api/schedules/bus-schedules/`,
    )
    console.log(response.data)
    busSchedules = response.data.map((schedule: ISchedule) => ({
      ...schedule,
      company_name: titleCaseString(schedule.company_name),
      route: `${titleCaseString(schedule.from_location)} → ${titleCaseString(
        schedule.to_location,
      )}`,
      fare: `₱${schedule.fare.toLocaleString()}`,
      travel_days: convertDaysString(schedule.travel_days),
    }))
    busSchedulesOptions.value = busSchedules
  } catch (err) {
    error.value = 'Failed to fetch schedules'
  } finally {
    setTimeout(() => {
      loading.value = false
    }, 1000) // 1 second delay
  }
}

const fetchFerrySchedules = async () => {
  console.log('Fetching ferry schedules...')
  loading.value = true
  try {
    const response = await axios.get(
      `${BACKEND_API_URL}/api/schedules/ferry-schedules/`,
    )
    console.log(response.data)
    ferrySchedules = response.data.map((schedule: ISchedule) => {
      try {
        return {
          ...schedule,
          company_name: titleCaseString(schedule.company_name),
          route: `${titleCaseString(schedule.from_location)} → ${titleCaseString(
            schedule.to_location,
          )}`,
          day_of_departure: convertDaysString(schedule.day_of_departure ?? ' '),
          day_of_arrival: convertDaysString(schedule.day_of_arrival ?? ' '),
          fare: `₱${schedule.fare.toLocaleString()}`,
          travel_days: convertDaysString(schedule.travel_days),
        }
      } catch (error) {
        console.error('Error processing schedule:', schedule, error)
        throw error
      }
    })
    ferrySchedulesOptions.value = ferrySchedules
  } catch (err) {
    error.value = 'Failed to fetch schedules'
  } finally {
    setTimeout(() => {
      loading.value = false
    }, 1000) // 1 second delay
  }
}

watch(selectedTransportationType, () => {
  selectedCompany.value = ''
  toLocationSearch.value = ''
  fromLocationSearch.value = ''
  console.log('Selected transportation type:', selectedTransportationType.value)
  if (selectedTransportationType.value === transportationTypes.Bus) {
    busSchedulesOptions.value = []
    fetchBusSchedules()
  } else {
    ferrySchedulesOptions.value = []
    fetchFerrySchedules()
  }
})

watch([selectedCompany, toLocationSearch, fromLocationSearch], () => {
  console.log('Search criteria changed:', {
    selectedCompany: selectedCompany.value,
    toLocationSearch: toLocationSearch.value,
    fromLocationSearch: fromLocationSearch.value,
  })

  let filteredSchedules = []

  if (selectedTransportationType.value === transportationTypes.Bus) {
    filteredSchedules = busSchedules
  } else {
    filteredSchedules = ferrySchedules
  }

  if (selectedCompany.value) {
    filteredSchedules = filteredSchedules.filter(
      schedule => schedule.company_name === selectedCompany.value,
    )
  }

  if (toLocationSearch.value) {
    filteredSchedules = filteredSchedules.filter(schedule =>
      schedule.to_location
        .toLowerCase()
        .includes(toLocationSearch.value.toLowerCase()),
    )
  }

  if (fromLocationSearch.value) {
    filteredSchedules = filteredSchedules.filter(schedule =>
      schedule.from_location
        .toLowerCase()
        .includes(fromLocationSearch.value.toLowerCase()),
    )
  }

  if (selectedTransportationType.value === transportationTypes.Bus) {
    busSchedulesOptions.value = filteredSchedules
  } else {
    ferrySchedulesOptions.value = filteredSchedules
  }
})

onMounted(async () => {
  await fetchBusSchedules()
  await fetchFerrySchedules()
  uniqueBusCompanies.value = uniq(
    busSchedules.map(schedule => schedule.company_name),
  )
  uniqueFerryCompanies.value = uniq(
    ferrySchedules.map(schedule => schedule.company_name),
  )
})
</script>
