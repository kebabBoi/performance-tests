from locust import User, between, task

from clients.http.gateway.users.client import build_users_gateway_locust_http_client, UsersGatewayHTTPClient
from clients.http.gateway.users.schema import CreateUserResponseSchema

from clients.http.gateway.accounts.client import build_accounts_gateway_locust_http_client, AccountsGatewayHTTPClient
from clients.http.gateway.accounts.schema import OpenDebitCardAccountResponseSchema


class GetUserScenarioUser(User):
    # Обязательное поле, требуемое Locust. Будет проигнорировано, но его нужно указать, иначе будет ошибка запуска.
    host = "localhost"

    # Пауза между запросами для каждого виртуального пользователя (в секундах)
    wait_time = between(1, 3)

    users_gateway_client: UsersGatewayHTTPClient
    create_users_response: CreateUserResponseSchema

    accounts_gateway_client: AccountsGatewayHTTPClient
    open_debit_card_account_response: OpenDebitCardAccountResponseSchema

    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь мы создаем нового пользователя, отправляя POST-запрос к /api/v1/users.
        """
        self.users_gateway_client = build_users_gateway_locust_http_client(self.environment)

        self.create_users_response = self.users_gateway_client.create_user()


    @task
    def post_open_debit_card_account(self):
        """
        Основная нагрузочная задача: открытие дебетового счета пользователю.
        Здесь выполняется POST-запрос к /api/v1/accounts/open-debit-card-account.
        """
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.environment)

        self.open_debit_card_account_response = self.accounts_gateway_client.open_debit_card_account(self.create_users_response.user.id)