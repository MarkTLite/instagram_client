"""
JSON Schema for Comments
"""
from pydantic import BaseModel
from datetime import datetime

class CommentRequest(BaseModel):
    """When a comment is created in a given post"""
    comment: str
    username: str
    post_id: int

class Comment(BaseModel):
    """When the comment is listed in a post"""
    comment: str
    username: str
    timestamp: datetime
    class Config:
        orm_mode = True
