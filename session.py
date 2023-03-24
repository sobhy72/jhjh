from flask import Flask, render_template, jsonify , request, session
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

