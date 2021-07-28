from sqlalchemy.orm import Session
from starlette import status
from api import models,schemas
from fastapi import HTTPException

def create_number(request:schemas.Number,db:Session):
    new_number = models.Number(name=request.name,body=request.body,country_id=request.country_id)
    db.add(new_number)
    db.commit()
    db.refresh(new_number)
    return new_number

def update_number(id:int,request:schemas.Number,db:Session):
    number = db.query(models.Number).filter(models.Number.id==id)

    if not number.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Number With ID:{id} not found')
    
    number.update(request.dict())
    db.commit()
    return 'Updated'


def delete_number(id:int,db:Session):
    number = db.query(models.Number).filter(models.Number.id == id)
    if not number.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Number With ID:{id} not found')
    number.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'


def show_number(number_id:int,db:Session):
    number = db.query(models.Number).filter(models.Number.id==number_id).first()
    if not number:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Number With ID:{number_id} not found')
    return number
