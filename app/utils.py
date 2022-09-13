import bcrypt  # utils is for password hashing 
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")
# pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto") # bcrypt hashing algoritum


def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)    