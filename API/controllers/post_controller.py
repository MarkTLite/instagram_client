from schemas.post_schema import PostRequest
from models.post_model import PostModel
from models.user_model import UserModel

from sqlalchemy.orm.session import Session
from datetime import datetime
from fastapi.exceptions import HTTPException
from fastapi import status
from fastapi.responses import JSONResponse


def create_post(db: Session, request: PostRequest):
    new_post = PostModel(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.utcnow(),
        user_id=request.creator_id,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all_posts(db: Session):
    return db.query(PostModel).all()


def delete_post_by_id(id: int, user_id: int, db: Session):
    post = db.query(PostModel).filter(PostModel.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} not there",
        )
    if user_id != post.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Only Post creator can delete this post",
        )
    db.delete(post)
    db.commit()
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT,
        content={"status": "deleted"},
    )
