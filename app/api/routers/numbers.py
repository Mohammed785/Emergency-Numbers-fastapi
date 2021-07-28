from fastapi import APIRouter,Depends,status
from typing import List
from api.repository import numbers
from api import schemas,database,oauth2
from sqlalchemy.orm import Session



router=APIRouter(
    prefix='/number',
    tags=['Number']
)

get_db=database.get_db


@router.post('/create/number',status_code=status.HTTP_201_CREATED)
def create_number(request: schemas.Number, db: Session = Depends(get_db), current_user: schemas.Admin = Depends(oauth2.get_current_user)):
    return numbers.create_number(request,db)


@router.put('/update/number{id}',status_code=status.HTTP_202_ACCEPTED)
def update_number(number_id, request: schemas.Number, db: Session = Depends(get_db), current_user: schemas.Admin = Depends(oauth2.get_current_user)):
    return numbers.update_number(number_id,request,db)

@router.delete('/delete/number/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_number(number_id:int,db:Session=Depends(get_db),current_user:schemas.Admin=Depends(oauth2.get_current_user)):
    return numbers.delete_number(number_id,db)


@router.get('/show/number/{id}',status_code=status.HTTP_302_FOUND,response_model=schemas.ShowNumber)
def show_number(number_id:int,db:Session=Depends(get_db)):
    return numbers.show_number(number_id,db)
