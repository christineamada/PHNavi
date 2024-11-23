export interface ISchedule {
  id: number
  company_name: string
  fare: string
  from_location: string
  from_latitude: string
  from_longitude: string
  to_location: string
  to_latitude: string
  to_longitude: string
  departure_time: string
  travel_class: string
  travel_days: string
  day_of_departure?: string
  day_of_arrival?: string
}
