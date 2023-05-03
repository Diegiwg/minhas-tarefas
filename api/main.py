from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from .data import config
from .models import task, user  # noqa: F401 - Register models on database

load_dotenv()
config.exec()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()


@app.get("/")
def root():
    return {"message": "API is running"}
