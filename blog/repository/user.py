from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
from ..hashing import Hash


def create(request: schemas.User, db: Session):
    new_user = models.UserAccounts(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(user_id: int, db: Session):
    user = db.query(models.UserAccounts).filter(models.UserAccounts.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {user_id} is not available")
    return user
