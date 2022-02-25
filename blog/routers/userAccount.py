from .. import database, schemas, oauth2
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from ..repository import userAccounts
from typing import List

router = APIRouter(
    prefix="/userAccounts",
    tags=['UserAccounts']
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUserAccount)
def create_user(request: schemas.UserAccount, db: Session = Depends(get_db)):
    return userAccounts.create(request, db)


@router.get('/{id}', response_model=schemas.UserAccount)
def get_user(id: int, db: Session = Depends(get_db), current_user: schemas.UserAccount = Depends(oauth2.get_current_user)):
    return userAccounts.show(id, db, current_user)


@router.get('/', response_model=List[schemas.ShowUserAccount])
def all(db: Session = Depends(get_db)):
    return userAccounts.get_all(db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.UserAccount = Depends(oauth2.get_current_user)):
    return userAccounts.destroy(id, db, current_user)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.AudioRecord, db: Session = Depends(get_db), current_user: schemas.UserAccount = Depends(oauth2.get_current_user)):
    return userAccounts.update(id, request, db, current_user)