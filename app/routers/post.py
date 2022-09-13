#from datetime import datetime
#from xmlrpc.client import DateTime
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from .. import schemas,model,oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from types import SimpleNamespace
import json
from typing import Optional, Text, Type,List
from sqlalchemy import func


router = APIRouter(
    prefix= "/posts",
    tags= ["Posts"]
)
#############################################################################################
@router.get("/",response_model= List[schemas.PostOut])   # Get all post 
#@router.get("/") 
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),limit:int = 100,
                                                                         skip: int = 0,search:Optional[str]= ""):
     print(limit) # limit is to limit the post and skip how many you need to skip the post that is 
                     # if http://127.0.0.1:8000/posts?limit=4&skip=1 in postman with limit it will 
                     # show 4 and with skip it will skip the first entry so showning three record     
     #posts = db.query(model.Post).filter(model.Post.title.contains(search)).limit(limit).offset(skip).all()
     #posts = db.query(model.Post).all()
     posts = db.query(model.Post,func.count(model.Vote.post_id).label("votes")).join(model.Vote, model.Vote.post_id == model.Post.id,isouter=True).group_by(model.Post.id).filter(model.Post.title.contains(search)).limit(limit).offset(skip).all() # PostOut
     ##select posts.id , COUNT(votes.post_id) as votes from posts LEFT JOIN votes ON posts.id = votes.post_id where post_id = 10 group_by(posts.id);  # By default Left Inner Join
     #print(results) sqlalechemy by default Left inner join.
     #return posts
     return posts 


    # return results  


###################################################################################
@router.get('/getrestdata',status_code=status.HTTP_200_OK) # ,response_model= List[schemas.PostResp] List from typing
def getrestdata(db: Session = Depends(get_db)):
    print("hitting api")
    posts = db.query(model.Post).all()  # post = db.query(model.Post).all()
    #posts = db.query(model.Post).filter(model.Post.owner_id == current_user.id).all() # only user whos has created the 
    #y = json.dumps(f'[{posts}]')                                                      # will the see the post    
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
@router.post("/",status_code=status.HTTP_201_CREATED,response_model= schemas.PostBase)  # create Post # working with Autherization
def create_posts(post:schemas.PostCreate,db:Session= Depends(get_db),user_id: int = Depends(oauth2.get_current_user)):  # post is for pydantic model ,current_user: int = Depends(oauth2.get_current_user)
    print(user_id.id)
    print(type(user_id.create_at))
    #print(cu)
    new_post = model.Post(owner_id = user_id.id,**post.dict())  # owner_id = user_id.id,
    #print(new_post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post) # new_post response comes in sqlAclemy model hence is class Config: in schemas file
    return new_post
#######################################################
@router.get("/{id}",response_model=schemas.PostOut)                       # get individual data 
#@app.get("/posts/{id}",status_code=status.HTTP_200_OK)                       # get individual data 
async def get_post(id: int, db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    #owner_id = current_user.id
    #print(owner_id)
    print(current_user.email)
    #post = db.query(model.Post).all()
    #post = db.query(model.Post).filter(model.Post.id == id).first()
    post = db.query(model.Post,func.count(model.Vote.post_id).label("votes")).join(model.Vote, model.Vote.post_id == model.Post.id,isouter=True).group_by(model.Post.id).filter(model.Post.id == id).first()
    #new_postsingle = model.Post(*post.dict())
    #print(f"response 1:{post}")
    #jsonpost = json.loads(json.dumps(f'[{post}]'),object_hook=lambda d: SimpleNamespace(**d))
    #print(f"json response :{json.dumps(jsonpost)}")
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail =f"post with id: {id} was not found")

    # if post.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
    #                          detail="Not authorized to perform requested action")                                  
    return post
#########################################################

@router.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT )    # Delete Post                   # delete individual data 
def del_post(id: int, db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    print(current_user)
    
    post_query = db.query(model.Post).filter(model.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                               detail = f"post with id: {id} does not exist" )

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                             detail="Not authorized to perform requested action")                                           

    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
#######################################################################################################
@router.put("/{id}",response_model=schemas.PostBase)      # Update Post
def update_post(id: int,Updated_post: schemas.PostCreate, db:Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)): # Updated_post is pydantic model
    print(current_user) 
    post_query = db.query(model.Post).filter(model.Post == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                                 detail=f"post with id: {id} does not exist") 

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                             detail="Not authorized to perform requestedaction")                                              
    
    post_query.update(Updated_post.dict(),synchronize_session=False)
    db.commit()
    return {"data": post_query.first()}
       
 ################################################################################  