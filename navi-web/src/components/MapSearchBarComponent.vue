<script setup lang="ts">
import { ref, watch } from 'vue'
import type { PropType } from 'vue'
import { GOOGLE_MAPS_API_KEY } from '@/config'

const props = defineProps({
  modelValue: {
    type: [Object, String] as PropType<Object | string>,
  },
  placeholder: {
    type: String,
    default: 'Search...',
  },
})

const emits = defineEmits(['update:modelValue'])

const query = ref(props.modelValue || '')
const results = ref<
  { description: string; coordinates: { lat: number; lng: number } }[]
>([])
const proxyUrl = 'https://cors-anywhere.herokuapp.com/'


const searchPlaces = async () => {
  if (typeof query.value === 'string' && query.value.length > 2) {
    try {
      const response = await fetch(
        `${proxyUrl}https://maps.googleapis.com/maps/api/place/autocomplete/json?input=${query.value}&key=${GOOGLE_MAPS_API_KEY}&types=(cities)&components=country:PH`,
      )
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const data = await response.json()
      results.value = await Promise.all(
        data.predictions.map(async (prediction: { place_id: any }) => {
          const placeDetailsResponse = await fetch(
            `${proxyUrl}https://maps.googleapis.com/maps/api/place/details/json?place_id=${prediction.place_id}&key=${GOOGLE_MAPS_API_KEY}`,
          )
          if (!placeDetailsResponse.ok) {
            throw new Error('Network response was not ok')
          }
          const placeDetails = await placeDetailsResponse.json()
          return {
            ...prediction,
            coordinates: placeDetails.result.geometry.location,
          }
        }),
      )
      console.log('Places:', results.value)
    } catch (error) {
      console.error('Failed to fetch places:', error)
      results.value = []
    }
  } else {
    results.value = []
  }
}

watch(query, newValue => {
  emits('update:modelValue', newValue)
  if (typeof newValue === 'string' && newValue.length <= 2) {
    results.value = []
  }
})

watch(
  () => props.modelValue,
  newValue => {
    if (newValue !== query.value) {
      query.value = newValue || ''
    }
  },
)
</script>

<template>
  <InputGroup>
    <AutoComplete
      v-model="query"
      :suggestions="results"
      option-label="description"
      :placeholder="placeholder"
      @complete="searchPlaces"
      fluid
    />
  </InputGroup>
</template>
