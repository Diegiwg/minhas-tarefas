from typing import Optional

from ..models.user import User
from .verify_password import verify_password


# TODO: Create a Pydantic Model for UserLogin
def authenticate_user(email: str, password: str) -> bool:
    user: Optional[User] = User.get(email=email)
    if not user:
        return False

    if not verify_password(password, user.hashed_password):
        return False

    return True
