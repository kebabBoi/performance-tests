from clients.http.client import HTTPClient

from httpx import Response, QueryParams

from typing import TypedDict

class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций по счёту.
    """
    accountId: str

class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения сводки по операциям.
    """
    accountId: str

class MakeOperationRequestDict(TypedDict):
    """
    Базовая структура данных для создания операции.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции покупки.
    """
    category: str

class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operatios сервиса http-gateway.
    """

    def get_operation_api(self, query: GetOperationsQueryDict):
        """
        Выполняет GET-запрос для получения информациеи об операции.

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

    def get_operations_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос для получения списка операций для опрделенного счета.

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
        return self.post("/api/v1/operations/make_top_up_operation", json=request)

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
        return self.post("/api/v1/operations/make-cash_withdrawal-operation", json=request)