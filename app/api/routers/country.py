from typing import List
from fastapi import APIRouter,Depends,status
from api import schemas,database,oauth2
from sqlalchemy.orm import Session
from api.repository import country


router = APIRouter(
    prefix='/country',
    tags=['Country']
)

get_db = database.get_db


@router.post('/create',status_code=status.HTTP_201_CREATED)
def create_country(request: schemas.Country, db: Session = Depends(get_db),current_user:schemas.Admin=Depends(oauth2.get_current_user)):
    return country.create_country(request,db)


@router.get('/show/{iso_code}', status_code=status.HTTP_302_FOUND, response_model=schemas.ShowCountry)
def show_country(iso_code: str, db: Session = Depends(get_db)):
    return country.get_country(iso_code, db)

@router.put('/update/{iso_code}',status_code=status.HTTP_202_ACCEPTED)
def update_country(iso_code: str,request:schemas.Country,db:Session=Depends(get_db),current_user:schemas.Admin=Depends(oauth2.get_current_user)):
    return country.update_country(iso_code,request,db)

@router.delete('/delete/{iso_code}',status_code=status.HTTP_204_NO_CONTENT)
def delete_country(iso_code: str, db: Session = Depends(get_db), current_user: schemas.Admin = Depends(oauth2.get_current_user)):
    return country.delete_country(iso_code,db)