from jose import JWTError, jwt   # oauth is for token creation 
from datetime import datetime,timedelta

from requests import Session
from . import schemas,database,model
from fastapi import Depends,status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from sqlalchemy import inspect
from starlette.exceptions import HTTPException as StarletteHTTPException
from types import SimpleNamespace
import json
from .config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


#SECRET_KEY
#Algorithm
#Expriation time 

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)  # to_encode payload

    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        print(token)
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])  
        id : str = payload.get("user_id")
        print(id)
        if id is None:
           raise credentials_exception
        token_data = schemas.Tokendata(id=id)    
    except JWTError as e :
        print(e)
        raise credentials_exception
    except AssertionError as e:
          print(e)    
    return token_data

# def object_as_dict(obj):
#     return {c.key: getattr(obj, c.key)
#             for c in inspect(obj).mapper.column_attrs}        

def get_current_user(token: str = Depends(oauth2_scheme),db:Session = Depends(database.get_db)):  # Calls the verrify_access_token
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"Could not validate credentials",
                            headers={"WWW-Authenticate":"Bearer"}  )
    token1 = verify_access_token(token,credentials_exception)
    print(token1.id)
    print(model.User.id)
    user = db.query(model.User).filter(model.User.id == token1.id).first()
    #print(dict(user).items)
    #x = json.loads(json.dumps(f'[{posts}]'),object_hook=lambda d: SimpleNamespace(**d))
    #user_new = json.loads(json.dumps(f'[{user}]'),object_hook=lambda g: SimpleNamespace(**g))
    print(type(user))
    return user
    #return verify_access_token(token,credentials_exception)                               