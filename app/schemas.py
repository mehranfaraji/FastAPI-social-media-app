from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional
from pydantic import conint

# from pydantic.types import conint

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class ConfigDict:
        from_attributes = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class ConfigDict:
        from_attributes = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class ConfigDict:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None
    

class Vote(BaseModel):
    post_id: int
    dir = Field(ge=0, le=1)