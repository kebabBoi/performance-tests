from clients.grpc.gateway.users.client import build_users_gateway_grpc_client
from clients.grpc.gateway.accounts.client import build_accounts_gateway_grpc_client
from clients.grpc.gateway.documents.client import build_documents_gateway_grpc_client

"""
Пример использования gRPC клиентов для последовательного выполнения операций:
1. Создание пользователя
2. Открытие кредитного счета
3. Получение документов по счету
"""

# Инициализация клиентов для работы с сервисами пользователей, счетов и документов
users_gateway_http_client = build_users_gateway_grpc_client()
accounts_gateway_http_client = build_accounts_gateway_grpc_client()
documents_gateway_http_client = build_documents_gateway_grpc_client()

# Создание нового пользователя в системе
create_user_response = users_gateway_http_client.create_user()
print("Create user response:", create_user_response)

# Открытие кредитной карты для созданного пользователя
# Использует ID пользователя из предыдущего шага
open_credit_card_account = accounts_gateway_http_client.open_credit_card_account(create_user_response.user.id)
print("Open credit card response:", open_credit_card_account)

# Получение тарифного документа для открытой кредитной карты
# Использует ID счета из предыдущего шага
get_tariff_document_response = documents_gateway_http_client.get_tariff_document(open_credit_card_account.account.id)
print("Get tariff document response:", get_tariff_document_response)

# Получение договора для открытой кредитной карты
# Использует ID счета из шага 2
get_contract_document_response = documents_gateway_http_client.get_contract_document(
    open_credit_card_account.account.id)
print("Get contract document:", get_contract_document_response)
