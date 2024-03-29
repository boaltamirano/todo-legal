from database.database_factory import get_db_instance

class AuthRepository:
    
    def __init__(self, db_type):
        self.db = get_db_instance(db_type)
        
    def authenticate_user(self, auth):
        query = "SELECT * FROM users WHERE email = %s"
        params = (auth["email"],)
        user = self.db.execute(query, params)
        return user