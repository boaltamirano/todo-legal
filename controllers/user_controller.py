from services.user_service import UserService
from fastapi.responses import JSONResponse
from fastapi import status
from utils.utils import json_response, user_response, user_token_response

class UserController:
    
    def __init__(self, db_type):
        self.user_service = UserService(db_type)
        
    def create_user(self, user):
        user_id = self.user_service.create_user(user)
        user = self.user_service.get_user_by_id(user_id)
        response_model = json_response( "User successfully registered", True, body= user_token_response(user))
        return JSONResponse(status_code=status.HTTP_201_CREATED,content=response_model.model_dump())
    
    def get_all_users(self):
        users = self.user_service.get_all_users()
        result = [user_response(user) for user in users]
        response_model = json_response( "Successful", True, body= result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=response_model.model_dump())
    
    def get_user_by_id(self, user_id):
        user = self.user_service.get_user_by_id(user_id)
        if not user:
            return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "User not found", False).model_dump())    
        return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "Successful", True, body= user_response(user).model_dump()).model_dump())
    
    def update_user(self, user_id, user_data):
        self.user_service.update_user(user_id, user_data)
        return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "User updated correctly").model_dump())
    
    def delete_user(self, user_id):
        self.user_service.delete_user(user_id)
        return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "User deleted currectly").model_dump())