from sqlalchemy import Column, String, Integer, Float, Date, DateTime
from datetime import datetime
import uuid
from app.db.session import Base

class FlightSearch(Base):
    __tablename__ = "flight_searches"

    id             = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    origin         = Column(String, nullable = False)
    destination    = Column(String, nullable = False)
    travel_date    = Column(Date, nullable = False)
    passengers     = Column(Integer, nullable = False)
    cabin_class    = Column(String, nullable = False)
    cheapest_price = Column(Float, nullable = False)
    provider       = Column(String, nullable = False)
    created_at     = Column(DateTime, default = datetime.utcnow)