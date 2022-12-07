from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id : Optional[int]
    username : str
    email : str
    password : str
    is_staff : Optional[bool]
    is_active : Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            'example' : {
                "username" : "johndoe",
                "email" : "johndoe@gmail.com",
                "password" : "password",
                "is_staff" : False,
                "is_active" : True
            }
        }

class Settings(BaseModel):
    authjwt_secret_key : str='5cf4c31dea22741a742a92d7b4ab7f67cdc26fc03bcea69596276aed6b37534a'

class LoginModel(BaseModel):
    username : str
    password : str
