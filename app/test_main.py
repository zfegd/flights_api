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


# Get TZ Tests
# tests - empty query, no query,


def test_get_tz_hyphenformat():
    response = client.get("/v0.1/tzformat?tz=Asia/Ulaanbaatar")
    assert response.status_code == 200


def test_get_tz_with_underscore():
    response = client.get("/v0.1/tzformat?tz=Asia/Phnom_Penh")
    assert response.status_code == 200


def test_get_tz_valid_but_no_entry():
    response = client.get("/v0.1/tzformat?tz=Etc/GMT")
    assert response.status_code == 404


def test_get_tz_invalid_timezone():
    response = client.get("/v0.1/tzformat?tz=Asia/Gangnam")
    assert response.status_code == 404


def test_get_tz_uncapped():
    response = client.get("/v0.1/tzformat?tz=asia/ulaanbaatar")
    assert response.status_code == 404


def test_get_tz_deprecated():
    response = client.get("/v0.1/tzformat?tz=Australia/Canberra")
    assert response.status_code == 404


def test_get_tz_regex_fail():
    response = client.get("/v0.1/tzformat?tz=America/Antigua%20%26%20Barbuda")
    assert response.status_code == 422


def test_get_tz_empty_query():
    response = client.get("/v0.1/tzformat?tz=")
    assert response.status_code == 422


def test_get_tz_no_query():
    response = client.get("/v0.1/tzformat?")
    assert response.status_code == 422


# Get dst Tests


def test_get_all_valid_dst():
    validzones = ["E", "A", "S", "O", "Z", "N", "U"]
    for zone in validzones:
        response = client.get("/v0.1/dst?dst=" + zone)
        assert response.status_code == 200


def test_get_dst_regex_wrong_char():
    response = client.get("/v0.1/dst?dst=C")
    assert response.status_code == 422


def test_get_dst_regex_wrong_caps():
    response = client.get("/v0.1/dst?dst=e")
    assert response.status_code == 422


def test_get_dst_regex_wrong_len():
    response = client.get("/v0.1/dst?dst=NO")
    assert response.status_code == 422


def test_get_dst_regex_multifail():
    response = client.get("/v0.1/dst?dst=Ez1")
    assert response.status_code == 422


def test_get_dst_empty_query():
    response = client.get("/v0.1/dst?dst=")
    assert response.status_code == 422


def test_get_dst_no_query():
    response = client.get("/v0.1/dst?")
    assert response.status_code == 422


# Get utc Tests


def test_get_utc_neg():
    response = client.get("/v0.1/utc?time_zone=-11")
    assert response.status_code == 200


def test_get_utc_neg_two():
    response = client.get("/v0.1/utc?time_zone=-5")
    assert response.status_code == 200


def test_get_utc_pos():
    response = client.get("/v0.1/utc?time_zone=13")
    assert response.status_code == 200


def test_get_utc_pos_two():
    response = client.get("/v0.1/utc?time_zone=5")
    assert response.status_code == 200


def test_get_utc_neutral():
    response = client.get("/v0.1/utc?time_zone=0")
    assert response.status_code == 200


def test_get_utc_halfhr():
    response = client.get("/v0.1/utc?time_zone=3.5")
    assert response.status_code == 200


def test_get_utc_oddity():
    response = client.get("/v0.1/utc?time_zone=5.75")
    assert response.status_code == 200


def test_get_utc_too_big():
    response = client.get("/v0.1/utc?time_zone=89")
    assert response.status_code == 400


def test_get_utc_too_small():
    response = client.get("/v0.1/utc?time_zone=-55")
    assert response.status_code == 400


def test_get_utc_nonexistent():
    response = client.get("/v0.1/utc?time_zone=-10.75")
    assert response.status_code == 404


def test_get_utc_validbutbad_regexformat():
    response = client.get("/v0.1/utc?time_zone=02")
    assert response.status_code == 404


def test_get_utc_regex_fail():
    response = client.get("/v0.1/utc?time_zone=+8")
    assert response.status_code == 422


def test_get_utc_regex_fail_two():
    response = client.get("/v0.1/utc?time_zone=8:00")
    assert response.status_code == 422


def test_get_utc_regex_fail_three():
    response = client.get("/v0.1/utc?time_zone=2.00")
    assert response.status_code == 422


def test_get_utc_regex_fail_length():
    response = client.get("/v0.1/utc?time_zone=111")
    assert response.status_code == 422


def test_get_utc_empty_query():
    response = client.get("/v0.1/utc?time_zone=")
    assert response.status_code == 422


def test_get_utc_no_query():
    response = client.get("/v0.1/utc?")
    assert response.status_code == 422
