from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import Request,status
from fastapi.exceptions import RequestValidationError
from utils.utils import json_response

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_msg = "Validation error"
    detail = []
    for error in exc.errors():
        error_msg = str(error['msg'])+ ': '+ str(error['loc'][1])
        detail.append({
            'loc': error['loc'],
            'msg': error['msg'],
            'type': error['type']
        })
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=json_response(error_msg,False).model_dump()
    )