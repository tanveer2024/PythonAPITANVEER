# from fastapi import FastAPI,Depends, HTTPException, Response,status
# from typing import List
# import schemas
# from sqlalchemy.orm import Session
# from ..database import get_db,engine
# from .. import model
import pandas as pd

# # app = FastAPI

# # @app.get("/")
# # async def root():
# #     return {"message":"Welcome to internet   "}


# # ################################################################################
# # @app.get("/getall", response_model=List[schemas.Post])   # All get data get method       
# # def get_posts(db: Session = Depends(get_db)):
# #     posts = db.query(model.Post).all()
# #     return posts

# ############################################################################### 
# # # Create a New Record using Post method    
# # @app.post("/posts",status_code= status.HTTP_201_CREATED,response_model= schemas.PostBase)
# # def create_post(post:schemas.PostCreate,db:Session = Depends(get_db)):
# #     new_post = model.Post(**post.dict())
# #     db.add(new_post)
# #     db.commit()
# #     db.refresh(new_post)
# #     return new_post
# ###################################################################################
# # Get method to fetch individual row 
# # @app.get("/posts/{id}",response_model=schemas.PostResp)
# # def get_post(id: int,db:Session = Depends(get_db)):
# #     post = db.query(model.Post).filter(model.Post.id == id).first()
# #     if not post:
# #         HTTPException(status_code=status.HTTP_404_NOT_FOUND,
# #                       detail = f"post of id: {id} was not found " )
# #     return post    
# #######################################################################################
# # Delete one record from the database
# # @app.delete("/posts/{id}", status_code= status.HTTP_204_NO_CONTENT)
# # def del_post(id: int,db: Session = Depends(get_db)):
# #     post = db.query(model.Post).filter(model.Post.id == id)

# #     if post.first() == None:
# #         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND
# #                             ,detail= f"post with id: {id} do not exist")
# #     post.delete(synchronize_session=False) 
# #     db.commit()
# #     return Response(status_code= status.HTTP_204_NO_CONTENT)
# #################################################################################
# # update the record in the database
# # @app.put("/posts/{id}", response_model=schemas.PostBase)
# # def update_post(id: int,update_post: schemas.PostCreate,db:Session = Depends(get_db)):
# #     post_query = db.query(model.Post).filter(model.Post.id == id)

# #     post = post_query.first()

# #     if post == None:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
# #                              detail= f"post with id: {id} does not exist")

# #     post_query.update(update_post.dict(),synchronize_session=False)
# #     db.commit()
# #     return post_query.first()     
#     ##################################################################################                    
# # Add a user in the userData Base 
# # @app.post("/users", status_code=status.HTTP_201_CREATED) 
# # def create_user(user: schemas.UserCreate,db: Session = Depends(get_db)):
# #     new_user = model.User(**user.dict()) # Un **user is meaning unpacking the dict
# #     db.add(new_user)
# #     db.commit()
# #     db.refresh(new_user)
# #     return new_user
#  ####################################################################################   
#  #Add a user in the user table
# # @app.post("/userdetail",status_code= status.HTTP_201_CREATED)  # main.py as hashing too
# # def create_user(user:schemas.UserCreate,db:Session = Depends(get_db)):
# #     new_user = model.User(**user.dict())
# #     db.add(new_user)
# #     db.commit()
# #     db.refresh(new_user)
# #     return new_user      

# #######################################################################################    
# # @app.get("/users/{id}") # Individual User Record is fetch
# # def get_userid(id: int, db: Session = Depends(get_db)):
# #     user1 = db.query(model.User).filter(model.User.id == id).first()
# #     if not user1:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND
# #                 ,detail=f"User with id : {id} does not exist")
# #     return user1            
# ##########################################################################################################

# # df = pd.DataFrame({'Vehicle':'cars':['kia','Lambagoni'],
# #                               'motors':['KTM RC','Pulsar','Honda']
# #                  })

# # print(df)
# # d =df.groupby('Type').count() # groupby function in python
# # print(d)


# # df1 = pd.DataFrame({'Vehicle':['Honda','Mini','Hydai']})
# # df2 = pd.DataFrame({'Motor': ['Bajaj','Yamaha','Susuki']})

# df=pd.DataFrame()
# bikes = ["Bajaj","TVS","Honda","Kawa","BMW"]
# cars = ["Lam","Mas","Ferra","Hyda","Ford"]

# d = {"bike": bikes,"car":cars}
# type1 = {"bikenew":bikes,"carnew":cars} 
# df=pd.DataFrame(d)
# df2=pd.DataFrame(type1)
# print(df)
# print(df2)
# d1 = df2.groupby(type1).count()
# print(d1)

# def add_n(n):
#     return n * 3
# nb = [1,2,3]
# print(list(map(add_n,nb)))     

# letters = ("A,B,C")
# n = letters.split("/")
# print(n)


# def smart_div(func):
#     def inner(a,b):
#         if a < b:
#             a,b = b,a
#         return func(a,b)
#     return inner

# @smart_div
# def div(a,b):
#     print(a/b)

# div(3,21)   


# cmp(l, l1)

# l = 1
# l1 = 2
# print(cmp(l,l1))

class A:

    def __init__(self) -> None:
        print(" Init of A ")

    def feature1(self):
        print("Feature 1-A is working")

    def feature2(self):
        print("Feature 2 is working")

class B:

     def __init__(self) -> None:
        print("Init of B")   # init not there here then A init is called
            

     def feature1(self):
        print("Feature 1-B is working")

     def feature4(self):
        print("Feature 4 is working")


class C(A,B): # class C(B,A)

    def __init__(self) -> None:
        super().__init__()
        print("in C init")
        super().__init__()

    def feat(self):
        super().feature2()

a1 = C() 
a1.feature1()
a1.feat()       


##################################################################
num = 29

flag = False

if num > 1:

    for x in range(2,num):
        if (num % x) == 0:
            flag = True
            break

if flag:
    print("THe number  is not a prime number",f"{num}")
else:
    print("The number  is  a prime", f"{num}")


#############################################################################################################
# Program to check if a number is prime or not
num  = 29

# To take input from the user
num = int(input ("Enter the number:\n" ))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if ( num % i ) == 0:
            # if factor is found, set flag to True
           flag = True
           # break out of loop
           break
# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")  
