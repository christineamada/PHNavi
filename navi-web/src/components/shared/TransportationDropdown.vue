<template>
  <Dropdown
    :options="transportationOptions"
    v-model="model"
    optionLabel="label"
    optionValue="value"
    placeholder="Select Transportation"
  />
</template>

<script lang="ts" setup>
import TransportationTypes from '@/enums/transportationTypes'

const transportationTypes = TransportationTypes
const model = defineModel()
const transportationOptions = [
  { label: transportationTypes.Bus, value: transportationTypes.Bus },
  { label: transportationTypes.Ferry, value: transportationTypes.Ferry },
]
</script>
