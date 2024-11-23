import axios from 'axios'
import { GOOGLE_MAPS_API_KEY } from '@/config'

const proxyUrl = 'https://cors-anywhere.herokuapp.com/'
const googleMapsUrl = 'https://maps.googleapis.com/maps/api/'

const dumagueteCoords: google.maps.LatLngLiteral = {
  lat: 9.3068,
  lng: 123.3054,
}

export const getDirections = async (origin: string, destination: string) => {
  const url = `${proxyUrl}${googleMapsUrl}directions/json?origin=${origin}&destination=${destination}&key=${GOOGLE_MAPS_API_KEY}&region=ph`
  try {
    const response = await axios.get(url)
    return response.data
  } catch (error) {
    console.error('Error fetching directions:', error)
    throw error
  }
}

export const searchPlaces = async (query: Object | string) => {
  const url = `${proxyUrl}${googleMapsUrl}place/autocomplete/json?input=${query}&key=${GOOGLE_MAPS_API_KEY}&types=geocode&components=country:ph`
  try {
    const response = await axios.get(url)
    return response.data
  } catch (error) {
    console.error('Error searching places:', error)
    throw error
  }
}

export const findNearbyPlaces = async (
  type: string,
  query: string,
  radius: number = 50000,
) => {
  const url = `${proxyUrl}${googleMapsUrl}place/nearbysearch/json?&radius=${radius}&type=${type}&keyword=${query}&key=${GOOGLE_MAPS_API_KEY}&components=country:ph`
  try {
    const response = await axios.get(url)
    return response.data
  } catch (error) {
    console.error('Error finding nearby places:', error)
    throw error
  }
}

export const getPlaceDetails = async (placeId: string) => {
  const url = `${proxyUrl}${googleMapsUrl}place/details/json?place_id=${placeId}&key=${GOOGLE_MAPS_API_KEY}&region=ph`
  try {
    const response = await axios.get(url)
    return response.data
  } catch (error) {
    console.error('Error fetching place details:', error)
    throw error
  }
}
