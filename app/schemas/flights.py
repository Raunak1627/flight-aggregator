from pydantic import BaseModel
from datetime import date
from typing import List

class FlightSearchRequest(BaseModel):
    origin: str   # DEL
    destination: str # BLR
    travel_date: date
    passengers: int = 1
    cabin_class: str = "economy"

#What the Result will be
class FlightResult(BaseModel):
    provider: str
    price: float
    currency: str
    duration_minutes: int
    stops: int

#API Response Schema
class FlightSearchResponse(BaseModel):
    search_id: str
    results: List[FlightResult]
    cheapest: FlightResult
    