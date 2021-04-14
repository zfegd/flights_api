from fastapi import HTTPException


def airports_zip_to_dict(values):
    keys = ["airportid", "name", "city", "country", "iata", "icao",
            "latitude", "longitude", "altitude", "timezone", "dst", "tz",
            "type", "source"]
    if len(values) != len(keys):
        return None
    return dict(zip(keys, values))


def result_parser(myresult, detailmsg="No Entries found"):
    results = {}
    index = 0
    if len(myresult) == 0:
        raise HTTPException(status_code=404, detail=detailmsg)
    for result in myresult:
        dictresult = airports_zip_to_dict(result)
        results.update({index: dictresult})
        index = index + 1
    return results
