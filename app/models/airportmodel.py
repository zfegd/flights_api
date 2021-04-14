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

    # def __init__(self, fields):
    #     self.airportid = fields[0]
    #     self.name = fields[1]
    #     self.city = fields[2]
    #     self.country = fields[3]
    #     self.iata = fields[4]
    #     self.icao = fields[5]
    #     self.latitude = fields[6]
    #     self.longitude = fields[7]
    #     self.altitude = fields[8]
    #     self.timezone = fields[9]
    #     self.dst = fields[10]
    #     self.tz = fields[11]
    #     self.type = fields[12]
    #     self.source = fields[13]
