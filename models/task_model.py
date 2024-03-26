from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
from models.user_model import UserResponse

class TaskModel(BaseModel):
    _id :           Optional[str] = None
    title:          str = Field(min_length=3, max_length= 50)
    description:    Optional[str] = Field(min_length=3, max_length= 150)
    status:         Optional[str]= None
    deadline:       Optional[int] = None
    user_id:        str = Field(min_length=32, max_length= 32)

class TaskResponse(BaseModel):
    id :            str
    title:          str
    description:    str
    status:         str
    deadline:       int
    user_id:        str
    created_at:     int
    updated_at:     int

class TasksByUserResponse(BaseModel):
    user:       UserResponse 
    tasks:      List[TaskResponse] = Field(default_factory=list)
    