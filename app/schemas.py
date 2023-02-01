from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

# schemas and pydantic models define the structure of a request and response
# this will ensure that when a user wants to create a post, the request will only go through if it has a "title" and "content" in the body
# this is esentially a validation process in a way
# we can also dictate a schema model what to send back to the user

# this defines the schema checking for validation is the user is entering data that contains a title, content, and str for both variables
# by creating a PostBase, you can create the schema under 1 class instead of having to copy and paste into multiple class
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass 

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

# Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, 
# but an ORM model (or any other arbitrary object with attributes), this applies when you have something that is not a str
    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)