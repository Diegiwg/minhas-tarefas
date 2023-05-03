from datetime import timedelta, utcnow
from os import getenv
from typing import Optional

from jose.jwt import encode

# NOTE: Do not provide a default value, for force to configure your Secret Key
JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = getenv("JWT_ALGORITHM", "HS256")


def create_access_token(response_data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = response_data.copy()

    if expires_delta:
        expire = utcnow() + expires_delta
    else:
        expire = utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt
