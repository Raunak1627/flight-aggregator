import asyncio
from app.schemas.flights import FlightResult
from app.providers.indigo import search_indigo_flights
from app.providers.airindiaexp import search_airindex_flights

def generate_cache_key(origin, destination, travel_date, passengers, cabin_class):
    return f"flight:{origin} : {destination} : {travel_date} : {passengers} : {cabin_class}"

def normalize_indigo(data) -> FlightResult:
    return FlightResult(
        provider = data["airline"],
        price= float(data["amount"]),
        currency=data["currency"],  
        duration_minutes=int(data["duration"].total_seconds()/60),
        stops= data["stops"]
    )


def normalize_airasia(data) -> FlightResult:
    return FlightResult(
        provider = data["provider_name"],
        price= float(data["fare"]["total"]),
        currency=data["currency"],  
        duration_minutes=int(data["flight_time_minutes"]),
        stops= data["stops"]
    )

async def search_all_providers(origin:str, destination:str, travel_date):
    
     indigo_task = search_indigo_flights(origin, destination, travel_date)
     airasia_task = search_airindex_flights(origin, destination, travel_date)


     indigo_raw, airasia_raw = await asyncio.gather(
        indigo_task,
        airasia_task
    )
    

     return [
        normalize_indigo(indigo_raw),
        normalize_airasia(airasia_raw)
    ]


    