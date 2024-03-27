from fastapi import APIRouter, Depends
from controllers.user_controller import UserController
from utils.user_validate import validate_user_data
from models.user_model import UserModel
from middleware.auth_middleware import AuthMiddleware

router = APIRouter()
database = 'postgres'
user_controller = UserController(database)

@router.post('/users',tags=['Users'])
def create_user(user: UserModel):
    response = user_controller.create_user(user.model_dump())
    return response

@router.get("/users",tags=['Users'], dependencies=[Depends(AuthMiddleware(database))])
def get_all_users():
    return user_controller.get_all_users()

@router.get("/users/{user_id}",tags=['Users'], dependencies=[Depends(AuthMiddleware(database))])
def get_user_by_id(user_id:str):
    return user_controller.get_user_by_id(user_id)

@router.put("/users/{user_id}", tags=['Users'], dependencies=[Depends(AuthMiddleware(database))])
def update_user(user_id: str, user_payload: dict):
    response = user_controller.update_user(user_id, user_payload)
    return response

@router.delete("/users/{user_id}", tags=['Users'], dependencies=[Depends(AuthMiddleware(database))])
def delete_user(user_id:str):
    response = user_controller.delete_user(user_id)
    return response
