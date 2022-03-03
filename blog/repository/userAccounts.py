from sqlalchemy.orm import Session
from sqlalchemy import Sequence
from .. import models, schemas
from fastapi import HTTPException, status
from ..hashing import Hash
from datetime import datetime


def get_all(db: Session, current_user: schemas.User):
    print(current_user)
    if current_user.email != 'admin@gmail.com':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not authenticated to see all user details. Only admins can see all users!")
    user_accounts = db.query(models.UserAccounts).all()
    return user_accounts


def create(request: schemas.UserAccountsBase, db: Session):
    new_user_id = db.execute(Sequence('xxfr_al_user_id_seq'))

    new_user = models.UserAccounts(user_id=new_user_id,
                                   user_name=request.user_name,
                                   email_address=request.email_address,
                                   first_name= request.first_name,
                                   middle_name= request.middle_name,
                                   last_name= request.last_name,
                                   password=Hash.bcrypt(request.password),
                                   creation_date=datetime.now(),
                                   last_updated_date=datetime.now(),
                                   created_by=request.user_name,
                                   last_updated_by=request.user_name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def destroy(user_account_id: int, db: Session, current_user: schemas.User):
    user_account_auth = db.query(models.UserAccounts).filter(models.UserAccounts.email_address == current_user.email).first()
    user_account_details = db.query(models.UserAccounts).filter(models.UserAccounts.user_id == user_account_id).first()

    if user_account_details is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User_id is not valid = {user_account_id}")
    if user_account_details.user_id != user_account_auth.user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not authenticated to delete details of user_id = {user_account_id}")
    if not user_account_auth.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User detail not found for authenticated user")
    user_account_auth.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(user_account_id: int, request: schemas.UserAccount, db: Session, current_user: schemas.User):
    user_account_auth = db.query(models.UserAccounts).filter(models.UserAccounts.email_address == current_user.email).first()
    user_account_details = db.query(models.UserAccounts).filter(models.UserAccounts.user_id == user_account_id).first()

    if user_account_details is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User_id is not valid = {user_account_id}")
    if user_account_details.user_id != user_account_auth.user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not authenticated to update details of user_id = {user_account_id}")
    if not user_account_auth.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User detail not found for authenticated user")
    user_account_auth.update(request)
    db.commit()
    return 'updated'


def show(user_account_id: int, db: Session, current_user: schemas.User):
    user_account_auth = db.query(models.UserAccounts).filter(models.UserAccounts.email_address == current_user.email).first()
    user_account_details = db.query(models.UserAccounts).filter(models.UserAccounts.user_id == user_account_id).first()

    if user_account_details is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User_id is not valid = {user_account_id}")
    if user_account_details.user_id != user_account_auth.user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not authenticated to see details of user_id = {user_account_id}")
    if not user_account_auth:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User detail not found for authenticated user")
    return user_account_auth
