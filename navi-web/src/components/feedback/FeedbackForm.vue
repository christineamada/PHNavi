<script lang="ts" setup>
import { useToast } from 'primevue/usetoast'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { BACKEND_API_URL } from '@/config'
import axios from 'axios'


const name = ref('')
const email = ref('')
const comment = ref('')
const city = ref('')
const province = ref('')
const rating = ref('')
const isSubmitted = ref(false)


const router = useRouter()
const toast = useToast()


// Function to submit the feedback
const submitFeedback = async () => {
  try {
    // Make the API call to submit the feedback to Django backend
    const response = await axios.post(
      `${BACKEND_API_URL}/api/feedback/submit`, // Ensure this is your Django backend URL
      {
        name: name.value,
        email: email.value,
        comment: comment.value,
        city: city.value,
        province: province.value,
        rating: rating.value,
      },
    )
    console.log('Response:', response.data)


    // Display success toast notification
    showSuccess()


    // Set submission status to true to show the success message
    isSubmitted.value = true
  } catch (error) {
    console.error('Error submitting feedback:', error)
    toast.add({
      severity: 'error',
      summary: 'Error Message',
      detail: 'Failed to submit feedback',
      life: 3000,
    })
  }
}


// Success toast notification
const showSuccess = () => {
  toast.add({
    severity: 'success',
    summary: 'Success Message',
    detail: 'Feedback was submitted successfully',
    life: 3000,
  })
}


// Redirect to the homepage after submission
const goHome = () => {
  router.push('/')
}
</script>


<template>
  <Card class="w-[400px]">
    <template #title>Feedback</template>
    <template #content>
      <div v-if="!isSubmitted" class="flex flex-col gap-3">
        <!-- Feedback form fields -->
        <FloatLabel variant="on">
          <InputText id="name_label" v-model="name" fluid />
          <label for="name_label">Name</label>
        </FloatLabel>
        <FloatLabel variant="on">
          <InputText id="email_label" v-model="email" fluid />
          <label for="email_label">Email</label>
        </FloatLabel>
        <FloatLabel variant="in">
          <Textarea id="feedback_label" v-model="comment" fluid />
          <label for="in_label">Comment</label>
        </FloatLabel>
        <FloatLabel variant="on">
          <InputText id="city_label" v-model="city" fluid />
          <label for="city_label">City</label>
        </FloatLabel>
        <FloatLabel variant="on">
          <InputText id="province_label" v-model="province" fluid />
          <label for="province_label">Province</label>
        </FloatLabel>
        <div class="flex flex-col">
          <div>
            <label>Rating</label>
            <Divider />
          </div>
          <div>
            <div class="flex items-center">
              <RadioButton
                v-model="rating"
                inputId="rating1"
                name="rating"
                value="Excellent"
              />
              <label for="rating1" class="ml-2">Excellent</label>
            </div>
            <div class="flex items-center">
              <RadioButton
                v-model="rating"
                inputId="rating2"
                name="rating"
                value="Very good"
              />
              <label for="rating2" class="ml-2">Very good</label>
            </div>
            <div class="flex items-center">
              <RadioButton
                v-model="rating"
                inputId="rating3"
                name="rating"
                value="Good"
              />
              <label for="rating3" class="ml-2">Good</label>
            </div>
            <div class="flex items-center">
              <RadioButton
                v-model="rating"
                inputId="rating4"
                name="rating"
                value="Average"
              />
              <label for="rating4" class="ml-2">Average</label>
            </div>
            <div class="flex items-center">
              <RadioButton
                v-model="rating"
                inputId="rating5"
                name="rating"
                value="Poor"
              />
              <label for="rating5" class="ml-2">Poor</label>
            </div>
          </div>
        </div>
        <Button label="Submit" @click="submitFeedback" />
      </div>


      <!-- Success message when feedback is submitted -->
      <div v-else class="flex flex-col items-center gap-3">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="w-16 h-16 text-green-500"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M5 13l4 4L19 7"
          />
        </svg>
        <p class="text-green-500 text-lg">Feedback submitted successfully!</p>
        <Button label="Go Home" @click="goHome" />
      </div>
    </template>
  </Card>
</template>