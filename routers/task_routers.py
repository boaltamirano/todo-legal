from fastapi import APIRouter, Depends
from typing import Optional
from controllers.task_controller import TaskController
from models.task_model import TaskModel
from middleware.auth_middleware import AuthMiddleware

router = APIRouter()
database = 'postgres'
task_controller = TaskController(database)

@router.post('/tasks',tags=['Tasks'], dependencies=[Depends(AuthMiddleware(database))])
def create_task(task: TaskModel):
    response = task_controller.create_task(task.model_dump())
    return response

@router.get("/tasks/{user_id}",tags=['Tasks'], dependencies=[Depends(AuthMiddleware(database))])
def get_tasks_by_user_id(user_id: str,  start_date: Optional[str] = None, end_date: Optional[str] = None):
    return task_controller.get_tasks_by_user_id(user_id, start_date, end_date)

@router.put("/tasks/{task_id}", tags=['Tasks'], dependencies=[Depends(AuthMiddleware(database))])
def update_task(task_id: str, task_payload: dict):
    return task_controller.update_task(task_id, task_payload)

@router.delete("/tasks/{task_id}", tags=['Tasks'], dependencies=[Depends(AuthMiddleware(database))])
def delete_task(task_id: str):
    return task_controller.delete_task(task_id)