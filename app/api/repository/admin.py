from sqlalchemy.orm import Session
from api import schemas,models
from fastapi import HTTPException,status
from api.hashing import Hash



def create_admin(request:schemas.Admin,db:Session):
    new_admin = models.Admin(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin

def show_admin(id:int,db:Session):
    admin = db.query(models.Admin).filter(models.Admin.id==id).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return admin
