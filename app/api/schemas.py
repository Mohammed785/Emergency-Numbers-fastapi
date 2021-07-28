from typing import List,Optional
from pydantic import BaseModel


class CountryBase(BaseModel):
    name:str
    iso_code : str

class Country(CountryBase):
    class Config():
        orm_mode = True


class NumberBase(BaseModel):
    name:str
    body:str
    country_id:int

class Number(NumberBase):
    class Config():
        orm_mode = True


class ShowNumber(BaseModel):
    name: str
    body:str
    country : Country=None
    class Config():
        orm_mode = True

class ShowCountryNumber(BaseModel):
    name: str
    body:str
    class Config():
        orm_mode = True


class ShowCountry(BaseModel):
    name: str
    iso_code: str=None
    numbers: List[ShowCountryNumber] = []
    class Config():
        orm_mode = True


class Login(BaseModel):
    email : str
    password:str

class Token(BaseModel):
    access_token: str
    token_type : str

class TokenData(BaseModel):
    email: Optional[str]=None


class Admin(BaseModel):
    name :str
    email : str
    password :str
    class Config():
        orm_mode = True
