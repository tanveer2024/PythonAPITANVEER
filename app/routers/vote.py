from multiprocessing import synchronize
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from .. import schemas, database,model,oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List,Optional

router = APIRouter(
    prefix = "/vote",
    tags = ['Vote']
)
#############################################################################################
@router.get("/",response_model= List[schemas.VoteReturn])   # Get all post
def get_votes(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
     #print(limit) # limit is to limit the post and skip how many you need to skip the post that is 
                     # if http://127.0.0.1:8000/posts?limit=4&skip=1 in postman with limit it will 
                     # show 4 and with skip it will skip the first entry so showning three record     
     votes = db.query(model.Vote).all()
     #posts = db.query(model.Post).all()

     return votes

###################################################################################

####################################################################################################
@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote,db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

        
    post = db.query(model.Post).filter(model.Post.id == vote.post_id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"Post with id:{vote.post_id} does not exist")

    
    vote_query = db.query(model.Vote).filter(model.Vote.post_id == vote.post_id,model.Vote.user_id == current_user.id)
    
    found_vote = vote_query.first()
    if(vote.dir == 1):
       if found_vote:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user {current_user.id} has already voted on post { vote.post_id}")
       new_vote = model.Vote(post_id = vote.post_id, user_id= current_user.id)
       db.add(new_vote)
       db.commit()
       return {"message": "successfully added vote"}

    else:
         if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exist")    
         vote_query.delete(synchronize_session= False)
         db.commit()

         return {"message": "successfully deleted  vote"}
##########################################################################################         
