from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from databases.database import get_db
from helpers import oauth2
from controllers import comment_controller
from schemas.comment_schema import CommentRequest
from schemas.user_schema import UserAuthSchema

router = APIRouter(
    prefix="/comments",
    tags=["comments"],
)


@router.post("/create")
def create_comment(
    request: CommentRequest,
    db: Session = Depends(get_db),
    authed_user: UserAuthSchema = Depends(oauth2.get_current_user),
):
    """Create a comment for a given Post"""
    return comment_controller.create_comment(request, db)


@router.get("/all/{post_id}")
def get_comments(
    post_id: int,
    db: Session = Depends(get_db),
):
    """Get all the comments under a given post"""
    return comment_controller.get_comments(db, post_id)
