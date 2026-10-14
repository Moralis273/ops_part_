from locust import HttpUser, task, between

#локуст будет создавать экземпляры этого класса , виратуальных пользователей, которые отправляют запросы

class MLService(HttpUser):
    wait_time=between(1,2)
    @task
    def predict(self):
        payload={"age":40,"purchase_amount":300}
        self.client.post("/predict",json=payload)