from pydantic import BaseModel, EmailStr
from typing import Optional


class UsersForm(BaseModel):
    name: str
    email: EmailStr
    hashed_password: str
    phone_number: str
    address: str
    is_active: bool

class InsuranceForm(BaseModel):
    user: int

class QRPAgentForm(BaseModel):
    nambve: str
    email : EmailStr
    hashed_password: str
    state: str
    address: str
    phone_number: str
    is_active: str



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None

class ForgetPassword(BaseModel):
    email: str



class BlacklistToken(BaseModel):
    email: EmailStr
    token: str

class ResetPassword(BaseModel):
    new_password: str
    confirm_password: str
