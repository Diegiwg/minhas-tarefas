from typing import Optional

from passlib.context import CryptContext
from pony.orm import db_session

from ..models.user import User
from .verify_password import verify_password


# TODO: Create a Pydantic Model for UserLogin
def authenticate_user(pwd_context: CryptContext, email: str, password: str) -> bool:
    user: Optional[User]
    with db_session:
        user = User.get(email=email)

    if not user:
        return False

    if not verify_password(pwd_context, password, user.hashed_password):
        return False

    return True
