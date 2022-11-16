from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from database import Base
from sqlalchemy.orm import relationship
import enum
from sqlalchemy import Integer, Enum

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    body = Column(String(100))
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    email = Column(String(50))
    password = Column(String(100))
    is_active = Column(Boolean, default = True)
    role = Column(String(100), nullable = False)

    blogs = relationship("Blog", back_populates="creator")
