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


@router.get('/{user_account_id}', response_model=schemas.UserAccount)
def get_user(user_account_id: int, db: Session = Depends(get_db), current_user: schemas.UserAccount = Depends(oauth2.get_current_user)):
    return userAccounts.show(user_account_id, db, current_user)


@router.get('/', response_model=List[schemas.ShowUserAccount])
def all(db: Session = Depends(get_db), current_user: schemas.UserAccount = Depends(oauth2.get_current_user)):
    return userAccounts.get_all(db, current_user)


@router.delete('/{user_account_id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(user_account_id: int, db: Session = Depends(get_db), current_user: schemas.UserAccount = Depends(oauth2.get_current_user)):
    return userAccounts.destroy(user_account_id, db, current_user)


@router.put('/{user_account_id}', status_code=status.HTTP_202_ACCEPTED)
def update(user_account_id: int, request: schemas.UserAccount, db: Session = Depends(get_db), current_user: schemas.UserAccount = Depends(oauth2.get_current_user)):
    return userAccounts.update(user_account_id, request, db, current_user)