from fastapi import FastAPI

from routers.user_routers import router as user_router
from routers.auth_routers import router as auth_router
from routers.task_routers import router as task_routers

app = FastAPI()
app.include_router(user_router, prefix="/api")
app.include_router(auth_router, prefix="/api")
app.include_router(task_routers, prefix="/api")
