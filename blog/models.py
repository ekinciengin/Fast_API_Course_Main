from sqlalchemy import Column, Integer, String, ForeignKey, Date, TIMESTAMP, Sequence
from .database import Base
from sqlalchemy.orm import relationship


class AudiRecord(Base):
    __tablename__ = 'xxfr_audio_life_user_records'

    audio_record_id = Column(Integer, Sequence('xxfr_al_audio_record_id_seq'), primary_key=True, index=True)

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

    user_id = Column(Integer, Sequence('xxfr_al_user_id_seq'), primary_key=True, index=True)
    user_name = Column(String)
    email_address = Column(String)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    created_by = Column(String)
    creation_date = Column(TIMESTAMP)
    last_updated_by = Column(String)
    last_updated_date = Column(TIMESTAMP)
    
    audiorecords = relationship('AudiRecord', back_populates="creator")