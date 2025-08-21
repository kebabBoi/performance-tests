from clients.http.gateway.users.client import build_users_gateway_http_client
from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.documents.client import build_documents_gateway_http_client

users_gateway_http_client = build_users_gateway_http_client()
accounts_gateway_http_client = build_accounts_gateway_http_client()
documents_gateway_http_client = build_documents_gateway_http_client()

create_user_response = users_gateway_http_client.create_user()
print("Create user response:", create_user_response)

open_credit_card_account = accounts_gateway_http_client.open_credit_card_account(create_user_response['user']['id'])
print("Open credit card response:", open_credit_card_account)

get_tariff_document_response = documents_gateway_http_client.get_tariff_document(open_credit_card_account['account']['id'])
print("Get tariff document response:", get_tariff_document_response)

get_contract_document_response = documents_gateway_http_client.get_contract_document(open_credit_card_account['account']['id'])
print("Get contract document:", get_contract_document_response)