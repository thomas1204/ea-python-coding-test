from typing import Optional
from pydantic import BaseModel, EmailStr


class Customer(BaseModel):
    # customerid: Optional[int]
    firstname: str
    lastname: str
    email: EmailStr
    phone: str
    username: str
    password: str
    age: int
    gender: str
    address1: str
    address2: str
    city: str
    state: str
    region: int
    zip: int
    country: str
    creditcardtype: int
    creditcard: str
    creditcardexpiration: str
    income: int
