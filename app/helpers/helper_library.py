def airports_zip_to_dict(values):
    keys = ["airportid", "name", "city", "country", "iata", "icao",
            "latitude", "longitude", "altitude", "timezone", "dst", "tz",
            "type", "source"]
    if len(values) != len(keys):
        return None
    return dict(zip(keys, values))
