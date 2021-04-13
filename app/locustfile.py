from locust import HttpUser, between, task


class MyUser(HttpUser):

    wait_time = between(1, 10)

    @task
    def get_airport_small(self):
        self.client.get("/v1/airport?airport_name=Heathrow")

    @task
    def get_airport_long_result(self):
        self.client.get("/v1/airport?airport_name=a")

    @task
    def get_airport_medium(self):
        self.client.get("/v1/airport?airport_name=city")

    @task
    def get_country_small(self):
        self.client.get("/v1/country?country_name=Singapore")

    @task
    def get_country_medium(self):
        self.client.get("/v1/country?country_name=Greece")

    @task
    def get_country_large(self):
        self.client.get("/v1/country?country_name=China")

    @task
    def get_city_small(self):
        self.client.get("/v1/city?city_name=Singapore")

    @task
    def get_city_mediun(self):
        self.client.get("/v1/city?city_name=London")

    @task
    def get_iata(self):
        self.client.get("/v1/IATA?iata_code=LHR")

    @task
    def get_icao(self):
        self.client.get("/v1/ICAO?icao_code=EGLL")

    @task
    def get_tz(self):
        self.client.get("/v1/tzformat?tz=Asia/Ulaanbaatar")

    @task
    def get_dst(self):
        self.client.get("/v1/dst?dst=E")

    @task
    def get_utc_pos(self):
        self.client.get("/v1/utc?time_zone=13")

    @task
    def get_utc_neg(self):
        self.client.get("/v1/utc?time_zone=-5")

    @task
    def get_utc_neutral(self):
        self.client.get("/v1/utc?time_zone=0")

    @task
    def get_utc_decimal(self):
        self.client.get("/v1/utc?time_zone=5.75")

    @task
    def get_geobox(self):
        url = "/v1/geobox/?southlat=20&northlat=22&westlon=100&eastlon=140"
        self.client.get(url)
