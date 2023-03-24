from flask import Flask, render_template, jsonify , request , redirect, session,url_for
from database import engine
import sqlalchemy
from sqlalchemy import text , insert , join , select , create_engine, Table, Column, Integer, String, ForeignKey,MetaData,DateTime,desc
from sqlalchemy.orm import Session
from datetime import date ,datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert , select, bindparam
from typing import Optional
from typing import List
from sqlalchemy.ext.declarative import declarative_base
import jyserver 
import jyserver.Flask as jsf
import json
import pytz
Base = declarative_base()
Session = sessionmaker(bind = engine)
sess = Session()
metadata_obj = MetaData()
meta = MetaData()


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

  
class User(Base):
     __tablename__ = "Engineers_Reg"
     id: Mapped[int] = mapped_column(primary_key=True)
     user_name: Mapped[str] = mapped_column(String(30))
     password: Mapped[str] = mapped_column(String(30))
     name: Mapped[str] = mapped_column(String(30))
     disipline: Mapped[str] = mapped_column(String(30))
     email: Mapped[str] = mapped_column(String(30))
     Mobile_no: Mapped[str] = mapped_column(String(30))
  
     def __repr__(self) -> str:
        return f"(id={self.id!r}, name={self.name!r}, user_name={self.user_name!r},password={self.password!r}, disipline={self.disipline!r}, email={self.email!r},Mobile_no={self.Mobile_no!r})"


      

class login_register(Base):
   __tablename__ = 'login_register'
   id = Column(Integer, primary_key =  True)
   user_name = Column(String)
   Login = Column(DateTime, default=datetime.utcnow)
   def __repr__(self) -> str:
        return f"(id={self.id!r}, user_name={self.user_name!r})"  

class Report_reg(Base):
 __tablename__ = 'Report_reg'
 report_no = Column(Integer, primary_key =  True)
 eng_id = Column(Integer)
 report_date = Column(DateTime, default=datetime.utcnow)

  
class Report(Base):
   __tablename__ = 'reprots'
   id = Column(Integer, primary_key =  True)
   descr = Column(String)
   unit = Column(String)
   remarks = Column(String)
   main_descr = Column(String)
   report_no = Column(Integer)
   eng_id = Column(Integer)
   area = Column(String)
   qty = Column(String)
    
   def __repr__(self) -> str:
        return f"(id={self.id!r},descr={self. descr!r},unit={self.unit!r}, remarks={self.remarks!r},main_Descr={self.main_descr!r}, report_no={self.report_no!r},eng_id={self.eng_id!r},area={self.area!r},qty={self.qty!r})"
