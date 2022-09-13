from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
from .config import settings



SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
# #SQLALCHEMY_DATABASE_URL =  'postgresql://postgres:lock@2000@192.168.1.29/fastapi'

#"postgresql://postgres:postgres@localhost:5432/dbname"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

async def get_db():
    db = SessionLocal()
    try:
          print("tanveer")
          yield db
    finally:
          db.close()



# while True:
#     try:
#        conn = psycopg2.connect(host ='192.168.1.29',database='fastapi',user='postgres',password = 'lock2000',cursor_factory=RealDictCursor)
#        cursor = conn.cursor()
#        print("Database connection was  successful!")
#        break
#     except Exception as error:
#         print("connecting to Database failed")
#         print("Error: ", error)
#         time.sleep(2)