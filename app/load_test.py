from locust import HttpUser, between, task


class MyUser(HttpUser):

    wait_time = between(5, 15)
    host = 'http://127.0.0.1'

    @task
    def get_airport_correct(self):
        self.client.get("/v0.1/airport?airport_name=Heathrow")

    @task
    def get_airport_long_result(self):
        self.client.get("/v0.1/airport?airport_name=a")



# class UserBehavior(TaskSet):
#
#     @task
#     def get_airport_correct(self):
#         self.client.get("/v0.1/airport?airport_name=Heathrow")
#
#     @task
#     def get_airport_no_entries(self):
#         self.client.get("/v0.1/airport?airport_name=kjsjdks")
#
#     @task
#     def get_airport_long_result(self):
#         self.client.get("/v0.1/airport?airport_name=a")
#
#     @task
#     def get_airport_invalid(self):
#         self.client.get("/v0.1/airport?airport_name=")
#
#
# class WebsiteUser(HttpUser):
#     task_set = UserBehavior
#     host = 'http://127.0.0.1'
#     min_wait = 5000
#     max_wait = 9000
