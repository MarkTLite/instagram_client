from schemas.user_schema import UserRequest, UserResponse
from controllers import (user_controller,)
from databases.database import get_db

from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

router = APIRouter(
    prefix='/user',
    tags=['user'],
)

@router.post('/create', response_model=UserResponse)
def create_user(user: UserRequest, db: Session = Depends(get_db)):
    user = user_controller.create_user(db, user)
    return user
