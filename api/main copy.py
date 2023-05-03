from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI
from pony.orm import db_session

from .data import config
from .models import task, user

load_dotenv()

config.exec()
app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Welcome to the API",
        "route": "/",
        "routes": [
            {"path": "/users", "method": "GET", "return": "List of users"},
            {
                "path": "/users",
                "method": "GET",
                "params": {"fullname": "str", "email": "str", "password": "str"},
                "return": "A new user",
            },
            {
                "path": "/tasks",
                "method": "GET",
                "params": {"user_id": "int", "title": "str"},
                "return": "List of tasks of a user",
            },
        ],
    }


@app.get("/users/create")
def create_user(fullname: str, email: str, password: str):
    # TODO: hashing password
    hashed_password = password

    with db_session:
        new_user = user.User(
            full_name=fullname, email=email, hashed_password=hashed_password
        )

    return new_user.to_dict()


@app.get("/users")
def get_users():
    users: Any
    with db_session:
        users = [
            {**user.to_dict(), "tasks": [task.to_dict() for task in user.tasks]}
            for user in user.User.select()
        ]

    return {"message": users}


@app.get("/tasks")
def create_task(user_id: int, title: str):
    with db_session:
        author = user.User[user_id]
        new_task = task.Task(title=title, description="desk", done=False, user=author)
    return new_task.to_dict()
