from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


# Blog Model
class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
    user: Optional[str] = None


class AudioRecordBase(BaseModel):
    audio_record_title: str
    audio_record_date: datetime
    audio_record_file_type: str


class AudioRecord(AudioRecordBase):
    class Config:
        orm_mode = True


class UserAccountsBase(BaseModel):
    user_id:int
    user_name: str
    email_address: str
    password: str


class UserAccount(UserAccountsBase):
    class Config:
        orm_mode = True


class ShowUserAccount(BaseModel):
    user_name: str
    email_address: str
    audioRecords: List[AudioRecord] = []

    class Config:
        orm_mode = True


class ShowAudioRecord(BaseModel):
    audio_record_title: str
    audio_record_date: datetime
    audio_record_file_type: str
    creator: ShowUserAccount

    class Config:
        orm_mode = True