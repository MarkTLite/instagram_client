"""
User Models
"""
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import relationship

from databases.database import Base

class UserModel(Base):
    """User Account Model"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    posts = relationship('PostModel', back_populates='user')

