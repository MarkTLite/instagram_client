from models.user_model import UserModel
from schemas.user_schema import UserRequest
from helpers.hashing import HashPwd

from sqlalchemy.orm.session import Session
from fastapi.exceptions import HTTPException
from fastapi import status

def create_user(db: Session, request: UserRequest):
    user = UserModel(
        email=request.email,
        username=request.username,
        password=HashPwd.bcrypt(request.password), # we need to hash the password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def read_user_by_username(db: Session, username: str):
    user = db.query(UserModel).filter(UserModel.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User "{user}" not found'
        )
    return user