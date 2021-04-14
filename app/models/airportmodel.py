from pydantic import BaseModel
from typing import Optional


class Airport(BaseModel):
    airportid: int
    name: str
    city: str
    country: str
    iata: Optional[str] = None
    icao: Optional[str] = None
    latitude: float
    longitude: float
    altitude: int
    timezone: Optional[str] = None
    dst: Optional[str] = None
    tz: Optional[str] = None
    type: str
    source: str
