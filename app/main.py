from dbm import dumb

from email import header
from gettext import find
from msilib.schema import Control
from multiprocessing import Value, connection
from sqlite3 import Cursor
from turtle import title

# from attr import attributes

from fastapi import FastAPI,Depends,status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from flask import jsonify
from pydantic import BaseModel, JsonWrapper
#from pydantic import BaseSettings
from os.path import dirname, basename, isfile, join
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

#from app.routers.vote import vote
from . import model
from .database import engine,get_db
from .config import settings
# import numpy as np
# import pandas as pd
import json
import pprint
# from temboo.Library.Google.Geocoding import GeocodeByAddress
# from temboo.core.session import TembooSession
# from flask_cors import CORS
# from flask import Flask, Response
# access-Control-allow-origin: http://localhost:4200
from fastapi.middleware.cors import CORSMiddleware
import requests
#import json
from types import SimpleNamespace
#.server import HTTPServer, SimpleHTTPRequestHandler,test 
import sys
from .routers import post,user,auth,vote


 
      

#from http.server import BaseHTTPRequestHandler, HTTPServer
#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

#################################################################################
#""" The HTTP request handler """
# class RequestHandler(BaseHTTPRequestHandler):

#   def _send_cors_headers(self):
#       """ Sets headers required for CORS """
#       self.send_header("Access-Control-Allow-Origin", "*")
#       self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
#       self.send_header("Access-Control-Allow-Headers", "x-api-key,Content-Type")

#   def send_dict_response(self, d):
#       """ Sends a dictionary (JSON) back to the client """
#       self.wfile.write(bytes(dumps(d), "utf8"))

#   def do_OPTIONS(self):
#       self.send_response(200)
#       self._send_cors_headers()
#       self.end_headers()

#   def do_GET(self):
#       self.send_response(200)
#       self._send_cors_headers()
#       self.end_headers()

#       response = {}
#       response["status"] = "OK"
#       self.send_dict_response(response)

#   def do_POST(self):
#       self.send_response(200)
#       self._send_cors_headers()
#       self.send_header("Content-Type", "application/json")
#       self.end_headers()

#       dataLength = int(self.headers["Content-Length"])
#       data = self.rfile.read(dataLength)

#       print(data)

#       response = {}
#       response["status"] = "OK"
#       self.send_dict_response(response)


# print("Starting server")
# httpd = HTTPServer(("127.0.0.1", 8000), RequestHandler)
# print("Hosting server on port 8000")
# httpd.serve_forever()


###################################################################################

# from OpenSSL import SSL
#cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost/auth"}})
#resp.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1/auth'

# @app.route('/auth', methods=['POST'])
# def auth_client():
#         ...
#         resp.headers['Access-Control-Allow-Origin'] = 'http://localhost'
#         resp.headers['Access-Control-Allow-Methods'] = '*'
#         resp.headers['Access-Control-Allow-Domain'] = '*'
#         resp.headers['Access-Control-Allow-Credentials'] = True
#         # Debug
#         print("Right")
#         return resp

#model.Base.metadata.create_all(bind=engine)

#models.Base.metadata.create_all(bind=engine)
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

#engine = create_engine(
 #   SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
#)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# app = Flask(__name__)
# CORS(app)
# cors = CORS(app, resources={
#     r"/*": {
#         "origins": "http://localhost:4200/"
#     }
# })

# class CORSRequestHandler (SimpleHTTPRequestHandler):
#     def end_headers(self): self.send_header('Access-Control-Allow-Origin','*'), SimpleHTTPRequestHandler.end_headers(self)

# if __name__ == '__main__':
#     test(CORSRequestHandler,HTTPServer,port=int(sys.argv[1])
#     if len(sys.argv) > 1 else 8000)




app = FastAPI()

origins = [
    "http://localhost:4200",
    "https://www.google.com/",
    #"https://www.youtube.com/",
        ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # specific http method we block put,post,delete request
    allow_headers=["*"], # specific header
)
# There are a few headers that allow sharing of resources across origins, 
# but the main one is Access-Control-Allow-Origin.
#  This tells the browser what origins are allowed to receive requests from this server.




    

# my_posts = [{"title":"title of post 1","content":"content of post 1","id":1},{"title":"favorite foods","content":"I like burger","id":2}]

# def find_post(id):
#  for p in my_posts:
#      if p ["id"] == id:
#          return p

# def find_index_post(id):
#     for i,p in enumerate(my_posts):
#         if p['id'] == id:
#             return i


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/") # @ decorator
async def root():
    return {"message":"Welcome to my API!!!!!!&&"}

# #@app.get("/posts") # @ decorator
# #def get_posts():
#  #   return{"data":"This is your posts"}

# @app.get("/getposts") # @ decorator
# def get_posts(db: Session = Depends(get_db)):
#     posts = db.query(Post.Post).all()
#     #print(posts.__dict__)
#     #print (posts.__getattribute__)  
#     return {"data":posts}
#     # conn = psycopg2.connect(host ='192.168.1.28',database='fastapi',user='postgres',password = 'lock2000',cursor_factory=RealDictCursor)
#     # cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
#     # cursor.execute("""SELECT * FROM posts""")
#     # posts=cursor.fetchall()
#     print (posts)
#     #print api
#     return{"data":posts}
#     #return{my_posts}

# #@app.post("/createposts") # @ decorator
# #def create_posts(payload: dict = Body(...)):
#  #   print(payload)
#   #  return {"new_post":f"title {payload['title']} content: {payload['content']}"}
# #@app.post("/createposts") # @ decorator
# #def create_posts(new_post: Post):
#     #print(new_post)
#     #print(new_post)
#     #print(new_post.content)
#     #print(new_post.published)
#     #print(new_post.rating)
#     #print(new_post.dict())
#     #return {"data": "new post"}

# @app.post("/saveposts",status_code= status.HTTP_201_CREATED) # @ decorator
# def create_posts(post: Post,db: Session = Depends(get_db)):
#     #pprint.PrettyPrinter(*post.dict())
#     #pprint(*post.json())
#     print(*post.json())
#     #print(*post.dict())
#     new_post = Post.Post(**post.dict())
#         #title = post.title,content=post.content,published=post.published )
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)  # return * kind off
#     return {"data":new_post}    
#     # cursor.execute("""INSERT INTO posts(title,content,published) VALUES (%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
#     # new_post = cursor.fetchone()
#     # #post_dict = post.dict()
#     # #post_dict['id'] = randrange(0,1000000)
#     # #my_posts.append(post_dict)
#     # #print(new_post.dict())
#     # print (new_post)
#     # conn.commit()
#     return {"data": new_post}
#     # title str, content str,Category,Boolean 


# @app.get("/getpostsbyid/{id}")  # @ decorator
# def get_post(id:int,db : Session = Depends(get_db)):  #def get_post(id):
#     #cursor.execute(""" select * from posts where id = 1""")
#     # cursor.execute(" select * from posts where id = %s", (str(id),))
#     # post = cursor.fetchone()
#     post = db.query(Post.Post).filter(Post.Post.id == id).first()
#     #print(post(attributes))
#     #print(geocodeByAddressResults.outputs)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not found")
#     return {"data": post}
#     #print(post)
#     #print((id)) 
#     #return {"post_detail": f"Here is the post {id}"}
#     # post = find_post((id))
#     # #print(post)
#     # #if not post:
#     #  #   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not found")
#     #     #response.status_code = status.HTTP_404_NOT_FOUND
#     #     #return {'message':f"post with id: {id} was not found"}
#     # return {"post_detail":post}

# #@app.get("/posts/latest") # @ decorator
# #def get_latest_post():
#  #   post = my_posts[len(my_posts)- 1]
#   #  return {"detail":post}

# @app.post("/deleteposts/{id}",status_code=status.HTTP_204_NO_CONTENT) # @ decorator
# def delete_post(id:int,db: Session = Depends(get_db)):
#     post = db.query(Post.Post).filter(Post.Post.id == id)
#     # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id),))
#     # delete_post = cursor.fetchone()
#     # conn.commit()
#     if post.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} does not exist")
    
#     post.delete(synchronize_session=False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)   
#     # deleting post
#     # find the index in the array that has required ID
#     # my_posts.pop(index)
#     # index = find_index_post(id)

#     # if index == None:
#     #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} does not exist")
#     # my_posts.pop(index)
#     # return Response(status_code=status.HTTP_204_NO_CONTENT)


# #@app.delete("/posts/{id}") # @ decorator
# #def delete_post():
#     # deleting post
#     # find the index in the array that has required ID
#     # my_posts.pop(index)
#  #   index = find_index_post(id)
#   #  if index == None:
#    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} does not exist")
#     #my_posts.pop(index)
#     #return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.post("/updateposts/{id}")
# def update_post(id: int, post: Post):
#     cursor.execute("""UPDATE posts SET title =%s, content = %s, published = %s WHERE id = %s RETURNING *""",(post.title,post.content,post.published,str(id)))
#     updated_post = cursor.fetchone()
#     conn.commit()
#     print (updated_post)
#     if updated_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                          detail=f"post with id: {id} does not exist")
#     return {"data":updated_post}


# @app.get("/sqlalchemy1")
# def test_post(db: Session = Depends(get_db)):
#     posts = db.query(Post.Post).all()   
#     return {"data":posts}
#  #return {"status":"success"}

# @app.get('/getrestdata',status_code=status.HTTP_200_OK)
# def getrestdata(firstName: str = 'Tanveer', lastName: str = 'Alam'):
#     print("hitting api")
#     print(firstName + " " + lastName)
#     response = requests.get('http://api.open-notify.org/astros.json')

#     x = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))
#     print(x.message)
#     print(x.people)
#     x.message
#     x.people
#     #print(response)
#     return response.json()


###################################################################################
@app.get('/getrestdata',status_code=status.HTTP_200_OK) # ,response_model= List[schemas.PostResp] List from typing
def getrestdata(db: Session = Depends(get_db)):
    print("hitting api")
    posts = db.query(model.Post).all()  # post = db.query(model.Post).all()
    #y = json.dumps(f'[{posts}]')
    #print(y)
    #resp = requests.get('http://localhost:8000/getrestdata',json.)
    #data = posts
    # data = json.loads(posts.__init__)
    # print(data)
    #pprint(*posts.__dict__())
    #x= json.dumps([posts])
    x = json.loads(json.dumps(f'[{posts}]'),object_hook=lambda d: SimpleNamespace(**d))
    print(x)
    #print(x.data)
    return  posts
    
###############################################     
# @app.post("/posts",status_code=status.HTTP_201_CREATED,response_model= schemas.PostBase)  # create Post
# def create_posts(post:schemas.PostCreate,db:Session=Depends(get_db)):  # post is for pydantic model
#     new_post = model.Post(**post.dict())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post) # new_post response comes in sqlAclemy model hence is class Config: in schemas file
#     return { new_post}
#######################################################
# @app.get("/posts/{id}",response_model=schemas.PostResp)                       # get individual data 
# #@app.get("/posts/{id}",status_code=status.HTTP_200_OK)                       # get individual data 
# async def get_post(id: int, db: Session = Depends(get_db)):
#     #post = db.query(model.Post).all()
#     post = db.query(model.Post).filter(model.Post.id == id).first()
#     #new_postsingle = model.Post(*post.dict())
#     #print(f"response 1:{post}")
#     #jsonpost = json.loads(json.dumps(f'[{post}]'),object_hook=lambda d: SimpleNamespace(**d))
#     #print(f"json response :{json.dumps(jsonpost)}")
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail =f"post with id: {id} was not found")
#     return post
#########################################################

# @app.delete("/posts/{id}", status_code= status.HTTP_204_NO_CONTENT)    # Delete Post                   # delete individual data 
# def del_post(id: int, db: Session = Depends(get_db)):
#     post = db.query(model.Post).filter(model.Post.id == id)
#     if post.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                                                detail = f"post with id: {id} does not exist" )

#     post.delete(synchronize_session=False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)
##########################################################
# @app.put("/posts/{id}",response_model=schemas.PostBase)      # Update Post
# def update_post(id: int,Updated_post: schemas.PostCreate, db:Session = Depends(get_db)): # Updated_post is pydantic model
#     post_query = db.query(model.Post).filter(model.Post == id)

#     post = post_query.first()

#     if post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                                                  detail=f"post with id: {id} does not exist") 
    
#     post_query.update(Updated_post.dict(),synchronize_session=False)
#     db.commit()
#     return {"data": post_query.first()}
       
 ################################################################################   
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)
#################################################################### 
# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)
#######################################################################################       

    #data = json.dumps(posts)
   # x = json.dumps(posts,skipkeys=True)
    #x = json.loads(posts, object_hook=lambda d: SimpleNamespace(**d))
    #print(x.Object)
    #data = json.dumps(posts)
    #resp = requests.get(data=json.dumps(posts))
    #return {"data" : data}
    #return {"data:": resp.json() }
    #print(resp.text)
    #print(response.json())
    #x = json.dumps
    #x.data
    #return resp.json()
    #print(x)
    #print(posts.__class_getitem__)
    #print(posts.__dict__)
    # print (posts.__getattribute__)
    #return {"data":response.json()}
    # print(posts)
    #response = requests.get(posts)
    # x = dict.loads(response.text,object_hook=lambda d: SimpleNamespace(**d))
    # print("hitting api")
    # print(x)
    # print(response.json)
    #return response
    #print(firstName + " " + lastName)
    
    #def get_posts(db: Session = Depends(get_db)):
    
    # posts = db.query(Post.Post).all()
    # print(posts.__dict__)
    # print (posts.__getattribute__)  
    # return {"data":posts}
     
    #p 
    # x = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))
    # print(x.message)
    # #print(x.people)
    # x.message
    # #x.people
       
    # return response.json()

# @app.post('/postrestdatawithfilter',status_code=status.HTTP_200_OK)
# def postrestdata():
#     print("inside post")
#     response = requests.

##############################################################################
# create a user in the user table
# @app.post("/users", status_code=status.HTTP_201_CREATED,response_model= schemas.UserOut) # ,response_model= List[schemas.UserCreate] 
# def create_user(user: schemas.UserCreate,db: Session = Depends(get_db)):
#     # hash the password - user.password
#     hashed_password = utils.hash(user.password)
#     user.password = hashed_password
#     new_user = model.User(**user.dict()) # Un **user is meaning unpacking the dict
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user
########################################################################
# @app.get("/users/{id}",response_model= schemas.UserOut) # Individual User Record is fetch
# def get_userid(id: int, db: Session = Depends(get_db)):
#     #hashed_password = utils.hash(model.User.password)
#     user1 = db.query(model.User).filter(model.User.id == id).first()
#     if not user1:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND
#                 ,detail=f"User with id : {id} does not exist")
#     return user1 
########################################################################    













