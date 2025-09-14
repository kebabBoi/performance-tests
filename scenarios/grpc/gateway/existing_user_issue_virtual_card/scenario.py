# Проверьте, пожалуйста, прошлое задание "Практика нагрузочного тестирования. Часть 2. Практика: Получение операций существующим пользователем(grpc)"
# Допустил ошибку при вводе команды пуша, а заметил только видимо в момент, когда Вы проверяли задание, прошу прощения за такой инцидент.

from locust import task, events
from locust.env import Environment
from tools.locust.user import LocustBaseUser

from clients.grpc.gateway.locust import GatewayGRPCTaskSet
from seeds.scenarios.existing_user_issue_virtual_card import ExistingUserIssueVirtualCardSeedsScenario
from seeds.schema.result import SeedUserResult


@events.init.add_listener
def init(environment: Environment, **kwargs):
    seeds_scenario = ExistingUserIssueVirtualCardSeedsScenario()
    seeds_scenario.build()

    environment.seeds = seeds_scenario.load()


class IssueVirtualCardTaskSet(GatewayGRPCTaskSet):
    seed_user: SeedUserResult

    def on_start(self) -> None:
        super().on_start()
        self.seed_user = self.user.environment.seeds.get_random_user()

    @task(3)
    def get_accounts(self):
        self.accounts_gateway_client.get_accounts(
            user_id=self.seed_user.user_id
        )

    @task(1)
    def issue_virtual_card(self):
        self.cards_gateway_client.issue_virtual_card(
            user_id=self.seed_user.user_id,
            account_id=self.seed_user.debit_card_accounts[0].account_id
        )


class IssueVirtualCardScenarioUser(LocustBaseUser):
    tasks = [IssueVirtualCardTaskSet]