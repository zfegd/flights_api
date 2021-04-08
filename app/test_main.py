from fastapi.testclient import TestClient
from main import app
# from .main import app


client = TestClient(app)


# Get Airport Tests


def test_get_valid_airport():
    response = client.get("/v0.1/airport?airport_name=Heathrow")
    assert response.status_code == 200
    assert len(response.json()) == 1


# def test_get_airport_randomcaps():
#     response = client.get("/v0.1/airport?airport_name=hEatHrOw")
#     assert response.status_code == 200
#     assert len(response.json()) == 1
#
#
# def test_get_airport_special():
#     response = client.get("/v0.1/airport?airport_name=Biała")
#     assert response.status_code == 200
#     assert len(response.json()) == 1


# def test_get_airport_fail():
#     response = client.get("/airport/kjsjdks")
#     assert response.status_code == 404
#
# test [&], &, multi words, empty query
#
# ## Get by Country Tests ##
#
# def test_get_country_airport():
#     response = client.get("/country/Singapore")
#     assert response.status_code == 200
#     assert len(response.json()) != 0
#
# def test_get_country_airport_randomcaps():
#     response = client.get("/country/sIngApORe")
#     assert response.status_code == 200
#     assert len(response.json()) != 0
#
# def test_get_country_airport_multiwords():
#     response = client.get("/country/united%20kingdom")
#     assert response.status_code == 200
#     assert len(response.json()) != 0
#
# def test_get_country_airport_fail():
#     response = client.get("/country/kjsjdks")
#     assert response.status_code == 404
#
#
# ## Get City Tests ##
#
# def test_get_city_airport():
#     response = client.get("/airport/London")
#     assert response.status_code == 200
#     assert len(response.json()) > 1
#
# def test_get_city_airport_randomcaps():
#     response = client.get("/airport/lOnDoN")
#     assert response.status_code == 200
#     assert len(response.json()) > 1
#
# def test_get_city_airport_multiwords():
#     response = client.get("/country/Biała%20Podlaska")
#     assert response.status_code == 200
#     assert len(response.json()) != 0
#
# def test_get_city_airport_hyphen():
#     response = client.get("/country/Bielsko-Biala")
#     assert response.status_code == 200
#     assert len(response.json()) == 1
#
# def test_get_city_airport_fail():
#     response = client.get("/airport/kjsjdks")
#     assert response.status_code == 404
#
# ## Get Timezone tests ##
#
# def test_get_timezone_airports_negative():
#     response = client.get("/timezone/-8")
#     assert response.status_code == 200
#     assert len(response.json()) > 1
#
#
# def test_get_timezone_airports_positive():
#     response = client.get("/timezone/13")
#     assert response.status_code == 200
#     assert len(response.json()) > 1
#
# def test_get_timezone_airports_utc():
#     response = client.get("/timezone/0")
#     assert response.status_code == 200
#     assert len(response.json()) > 1
#
# def test_get_timezone_airports_str():
#     response = client.get("/timezone/askla")
#     assert response.status_code == 400
#
# def test_get_timezone_airports_wrongint():
#     response = client.get("/timezone/200")
#     assert response.status_code == 400
#
# def test_get_timezone_airports_wrongfloat():
#     response = client.get("/timezone/10.233")
#     assert response.status_code == 404
