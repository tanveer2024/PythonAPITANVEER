from pydoc import text
from .database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from typing import Optional
#alembic  tool help us to modify the table column 


    

class Post(Base):
    __tablename__ = "postsal"
    
    id = Column(Integer, primary_key= True, nullable= False)
    title = Column(String,nullable=False)
    content = Column(String,nullable= False)
    published = Column(Boolean,server_default='TRUE',nullable=False)
    create_at = Column(TIMESTAMP(timezone=True), nullable=False,server_default=text('now()'))
    owner_id = Column(Integer,ForeignKey("usersal.id",ondelete="CASCADE") ,nullable = False)
    #parent = relationship("User",back_populates = "children")
    #owner_id = relationship("user.id",cascade = "all,delete")

    owner = relationship("User")   # A one to many relationship places a foreign key on the child table referencing the parent.
                                    #  relationship() is then specified on the parent,
                                    #   as referencing a collection of items represented by the child:
  
class User(Base):
    __tablename__ = "usersal"

    id = Column(Integer,primary_key = True, nullable = False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False) 
    create_at = Column(TIMESTAMP(timezone=True), nullable=False,server_default=text('now()'))
    phone_number = Column(String)
   

    #children = relationship("Post.id",back_populates = "user")

     # Sqlalchemy model, Responsible for defining the column of our "posts"
                  # table within postgress
                  # Is used to query,create,delete and update entries within the DB

class Vote(Base):
    __tablename__ = "votesal"
    user_id = Column(Integer,ForeignKey(
    "usersal.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer,ForeignKey(
    "postsal.id", ondelete="CASCADE"), primary_key=True)              