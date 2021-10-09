from fastapi.param_functions import Depends
from sqlalchemy.orm import Session

from ..db.model.user import User
import uuid

from ..db.database import SessionLocal

def get_user(user_id: int) -> User or None:
    with SessionLocal() as db:
        return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(username: str) -> User or None:
    with SessionLocal() as db:
        return db.query(User).filter(User.username == username).first()

def get_user_by_email(user_email: str) -> User or None:
    with SessionLocal() as db:
        return db.query(User).filter(User.email == user_email).first()

def create_user(user_data: dict):
    with SessionLocal() as db:
        try:
            user = User()
            user.id = str(uuid.uuid4())
            user.username = user_data["username"]
            user.email = user_data["email"]
            user.password_hash = user_data["password_hash"]

            db.add(user)
            db.commit()
            return user

        except Exception as e:
            return None

