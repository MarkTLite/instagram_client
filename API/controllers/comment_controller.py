from sqlalchemy.orm.session import Session
from datetime import datetime

from schemas.comment_schema import CommentRequest
from models.comment_model import CommentModel

def create_comment(request: CommentRequest, db: Session):
    """Create a comment in the db"""
    comment = CommentModel(
        username=request.username,
        comment=request.comment,
        post_id=request.post_id,
        timestamp=datetime.utcnow(),
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def get_comments(db: Session, post_id):
    """Get all comments of a given post"""
    return db.query(CommentModel).filter(CommentModel.id == post_id)