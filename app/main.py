from typing import Optional
from fastapi import FastAPI
# import fileparser as fp
# import pandas as pd

app = FastAPI()
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}


@app.get("/airport/{airport_name}")
def get_airport_details(airport_name: str):
    df = fp.load_unto_dataframe()
    relevant = df[df["Name"].str.contains(airport_name)]
    # convert relevant dataframe to json object
    return None

@app.get("/country/{country_name}")
def get_country_airports(country_name: str):
    df = fp.load_unto_dataframe()
    relevant = df[df["Country"] == country_name]
    # convert relevant dataframe to json object
    return None

@app.get("/city/{city_name}")
def get_city_airports(city_name: str):
    df = fp.load_unto_dataframe()
    relevant = df[df["City"] == city_name]
    # convert relevant dataframe to json object
    return None

@app.get("/timezone/{time_zone}")
def get_airports_within_timezone(time_zone : int):
    df = fp.load_unto_dataframe()
    relevant = df[df["Timezone"] == str(time_zone)]
    # convert relevant dataframe to json object
    return None

# def get_airport_within_geobox():
#     return None
#
