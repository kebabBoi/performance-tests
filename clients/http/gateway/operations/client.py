from clients.http.client import HTTPClient

from httpx import Response, QueryParams, request

from typing import TypedDict

from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    """
    Структура данных, представляющая операцию.
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str

class OperationSummaryDict(TypedDict):
    """
    Структура данных, представляющая сводку по операциям.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float

class OperationReceiptDict(TypedDict):
    """
   Структура данных, представляющая чек операции.
    """
    url: str
    document: str

class MakeOperationRequestDict(TypedDict):
    """
    Базовая структура данных для создания операции.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций по счёту.
    """
    accountId: str

class GetOperationsResponseDict(TypedDict):
    operations: list[OperationDict]

class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения сводки по операциям.
    """
    accountId: str

class GetOperationsSummaryResponseDict(TypedDict):
    """
    Структура данных ответа на запрос получения сводки по операциям.
    """
    summary: OperationSummaryDict

class GetOperationReceiptResponseDict(TypedDict):
    """
    Структура данных ответа на запрос получения чека операции.
    """
    receipt: OperationReceiptDict

class GetOperationResponseDict(TypedDict):
    """
    Структура данных ответа на запрос получения информации об операции.
    """
    operation: OperationDict

class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции комиссии.
    Наследует все атрибуты от MakeOperationRequestDict.
    """
    pass

class MakeFeeOperationResponseDict(TypedDict):
    """
    Структура данных ответа на запрос создания операции комиссии.
    """
    operation: OperationDict

class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции пополнения счёта.
    Наследует все атрибуты от MakeOperationRequestDict.
    """
    pass

class MakeTopUpOperationResponseDict(TypedDict):
    """
    Структура данных ответа на запрос создания операции пополнения счёта.
    """
    operation: OperationDict

class MakeCashBackOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции кэшбэка.
    Наследует все атрибуты от MakeOperationRequestDict.
    """
    pass

class MakeCashBackOperationResponseDict(TypedDict):
    """
   Структура данных ответа на запрос создания операции кэшбэка.
    """
    operation: OperationDict

class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции перевода.
    Наследует все атрибуты от MakeOperationRequestDict.
    """
    pass

class MakeTransferOperationResponseDict(TypedDict):
    """
    Структура данных ответа на запрос создания операции перевода.
    """
    operation: OperationDict

class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции покупки.
    """
    category: str

class MakePurchaseOperationResponseDict(TypedDict):
    """
    Структура данных ответа на запрос создания операции покупки.
    """
    operation: OperationDict

class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции оплаты счёта.
    Наследует все атрибуты от MakeOperationRequestDict.
    """
    pass

class MakeBillPaymentOperationResponseDict(TypedDict):
    """
    Структура данных ответа на запрос создания операции оплаты счёта.
    """
    operation: OperationDict

class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции снятия наличных.
    Наследует все атрибуты от MakeOperationRequestDict.
    """
    pass

class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """
    Структура данных ответа на запрос создания операции снятия наличных.
    """
    operation: OperationDict

class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operatios сервиса http-gateway.
    """

    def get_operations_api(self, query: GetOperationsQueryDict):
        """
        Выполняет GET-запрос для получения списка операций для опрделенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с информацией об операции.
        """
        return self.get("/api/v1/operations/", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict):
        """
        Выполняет GET-запрос для получения статистики по операциям счёта.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response со статистикой по операциям для определенного счета.
        """
        return self.get("/api/v1/operations/operations-summary/", params=QueryParams(**query))

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос для получения чека операции.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с данными чека операции.
        """
        return self.get(f"api/v1/operations/operation-receipt/{operation_id}")

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос для получения информации об операции.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response со списком операций для определенного счета.
        """
        return self.get(f"api/v1/operations/{operation_id}")

    def make_fee_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param request: Словарь с данными для создания операции комиссии.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения счёта.

        :param request: Словарь с данными для создания операции пополнения.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Словарь с данными для создания операции кэшбэка.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Словарь с данными для создания операции перевода.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Словарь с данными для создания операции покупки.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счёту.

        :param request: Словарь с данными для создания операции оплаты счёта.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill_payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции снятия наличных.

        :param request: Словарь с данными для создания операции снятия наличных.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=100.15,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=100.15,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cash_back_operation(self, card_id: str, account_id: str) -> MakeCashBackOperationResponseDict:
        request = MakeCashBackOperationRequestDict(
            status="COMPLETED",
            amount=100.15,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=100.15,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=100.15,
            cardId=card_id,
            accountId=account_id,
            category="taxi"
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=100.15,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=100.15,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()

def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр CardsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CardsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())