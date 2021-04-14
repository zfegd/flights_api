from fastapi import HTTPException
from models import airportmodel


def airports_zip_to_dict(values):
    keys = airportmodel.get_fields()
    if len(values) != len(keys):
        return None
    return dict(zip(keys, values))


def result_parser(myresult, detailmsg="No Entries found"):
    results = []
    if len(myresult) == 0:
        raise HTTPException(status_code=404, detail=detailmsg)
    for result in myresult:
        nextairport = airports_zip_to_dict(result)
        results = results + [nextairport]
    return results
