from pydantic import BaseModel, Field

class AuthModel(BaseModel):
    email:  str = Field("example@example.com")
    password:   str