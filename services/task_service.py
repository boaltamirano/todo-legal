from repository.task_repository import TaskRepository

class TaskService:
    
    def __init__(self, db_type):
        self.task_repository = TaskRepository(db_type)
    
    def create_task(self, task):
        return self.task_repository.create_task(task)

    def get_task_by_id(self, task_id):
        return self.task_repository.get_task_by_id(task_id)

    def get_tasks_by_user_id(self, user_id):
        return self.task_repository.get_tasks_by_user_id(user_id)