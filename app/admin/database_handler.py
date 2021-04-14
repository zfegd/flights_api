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
