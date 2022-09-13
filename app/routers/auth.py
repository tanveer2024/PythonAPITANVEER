from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
from .. import database,schemas,model,utils,oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router = APIRouter(tags=['Authentication'])  # OAuth2PasswordRequestForm has a 
                                             # username used in schema so instead
@router.post('/login',response_model= schemas.Token)                       # email we change it to username 
def login(user_credentials: OAuth2PasswordRequestForm = Depends() ,db:Session = Depends(database.get_db)):  # user_credentials:schemas.UserLogin # OAuth2PasswordRequestForm = Depends()
 #{
   #  OAuth2PasswordRequestForm
   #  "username": ""
   # "password": "" 
 #}
 user = db.query(model.User).filter(model.User.email== user_credentials.username).first()  # change to email
 if not user:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                        detail=f"Invalid Credentials")

 if not utils.verify(user_credentials.password, user.password):
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                         detail=f"Invalid Credentials")
 access_token = oauth2.create_access_token(data = {"user_id": user.id})
 print(access_token)                       

  # create token                       
 return {"access_token": access_token, "token_type": "bearer"}                                                