import random
import asyncio

async def search_airindex_flights(origin:str, destination:str, travel_date):
    await asyncio.sleep(random.uniform(0.3,0.8))
    #MOCK Response
    return{
        "provider_name" : "Air India Express",
        "fare" : {
            "total" : random.randint(4900,5700)
        },
        "currency" : "INR",
        "flight_time_minutes" : random.randint(140,165),
        "stops" : random.choice([0,1])
    }