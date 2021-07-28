from fastapi import FastAPI
from api import models
from api.database import engine
from api.routers import country,numbers,admin,authentication

app = FastAPI()


models.Base.metadata.create_all(engine)

app.include_router(country.router)
app.include_router(numbers.router)
app.include_router(authentication.router)
app.include_router(admin.router)