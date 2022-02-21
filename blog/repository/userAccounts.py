from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
from ..hashing import Hash


def get_all(db: Session):
    user_accounts = db.query(models.UserAccounts).all()
    return user_accounts


def create(request: schemas.UserAccountsBase, db: Session):
    new_user = models.UserAccounts(user_name=request.user_name, email_address=request.email_address,
                                   password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def destroy(user_account_id: int, db: Session):
    user_account = db.query(models.UserAccounts).filter(models.UserAccounts.user_id == user_account_id)

    if not user_account.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {user_account_id} not found")

    user_account.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(user_account_id: int, request: schemas.AudioRecord, db: Session):
    user_account = db.query(models.UserAccounts).filter(models.UserAccounts.user_id == user_account_id)

    if not user_account.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {user_account_id} not found")
    user_account.update(request)
    db.commit()
    return 'updated'


def show(user_account_id: int, db: Session):
    user_account = db.query(models.UserAccounts).filter(models.UserAccounts.user_id == user_account_id).first()
    if not user_account:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {user_account_id} is not available")
    return user_account
