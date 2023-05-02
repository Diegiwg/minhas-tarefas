from pony.orm import Database as PonyDatabase


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Database(PonyDatabase, metaclass=SingletonMeta):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
