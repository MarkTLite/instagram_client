from fastapi import status
from fastapi.param_functions import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from fastapi.exceptions import HTTPException

from models.user_model import UserModel
from helpers.hashing import HashPwd

def verify_oauth2_creds(request: OAuth2PasswordRequestForm, db: Session):
    """Verify Oauth2 creds and return the user if correct"""
    user = db.query(UserModel).filter(UserModel.username == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Invalid username'
        )
    if not HashPwd.verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Incorrect Password'
        )
    return user