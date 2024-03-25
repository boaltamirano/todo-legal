from pydantic import BaseModel
from datetime import datetime

class UserModel(BaseModel):
    name: str
    email: str
    password: str
    phone: str = ''
    address: str = ''
