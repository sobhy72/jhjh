from flask import Flask, render_template, jsonify , request
from flask_login import UserMixin
from database import engine
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import text , insert , join , select , create_engine, Table, Column, Integer, String, ForeignKey,MetaData
from sqlalchemy.orm import Session
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import List
from typing import Optional


Base = declarative_base()

Session = sessionmaker(bind = engine)
session = Session()

metadata_obj = MetaData()
meta = MetaData()
today = date.today()

class User(Base):
    __tablename__ = "Engineers_Reg"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    user_name: Mapped[str] = mapped_column(String(30))
    
    def __repr__(self) -> str:
        return f"(id={self.id!r}, name={self.name!r}, user_name={self.user_name!r})"

      
Engineers_Reg = Table(
       'Engineers_Reg', meta, 
       Column('id'), 
       Column('name'),
       Column('user_name'), 
       Column('password'), 
       Column('disipline'),)
respons = Table(
       'respons', meta, 
       Column('id'), 
       Column('user_name'),
       Column('discipline'), 
       Column('respons'), 
       Column('unit'),
       Column('type'),
       Column('area'),
       )
   
reprots = Table(
       'reprots', meta, 
       Column('id'), 
       Column('eng_id'))


def tes():
  
  b = session.query(User).all()
  x=""
  for row in b:
    x += row.name
    print(x)
    print(type(row.id))
  
  
  

def test():
  res = select(respons.c.respons).where(respons.c.user_name ==                      
   "sobhy7")
  res=session.execute(res)
  res = res.fetchall()
  print("items" , len(res))

  for item in res:
    print(item)
    print(type(item))
    print(item[0])
    print(type(item[0]))
  return item
