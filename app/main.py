from typing import Optional
from fastapi import FastAPI
import pandas as pd

app = FastAPI()

def load_unto_dataframe():
    myheaders = ["Airport ID","Name","City","Country","IATA","ICAO","Latitude",
        "Longitude", "Altitude", "Timezone", "DST", "TZ", "Type", "Source"]
    df = pd.read_csv("data/airports.dat", names=myheaders)
    df = df.replace("\\N", "Not Found")
    # resolve issue where can't be displayed - name,city (need to encode to UTF8)
    # issue due to polish letters
    return df

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/df/")
def test_df():
    df = load_unto_dataframe()
    size = df.shape[0]
    return {"Data": size}

@app.get("/airport/{airport_name}")
def get_airport_details(airport_name: str):
    df = load_unto_dataframe()
    df["Name"] = df["Name"].str.lower()
    relevant = df[df["Name"].str.contains(airport_name.lower())]
    # convert relevant dataframe to json object
    count = relevant.shape[0]
    return {"Airports":count}

#
# @app.get("/country/{country_name}")
# def get_country_airports(country_name: str):
#     df = load_unto_dataframe()
#     relevant = df[df["Country"] == country_name]
#     # convert relevant dataframe to json object
#     return None
#
# @app.get("/city/{city_name}")
# def get_city_airports(city_name: str):
#     df = load_unto_dataframe()
#     relevant = df[df["City"] == city_name]
#     # convert relevant dataframe to json object
#     return None
#
# @app.get("/timezone/{time_zone}")
# def get_airports_within_timezone(time_zone : int):
#     df = load_unto_dataframe()
#     relevant = df[df["Timezone"] == str(time_zone)]
#     # convert relevant dataframe to json object
#     return None

# def get_airport_within_geobox():
#     return None
#
