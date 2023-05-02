from pony.orm import Required
from ..data.singleton import Database
from .user import User


class Task(Database().Entity):
    title = Required(str)
    description = Required(str)
    done = Required(bool)
    user = Required(User)
