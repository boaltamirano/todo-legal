from services.auth_service import AuthService
from fastapi.responses import JSONResponse
from fastapi import status
from utils.utils import json_response, verify_password, user_token_response

class AuthController:
    
    def __init__(self, db_type):
        self.auth_service = AuthService(db_type)
        
    def authenticate_user(self, auth):
        user = self.auth_service.authenticate_user(auth)
        if not user or  not verify_password(auth["password"],user["password"]):
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                content=json_response( "Invalid user or password ", False).model_dump())    
        return JSONResponse(status_code=status.HTTP_200_OK,content=json_response( "Successful", True, body= user_token_response(user)).model_dump())
        