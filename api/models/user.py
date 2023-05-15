from typing import TypedDict

from pony.orm import Required, Set

from ..data.singleton import Database


class User(Database().Entity):
    full_name = Required(str)
    email = Required(str, unique=True)
    hashed_password = Required(str)
    tasks = Set("Task")


# TODO: create a Pydantic model for the user actions


class UserCreate(TypedDict):
    full_name: str
    email: str
    password: str


class UserLogin(TypedDict):
    email: str
    password: str
