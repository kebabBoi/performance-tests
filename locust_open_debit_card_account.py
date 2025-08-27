from locust import HttpUser, between, task

from tools.fakers import fake  # генератор случайных данных


class GetUserScenarioUser(HttpUser):
    # Пауза между запросами для каждого виртуального пользователя (в секундах)
    wait_time = between(1, 3)

    # В этой переменной будем хранить данные созданного пользователя
    user_data: dict

    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь мы создаем нового пользователя, отправляя POST-запрос к /api/v1/users.
        """
        request = {
            "email": fake.email(),
            "lastName": fake.last_name(),
            "firstName": fake.first_name(),
            "middleName": fake.middle_name(),
            "phoneNumber": fake.phone_number()
        }
        response = self.client.post("/api/v1/users", json=request)

        # Сохраняем полученные данные, включая ID пользователя
        self.user_data = response.json()


    @task
    def post_open_debit_card_account(self):
        """
        Основная нагрузочная задача: открытие дебетового счета пользователю.
        Здесь выполняется POST-запрос к /api/v1/accounts/open-debit-card-account.
        """
        request = {
            "userId": f"{self.user_data['user']['id']}"
        }

        self.client.post("/api/v1/accounts/open-debit-card-account", json=request)