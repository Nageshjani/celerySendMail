from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def my_task(self):
        self.client.get('http://127.0.0.1:8000/mail/')
        #self.client.get('/')
