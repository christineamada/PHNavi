<template>
  <div class="card grid grid-cols-1 md:grid-cols-2 gap-4">
    <InputGroup>
      <InputGroupAddon>
        <i class="pi pi-user"></i>
      </InputGroupAddon>
      <InputText v-model="text1" placeholder="Username" />
    </InputGroup>

    <InputGroup>
      <InputGroupAddon>$</InputGroupAddon>
      <InputNumber v-model="number" placeholder="Price" />
      <InputGroupAddon>.00</InputGroupAddon>
    </InputGroup>

    <InputGroup>
      <InputGroupAddon>www</InputGroupAddon>
      <InputText v-model="text2" placeholder="Website" />
    </InputGroup>

    <InputGroup>
      <InputGroupAddon>
        <i class="pi pi-map"></i>
      </InputGroupAddon>
      <Select
        v-model="selectedCity"
        :options="cities"
        optionLabel="name"
        placeholder="City"
      />
    </InputGroup>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const text1 = ref(null)
const text2 = ref(null)
const number = ref(null)
const selectedCity = ref()
const cities = ref([
  { name: 'New York', code: 'NY' },
  { name: 'Rome', code: 'RM' },
  { name: 'London', code: 'LDN' },
  { name: 'Istanbul', code: 'IST' },
  { name: 'Paris', code: 'PRS' },
])
</script>
