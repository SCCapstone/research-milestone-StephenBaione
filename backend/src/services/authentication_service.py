from passlib.context import CryptContext

from . import user_service
from ..db.model.user import User
class AuthenticationService():
    def __init__(self) -> None:
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_password_hash(self, password: str):
        return self.pwd_context.hash(password)

    def verify_password(self, password: str, password_hash: str):
        return self.pwd_context.verify(password, password_hash)

    def authenticate_user(self, username: str, password: str) -> bool:
        # Check if user exists with given username
        user: User = user_service.get_user_by_username(username)
        if user is None:
            return False

        # User is authenticated if supplied password matches hashed password
        return self.verify_password(password, user.password_hash)
