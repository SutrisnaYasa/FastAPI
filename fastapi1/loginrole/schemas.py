from pydantic import EmailStr
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True

# class ShowBlog(Blog):
#     class Config():
#         orm_mode = True

class Roles(str, Enum):
    user = "user",
    admin = "admin"

class User(BaseModel):
    username:str
    email:str
    password:str
    is_active: bool = True
    role: Roles

class ShowUser(BaseModel):
    username:str
    email:str
    is_active: bool = True
    role: Roles
    blogs : List[Blog] = []

    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None 

