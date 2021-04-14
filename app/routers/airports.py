from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import Dict, Optional
import re
import mysql.connector
from admin import database_handler
from helpers import descriptors, helper_library

router = APIRouter()


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


class Message(BaseModel):
    message: str


@router.get(
    "/v1/airport",
    response_model=Dict[str, Airport],
    responses={
         404: {"model": Message, "description": "No Entries found"},
         200: {
            "description": "Airports found containing requested name",
            "content": descriptors.airportexamplecontent,
            },
    },
)
def get_airport_details(airport_name: str = Query(..., min_length=1,
                        description="Name of the airport you are trying to " +
                        "find, can be its full name or just a phrase",
                                                  example="Heathrow")):
    """
    Find all the airports in the database that contains the name you queried.

    For example, you can search for "Heathrow" or "London"
    """
    esc_name = re.escape(airport_name)
    try:
        mydb = database_handler.open_connection()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Could not connect to database")
    try:
        mycursor = mydb.cursor()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Database Error")
    query = "SELECT * FROM Airports where name LIKE \"%" + esc_name + "%\""
    try:
        mycursor.execute(query)
        myresult = mycursor.fetchall()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Query to database failed!")
    results = {}
    index = 0
    if len(myresult) == 0:
        raise HTTPException(status_code=404, detail="No Entries found")
    for result in myresult:
        dictresult = helper_library.airports_zip_to_dict(result)
        results.update({index: dictresult})
        index = index + 1
    mycursor.close()
    return results


@router.get(
    "/v1/country/",
    response_model=Dict[str, Airport],
    responses={
         404: {"model": Message, "description": "No Entries found"},
         200: {
            "description": "Airports found in the country requested",
            "content": descriptors.airportexamplecontent,
            },
    },
)
def get_country_airports(country_name: str = Query(..., min_length=1,
                         description="Country whose airports you want " +
                         "to find", example="Malaysia")):
    """
    Find all the airports in the database that are in a specific country

    For example, you can search for "Malaysia"
    """
    country_name_esc = re.escape(country_name)
    try:
        mydb = database_handler.open_connection()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Could not connect to database")
    try:
        mycursor = mydb.cursor()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Database Error")
    query = "SELECT * FROM Airports where country=\"" + country_name_esc + "\""
    try:
        mycursor.execute(query)
        myresult = mycursor.fetchall()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Query to database failed!")
    results = {}
    index = 0
    if len(myresult) == 0:
        raise HTTPException(status_code=404, detail="No Entries found")
    for result in myresult:
        dictresult = helper_library.airports_zip_to_dict(result)
        results.update({index: dictresult})
        index = index + 1
    mycursor.close()
    return results


@router.get(
    "/v1/city/",
    response_model=Dict[str, Airport],
    responses={
         404: {"model": Message, "description": "No Entries found"},
         200: {
            "description": "Airports found in the city requested",
            "content": descriptors.airportexamplecontent,
            },
    },
)
def get_city_airports(city_name: str = Query(..., min_length=1,
                      description="City whose airports you want " +
                      "to find", example="Manchester")):
    """
    Find all the airports in the database that are in a specific city

    For example, you can search for "Manchester"
    """
    city_name_esc = re.escape(city_name)
    try:
        mydb = database_handler.open_connection()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Could not connect to database")
    try:
        mycursor = mydb.cursor()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Database Error")
    query = "SELECT * FROM Airports where city=\"" + city_name_esc + "\""
    try:
        mycursor.execute(query)
        myresult = mycursor.fetchall()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Query to database failed!")
    results = {}
    index = 0
    if len(myresult) == 0:
        raise HTTPException(status_code=404, detail="No Entries found")
    for result in myresult:
        dictresult = helper_library.airports_zip_to_dict(result)
        results.update({index: dictresult})
        index = index + 1
    mycursor.close()
    return results


@router.get(
    "/v1/IATA/",
    response_model=Dict[str, Airport],
    responses={
         404: {"model": Message, "description": "No Entries found"},
         200: {
            "description": "Airport with the IATA code requested",
            "content": descriptors.airportexamplecontent,
            },
    },
)
def get_iata_airport(iata_code: str = Query(..., regex="^[A-Z]{3}$",
                     description="Airport with the code requested",
                     example="LHR")):
    """
    Find the airport in the database that has your requested IATA code,
    excludes unknown or unassigned airports

    For example, you can search for "LHR"
    """
    try:
        mydb = database_handler.open_connection()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Could not connect to database")
    try:
        mycursor = mydb.cursor()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Database Error")
    query = "SELECT * FROM Airports where iata=\"" + iata_code + "\""
    try:
        mycursor.execute(query)
        myresult = mycursor.fetchall()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Query to database failed!")
    results = {}
    index = 0
    if len(myresult) == 0:
        raise HTTPException(status_code=404, detail="No Entries found")
    for result in myresult:
        dictresult = helper_library.airports_zip_to_dict(result)
        results.update({index: dictresult})
        index = index + 1
    mycursor.close()
    return results


@router.get(
    "/v1/ICAO/",
    response_model=Dict[str, Airport],
    responses={
         404: {"model": Message, "description": "No Entries found"},
         200: {
            "description": "Airport with the ICAO code requested",
            "content": descriptors.airportexamplecontent,
            },
    },
)
def get_icao_airport(icao_code: str = Query(..., regex="^[A-Z]{4}$",
                     description="Airport with the code requested",
                     example="EGLL")):
    """
    Find the airport in the database that has your requested ICAO code,
    excludes unknown or unassigned airports


    For example, you can search for "EGLL"
    """
    try:
        mydb = database_handler.open_connection()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Could not connect to database")
    try:
        mycursor = mydb.cursor()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Database Error")
    query = "SELECT * FROM Airports where icao=\"" + icao_code + "\""
    try:
        mycursor.execute(query)
        myresult = mycursor.fetchall()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Query to database failed!")
    results = {}
    index = 0
    if len(myresult) == 0:
        raise HTTPException(status_code=404, detail="No Entries found")
    for result in myresult:
        dictresult = helper_library.airports_zip_to_dict(result)
        results.update({index: dictresult})
        index = index + 1
    mycursor.close()
    return results


@router.get(
    "/v1/tzformat/",
    response_model=Dict[str, Airport],
    responses={
         404: {"model": Message, "description": "No Entries found"},
         200: {
            "description": "Airports within this tz timezone",
            "content": descriptors.airportexamplecontent,
            },
    },
)
def get_tz_airports(tz: str = Query(..., regex="^[a-zA-Z0-9-+/_]+$",
                    description="Airports within timezone requested",
                    example="Europe/London")):
    """
    Find the airport in the database that falls within a timezone, as
     specified by the tz (Olson) format


    For example, you can search for "Europe/London"
    """
    try:
        mydb = database_handler.open_connection()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Could not connect to database")
    try:
        mycursor = mydb.cursor()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Database Error")
    query = "SELECT * FROM Airports where tz=\"" + tz + "\""
    try:
        mycursor.execute(query)
        myresult = mycursor.fetchall()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Query to database failed!")
    results = {}
    index = 0
    if len(myresult) == 0:
        raise HTTPException(status_code=404, detail="No Entries found")
    for result in myresult:
        dictresult = helper_library.airports_zip_to_dict(result)
        results.update({index: dictresult})
        index = index + 1
    mycursor.close()
    return results


@router.get(
    "/v1/dst/",
    response_model=Dict[str, Airport],
    responses={
         404: {"model": Message, "description": "No Entries found"},
         200: {
            "description": "Airports within a dst timezone",
            "content": descriptors.airportexamplecontent,
            },
    },
)
def get_dst_airports(dst: str = Query(..., regex="^[EASOZNU]{1}$",
                     description="Airports within timezone requested",
                     example="Z")):
    """
    Find the airport in the database that falls within a timezone, as
     specified by DST. Possible zones are 'E' for europe, 'A' for North
     America, 'S' for South America, 'O' for Australia, 'Z' for New Zealand,
     'N' for none, or 'U' for unknown


    For example, you can search for "E"
    """
    try:
        mydb = database_handler.open_connection()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Could not connect to database")
    try:
        mycursor = mydb.cursor()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Database Error")
    query = "SELECT * FROM Airports where dst=\"" + dst + "\""
    try:
        mycursor.execute(query)
        myresult = mycursor.fetchall()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Query to database failed!")
    results = {}
    index = 0
    if len(myresult) == 0:
        # should never enter this branch?
        raise HTTPException(status_code=404, detail="No Entries found")
    for result in myresult:
        dictresult = helper_library.airports_zip_to_dict(result)
        results.update({index: dictresult})
        index = index + 1
    mycursor.close()
    return results


@router.get(
    "/v1/utc/",
    response_model=Dict[str, Airport],
    responses={
         404: {"model": Message, "description": "No Entries found"},
         200: {
            "description": "Airports within this UTC offset range",
            "content": descriptors.airportexamplecontent,
            },
    },
)
def get_utc_airports(time_zone: str = Query(...,
                     regex="^-?[0-9]{1,2}(.5|.75)?$",
                     description="Airports within this UTC offset range",
                     example="0")):
    """
    Find the airport in the database that falls within a timezone, as
     specified by the offset from UTC. Input should be a decimal offset,
     with no need for "+" in positive offsets, and ":" not being used either


    For example, you can search for "0", "-11", "14", "5.75", or "3.5"
    """
    try:
        mydb = database_handler.open_connection()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Could not connect to database")
    try:
        mycursor = mydb.cursor()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Database Error")
    timezonenum = float(time_zone)
    if timezonenum < -12 or timezonenum > 14:
        raise HTTPException(status_code=400, detail="Timezone not valid")
    query = "SELECT * FROM Airports where timezone=\"" + time_zone + "\""
    try:
        mycursor.execute(query)
        myresult = mycursor.fetchall()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Query to database failed!")
    results = {}
    index = 0
    if len(myresult) == 0:
        raise HTTPException(status_code=404,
                            detail="No Entries found or timezone not valid")
    for result in myresult:
        dictresult = helper_library.airports_zip_to_dict(result)
        results.update({index: dictresult})
        index = index + 1
    mycursor.close()
    return results


@router.get(
    "/v1/geobox/",
    response_model=Dict[str, Airport],
    responses={
         404: {"model": Message, "description": "No Entries found"},
         200: {
            "description": "Airports within this area",
            "content": descriptors.airportexamplecontent,
            },
    },
)
def get_airport_in_geobox_naive(southlat: float = Query(..., ge=-90, le=90),
                                northlat: float = Query(..., ge=-90, le=90),
                                westlon: float = Query(..., ge=-180, le=180),
                                eastlon: float = Query(..., ge=-180, le=180)):
    """
    Find the airports that falls within a specific geographical bound, as
     specified by Longitudinal and Latitudinal values
    """
    try:
        mydb = database_handler.open_connection()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Could not connect to database")
    try:
        mycursor = mydb.cursor()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Database Error")
    querytotal = get_airport_geobox_query(southlat, northlat, westlon, eastlon)
    try:
        mycursor.execute(querytotal)
        myresult = mycursor.fetchall()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Query to database failed!")
    results = {}
    index = 0
    if len(myresult) == 0:
        raise HTTPException(status_code=404, detail="No Entries found")
    for result in myresult:
        dictresult = helper_library.airports_zip_to_dict(result)
        results.update({index: dictresult})
        index = index + 1
    mycursor.close()
    return results


def get_airport_geobox_query(southlat, northlat, westlon, eastlon):
    if southlat <= northlat and westlon <= eastlon:
        q1 = "SELECT * FROM Airports WHERE latitude BETWEEN " + str(southlat)
        q2 = " AND " + str(northlat) + " AND longitude BETWEEN " + str(westlon)
        q3 = " AND " + str(eastlon)
        querytotal = q1 + q2 + q3
        return querytotal
    elif southlat <= northlat and westlon > eastlon:
        q1 = "SELECT * FROM Airports WHERE latitude BETWEEN " + str(southlat)
        q2 = " AND " + str(northlat) + " AND (longitude > "
        q3 = str(westlon) + " OR longitude < " + str(eastlon) + ")"
        querytotal = q1 + q2 + q3
        return querytotal
    elif southlat > northlat and westlon <= eastlon:
        q1 = "SELECT * FROM Airports WHERE (latitude > " + str(southlat)
        q2 = " OR latitude < " + str(northlat) + ") AND longitude"
        q3 = " BETWEEN " + str(westlon) + " AND " + str(eastlon)
        querytotal = q1 + q2 + q3
        return querytotal
    q1 = "SELECT * FROM Airports WHERE (latitude > " + str(southlat)
    q2 = " OR latitude < " + str(northlat) + ") AND (longitude > "
    q3 = str(westlon) + " OR longitude < " + str(eastlon) + ")"
    querytotal = q1 + q2 + q3
    return querytotal
