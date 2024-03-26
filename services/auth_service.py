from repository.auth_repository import AuthRepository

class AuthService:
    
    def __init__(self, db_type):
        self.auth_repository = AuthRepository(db_type)
    
    def authenticate_user(self, auth):
        return self.auth_repository.authenticate_user(auth)