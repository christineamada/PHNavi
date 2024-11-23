/** @type {import('tailwindcss').Config} */
import tailwindCSSPrimeUi from 'tailwindcss-primeui'
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        Lato: 'Lato',
      },
    },
  },
  plugins: [tailwindCSSPrimeUi],
}
