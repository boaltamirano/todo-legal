import uuid
from database.database_factory import get_db_instance

class UserRepository:
    
    def __init__(self, db_type):
        self.db = get_db_instance(db_type)
        
    def create_user(self, user):
        user_id = str(uuid.uuid4()).replace('-', '')
        query = "INSERT INTO users (id, name, email, password) VALUES (%s, %s, %s, %s)"
        params = (user_id, user['name'], user['email'], user['password'])
        self.db.execute(query, params)
        
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
        