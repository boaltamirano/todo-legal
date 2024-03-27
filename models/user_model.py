from pydantic import BaseModel, Field, constr, validator
from typing import Optional, ClassVar
import re

class UserModel(BaseModel):
    id :            Optional[str] = ""
    name:           str = Field(min_length=3, max_length= 50)
    email_pattern:  ClassVar[str] = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    email:          constr(min_length=3, max_length=320)
    password:       str = Field(min_length=8, max_length= 16)
    phone:          Optional[str] = Field(None, min_length=10, max_length= 10)
    address:        Optional[str] = Field(None, min_length=3, max_length= 50)

    @validator("email")
    def validate_email(cls, v):
        if not re.match(cls.email_pattern, v):
            raise ValueError("Invalid email address")
        return v

class UserResponse(BaseModel):
    id :        str
    name:       str
    email:      str
    phone:      Optional[str] = None
    address:    Optional[str] = None
    created_at: int
    updated_at: int

    
class UserToken(BaseModel):
    token:      str 
    user:       UserResponse 