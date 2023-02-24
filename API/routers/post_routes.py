from controllers import post_controller
from databases.database import get_db
from helpers import file_helper, oauth2
from schemas.user_schema import UserAuthSchema

from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from schemas.post_schema import (
    PostRequest,
    PostResponse,
)
from typing import List
import time, shutil

router = APIRouter(
    prefix="/post",
    tags=["post"],
)

image_url_types = ["absolute", "relative"]


@router.post("/create", response_model=PostResponse)
def create_post(
    request: PostRequest,
    db: Session = Depends(get_db),
    authed_user: UserAuthSchema = Depends(oauth2.get_current_user),
):
    """Creates a post"""
    if request.image_url_type not in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Url type not recognized. Use either absolute or relative",
        )
    return post_controller.create_post(db, request)


@router.get("/all", response_model=List[PostResponse])
def get_all_posts(
    db: Session = Depends(get_db),
    authed_user: UserAuthSchema = Depends(oauth2.get_current_user),
):
    """Gets all posts in db"""
    return post_controller.get_all_posts(db)


@router.post("/image")
def upload_image(
    image: UploadFile = File(...),
    authed_user: UserAuthSchema = Depends(oauth2.get_current_user),
):
    """Uploads an image to be used for creating a post"""
    path = f"images/{file_helper.create_unique_name(image.filename)}"
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"image_path": path}


@router.delete("/delete/{id}")
def delete_post(
    id: int,
    db: Session = Depends(get_db),
    authed_user: UserAuthSchema = Depends(oauth2.get_current_user),
):
    """Delete a post using its ID"""
    return post_controller.delete_post_by_id(id, authed_user.id, db)
