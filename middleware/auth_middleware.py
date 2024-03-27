import jwt
from fastapi.security import HTTPBearer
from fastapi import HTTPException, Request, status
from repository.user_repository import UserRepository
from utils.utils import KEY, ALGORITHM, json_response

class AuthMiddleware(HTTPBearer):
    
    def __init__(self, db_type: str):
        self.db_type = db_type
        super().__init__()


    async def __call__(self, request: Request):
        try:
            user_repository = UserRepository(self.db_type)
            token = request.headers["Authorization"].split(" ")[1]
            payload = jwt.decode(token, KEY, algorithms=[ALGORITHM])
            email = payload.get("email")
            user = user_repository.get_user_by_email(email)
            if user:
                request.state.user = user
                response = await super().__call__(request) 
                return response
        except (jwt.exceptions.DecodeError, KeyError):
            pass
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=json_response( "Invalid or missing token",False).model_dump(),
        )