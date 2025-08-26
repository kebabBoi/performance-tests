from clients.grpc.gateway.users.client import build_users_gateway_grpc_client
from clients.grpc.gateway.accounts.client import build_accounts_gateway_grpc_client
from clients.grpc.gateway.operations.client import build_operations_gateway_grpc_client

"""
Пример использования gRPC клиентов для последовательного выполнения операций:
1. Регистрация пользователя в системе
2. Открытие дебетового счета с картой
3. Пополнение баланса счета
"""

# Инициализация клиентов для работы с сервисами пользователей, счетов и документов
users_gateway_client = build_users_gateway_grpc_client()
accounts_gateway_client = build_accounts_gateway_grpc_client()
operations_gateway_client = build_operations_gateway_grpc_client()

# Создание нового пользователя в системе
create_user_response = users_gateway_client.create_user()
print("Create user response:", create_user_response)

# Открытие дебетового счета для созданного пользователя
# Использует ID пользователя из предыдущего шага
open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(create_user_response.user.id)
print("Open debit card account response:", open_debit_card_account_response)

# Выполнение операции пополнения счета
# Использует ID карты (из массива cards) и ID счета из ответа на открытие счета
make_top_up_operation_response = operations_gateway_client.make_top_up_operation(
    card_id=open_debit_card_account_response.account.cards[0].id,
    account_id=open_debit_card_account_response.account.id
)
print("Make top up operation response:", make_top_up_operation_response)
