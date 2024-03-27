from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from routers.user_routers import router as user_router
from routers.auth_routers import router as auth_router
from routers.task_routers import router as task_routers
from middleware.error_middleware import ErrorHandler
from middleware.validation_middleware import validation_exception_handler


app = FastAPI()
app.add_middleware(
    ErrorHandler
)
app.include_router(user_router, prefix="/api")
app.include_router(auth_router, prefix="/api")
app.include_router(task_routers, prefix="/api")

@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(request, exc):
    return await validation_exception_handler(request, exc)