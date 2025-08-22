from pydantic import BaseModel

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = True

user = User(
    id=1,
    name="Kolya",
    email="kolyasik@krasava.com",
    # address={"city": "Moskva", "zip_code": "10101"}
    address=Address(city="SPb", zip_code="20202")
)
print(user)
print(user.address.city)