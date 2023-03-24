from flask import Flask, render_template, jsonify , request , redirect, session,url_for
from database import engine
import sqlalchemy
from sqlalchemy import text , insert , join , select , create_engine, Table, Column, Integer, String, ForeignKey,MetaData
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
from app import *

utc=pytz.UTC

def credent():
  x = utc.localize(datetime.now())
  print(x)
  if x > session['date']+timedelta(minutes=90):
   print("form Here")
   print(x,(session['date']+timedelta(minutes=1)))
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   session.pop('date', None)
   
   
def name():
  print("hello")
  return render_template('report.html',rws=10) 

   