from typing import Optional
from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

def load_unto_dataframe():
    myheaders = ["AirportID","Name","City","Country","IATA","ICAO","Latitude",
        "Longitude", "Altitude", "Timezone", "DST", "TZ", "Type", "Source"]
    df = pd.read_csv("data/airports.dat", names=myheaders)
    df = df.replace("\\N", "Not Found")
    return df

@app.get("/airport/{airport_name}")
def get_airport_details(airport_name: str):
    df = load_unto_dataframe()
    df["Name"] = df["Name"].str.lower()
    relevant = df[df["Name"].str.contains(airport_name.lower())]
    if relevant.shape[0] is 0:
        raise HTTPException(status_code=404, detail="No Entries found")
    return relevant.to_json()

@app.get("/country/{country_name}")
def get_country_airports(country_name: str):
    df = load_unto_dataframe()
    df["Country"] = df["Country"].str.lower()
    relevant = df[df["Country"] == country_name.lower()]
    if relevant.shape[0] is 0:
        raise HTTPException(status_code=404, detail="No Entries found")
    return relevant.to_json()

@app.get("/city/{city_name}")
def get_city_airports(city_name: str):
    df = load_unto_dataframe()
    df["City"] = df["City"].str.lower()
    relevant = df[df["City"] == city_name.lower()]
    if relevant.shape[0] is 0:
        raise HTTPException(status_code=404, detail="No Entries found")
    return relevant.to_json()

@app.get("/timezone/{time_zone}")
def get_airports_within_timezone(time_zone : str):
    try:
        timezonenum = float(time_zone)
        if timezonenum < -12 or timezonenum > 14:
            raise HTTPException(status_code=400, detail="Timezone not valid")
    except ValueError:
        raise HTTPException(status_code=400, detail="Timezone not valid")
    df = load_unto_dataframe()
    relevant = df[df["Timezone"] == time_zone]
    if relevant.shape[0] is 0:
        # throws a 404 because the user can submit a time_zone of "10.9" -> can be refactored into two cases for different error codes
        raise HTTPException(status_code=404, detail="No Entries found or timezone not valid")
    return relevant.to_json()

# def get_airport_within_geobox():
#     return None
#
