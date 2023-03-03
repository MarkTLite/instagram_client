"""
JSON Schema for post endpoints
"""
from pydantic import BaseModel
from datetime import datetime
from schemas.comment_schema import Comment
from typing import List

class PostRequest(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: str


# For use in post response
class UserSchema(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class PostResponse(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: UserSchema
    comments: List[Comment]

    class Config:
        orm_mode = True
