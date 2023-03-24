from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
import datetime
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from database import engine
from sqlalchemy.orm import mapped_column
from sqlalchemy import text , insert , join , select , create_engine, Table, Column, Integer, String, ForeignKey,MetaData
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

Base= declarative_base()
Session = sessionmaker(bind = engine)
session = Session()

metadata_obj = MetaData()
meta = MetaData()
class UserMixin(object):
    id = Column(Integer, primary_key=True)
    user_name = Column(String(255), unique=True, nullable=False)
    last_read = Column("last_read", DateTime)

    @hybrid_property
    def is_online(self):
        if self.last_read is not None:
            return self.last_read <= \
                    datetime.datetime.now() - \
                    datetime.timedelta(minutes=30)
        else:
            return False

    @is_online.expression
    def is_online(cls):
        return case([(cls.last_read != None, 
                cls.last_read <= func.now() - 
                datetime.timedelta(minutes=30))], else_=literal(False))

class User(UserMixin, Base):
     __tablename__ = "Engineers_Reg"
     id: Mapped[int] = mapped_column(primary_key=True)
     name: Mapped[str] = mapped_column(String(30))
     user_name: Mapped[str] = mapped_column(String(30))
     password: Mapped[str] = mapped_column(String(30))
     fullname: Mapped[Optional[str]]
     def __repr__(self) -> str:
        return f"(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"