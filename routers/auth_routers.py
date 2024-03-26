from fastapi import APIRouter
from controllers.auth_controller import AuthController
from utils.user_validate import validate_user_data
from models.auth_model import AuthModel

router = APIRouter()
auth_controller = AuthController('postgres')

@router.post('/auth',tags=['Auth'], status_code=201)
def authenticate_user(auth: AuthModel):
    response = auth_controller.authenticate_user(auth.model_dump())
    return response