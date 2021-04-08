CREATE DATABASE OpenFlights;

CREATE TABLE OpenFlights.Airports(
  AirportID int,
  Name varchar(255),
  City varchar(255),
  Country varchar(255),
  IATA varchar(255),
  ICAO varchar(255),
  Latitude float,
  Longitude float,
  Altitude int,
  Timezone varchar(255),
  DST varchar(255),
  TZ varchar(255),
  Type varchar(255),
  Source varchar(255)
);

LOAD DATA INFILE "../app/data/airports.dat"
INTO TABLE Airports
FIELDS TERMINATED BY ','
