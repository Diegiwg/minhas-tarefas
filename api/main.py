from dotenv import load_dotenv
from fastapi import FastAPI

from .data import config
from .models import task, user  # noqa: F401 - Register models on database

load_dotenv()

config.exec()
app = FastAPI()


@app.get("/")
def root():
    return {"message": "API is running"}
