from repository.task_repository import TaskRepository

class TaskService:
    
    def __init__(self, db_type):
        self.task_repository = TaskRepository(db_type)
    
    def create_task(self, task):
        return self.task_repository.create_task(task)

    def mass_tasks_creation(self, user_id, tasks):
        return self.task_repository.mass_tasks_creation(user_id, tasks)

    def get_task_by_id(self, task_id):
        return self.task_repository.get_task_by_id(task_id)

    def get_tasks_by_user_id(self, user_id, start_date, end_date):
        return self.task_repository.get_tasks_by_user_id(user_id, start_date, end_date)
    
    def update_task(self, task_id, task_data):
        return self.task_repository.update_task(task_id, task_data)
    
    def delete_task(self, task_id):
        return self.task_repository.delete_task(task_id)