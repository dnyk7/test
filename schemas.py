# schema.py

from typing import List
from pydantic import BaseModel

from backend.models import Account

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    accounts: list
    # accounts: List[Account] = []

    class Config:
        # orm_mode = True
        from_attributes = True

# from fren
class TransactionBase(BaseModel):
    amount: int
    from_account_id: int
    to_account_id: int

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True