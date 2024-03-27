from pydantic import BaseModel, Field, constr, validator
from typing import ClassVar
import re

class AuthModel(BaseModel):
    email_pattern:  ClassVar[str] = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    email:          constr(min_length=3, max_length=320)
    password:       str = Field(min_length=8, max_length= 16)

    @validator("email")
    def validate_email(cls, v):
        if not re.match(cls.email_pattern, v):
            raise ValueError("Invalid email address")
        return v
