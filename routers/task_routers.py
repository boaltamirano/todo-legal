from fastapi import APIRouter, Depends
from controllers.task_controller import TaskController
from utils.user_validate import validate_user_data
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
def get_tasks_by_user_id(user_id):
    return task_controller.get_tasks_by_user_id(user_id)