import re
from fastapi import HTTPException
from models.user_model import UserModel

def validate_user_data(func):
    def create_user(user: UserModel):
        try:
            if len(user.password) < 8:
                raise ValueError("La contraseña debe tener al menos 8 caracteres")
            
            if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', user.email):
                raise ValueError("El formato del correo electrónico no es válido")
            
            return func(user)
        except ValueError as ve:
            raise HTTPException(status_code=400, detail=str(ve))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    return create_user