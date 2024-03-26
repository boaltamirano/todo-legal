from repository.user_repository import UserRepository

class UserService:
    
    def __init__(self, db_type):
        self.user_repository = UserRepository(db_type)
    
    def create_user(self, user):
        return self.user_repository.create_user(user)
    
    def get_all_users(self):
        return self.user_repository.get_all_users()
    
    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)
    
    def update_user(self, user_id, user_data):
        self.user_repository.update_user(user_id, user_data) 
        
    def delete_user(self, user_id):
        self.user_repository.delete_user(user_id)
        