from fastapi import FastAPI
from app.schemas.flights import FlightResult, FlightSearchRequest, FlightSearchResponse
from app.services.flight_aggregator import search_all_providers, generate_cache_key
from app.cache.redis_client import get_cache, set_cache
from app.db.init_db import init_db
from app.db.session import SessionLocal
from app.db.models import FlightSearch
import uuid

app = FastAPI(title="Flight Aggregator API")

@app.get("/")
def root():
    return {"message" : "Flight Aggregator API is running"}

@app.post("/search-flights", response_model=FlightSearchResponse)
async def search_flights(payload: FlightSearchRequest):

    cache_key = generate_cache_key(

        payload.origin,
        payload.destination,
        payload.travel_date,
        payload.passengers,
        payload.cabin_class

    )

    cached_data = get_cache(cache_key)
    if cached_data:
        return cached_data
    
    results = await search_all_providers(
        payload.origin,
        payload.destination,
        payload.travel_date
    )

    cheapest = min(results, key=lambda x: x.price)

    db = SessionLocal()

    db_search = FlightSearch(
        origin = payload.origin,
        destination = payload.destination,
        travel_date = payload.travel_date,
        passengers  = payload.passengers,
        cabin_class = payload.cabin_class,
        cheapest_price = cheapest.price,
        provider = cheapest.provider
    )

    db.add(db_search)
    db.commit()
    db.close()

    response = FlightSearchResponse(
        search_id = str(uuid.uuid4()),
        results = results,
        cheapest = cheapest
    )

    set_cache(cache_key, response.model_dump())

    return response

@app.on_event("startup")
def startup():
    init_db()