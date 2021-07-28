from sqlalchemy.orm import Session
from api import models,schemas
from fastapi import HTTPException,status
import json

def create_country(request:schemas.Country,db:Session):
    new_country = models.Country(name=request.name,iso_code=request.iso_code)
    db.add(new_country)
    db.commit()
    db.refresh(new_country)
    return new_country

def get_country(iso_code:str,db:Session):
    country = db.query(models.Country).filter(models.Country.iso_code==iso_code).first()
    if not country:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Country With ISO Code:{iso_code} not found')
    return country

def update_country(iso_code:str,request:schemas.Country,db:Session):
    country =db.query(models.Country).filter(models.Country.iso_code==iso_code)

    if not country.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Blog With ISO Code:{iso_code} not found')
    
    country.update(request.dict())
    db.commit()
    return 'Updated'

def delete_country(iso_code:str,db:Session):
    country = db.query(models.Country).filter(models.Country.iso_code==iso_code)

    if not country.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Country With ISO Code{iso_code} not found')
    
    country.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'


