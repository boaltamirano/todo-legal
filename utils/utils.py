from dotenv import load_dotenv
from models.response_model import Response
from datetime import datetime, timedelta
from models.user_model import  UserToken, UserResponse
from models.task_model import  TaskResponse, TasksByUserResponse
import jwt 
import os
import bcrypt

load_dotenv()
KEY = os.getenv("KEY")
TOKEN_EXPIRATION_MINUTES = os.getenv("TOKEN_EXPIRATION_MINUTES")
ALGORITHM = os.getenv("ALGORITHM")

def generate_token(email):
        payload = {
            "email": email,
            "exp": datetime.utcnow() + timedelta(minutes=int(TOKEN_EXPIRATION_MINUTES)),
        }
        token = jwt.encode(payload, KEY, algorithm=ALGORITHM)
        return token

def user_token_response(user):
    token = generate_token(user["email"])
    return UserToken(token= token, user=user_response(user)).model_dump()


def json_response(message, ok = True, body = []):
    return Response(ok=ok, message=message, body=body)

def hash_password(password) :
    hashed_password = bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt())
    return hashed_password.decode("utf-8")

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def tasks_by_user_response(user,tasks):
    return TasksByUserResponse(user= user_response(user), tasks=[task_response(task) for task in tasks]).model_dump()

def user_response(user):
    return UserResponse(
        id= str(user["id"]), 
        name= user["name"], 
        email= user["email"], 
        phone= str(user["phone"]), 
        address=user["address"],
        created_at= int((user["created_at"]).timestamp()), 
        updated_at= int((user["updated_at"]).timestamp())
    )

def task_response(task):
    return TaskResponse(
        id= str(task["id"]), 
        title= task["title"], 
        description= task["description"], 
        status= str(task["status"]), 
        deadline=task["deadline"],
        user_id=task["user_id"],
        created_at= int((task["created_at"]).timestamp()), 
        updated_at= int((task["updated_at"]).timestamp())
    )