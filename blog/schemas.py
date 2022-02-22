from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


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