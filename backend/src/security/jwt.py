from datetime import date, datetime, timedelta, timezone

from typing import Optional

from jose import jwt
from passlib.context import CryptContext

# TODO:// Secure secret key in production
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
# Token Expires every 60 minutes
# Expiration will be longer in production
TOKEN_EXPIRATION = 3600

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    # Check if expiration should differ from standard
    expires_at = datetime.utcnow()
    expires_at = expires_at + expires_delta if expires_delta else expires_at + timedelta(minutes=TOKEN_EXPIRATION)

    # Convert datetime object to timestamp for serialization
    expires_at = datetime.timestamp(expires_at)

    data.update({"expires_at": expires_at})
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": encoded_jwt, "token_type": "bearer"}

def decode_access_token(token):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return decoded_token
    except Exception as e:
        return None

def is_token_expired(token, time_zone: timezone = timezone.utc, decode=True) -> bool:
    if decode:
        token = decode_access_token(token)
    expiration = datetime.fromtimestamp(token["expiration"], tz=time_zone)

    if datetime.now(tz=time_zone) > expiration:
        return True
    return False




