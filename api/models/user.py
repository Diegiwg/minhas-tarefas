from pony.orm import Required, Set

from ..data.singleton import Database


class User(Database().Entity):
    full_name = Required(str)
    email = Required(str, unique=True)
    hashed_password = Required(str)
    tasks = Set("Task")
