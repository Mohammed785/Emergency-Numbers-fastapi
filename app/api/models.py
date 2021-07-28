from sqlalchemy import Column,Integer,String,ForeignKey
from .database import Base
from sqlalchemy.orm import relationship



class Country(Base):
    __tablename__ = 'countrys'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    iso_code = Column(String)
    numbers = relationship('Number',back_populates='country')

class Number(Base):
    __tablename__ = 'numbers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    body = Column(String)
    country_id = Column(Integer,ForeignKey('countrys.id'))
    country = relationship('Country', back_populates='numbers')


class Admin(Base):
    __tablename__='admins'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
