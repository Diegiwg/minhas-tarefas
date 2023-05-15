from passlib.context import CryptContext

pwd_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")
