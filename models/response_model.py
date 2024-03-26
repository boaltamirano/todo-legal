from typing import Union
from pydantic import BaseModel


class Response(BaseModel):
    ok :        bool
    message:    str 
    body:       Union[str, int, bool, dict, list]