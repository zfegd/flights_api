from fastapi.testclient import TestClient
from main import app
# from .main import app


client = TestClient(app)


# Get Airport Tests


def test_get_valid_airport():
    response = client.get("/v0.1/airport?airport_name=Heathrow")
    assert response.status_code == 200


def test_get_airport_randomcaps():
    response = client.get("/v0.1/airport?airport_name=hEatHrOw")
    assert response.status_code == 200


def test_get_airport_special():
    response = client.get("/v0.1/airport?airport_name=Biała")
    assert response.status_code == 200


def test_get_airport_no_entries():
    response = client.get("/airport/kjsjdks")
    assert response.status_code == 404


def test_get_airport_sanitised_regex():
    response = client.get("/v0.1/airport?airport_name=%5B%26%5D")
    assert response.status_code == 404


def test_get_airport_sanitised_regex_two():
    response = client.get("/v0.1/airport?airport_name=%5Ba-zA-Z%5D")
    assert response.status_code == 404


def test_get_airport_valid_ampersand():
    response = client.get("/v0.1/airport?airport_name=%26")
    assert response.status_code == 200


def test_get_airport_empty_query():
    response = client.get("/v0.1/airport?airport_name=")
    assert response.status_code == 200
    assert len(response.json()) == 7698


def test_get_airport_no_query():
    response = client.get("/v0.1/airport?")
    assert response.status_code == 422


def test_get_airport_multiwords():
    response = client.get("/v0.1/airport?airport_name=city%20airport")
    assert response.status_code == 200


# Get by Country Tests


def test_get_country_airport():
    response = client.get("/v0.1/country?country_name=Singapore")
    assert response.status_code == 200
    assert len(response.json()) != 0


def test_get_country_airport_randomcaps():
    response = client.get("/v0.1/country?country_name=sIngApORe")
    assert response.status_code == 200
    assert len(response.json()) != 0


def test_get_country_airport_multiwords():
    response = client.get("/v0.1/country?country_name=united%20kingdom")
    assert response.status_code == 200
    assert len(response.json()) != 0


def test_get_country_airport_no_entries():
    response = client.get("/v0.1/country?country_name=kjsjdks")
    assert response.status_code == 404


def test_get_country_regex():
    response = client.get("/v0.1/country?country_name=%5Ba-zA-Z%5D")
    assert response.status_code == 404


def test_get_country_empty_query():
    response = client.get("/v0.1/country?country_name=")
    assert response.status_code == 404


def test_get_country_no_query():
    response = client.get("/v0.1/country?")
    assert response.status_code == 422


# Get City Tests


def test_get_city_airport():
    response = client.get("/v0.1/city?city_name=London")
    assert response.status_code == 200
    assert len(response.json()) > 1


def test_get_city_airport_randomcaps():
    response = client.get("/v0.1/city?city_name=lOnDoN")
    assert response.status_code == 200
    assert len(response.json()) > 1


def test_get_city_airport_multiwords():
    response = client.get("/v0.1/city?city_name=Biała%20Podlaska")
    assert response.status_code == 200
    assert len(response.json()) != 0


def test_get_city_airport_hyphen():
    response = client.get("/v0.1/city?city_name=Bielsko-Biala")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_city_airport_no_entries():
    response = client.get("/v0.1/city?city_name=kjsjdks")
    assert response.status_code == 404


def test_get_city_regex():
    response = client.get("/v0.1/city?city_name=%5Ba-zA-Z%5D")
    assert response.status_code == 404


def test_get_city_empty_query():
    response = client.get("/v0.1/city?city_name=")
    assert response.status_code == 404


def test_get_city_no_query():
    response = client.get("/v0.1/city?")
    assert response.status_code == 422


# Get IATA Tests


def test_get_iata_airport():
    response = client.get("/v0.1/IATA?iata_code=LHR")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_iata_wrong():
    response = client.get("/v0.1/IATA?iata_code=ZZZ")
    assert response.status_code == 404


def test_get_iata_regex_noncaps():
    response = client.get("/v0.1/IATA?iata_code=lhr")
    assert response.status_code == 422


def test_get_iata_regex_length_short():
    response = client.get("/v0.1/IATA?iata_code=HR")
    assert response.status_code == 422


def test_get_iata_regex_length_long():
    response = client.get("/v0.1/IATA?iata_code=EGLL")
    assert response.status_code == 422


def test_get_iata_regex_multifailure():
    response = client.get("/v0.1/IATA?iata_code=l2HR")
    assert response.status_code == 422


def test_get_iata_empty_query():
    response = client.get("/v0.1/IATA?iata_code=")
    assert response.status_code == 422


def test_get_iata_no_query():
    response = client.get("/v0.1/IATA?")
    assert response.status_code == 422


# Get ICAO Tests


def test_get_icao_airport():
    response = client.get("/v0.1/ICAO?icao_code=EGLL")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_icao_wrong():
    response = client.get("/v0.1/ICAO?icao_code=ZZZZ")
    assert response.status_code == 404


def test_get_icao_regex_noncaps():
    response = client.get("/v0.1/ICAO?icao_code=egll")
    assert response.status_code == 422


def test_get_icao_regex_length_short():
    response = client.get("/v0.1/ICAO?icao_code=HR")
    assert response.status_code == 422


def test_get_icao_regex_length_long():
    response = client.get("/v0.1/ICAO?icao_code=EGGZZ")
    assert response.status_code == 422


def test_get_icao_regex_multifailure():
    response = client.get("/v0.1/ICAO?icao_code=lA2HRs")
    assert response.status_code == 422


def test_get_icao_empty_query():
    response = client.get("/v0.1/ICAO?icao_code=")
    assert response.status_code == 422


def test_get_icao_no_query():
    response = client.get("/v0.1/ICAO?")
    assert response.status_code == 422

# get tz tests
# tests - pass defaultformat, pass formatnohypen, pass with number,
# pass w underscore, invalid timezone, regexfail chars, empty query, no query,


# get dst tests
# tests - pass x7, regexfail char, regexfail length, regexfail multi,
# empty query, no query

# get utc tests
# pass neg singledigit, pass neg doubledigit, pass positive singledigit,
# pass positive doubledigit, pass 0, pass halfhr, pass 45mins, fail toobig,
# fail tooneg, nonexistent timezone, pass badregexformats (eg 02),
# regexfail char, regexfail length, regexfail mix, empty query, no query
