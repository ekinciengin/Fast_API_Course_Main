from typing import List, Optional
from pydantic import BaseModel, validator
from datetime import datetime
from sqlalchemy.orm import Session
from . import models


class User(BaseModel):
    username: str
    email: str
    full_name: str
    disabled: bool


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
    audio_record_date: Optional[datetime] = datetime.now()
    audio_record_file_type: str


class AudioRecord(AudioRecordBase):
    class Config:
        orm_mode = True


class UserAccountsBase(BaseModel):
    user_name: str
    email_address: str
    password1: str
    password2: str
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]

    @validator('user_name')
    def user_name_exists(cls, value, db: Session):
        user_account_details = db.query(models.UserAccounts).filter(
            models.UserAccounts.user_name == value).first()
        if user_account_details is not None:
            raise ValueError('This user name is in used. Please choose a different user name!')
        return value.title()

    @validator('email_address')
    def email_address_format_validation(cls, value):
        if '@' not in value:
            raise ValueError('Email address is not in valid format')
        return value.title()

    @validator('email_address')
    def email_address_exists(cls, value, db: Session):
        user_account_details = db.query(models.UserAccounts).filter(
            models.UserAccounts.email_address == value).first()
        if user_account_details is not None:
            raise ValueError('This email address is in used. Please choose a different email address!')
        return value.title()

    @validator('password2')
    def passwords_match(cls, value, values, **kwargs):
        if 'password1' in values and value != values['password1']:
            raise ValueError('Passwords do not match')
        return value

class UserAccount(UserAccountsBase):
    class Config:
        orm_mode = True


class ShowUserAccount(BaseModel):
    user_name: str
    email_address: str
    first_name: str
    middle_name: str
    last_name: str
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