from fastapi import APIRouter
from controllers.user_controller import UserController
from utils.user_validate import validate_user_data
from models.user_model import UserModel

router = APIRouter()
user_controller = UserController('postgres')

@router.post('/users', status_code=201)
@validate_user_data
def create_user(user: UserModel):
    response = user_controller.create_user(user.model_dump())
    return response

@router.get("/users", status_code=200)
def get_all_users():
    users = user_controller.get_all_users()
    return users

@router.get("/users/{user_id}", status_code=200)
def get_user_by_id(user_id):
    users = user_controller.get_user_by_id(user_id)
    if len(users) > 0:
        return users[0]
    return users

@router.put("/users/{user_id}", status_code=200)
def update_user(user_id, user_payload: dict):
    response = user_controller.update_user(user_id, user_payload)
    return response

@router.delete("/users/{user_id}", status_code=200)
def delete_user(user_id):
    response = user_controller.delete_user(user_id)
    return response
