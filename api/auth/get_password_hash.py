from passlib.context import CryptContext


def exec(pwd_context: CryptContext, password: str) -> str:
    return pwd_context.hash(password)
