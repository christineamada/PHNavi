export interface IRoute {
  id: number
  from_location: string
  to_location: string
  from: LatLng
  to: LatLng
}

export type LatLng = {
  lat: number
  lng: number
}
