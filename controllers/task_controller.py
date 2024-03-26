from services.task_service import TaskService
from services.user_service import UserService
from fastapi.responses import JSONResponse
from fastapi import status
from utils.utils import json_response, task_response, tasks_by_user_response

class TaskController:
    
    def __init__(self, db_type):
        self.task_service = TaskService(db_type)
        self.user_service = UserService(db_type)
        
    def create_task(self, task):
        task_id = self.task_service.create_task(task)
        task = self.task_service.get_task_by_id(task_id)
        response_model = json_response( "Task successfully registered", True, body= task_response(task).model_dump())
        return JSONResponse(status_code=status.HTTP_201_CREATED,content=response_model.model_dump())

    def get_tasks_by_user_id(self, user_id):
        tasks = self.task_service.get_tasks_by_user_id(user_id)
        user = self.user_service.get_user_by_id(user_id)
        response_model = json_response( "Successful", True, body= tasks_by_user_response(user, tasks))
        return JSONResponse(status_code=status.HTTP_200_OK, content=response_model.model_dump())

    def update_task(self, task_id, task_data):
        self.task_service.update_task(task_id,task_data)
        return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "Task updated correctly").model_dump())
    
    def delete_task(self, task_id):
        self.task_service.delete_task(task_id)
        return JSONResponse(status_code=status.HTTP_200_OK, content=json_response( "Task deleted currectly").model_dump())