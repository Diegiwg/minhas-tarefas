from passlib.context import CryptContext


def get_password_hash(pwd_context: CryptContext, password: str) -> str:
    return pwd_context.hash(password)
