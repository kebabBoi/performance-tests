from locust import User, between, task

from clients.grpc.gateway.users.client import UsersGatewayGRPCClient, build_users_gateway_locust_grpc_client
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse

from clients.grpc.gateway.accounts.client import AccountsGatewayGRPCClient, build_accounts_gateway_locust_grpc_client
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountResponse


class GetUserScenarioUser(User):
    # Обязательное поле, требуемое Locust. Будет проигнорировано, но его нужно указать, иначе будет ошибка запуска.
    host = "localhost"

    # Пауза между запросами для каждого виртуального пользователя (в секундах)
    wait_time = between(1, 3)

    users_gateway_client: UsersGatewayGRPCClient
    create_users_response: CreateUserResponse

    accounts_gateway_client: AccountsGatewayGRPCClient
    open_debit_card_account_response: OpenDebitCardAccountResponse

    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь мы создаем нового пользователя, отправляя POST-запрос к /api/v1/users.
        """
        self.users_gateway_client = build_users_gateway_locust_grpc_client(self.environment)

        self.create_users_response = self.users_gateway_client.create_user()
        self.accounts_gateway_client = build_accounts_gateway_locust_grpc_client(self.environment)


    @task
    def post_open_debit_card_account(self):
        """
        Основная нагрузочная задача: открытие дебетового счета пользователю.
        Здесь выполняется POST-запрос к /api/v1/accounts/open-debit-card-account.
        """
        self.open_debit_card_account_response = self.accounts_gateway_client.open_debit_card_account(self.create_users_response.user.id)