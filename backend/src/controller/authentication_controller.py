from datetime import datetime, timedelta

from sqlalchemy.orm.session import Session
from ..services.authentication_service import AuthenticationService
from ..services import user_service
from ..security import jwt
from fastapi import Depends

from ..db.database import SessionLocal

class AuthenticationController():
    def __init__(self) -> None:
        self.authentication_service = AuthenticationService()

    def post_login(self, username: str, password: str):

        # Validate authentication
        if self.authentication_service.authenticate_user(username, password):
            
            # Get relevant fields from User
            with SessionLocal() as db:
                user = user_service.get_user_by_username(username)
                to_encode = {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                }

                # Set user token to expire in one week
                return jwt.create_access_token(to_encode, expires_delta = timedelta(days=7))
        return None

    def post_signup(self, username, email, password):
        
        # Hash user password
        password_hash = self.authentication_service.get_password_hash(password)

        user_data = {
            "username": username,
            "email": email,
            "password_hash": password_hash
        }

        result = user_service.create_user(user_data)
        if result:
            user = user_service.get_user_by_username(username)
            to_encode = {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }

            # Set user token to expire in one week
            return jwt.create_access_token(to_encode, expires_delta = timedelta(days=7))

        return None
