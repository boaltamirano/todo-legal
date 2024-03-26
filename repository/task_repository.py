import uuid
from database.database_factory import get_db_instance

class TaskRepository():
    def __init__(self, db_type):
        self.db = get_db_instance(db_type)
        
    def create_task(self, task):
        task_id = str(uuid.uuid4()).replace('-', '')
        query = "INSERT INTO tasks (id, title, description, status, deadline, user_id) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (task_id, task['title'], task['description'], task['status'], task['deadline'], task['user_id'])
        self.db.execute(query, params)
        return task_id

    def get_task_by_id(self, task_id):
        query = "SELECT * FROM tasks WHERE id = %s"
        params = (task_id,)
        result = self.db.execute(query, params)
        return result[0]

    def get_tasks_by_user_id(self, user_id):
        query = "SELECT * FROM tasks WHERE user_id = %s"
        params = (user_id,)
        result = self.db.execute(query, params)
        return result
    
    def update_task(self, task_id, task_data):
        query_parts = []
        params = []
        for key, value in task_data.items():
            query_parts.append(f"{key} = %s")
            params.append(value)
        params.append(task_id) 
        query = f"UPDATE tasks SET {', '.join(query_parts)} WHERE id = %s"
        self.db.execute(query, params)
    
    def delete_task(self, task_id):
        query = "DELETE FROM tasks WHERE id = %s"
        params = (task_id,)
        self.db.execute(query, params)