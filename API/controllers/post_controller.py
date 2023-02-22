from schemas.post_schema import PostRequest
from models.post_model import PostModel
from models.user_model import UserModel

from sqlalchemy.orm.session import Session
from datetime import datetime

def create_post(db: Session, request: PostRequest):
    new_post = PostModel(
        image_url = request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.utcnow(),
        user_id = request.creator_id,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all_posts(db: Session):
    return db.query(PostModel).all()
