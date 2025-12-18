import random
import asyncio
from datetime import timedelta

async def search_indigo_flights(origin:str, destination:str, travel_date):
    await asyncio.sleep(random.uniform(0.3,0.8)) # Simulating Network Delay
    #Mock Response
    return{
        "airline" : "Indigo",
        "amount"  : random.randint(4800,5600),
        "currency": "INR",
        "duration": timedelta(hours=2, minutes=15),
        "stops"   : 0

    }

