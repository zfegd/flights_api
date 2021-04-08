CREATE TABLE Airports(
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

-- INSERT INTO Airports
-- VALUES (1,"Goroka Airport","Goroka","Papua New Guinea","GKA","AYGA",-6.081689834590001,145.391998291,5282,10,"U","Pacific/Port_Moresby","airport","OurAirports");

LOAD DATA LOCAL INFILE "../app/data/airports.dat"
INTO TABLE Airports
FIELDS TERMINATED BY ',';
