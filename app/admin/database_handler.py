from fastapi import HTTPException
import mysql.connector
from admin import config


def open_connection():
    mydb = mysql.connector.connect(
      host="db",
      user=config.user,
      password=config.password,
      database="openflights"
    )
    return mydb


def fetch_query_results(query):
    try:
        mydb = open_connection()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Could not connect to database")
    try:
        mycursor = mydb.cursor()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Database Error")
    try:
        mycursor.execute(query)
        myresult = mycursor.fetchall()
    except mysql.connector.Error:
        raise HTTPException(status_code=500,
                            detail="Query to database failed!")
    mycursor.close()
    return myresult
