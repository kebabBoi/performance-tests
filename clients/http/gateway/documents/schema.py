from pydantic import BaseModel, HttpUrl

class DocumentSchema(BaseModel):
    """
    Описание структуры документов.
    """
    url: HttpUrl
    document: str

class GetTariffDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа выдачи документа тарифа.
    """
    tariff: DocumentSchema

class GetContractDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа выдачи документа контракта.
    """
    contract: DocumentSchema