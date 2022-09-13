from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from .. import schemas,model,utils
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix= "/users",
    tags= ['Users']
)

##############################################################################
# create a user in the user table
@router.post("/", status_code=status.HTTP_201_CREATED,response_model= schemas.UserOut) # ,response_model= List[schemas.UserCreate] 
def create_user(user: schemas.UserCreate,db: Session = Depends(get_db)):
    # hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = model.User(**user.dict()) # Un **user is meaning unpacking the dict
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
########################################################################
@router.get("/{id}",response_model= schemas.UserOut) # Individual User Record is fetch
def get_userid(id: int, db: Session = Depends(get_db)):
    #hashed_password = utils.hash(model.User.password)
    user1 = db.query(model.User).filter(model.User.id == id).first()
    if not user1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND
                ,detail=f"User with id : {id} does not exist")
    return user1 
########################################################################    