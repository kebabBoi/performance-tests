from locust import TaskSet, task, HttpUser, between

class MyTaskSet(TaskSet):
    @task
    def task_one(self):
        self.client.get("/page1")

    @task
    def task_two(self):
        self.client.get("/page2")

class MyUser(HttpUser):
    wait_time = between(1,3)
    tasks = [MyTaskSet]
