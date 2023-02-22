"""
JSON Schemas for User Routes
"""

from pydantic import BaseModel

class UserRequest(BaseModel):
    """Schema for User Requests"""
    email:str
    password:str
    username:str

class UserResponse(BaseModel):
    """Schema for User Responses"""
    email:str
    username:str
    class Config:
        orm_mode = True

class UserAuthSchema(BaseModel):
    id: int
    username: str
    email:str