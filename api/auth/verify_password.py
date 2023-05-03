from passlib.context import CryptContext


def verify_password(
    pwd_context: CryptContext, plain_password: str, hashed_password: str
) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
