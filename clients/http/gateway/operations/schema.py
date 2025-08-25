from pydantic import BaseModel, HttpUrl, Field, ConfigDict
from enum import StrEnum
from tools.fakers import fake

class OperationType(StrEnum):
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"

class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"

class OperationSchema(BaseModel):
    """
    Структура данных, представляющая операцию.
    """
    model_config = ConfigDict(populate_by_name=True)
    id: str
    type: OperationType
    status: str
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class OperationSummarySchema(BaseModel):
    """
    Структура данных, представляющая сводку по операциям.
    """
    model_config = ConfigDict(populate_by_name=True)
    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")

class OperationReceiptSchema(BaseModel):
    """
   Структура данных, представляющая чек операции.
    """
    url: HttpUrl
    document: str

class MakeOperationRequestSchema(BaseModel):
    """
    Базовая структура данных для создания операции.
    """
    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения списка операций по счёту.
    """
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")

class GetOperationsResponseSchema(BaseModel):
    operations: list[OperationSchema]

class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура данных для получения сводки по операциям.
    """
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")

class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Структура данных ответа на запрос получения сводки по операциям.
    """
    summary: OperationSummarySchema

class GetOperationReceiptResponseSchema(BaseModel):
    """
    Структура данных ответа на запрос получения чека операции.
    """
    receipt: OperationReceiptSchema

class GetOperationResponseSchema(BaseModel):
    """
    Структура данных ответа на запрос получения информации об операции.
    """
    operation: OperationSchema

class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции комиссии.
    Наследует все атрибуты от MakeOperationRequestSchema.
    """
    pass

class MakeFeeOperationResponseSchema(BaseModel):
    """
    Структура данных ответа на запрос создания операции комиссии.
    """
    operation: OperationSchema

class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции пополнения счёта.
    Наследует все атрибуты от MakeOperationRequestSchema.
    """
    pass

class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Структура данных ответа на запрос создания операции пополнения счёта.
    """
    operation: OperationSchema

class MakeCashBackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции кэшбэка.
    Наследует все атрибуты от MakeOperationRequestSchema.
    """
    pass

class MakeCashBackOperationResponseSchema(BaseModel):
    """
   Структура данных ответа на запрос создания операции кэшбэка.
    """
    operation: OperationSchema

class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции перевода.
    Наследует все атрибуты от MakeOperationRequestSchema.
    """
    pass

class MakeTransferOperationResponseSchema(BaseModel):
    """
    Структура данных ответа на запрос создания операции перевода.
    """
    operation: OperationSchema

class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции покупки.
    """
    category: str = Field(default_factory=fake.category)

class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Структура данных ответа на запрос создания операции покупки.
    """
    operation: OperationSchema

class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции оплаты счёта.
    Наследует все атрибуты от MakeOperationRequestSchema.
    """
    pass

class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Структура данных ответа на запрос создания операции оплаты счёта.
    """
    operation: OperationSchema

class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции снятия наличных.
    Наследует все атрибуты от MakeOperationRequestSchema.
    """
    pass

class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Структура данных ответа на запрос создания операции снятия наличных.
    """
    operation: OperationSchema