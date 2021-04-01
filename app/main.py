from typing import Optional
from fastapi import FastAPI
import pandas as pd

app = FastAPI()

def load_unto_dataframe():
    myheaders = ["AirportID","Name","City","Country","IATA","ICAO","Latitude",
        "Longitude", "Altitude", "Timezone", "DST", "TZ", "Type", "Source"]
    df = pd.read_csv("data/airports.dat", names=myheaders)
    df = df.replace("\\N", "Not Found")
    # resolve issue where can't be displayed - name,city (need to encode to UTF8)
    # issue due to polish letters
    return df


@app.get("/airport/{airport_name}")
def get_airport_details(airport_name: str):
    df = load_unto_dataframe()
    df["Name"] = df["Name"].str.lower()
    relevant = df[df["Name"].str.contains(airport_name.lower())]
    return relevant.to_json()

@app.get("/country/{country_name}")
def get_country_airports(country_name: str):
    df = load_unto_dataframe()
    df["Country"] = df["Country"].str.lower()
    relevant = df[df["Country"] == country_name.lower()]
    return relevant.to_json()

@app.get("/city/{city_name}")
def get_city_airports(city_name: str):
    df = load_unto_dataframe()
    df["City"] = df["City"].str.lower()
    relevant = df[df["City"] == city_name.lower()]
    return relevant.to_json()

@app.get("/timezone/{time_zone}")
def get_airports_within_timezone(time_zone : int):
    df = load_unto_dataframe()
    relevant = df[df["Timezone"] == str(time_zone)]
    return relevant.to_json()

# def get_airport_within_geobox():
#     return None
#
