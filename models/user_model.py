from pydantic import BaseModel, Field
from typing import Optional

class UserModel(BaseModel):
    _id :       Optional[str] = None
    name:       str = Field(min_length=3, max_length= 50)
    email:      str = Field("example@example.com")
    password:   str
    phone:      Optional[str] = Field(min_length=10, max_length= 10)
    address:    Optional[str] = Field(min_length=3, max_length= 50)

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