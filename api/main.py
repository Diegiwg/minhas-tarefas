from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

from .data import config
from .models import task, user  # noqa: F401 - Register models on database
from .routes import login, users

load_dotenv()
config.exec()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

app.include_router(login.router)
app.include_router(users.router)


@app.get("/")
def root():
    return {"message": "API is running"}
