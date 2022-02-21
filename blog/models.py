from sqlalchemy import Column, Integer, String, ForeignKey, Date, TIMESTAMP
from .database import Base
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('Blog', back_populates="creator")


class AudiRecord(Base):
    __tablename__ = 'xxfr_audio_life_user_records'

    audio_record_id = Column(Integer, primary_key=True, index=True)
    audio_record_title = Column(String)
    audio_record_date = Column(Date)
    audio_record_file_type = Column(String)
    created_by = Column(String)
    creation_date = Column(TIMESTAMP)
    last_updated_by = Column(String)
    last_updated_date = Column(Date)
    user_id = Column(Integer, ForeignKey('xxfr_audio_life_users.user_id'))

    creator = relationship("UserAccounts", back_populates="audiorecords")


class UserAccounts(Base):
    __tablename__ = 'xxfr_audio_life_users'

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    email_address = Column(String)
    password = Column(String)
    created_by = Column(String)
    creation_date = Column(Date)
    last_updated_by = Column(String)
    last_updated_date = Column(Date)

    audiorecords = relationship('AudiRecord', back_populates="creator")
