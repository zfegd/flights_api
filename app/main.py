from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Dict
import pandas as pd

app = FastAPI(
    title="Open Flights Project",
    description="Basic project to obtain Airport info from OpenFlights",
    version="0.1",
)


class Airport(BaseModel):
    AirportID: int
    Name: str
    City: str
    Country: str
    IATA: str
    ICAO: str
    Latitude: float
    Longitude: float
    Altitude: int
    Timezone: str
    DST: str
    TZ: str
    Type: str
    Source: str


class Message(BaseModel):
    message: str


def load_unto_dataframe():
    myheaders = ["AirportID", "Name", "City", "Country", "IATA", "ICAO",
                 "Latitude", "Longitude", "Altitude", "Timezone", "DST", "TZ",
                 "Type", "Source"]
    df = pd.read_csv("/data/airports.dat", names=myheaders)
    df = df.replace("\\N", "Not Found")
    return df


@app.get(
    "/v0.1/airport",
    response_model=Dict[str, Airport],
    responses={
         404: {"model": Message, "description": "No Entries found"},
         200: {
            "description": "Airports found containing requested name",
            "content": {
                "application/json": {
                    "example": {
                        "502": {
                            "AirportID": 507,
                            "Name": "London Heathrow Airport",
                            "City": "London",
                            "Country": "United Kingdom",
                            "IATA": "LHR",
                            "ICAO": "EGLL",
                            "Latitude": 51.4706,
                            "Longitude": -0.461941,
                            "Altitude": 83,
                            "Timezone": "0",
                            "DST": "E",
                            "TZ": "Europe/London",
                            "Type": "airport",
                            "Source": "OurAirports"
                                }
                                }
                            }
                    },
            },
    },
)
def get_airport_details(airport_name: str = Query(...,
                        description="Name of the airport you are trying to " +
                        "find, can be its full name or just a phrase",
                                                  example="Heathrow")):
    """
    Find all the airports in the database that contains the name you queried.

    For example, you can search for "Heathrow" or "London"
    """
    df = load_unto_dataframe()
    relevant = df[df["Name"].str.contains(airport_name, case=False)]
    if relevant.shape[0] is 0:
        raise HTTPException(status_code=404, detail="No Entries found")
    return relevant.to_dict('index')


@app.get(
    "/v0.1/country/",
    response_model=Dict[str, Airport],
    responses={
         404: {"model": Message, "description": "No Entries found"},
         200: {
            "description": "Airports found in the country requested",
            "content": {
                "application/json": {
                    "example": {
                        "502": {
                            "AirportID": 507,
                            "Name": "London Heathrow Airport",
                            "City": "London",
                            "Country": "United Kingdom",
                            "IATA": "LHR",
                            "ICAO": "EGLL",
                            "Latitude": 51.4706,
                            "Longitude": -0.461941,
                            "Altitude": 83,
                            "Timezone": "0",
                            "DST": "E",
                            "TZ": "Europe/London",
                            "Type": "airport",
                            "Source": "OurAirports"
                                }
                                }
                            }
                    },
            },
    },
)
def get_country_airports(country_name: str = Query(...,
                         description="Country whose airports you want " +
                         "to find", example="Malaysia")):
    """
    Find all the airports in the database that are in a specific country

    For example, you can search for "Malaysia"
    """
    df = load_unto_dataframe()
    df["LowerCountry"] = df["Country"].str.lower()
    relevant = df[df["LowerCountry"] == country_name.lower()]
    del relevant["LowerCountry"]
    if relevant.shape[0] is 0:
        raise HTTPException(status_code=404, detail="No Entries found")
    return relevant.to_dict('index')


@app.get(
    "/v0.1/city/",
    response_model=Dict[str, Airport],
    responses={
         404: {"model": Message, "description": "No Entries found"},
         200: {
            "description": "Airports found in the city requested",
            "content": {
                "application/json": {
                    "example": {
                        "502": {
                            "AirportID": 507,
                            "Name": "London Heathrow Airport",
                            "City": "London",
                            "Country": "United Kingdom",
                            "IATA": "LHR",
                            "ICAO": "EGLL",
                            "Latitude": 51.4706,
                            "Longitude": -0.461941,
                            "Altitude": 83,
                            "Timezone": "0",
                            "DST": "E",
                            "TZ": "Europe/London",
                            "Type": "airport",
                            "Source": "OurAirports"
                                }
                                }
                            }
                    },
            },
    },
)
def get_city_airports(city_name: str = Query(...,
                      description="City whose airports you want " +
                      "to find", example="Manchester")):
    """
    Find all the airports in the database that are in a specific city

    For example, you can search for "Manchester"
    """
    df = load_unto_dataframe()
    df["LowerCity"] = df["City"].str.lower()
    relevant = df[df["LowerCity"] == city_name.lower()]
    del relevant["LowerCity"]
    if relevant.shape[0] is 0:
        raise HTTPException(status_code=404, detail="No Entries found")
    return relevant.to_dict('index')

# @app.get("/v0.1/timezone/")
# def get_airports_within_timezone(time_zone : str):
#     try:
#         timezonenum = float(time_zone)
#         if timezonenum < -12 or timezonenum > 14:
#             raise HTTPException(status_code=400, detail="Timezone not valid")
#     except ValueError:
#         raise HTTPException(status_code=400, detail="Timezone not valid")
#     df = load_unto_dataframe()
#     relevant = df[df["Timezone"] == time_zone]
#     if relevant.shape[0] is 0:
#         # throws a 404 because the user can submit a time_zone of "10.9"
#    -> can be refactored into two cases for different error codes
#         raise HTTPException(status_code=404, detail="No Entries
#       found or timezone not valid")
#     return relevant.to_dict()

# def get_airport_within_geobox():
#     return None
#
