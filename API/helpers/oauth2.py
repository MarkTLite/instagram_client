from typing import Optional
from datetime import timedelta, datetime
from sqlalchemy.orm.session import Session
import os
from os.path import join, dirname

from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose.exceptions import JWTError
from dotenv import load_dotenv

from databases.database import get_db
from controllers import user_controller

oauth2_schema = OAuth2PasswordBearer(tokenUrl='auth/login')

#load env vars
dotenv_path = join(dirname(dirname(__file__)), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    cred_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate your credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload['username']
        if not username:
            raise cred_exception
    except JWTError:
        raise cred_exception

    user = user_controller.read_user_by_username(db, username)
    if not user:
        raise cred_exception

    return user