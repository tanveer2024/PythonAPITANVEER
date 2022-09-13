from datetime import datetime
from pydantic import BaseModel, Field,EmailStr
from typing import List, Union
from typing import Optional,Tuple
from pydantic.types import conint

#from pytz import timezone
class PostMain(BaseModel):
    id:int
    title:str
    content: str
    published: bool = True
    #create_at : datetime
    #owner_id = int

    # id = Column(Integer, primary_key= True, nullable= False)
    # title = Column(String,nullable=False)
    # c = Column(String,nullable= False)
    # published = Column(Boolean,server_default='TRUE',nullable=False)
    # create_at = Column(TIMESTAMP(timezone=True), nullable=False,server_default=text('now()'))
    # owner_id = Column(Integer,ForeignKey("user.id",ondelete="CASCADE") ,nullable = False)

class UserOut(BaseModel):
    email: EmailStr
    id:int
    create_at: datetime
    class Config:
        orm_mode = True



class PostBase(PostMain):
                            # Response comes in Pydantic model
    # id: int
    # title: str                     
    # c: str
    # published: bool = True
    create_at: datetime
     
    owner_id:int
    pass
    # class Config:
    #     orm_mode = True
    owner : UserOut
     
    class Config:
        orm_mode = True
        pass


class PostOut(BaseModel):
    Post: PostBase
    votes: int
    class Config:
        orm_mode = True
    

class PostCreate(PostMain):
    id: int
    title: str
    content:str
    published: bool = True
    #created_at: datetime
    
    
class PostTest(PostBase):
    id: int
    title: str                     
    content: str
    published: bool = True
    #created_at: datetime 
    #owner_id: int
       
    

class PostResp(PostMain):

    # id: int
    # title: str   # coming from Parent PostBase 
    # c: str
    # published: bool = True    # This for Response back to 
    #created_at: datetime
    owner_id: int
    pass                      # limit the user what needs to be send
    class Config:
        orm_mode = True
    
                              # back 
   
           #This for Response  coz pydantic model only read dict and response 
                 # is coming from sqlalchemy which is not dictionary format


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    #create_at: datetime
    #id: int 
    


class UserLogin(BaseModel):
    email: EmailStr
    password: str 
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class Tokendata(BaseModel):
    id:Optional[str]  = None

class Vote(BaseModel):
    post_id : int
    dir : conint(le=1)        # Direction of 0 and 1     
    class Config:
        orm_mode = True
class VoteReturn(BaseModel):
    user_id : int
    post_id : int
    pass
    class Config:
        orm_mode = True

