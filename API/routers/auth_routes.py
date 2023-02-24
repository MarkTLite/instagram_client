from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from fastapi.exceptions import HTTPException

from databases.database import get_db
from controllers import auth_controller
from helpers.oauth2 import create_access_token

router = APIRouter(
    prefix='/auth',
    tags=['authentication'],
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth_controller.verify_oauth2_creds(request, db)
    access_token = create_access_token(data={'username':user.username})
    return {
        'access_token': access_token,
        'token_type': 'Bearer',
        'user_id': user.id,
        'username': user.username,
    }