import uuid

from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserSchema(BaseModel):
    """
    Схема данных пользователя.
    """
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")

class CreateUserRequestSchema(BaseModel):
    """
    Схема данных для запроса создания пользователя.
    """
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")

class CreateUserResponseSchema(UserSchema):
    """
    Схема данных для ответа на запрос создания пользователя.
    Наследует все атрибуты от UserSchema и добавляет поле user.
    """
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )
    user: UserSchema