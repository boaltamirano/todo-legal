from services.user_service import UserService

class UserController:
    
    def __init__(self, db_type):
        self.user_service = UserService(db_type)
        
    def create_user(self, user):
        self.user_service.create_user(user)
        return {"message": "User created correctly"}
    
    def get_all_users(self):
        users = self.user_service.get_all_users()
        return users
    
    def get_user_by_id(self, user_id):
        user = self.user_service.get_user_by_id(user_id)
        return user
    
    def update_user(self, user_id, user_data):
        self.user_service.update_user(user_id, user_data)
        return {'message': 'User updated correctly'}
    
    def delete_user(self, user_id):
        self.user_service.delete_user(user_id)
        return {'message': 'User deleted currectly'}