from fastapi import HTTPException
from models import airportmodel


def parse_to_airport(values):
    keys = airportmodel.get_fields()
    if len(values) != len(keys):
        return None
    return airportmodel.Airport.parse_obj(dict(zip(keys, values)))


def result_parser(myresult, detailmsg="No Entries found"):
    results = []
    if len(myresult) == 0:
        raise HTTPException(status_code=404, detail=detailmsg)
    for result in myresult:
        nextairport = parse_to_airport(result)
        results = results + [nextairport]
    return results
