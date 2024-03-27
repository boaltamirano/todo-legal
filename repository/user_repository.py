import uuid
from database.database_factory import get_db_instance
from utils.utils import hash_password

class UserRepository:
    
    def __init__(self, db_type):
        self.db = get_db_instance(db_type)
        
    def create_user(self, user):
        user["id"]= str(uuid.uuid4()).replace('-', '')
        user['password'] = hash_password(user['password'])
        query_parts = []
        values = []
        params = []
        for key, value in user.items():
            if value != None:
                query_parts.append(f"{key}")
                values.append("%s")
                params.append(value)
        query = f"INSERT INTO users ({', '.join(query_parts)}) VALUES ({', '.join(values)})"
        self.db.execute(query, params)
        return user["id"]
        
    def get_all_users(self):
        query = "SELECT * FROM users"
        result = self.db.execute(query)
        return result
    
    def get_user_by_id(self, user_id):
        query = "SELECT * FROM users WHERE id = %s"
        params = (user_id,)
        result = self.db.execute(query, params)
        return result
    
    def update_user(self, user_id, user_data):
        query_parts = []
        params = []
        for key, value in user_data.items():
            query_parts.append(f"{key} = %s")
            params.append(value)
        
        params.append(user_id) 
        query = f"UPDATE users SET {', '.join(query_parts)} WHERE id = %s"
        self.db.execute(query, params)
        
    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id = %s"
        params = (user_id,)
        self.db.execute(query, params)

    def get_user_by_email(self, email):
        query = "SELECT * FROM users WHERE email = %s"
        params = (email,)
        result = self.db.execute(query, params)
        return result[0]
        