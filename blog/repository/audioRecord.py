from datetime import datetime

from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    audio_records = db.query(models.AudiRecord).all()
    return audio_records


def create(request: schemas.AudioRecordBase, db: Session, current_user: schemas.UserAccount):
    user_account = db.query(models.UserAccounts).filter(models.UserAccounts.user_name == current_user.username).first()
    new_audio_record = models.AudiRecord(audio_record_title=request.audio_record_title,
                                         audio_record_date=request.audio_record_date,
                                         audio_record_file_type=request.audio_record_file_type,
                                         creation_date=datetime.now(),
                                         last_updated_date=datetime.now(),
                                         user_id=user_account.user_id)
    db.add(new_audio_record)
    db.commit()
    db.refresh(new_audio_record)
    return new_audio_record


def destroy(audio_record_id: int, db: Session):
    audio_record = db.query(models.Blog).filter(models.Blog.id == audio_record_id)

    if not audio_record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {audio_record_id} not found")

    audio_record.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(audio_record_id: int, request: schemas.AudioRecord, db: Session):
    audio_record = db.query(models.AudiRecord).filter(models.AudiRecord.audio_record_id == audio_record_id)

    if not audio_record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {audio_record_id} not found")
    audio_record.update(request)
    db.commit()
    return 'updated'


def show(audio_record_id: int, db: Session):
    audio_record = db.query(models.AudiRecord).filter(models.AudiRecord.audio_record_id == audio_record_id).first()
    if not audio_record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {audio_record_id} is not available")
    return audio_record
