from databases.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class CommentModel(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)
    username = Column(String, ForeignKey('users.username'))
    timestamp = Column(DateTime)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship('PostModel', back_populates='comments')
