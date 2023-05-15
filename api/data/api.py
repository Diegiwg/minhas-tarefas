import re

from pony.orm import db_session

from ..auth.create_access_token import create_access_token
from ..auth.get_password_hash import get_password_hash
from ..auth.verify_password import verify_password
from ..models.user import User, UserCreate, UserLogin
from ..utils import email_regex


@db_session
def create_user(user: UserCreate):
    # NOTE: Verify email is a valid email with Pydantic
    if not re.match(email_regex.pattern, user["email"]):
        return {"message": "Invalid email"}

    hashed_password = get_password_hash(user["password"])
    User(
        full_name=user["full_name"],
        email=user["email"],
        hashed_password=hashed_password,
    )
    return {"message": "User created"}


@db_session
def login(user_login: UserLogin):
    # NOTE: Verify email is a valid email with Pydantic
    if not re.match(email_regex.pattern, user_login["email"]):
        return {"message": "Invalid email"}

    user: User = User.get(email=user_login["email"])
    if not user:
        return {"message": "User not found"}

    if not verify_password(user_login["password"], user.hashed_password):
        return {"message": "Invalid password"}

    return {
        "token": create_access_token({"email": user.email, "full_name": user.full_name})
    }
