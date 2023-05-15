from ..state.state import pwd_context


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
