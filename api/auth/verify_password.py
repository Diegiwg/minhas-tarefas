from ..state.state import pwd_context


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hash=hashed_password)
