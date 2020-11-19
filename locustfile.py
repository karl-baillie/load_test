from locust import HttpUser, task, between


class MyUser(HttpUser):

    @task
    def index(self):
        self.client.get("/fc/healthcheck")