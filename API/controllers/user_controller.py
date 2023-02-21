from models.user_model import UserModel
from schemas.user_schema import UserRequest

from sqlalchemy.orm.session import Session

def create_user(db: Session, request: UserRequest):
    user = UserModel(
        email=request.email,
        username=request.username,
        password=request.password, # we need to hash the password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user