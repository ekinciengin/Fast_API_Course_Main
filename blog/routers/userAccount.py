from .. import database, schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from ..repository import userAccounts

router = APIRouter(
    prefix="/userAccounts",
    tags=['UserAccounts']
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUserAccount)
def create_user(request: schemas.UserAccount, db: Session = Depends(get_db)):
    return userAccounts.create(request, db)


@router.get('/{id}', response_model=schemas.UserAccount)
def get_user(id: int, db: Session = Depends(get_db)):
    return userAccounts.show(id, db)
