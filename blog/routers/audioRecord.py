from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from ..repository import audioRecord

router = APIRouter(
    prefix="/audioRecord",
    tags=['AudioRecords']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowAudioRecord])
def all(db: Session = Depends(get_db), current_user: schemas.UserAccount = Depends(oauth2.get_current_user)):
    return audioRecord.get_all(db, current_user)


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.AudioRecord, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return audioRecord.create(request, db, current_user)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.UserAccount = Depends(oauth2.get_current_user)):
    return audioRecord.destroy(id, db, current_user)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.AudioRecord, db: Session = Depends(get_db), current_user: schemas.UserAccount = Depends(oauth2.get_current_user)):
    return audioRecord.update(id, request, db, current_user)


@router.get('/{id}', status_code=200, response_model=schemas.ShowAudioRecord)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.UserAccount = Depends(oauth2.get_current_user)):
    return audioRecord.show(id, db, current_user)
