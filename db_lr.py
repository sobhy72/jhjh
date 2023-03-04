from sqlalchemy import MetaData
from sqlalchemy import ForeignKey
from sqlalchemy import Table, Column, Integer, String , column
from database import engine
from sqlalchemy.orm import DeclarativeBase
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert , select, bindparam
from sqlalchemy.orm import Session




metadata_obj = MetaData()


class Base(DeclarativeBase):
    pass




class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(back_populates="user")
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))
    user: Mapped[User] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

      
class Base(DeclarativeBase):
    pass

address_table = Table(
     "address",
     metadata_obj,
     Column("id", Integer, primary_key=True),
     Column("user_id",Integer),
     Column("email_address", String(60), nullable=False),
 )

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String(30)),
)

stmt = insert(user_table).values(name="spongebob", fullname="Spongebob Squarepants")

from sqlalchemy import select, bindparam

scalar_subq = (
    select(user_table.c.id)
    .where(user_table.c.name == bindparam("username"))
    .scalar_subquery()
)

def smrtinsrt():   
   with engine.connect() as conn:
      result = conn.execute(             
       insert(address_table).values(user_id=scalar_subq),
       [{ "username": "spongebob","email_address": 
          "spongebob@sqlalchemy.org",
         },
         {"username": "sandy", "email_address": 
         "sandy@sqlalchemy.org"},
          {"username": "sandy", "email_address": 
          "sandy@squirrelpower.org"},
            ],
        )
      conn.commit() 

   
def smrtrtrn(): 
  
    stmt=insert(user_table).values(name="spongebob", fullname="Spongebob Squarepants")
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()

def sm1():

  scalar_subq = (
     select(user_table.c.id)
     .where(user_table.c.name == bindparam("username"))
     .scalar_subquery())
 
  with engine.connect() as conn:
        result = conn.execute(             
         insert(address_table).values(user_id=scalar_subq),
         [{ "username": "spongebob","email_address": 
            "spongebob@sqlalchemy.org",
           },
           {"username": "sandy", "email_address": 
           "sandy@sqlalchemy.org"},
            {"username": "sandy", "email_address": 
            "sandy@squirrelpower.org"},
              ],
          ).returning(
           address_table.c.id, address_table.c.email_address
            )
        conn.commit()   

def sm2():

  scalar_subq = select(user_table.c.id, user_table.c.name + "@aol.com")
  
 
  with engine.connect() as conn:
        result = conn.execute(             
         insert(address_table).from_select(
      ["user_id", "email_address"]),scalar_subq)
        conn.commit()  

def sm3():

    select_stmt = select(user_table.c.id, user_table.c.name + "@aol.com")
    insert_stmt = insert(address_table).from_select(
        ["user_id", "email_address"], select_stmt
    )

 
    with engine.connect() as conn:
        result = conn.execute(insert_stmt)          
        conn.commit()  

def sm4():
    select_stmt = select(user_table.c.id, user_table.c.name + "@aol.com")
    insert_stmt = insert(address_table).from_select(
        ["user_id", "email_address"], select_stmt
    )
    with engine.connect() as conn:
        result = conn.execute(insert_stmt)          
        conn.commit()  
    insert_stmt = insert().returning(
    address_table.c.id, address_table.c.email_address)
    print(insert_stmt)  
    with engine.connect() as conn:
        result = conn.execute(insert_stmt)          
        conn.commit()


def sm5():
    stmt = insert(user_table).values(name="spongebob", fullname="Spongebob Squarepants")
    
    with engine.connect() as conn:
        result = conn.execute(stmt)          
        conn.commit() 
def sm6():
    stmt = select(user_table).where(user_table.c.name == "spongebob")
    
    with engine.connect() as conn:
     for row in conn.execute(stmt):
      print(row)        
      
    
def sm7():
    stmt = select(User).where(User.name == "spongebob")
    with Session(engine) as session:
      for row in session.execute(stmt):
        print(type(row))
        print(row)

def sm8():
    stmt = select(user_table)
    with Session(engine) as session:
      for row in session.execute(stmt):
        print(type(row))
        print(row)       
def sm9():
    stmt = select(user_table.c["name", "fullname"])
    with Session(engine) as session:
      for row in session.execute(stmt):
        print(type(row))
        print(row)
        return row

def sm10():
    session = Session()
    
    with Session(engine) as session:
      row = session.execute(select(User)).first()
      print(type(row))
      print(row)
      return row

def sm11():
    row = Session(engine).execute(select(User)).first()
    print(row)

def sm12():
     
    with Session(engine) as session:
      row = session.execute(select(User)).first()
      print(type(row))
      print(row)
      return row  
    
def sm13():
     
    with Session(engine) as session:
      user = session.scalars(select(User)).first()
      print(type(user))
      print(user)
      return user   

select(address_table.c.email_address)  .select_from(user_table).join(address_table, user_table.c.id == address_table.c.user_id)