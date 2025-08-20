from httpx import Response

from typing import TypedDict

from clients.http.client import HTTPClient

class CreateCardResponseDict(TypedDict):
    """
    Структура данных для создания новой карты.
    """
    userId: str
    accountId: str

class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: CreateCardResponseDict) -> Response:
        return self.post("/api/v1/cards/issue-virtual-card",json=request)
    """
    Создание виртуальной карты.

    :param request: Словарь с данными для создания виртуальной карты.
    :return: Ответ от сервера (объект httpx.Response).
    """

    def issue_physical_card_api(self, request: CreateCardResponseDict) -> Response:
        return self.post("/api/v1/cards/issue-physical-card", json=request)
    """
    Создание физической карты.

    :param request: Словарь с данными для создания физической карты.
    :return: Ответ от сервера (объект httpx.Response).
    """