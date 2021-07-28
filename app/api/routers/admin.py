from fastapi import APIRouter,Depends
from api import database,schemas,models
from sqlalchemy.orm import Session
from api.repository import admin



router = APIRouter(
    prefix='/admin',
    tags=['Admin']
)
get_db = database.get_db


@router.post('/',response_model=schemas.Admin)
def create_user(request:schemas.Admin,db:Session=Depends(get_db)):
    return admin.create_admin(request,db)


@router.get('/show/{id}',response_model=schemas.Admin)
def get_admin(id:int,db:Session=Depends(get_db)):
    return admin.show_admin(id,db)
