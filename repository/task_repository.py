import uuid
from database.database_factory import get_db_instance

class TaskRepository():
    def __init__(self, db_type):
        self.db = get_db_instance(db_type)
        
    def create_task(self, task):
        task["id"] = str(uuid.uuid4()).replace('-', '')
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
        return task_id

    def get_task_by_id(self, task_id):
        query = "SELECT * FROM tasks WHERE id = %s"
        params = (task_id,)
        result = self.db.execute(query, params)
        return result

    def get_tasks_by_user_id(self, user_id, start_date, end_date):
        query = "SELECT * FROM tasks WHERE user_id = %s"
        params = (user_id,)
        if start_date is not None and end_date is not None:
            query += "AND created_at >= %s AND created_at <= %s"
            params= (user_id, start_date, end_date, )
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