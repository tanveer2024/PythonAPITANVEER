
from ast import JoinedStr
from cProfile import run
from calendar import c
from collections import _OrderedDictKeysView
from copy import copy
from ctypes import Union
#from curses import use_default_colors
import datetime
from distutils.archive_util import make_archive
#from distutils.sysconfig import customize_compiler
from genericpath import samefile
from graphlib import TopologicalSorter
from http.client import HTTPS_PORT
from importlib.util import module_for_loader
from inspect import ClassFoundException
from json import tool
from ntpath import join
from operator import index
from optparse import Values
import os.path
from platform import python_branch
from pyclbr import Function
from re import M, X
from reprlib import aRepr
from runpy import run_module
from select import select
from sqlite3 import Row
from telnetlib import STATUS
from tracemalloc import DomainFilter
from turtle import begin_fill, onclick, title
from urllib import request
import json
import urllib
#import requests
#from .add import add_together
import random
import math
import operator
from urllib.parse import quote_from_bytes
from winreg import REG_LEGAL_OPTION
from fastapi import FastAPI
from gridfs import Database
#import mypy_extensions
#import mypy
#import MySQLdb
import pymongo

# curl is a command-line tool to transfer data to or
#  from a server, 
#  using any of the supported protocols
#   (HTTP, FTP, IMAP, POP3, SCP, SFTP, SMTP, TFTP, TELNET, LDAP, or FILE).
#   curl is powered by Libcurl.
#    This tool is preferred for automation since it is designed to work without user interaction. 
# curl can transfer multiple files at once. 


#from asyncore import read
# from ast import Index
# from code import InteractiveInterpreter
# from crypt import methods
# from doctest import OutputChecker
# from itertools import count
# from multiprocessing.sharedctypes import Value
# from operator import countOf, index, itemgetter
# from optparse import Values
# from platform import python_branch
# from tkinter import Variable
# from typing import ItemsView, KeysView
# from unicodedata import name
# from xml.dom.xmlbuilder import _DOMInputSourceEncodingType
# from h11 import Data
import pandas as pd
import numpy as np
from functools import reduce
import decimal
from psycopg2 import ProgrammingError

from pyparsing import Or
from sqlalchemy import desc, table
from yarl import URL
# # from math import factorial
# import random
# from random import shuffle










# df=pd.DataFrame()
# bikes = ["Bajaj","TVS","Honda","Kawa","BMW"]
# cars = ["Lam","Mas","Ferra","Hyda","Ford"]
# df["cars"] = cars
# df["bikes"] = bikes
# print(df) 
######################################################################
# df=pd.DataFrame()
# bikes = ["Bajaj","TVS","Honda","Kawa","BMW"]
# cars = ["Lam","Mas","Ferra","Hyda","Ford"]
# df["cars"] = cars
# df["bikes"] = bikes
# print(df)
########################################################################
# x = np.diag([1, 2, 3, 4, 5])
# print(x)
# Output

# [[1 0 0 0 0]
#  [0 2 0 0 0]
#  [0 0 3 0 0]
#  [0 0 0 4 0]
#  [0 0 0 0 5]]

 ##############################################################################
# x = np.zeros([5,5])
# print(x)
# create list (bikes and cars)
# create dictionary
# pass and argument convert dictionary into dataframe

# df = pd.DataFrame(d)

# data  = ["1",2 ,"three",4.0]
# series = pd.Series(data)
# print (series)
# print(type(series))

df = pd.DataFrame({'Vehicle':['kia','Lambagoni','KTM RC','Pulsar','Honda'],'Type': ["car","car","Motor","Motor"]})
print(df)
d =df.groupby('Type').count() # groupby function in python
print(d)

# n1 = np.zeros((5,5))
# print(n1)
# df = pd.read_csv("C:\\Users\\tanveer.ansari_quali\\Documents\\data.csv")
# print(df.head(1))

# df=pd.DataFrame() # empty Dataframe
# bikes=["Bajaj","TVS","Honda","Kawa","BMW"]  # list
# cars= ["Lam","Masserati","Ferra","Hyundai","Ford"]

# d = {"cars":cars,"bikes":bikes} # dictionary
# df = pd.DataFrame(d)
# print(df)

# df1=pd.DataFrame()
# colours=["yellow", "Red","White","Black","Purple"]
# model1 = ["normal","SUV","Jeep","HunchBack","Lumosieon"] 
# d1 ={"Colours":colours,"model1":model1}
# df1 = pd.DataFrame(d1)
# print(df1)
# df2 = pd.DataFrame()
# d2 = {df.index, df1.index}
# # df2 = pd.DataFrame(d2)
# df2 = pd.DataFrame(d2)
# print(df2)
# df2 = pd.DataFrame(d2)
# print(df2)


# df=pd.DataFrame()
# a=[10,20,30,40,50]
# df.index=a
# df["cars"]= cars
# df["bikes"] = bikes

# print(df.loc[10])

# n1 = np.array([10,20,30,40,50,60])
# print(np.mean(n1))
# print(np.median(n1))
# print(np.std(n1))

# dict = {1:'a',2:'b',3:'c'}
# print(dict.keys())

# n = "tanveer"
# print(n.capitalize())

# list = [0,1,2,3,4,5,6,7,8,9]
# list.insert(6,10) # Insert 10 at 6th index
# print(list)
########################################
lit = [1,2,3,4,20]
# # def list_sum(num1,num2,num3,num4,num5):
#     #lit = [1,2,3,4,5]
#     # return num1+num2+num3+num4+num5
l = sum(lit)
print(l)
#########################################
lit = [1,2,3,4,5]
print(*lit * 2)


# list.insert(6,10) # Insert 10 at 6th index
# print(list)

# my_list = ["a","b","c","c","d","e","e","f","u","v"]
# my_list1 = list(set(my_list)) # set do not support duplicates
# #my_list1 = list(dict.fromkeys(my_list)) # dict do not allow duplicate keys
# print(my_list1)

# keys = {'a','e'}
# value = [1]
# vowels = dict.fromkeys(keys,value)
# print(vowels)
#o/p {'e': [1], 'a': [1]}
# value.append(2)
# print(vowels)
#o/p {'e': [1, 2], 'a': [1, 2]}

#list comprehension
# list = [i for i in range(1000)]
# print(list)

# #bytes()

# def add_func(n):
#     return n * 3
# nb = (1,2,3,4,5,6,7,8)   
# result = map(add_func,nb)
# print(list(result))    
# var = copy(nb)
# print(var)

# n=10
# print(type(n))
# new_n = str(n)
# print(type(new_n))

# letters = ("A,B,C")
# n = letters.split("/")
# print(n)

# triple = lambda x: x * 3 # lambda arguments : expression
# print(triple(100))
##############################################
def factorial (a):
    if a==1:
        return 1
    else:
        return (a * factorial(a - 1))

input_number = input ("Enter the factorial number :  ")
n= int(input_number)
print("The factorial of ", n,"is",factorial(n))

# a = "Hello"
# b = 15
# c = 0
# sample_list = []
# print(bool(a))
# print(bool(b))
# print(bool(c))
# print(bool(sample_list)) # if value zero or empty error bool will give false result.

# a=[1,2,3]
# b=[2,3,4]

# d = {"col1":a,"col2":b}
# df= pd.DataFrame(d)

# df["Sum"] = df["col1"]+df["col2"]
# df["Difference"] = df["col2"]-df["col1"]

# print(df)
# data = {"col1":[1, 2, 3], "col2":[4, 5, 6], "col3":[7, 8, 9]}
# df = pd. DataFrame(data)
# selected_Columns = df[["col1","col2"]]
# new_df =  selected_Columns.copy()
# print(new_df)

# d = {"col1":[1,2,3],"col2": ["A","B","C"], "col3":["A1","B2","C3"]}

# df=pd.DataFrame(d)
# print(df)
# df=df.drop(['col3'],axis=1) # axis= 1 is for the column and axis = 0 is for rows
# df=df.drop([1,2],axis=0)
# df=df.drop([0,2],axis=0)

# print(df)
#df=df.drop([0-1],axis=0)
#df = df.iloc[0] # for rows only use loc to locate row and column both
# df = df.loc[:,['col2']] # it takes row 0 as output i.e 0 means 
# print(df)
# df.dropna(inplace=True)
# df=df[df.col2!='B']
# print(df)
# df=pd.DataFrame() # empty Dataframe
# bikes=["Bajaj","TVS","Honda","Kawa","BMW"]  # list
# cars= ["Lam","Masserati","Ferra","Hyundai","Ford"]
# d = {"cars":cars,"bikes":bikes} # dictionary
# df = pd.DataFrame(d)
# a=[10,20,30,40,50]
# df.index=a
# print(df)
            

# sequ = [5,8,10,20,50,100]          
# sum =  reduce(lambda x,y: x+y,sequ)  
# print(sum)     


# n1 = np.array([20,50])
# n2 = np.array([35,85])
# print(np.hstack((n1,n2)))
# print(np.vstack((n1,n2)))  

# str1 = " Good    Morning    India "  # spaces can be removed using strip() or replace() functions
# #print(str1.replace(" ","-")) # strip() function is used to remove the leading and trailing white spaces
# #print(str1.strip())
# print(str1.lstrip())
# print(str1.rstrip())
# print(str1.strip('._'))

# def smart_divide(func):
#     def inner(a,b): # decorator are function that takes another function as argument
#         print("Dividing",a, "by", b)
#         if b == 0:
#             print("Make sure Denominator is not zero")
#             return
#         return func(a,b)
#     return inner
# @smart_divide #same as code "divide=smart_div(divide)"
# def divide(a,b):
#     print(a/b)
# divide(14,0)
# x = int(input("Enter number:"))            
# for n in range(x):
#     for i in range (x-1):
#         print(n, end=" ")
#         print("\n")    # Pattern printing



# temp = n
# rev = 0

# while (n > 0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp == rev):
#     print("The number is a palindrome")
# else:
#     print("The number is not a palindrome")
# n = int(input ("Enter The number for pattern:" ))           
# def pattern_print(n):
#     for i in range(0,n):
#         for j in range(0,i+1):
#             print( i , end= " ")
#         print("\r")
# pattern_print(n)  
# 
# #####################################################################################################          
# def pattern_3(num):
#     number = 1
#     #outer loop -handling the number of rows
#     # inner loop controlling the number
#     for i in range (0, num):
#         number = 0
#     # inner loop to handle number of columns
#         for j in range(0,i+1):
#              print(number, end = " ")
#              number = number + 1
#         print("\r")
# num = int(input ("Enter The number for pattern:" ))
# pattern_3(num)



#test#####################################################

# def pattern_3(num):
#     number = 1
#     #outer loop -handling the number of rows
#     # inner loop controlling the number
#     for i in range (0, num):
#         number = 0
#     # inner loop to handle number of columns
#         for j in range(0,i+1):
#              print(number, end = " ")
#              number = number + 1
#         print("\r")
# num = int(input ("Enter The number for pattern:" ))
# pattern_3(num)

############################################################################################
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#########################################################################################
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break
###########################################################################################
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)

#########################################################################################
# for x in range(0,6):
#   print(x)  
############################################################################################
# for x in range(2, 6):
#   print(x)

##################################################################################################
# for x in range(2, 30, 3):
#   print(x)
#########################################################################################################################
# n= 6
# for x in range(n):
#     for y in range(n-x+1):
#         print(end = " ")
#     for y in range(x+1):
#         # Formula for nCr = n!/((n-r)!*r!)
#         print(factorial(x)//(factorial(y)*factorial(x-y)), end= " ")
#     print() ##  pascal factorial triangle


    #############################################################################################
    # def pattern_3(num):
    # #number = 1
    # #outer loop -handling the number of rows
    # # inner loop controlling the number
    #  for i in range (0, num):
    #     number = 0
    #     num = num + 1
    #     print(number)
    #     print(num)
    # num = int(input("Enter the number of n:"))
    # pattern_3(num)    



    #0C0
    #1C0 1C1
    #2C0 2C1 2C2
    #3C0 3C1 3C2 3C3
###########################################################################################################
# def pattern_5(num):
#         # initiated value of A as 65
#         # ASCII value equivalent
#         number = 65
#         # outer loop always handles the number of rows
#         for i in range(0,num):
#             # inner loop handles  the number of columns
#              for j in range(0,i+1):
#                  # finding the ASCII equivalent
#                  char = chr(number)
#                  # printing char values 
#                  print(char,end=" ")
#              # incrementing the number
#              number = number + 1
#              # ending line after each row 
#              print("\r")
# num = int(input("Enter the number of rows in pattern"))
# pattern_5(num)             

##################################################################################################
# def pattern_6(num):
#         # initiated value of A as 65
#         # ASCII value equivalent
#         number = 65
#         # outer loop always handles the number of rows
#         for i in range(0,num):
#             # inner loop handles  the number of columns
#              for j in range(0,i+1):
#                  # finding the ASCII equivalent
#                  char = chr(number)
#                  # printing char values 
#                  print(char,end=" ")
#              # incrementing the number
#                  number = number + 1 # This number = number + 1 runs within inner loop
#              # ending line after each row 
#              print("\r")
# num = int(input("Enter the number of rows in pattern"))
# pattern_6(num)          

###########################################################################################################
# def pattern_7(num):
#         # initiated value of A as 65
#         # ASCII value equivalent
#         number = 65
#         # outer loop always handles the number of rows
#         for i in range(0,num):
#             # inner loop handles  the number of columns
#              for j in range(0,i+1):
#                  # finding the ASCII equivalent
#                  char = chr(number)
#                  # printing char values 
#                  print(char,end=" ")
#              # incrementing the number
#              number = number + 1 # This number = number + 1 runs within outer loop
#              # ending line after each row 
#              print("\r")
# num = int(input("Enter the number of rows in pattern"))
# pattern_7(num)

######################################################################################################
# d1 = {"k1":10,"k2":20,"k3":30}
# #d1 = {"k1":10,"k2":20,"k3":30}
# for i in d1.keys():
     
#     d1[i] = d1[i] + 1
#     print(d1[i])
# print(d1.values())   ### how to increase dictionary value 

# Dictionary in Python is a collection of data values which only 
# maintains the order of insertion, used to store data values like a map,
#  which, unlike other Data Types that hold only a single value as an element,
#   Dictionary holds key: value pair.

# keys() method in Python Dictionary, 
# returns a view object that displays a list of all the keys in
#  the dictionary in order of insertion.

# map() function returns a map object(which is an iterator) of the 
# results after applying the given function to each 
# item of a given iterable (list, tuple etc.)

# Syntax :

# map(func, iter)
# Parameters :

# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.

def addition(n):
    return n + n
  
# We double all numbers using map()
numbers = (1, 2, 3, 4,5)
result = map(addition, numbers)
print( list(result))

#########################################################################################    
# n = random.random()
# print(n)  # generate random number

################################################################################################################
# n = random.randint(10,20) # give random number in the range of 10 to 20
# print(n)   
#####################################################################################################
# def func1(*args, **kwargs):
#      print(args)
#      print(kwargs)      # Name argument is take up by **kwargs i.e name='Tanveer'
#                          #  and unnamed argument is take up by args is 1,hello
# func1(1,'hello', name='Tanveer')    

# ######################################################################################################
# first_list = [1,2,3,4,5]
# second_list = first_list
# print(first_list)
# second_list.append(6)
# print(first_list)
# print(second_list)   # this is shallow copy and not deep copy in python coz both are in the same memory location
# print(hex(id(first_list)))
# print(hex(id(second_list)))
######################################################################################################
# a = [1,2,3,4,5,6,7,8,9]
# # print(a[-1:-5:-1])  # -5:-2 is range function o/p 9,8,7  o/p  [9, 8, 7, 6]
# # print(a[-1:-5:-2])   # 0/p is 9,7 that is -5:-2 gets in range function o/p [9, 7]
# # print(a[-1:-5:-3])    # 0/p is 9,6
# # print(a[-1:-5:-5])
# print(a[-1:-4:-2])
 #################################################################################################
# import random
# value = 'A'
# print("ASCII value of '" + value +"' is ", ord(value))
# values = ['You','Never', 'Hated', 'Me']
# random.shuffle(values)
# print(values)

######################################################################################################
# floor division takes out the decimel value and gives the lowest value o/p
# print(5//2) # o/p 3
# print(-7//2) # o/p -4 coz -3.5 than convert to lowest value that is -4 
# print(7.0//2) # 3.0
# print(-7.0//2) # -4.0

######################################################################################################
#Pass by value and Pass by Reference

# def check_pass(arr):
#     arr.append(4)
# arr = [1,2,3]
# #arr.append(5)
# print(arr) # Call by value memory address remain the same 
# #print (hex(id(arr)))
# check_pass(arr) # pass the memory location of the value where it is stored so the changes is reflected everywhere
# print(arr) # Call by Reference sending the memory location where the value is stored so if append  
# print (hex(id(arr)))
# arr.append(5)
# print(arr)

#o/p
#[1, 2, 3]
#[1, 2, 3, 4]
#[1, 2, 3, 4, 5]
# Now present code
#[1, 2, 3, 4]
#[1, 2, 3, 4, 4]
#[1, 2, 3, 4, 4, 5]

#########################################################################################################
# def check_num(x):
#     x=10
#     print(x)
#     print(hex(id(x)))
#check_num(20)    



# x = 8
# print(x)
# print(hex(id(x)))
# check_num(x)

   

#########################################################################################################
#o/p of following code 
# print("Hello World"[:-2])
# print("Hello World"[::-1]) # reverse the O/p
# #########################################################################################
# #O/p for list:list x 2
# list1 = [1,2,3,4,5,6]
# print(list1*2) # if you using this with list the o/p of the list will be double
# print(list1*3) # if you using this with list the o/p of the list will be triple 
###################################################################################################
##Armstrong number 153  1 cube is 1, 5 cube is 125 3 cube is 27 so sum of 1+125+27 is 153
# number_input = int(input("Enter a number:"))
# sum = 0

# temp = number_input # Finding the cube of every digit
# while temp > 0:
#     digit = temp % 10
#     print(digit) # 153 3 is Out first loop,5 is out second loop, three 1 is out
#     sum += digit ** 3 
#     print(sum) #  3 * 3 *3 = 27,5 * 5 * 5 = 125, 1 * 1 * 1 = 1
#     temp //=10 
#     print(temp)  # 15 goes back to the loop

# #temp = 153
# #temp = temp % 10 # 3 is o/p
# #temp //=10
# #print(temp)

# if number_input == sum:
#      print(number_input,"is an Armstrong number")
# else:
#     print(number_input,"is not an Armstrong number")    

# o/p    Enter a number:153
# 3
# 27
# 15
# 5
# 152
# 1
# 1
# 153
# 0
################################################################################
#  Done
## perfect number is where the sum of the number is the number itself i.e is 6 is perfect number coz
# 6 = 1 x 6 , 2x 3, 3 x 2 ..... 1+2+3 = 6
# number_input = int(input(" Please Enter any Number: "))

# sum = 0

# for i in range(1,number_input):
#     if(number_input % i == 0):
#         print(number_input)
#         print(i)
#         sum = sum + i
# if (sum == number_input):
#     print("%d is a perfect Number" %number_input)
# else:
#     print("%d is a not perfect Number" %number_input)         

###########################################################################################################
   # Print a strong number in python
   # sum of factorial of each number must be same as input 145 --> 1! + 4! + 5! = 145

# number_input = int(input("Enter the number:"))
# sum = 0
# temp = number_input
    
# #temp = temp % 10  #Reminder goes in temp that is 14[5]/10 then 5 goes in temp
# while(number_input):
#     i = 1
#     fact = 1
#     rem = number_input%10
#     while (i<=rem):
#          fact = fact * i
#          i = i + 1
#     sum= sum+fact
#     number_input //= 10
# if(sum==temp):
#     print("Given number is strong number")
# else:
#     print("Given number is not strong number") 

###############################################################################################################
temp = 8.7
temp = temp // 2
print(temp)   

# i=1
# fact = 1
# n = int(input("Enter the number for factorial :"))
# while (int(i)<=n):
#     fact=fact*i
#     i=i+1
# print(fact)
################################################################################################
# sample_list = []

# n = int(input("Enter number of element:"))

# for i in range(1,n+1):
#     b=int(input(f"Enter the element {i} :"))
#     sample_list.append(b)
#     sample_list.sort()
# print("The Second largest element is :",sample_list[n-2])    

##################################################################################################
# sample_list = []

# n = int(input("Enter number of element:"))

# for i in range(1,n+1):
#     b=int(input(f"Enter the element {i} :"))
#     sample_list.append(b)
#     sample_list.sort()
# print("The second largest element is :",sample_list[n-2])  
# 
# #####################################################
# n = 195//10
# print(n)  # strong number
# number_input = int(input("Enter the number_input :"))
# sum = 0 
# temp = number_input
# while (number_input):
#     i = 1
#     fact = 1
#     rem = number_input%10
#     while (i<=rem):
#         fact = fact * i
#         i = i + 1
#     sum=sum+fact
#     number_input //= 10
# if (temp == sum):
#  print (f"The given number {temp} is strong number. ")
# else:
#  print(f"The given number {temp} is not a strong number.")   
           
###################################################################################################
# Prints all letters except 'e' and 's' Python Continue Statement returns the control to the beginning of the loop.
# i = 0
# a = 'geeksforgeeks'
 
# while i < len(a):
#     if a[i] == 'e' or a[i] == 's':
#         i += 1
#         continue
         
#     print('Current Letter :', a[i])
#     i += 1
##########################################################################################################
# break the loop as soon it sees 'e' Python Break Statement brings control out of the loop.
# or 's'
# i = 0
# a = 'geeksforgeeks'
 
# while i < len(a):
#     if a[i] == 'e' or a[i] == 's':
#         i += 1
#         break
         
#     print('Current Letter :', a[i])
#     i += 1
############################################################################################################
# An empty loop The Python pass statement to write empty loops. 
# Pass is also used for empty control statements, functions, and classes.
# a = 'geeksforgeeks'
# i = 0
 
# while i < len(a):

#     i += 1
#     pass
   
#     print('Value of i :', i)

# In Python, pass is a null statement. The interpreter does not ignore a pass statement,
#  but nothing happens and the statement results into no operation. The pass statement is useful 
# when you don't write the implementation of a function but you want to implement it in the future.
         
 #########################################################################################################
 # Python program to demonstrate
# while-else loop
 
# i = 0
# while i < 4:
#     i += 1
#     print(i)
# else:  # Executed because no break in for
#     print("No Break\n")
 
# i = 0
# while i < 4:
#     i += 1
#     print(i)
#     break
# else:  # Not executed as there is a break
#     print("Tanveer")        
####################################################################################################
# number_input = int(input("Enter the number :"))

# sum = 0

# for i in range(1,number_input):
#     if(number_input % i == 0):
#         sum = sum + i
# if(sum == number_input):
#     print('%d is a perfect number:'%number_input)
# else:
#     print('%d is a not perfect number:'%number_input) 

########################################################################################################
# sum = 0
# digit = 3
# sum += digit ** 3
##############################################################################################################


# def pattern(num):
#     number = 65
#     for i in range(0,num):
#         for j in range(0,i+1):
#             char = chr(number)
#             print(char,end=" ")
#             number = number + 1
#         print("\r")
# num = int(input("Enter the pattern number"))
# pattern(num)       
# 
# #####################################################################################
# # # Mutable data type are 
# # lists
# # Dictionaries
# # sets

# # color = ["Red", "Green", "Blue"]
# # print(color)
# # color[0] = "Black"
# # color[-1] = "White"
# # print(color)     

# # # Lists
# # l = []
 
# # # Adding Element into list
# # l.append(5)  # list use append and pop , set use add and remove
# # l.append(10)
# # print("Adding 5 and 10 in list", l)
 
# # # Popping Elements from list
# # l.pop(0)
# # print("Popped one element from list", l)
# # #print()

# # Set
# # s = set()
 
# # Adding element into set
# # s.add(5)
# # s.add(10)
# # print("Adding 5 and 10 in set", s)
 
# # # Removing element from set
# # s.remove(5)
# # print("Removing 5 from set", s)
# # print()

# # Tuple
# # l=[]
# t = tuple()
 
# # # # Tuples are immutable
# y = t.count(2)
# print("Tuple", t)
# print(y)
# # print()
 
# # Dictionary
# d = {}
# Adding the key value pair
# d[5] = 5
# d[10] = 10
# print("Dictionary", d)  # 
 
# # Removing key-value pair
# del d[10]
# print("Dictionary", d)

# df=pd.DataFrame()

# Bikes = ["Bajaj","Hero"]
# Cars = ["Maruti","Hyundai"]

# d= {"Cars": Cars, "bikes":Bikes}
# df=pd.DataFrame(d)
# print(df)


# myTuple = ("John", "Peter", "Vicky")
# myTuple1 = ("a","b","c")
# mySeparator = ["Look", "Look1"]
# a = myTuple.index("Peter")
# print(a)
# myTuple3 = myTuple + myTuple1
# x = np.vstack((myTuple,mySeparator))
# x = mySeparator.leftjoin(myTuple3)
# print(x)
#print(x)
# myDict = {"name": "John", "country": "Norway"}
# mySeparator = {"TEST", "TEST1"}

# myDict = {"name": "John", "country": "Norway"}
# mySeparator = "TEST"

# x = mySeparator.join(myDict)
# print(x)
# join is used when we need to extract data from different Dataframes which are having one
# or more common  columns
# 
# the stacking is done in a horizonal matter if the join() function is used.
# Pandas supports left join,inner join , right join and outer join 

# recursion function

# def tri_recursion(k):
      
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(k)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)
##################################################################################

#comprehension is copying list value another list 
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)
############################################################
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)
##################################################################
# str = "Welcome to Geeksforgeeks"

# arr = bytes(str, 'utf-8')

# print(arr)
########################################################
# x = bytes(6)
# print(x)
# ##############################################
# str = "Tanveer"
# for n in str:
#  print(str)
#  me = int(count(n,str))
# print(me)

# print("tanveer"[::-1])
#####################################################################
# age = 20
# age = 30
# print(age)

##############################################
# name = input("What is your name?")
# print("Hello " + name)
 
# birth_year = input("Enter your birth year:")
# age = 2022 - int(birth_year)
# print(age)

# converting the type Variable

# int()
# float()
# bool()
# str()

# first = input("First: ")
# second = input("Second: ")
# sum =float(first)+ float(second)
# print(sum)

# course = 'pythony'

# print(course.count('y'))
# print(course.capitalize)
# print(course.center)
# print(course.format)
# print(course.find('t'))

# text = "Tanveer"[:-1]
# print(text)


# f = open("D:\\Tanveer\\app\\demofile.txt","r")
# print(f.read(7))
# for e in f:
#     print(e)
# f.close()

# for e in f:
#  print(e)


# f = open("D:\\Tanveer\\app\\demofile.txt","a")
# f.write("I Love You!")
# f.close()
# f = open("D:\\Tanveer\\app\\demofile.txt","r")
# print(f.read())


# thisset = set(("apple","cup","va"))
# print(thisset) #{1,2,3}

# print(len(thisset))

# def hello() -> bool:
#     return "hello"
# print(hello())    

# test = "tanveer"[::-1]
# print(test)

#ternary if statment if statement in one line.
# number = -4
# message = "positive" if number > 0 else "0 or negative" 
# print(message)


# print(type([]))

# numbers = [1,2,2,3,4,"A",["B","C"]] 
# print(numbers[-1][1])

# Method in list 

# print (4 in numbers)

# deleting a number
# numbers.remove(2)
# print(numbers)
# del numbers[0:1]

# set duplicate is not allowed set has unordered displayed....
# numberList = [1,1]  List
# numbersSet = {1,1}  Set
# print(numberList)
# print(numbersSet)
# o/p 
# [1, 1]
# {1}
# set union , intersection, difference 

# lettersA = {"A","B","C","D"}
# lettersB = {"A","E","Z","C","D"}
#print(unions) # unions

# unions = lettersA.union(lettersB) # unions
# print(f"unions= {unions}") # unions
# intersection = lettersA & lettersB # intersection
# print(f"intersection= {intersection}") # intersection
# difference = lettersB - lettersA # difference
# print(f"difference= {difference}")
# 12 june 2022
# dictionary is key-value pair , duplicate keys are not allowed in dictionaries

# person = {
#   "name":"Tanveer",
#   "age":20,
#   "address": "USA"
  
#  }
# print(person["address"])
# print(person.keys())
# print(person.values())
# person["age"] = 100 # update age
# print(person)

# loop access set , list , dictionaries items

# names = ["a","b","c", "d"]
# names1 = {"a","b","c", "d"}

# for n in names:  # for loop
#     print(n)
# for n1 in names1:
#     print(n1)     

# for key in person:
#     print(f"key:{key}  value:{person[key]}")    

# for key, value in person.items():
#     print(f"key:{key}  value:{value}")

# numbers = [1,2,3,4,5,6]
# sum = 0
# for n in numbers:
#     sum += n
# print (f"sum = {sum}")

# for x in "bana":
#   print(x)

 

# n= 0
# for n in "tanveer":
#   n +=1
#   temp = text[::-n]
# print(temp)

# number = 0
# while number < 10:
#   if number == 5:
#     continue
#   number +=1
#   print(number)



# temp = str (text/10)
# print(ord(temp))
# print(text)

# text = "tanveer"[:-1]
# print(text)

# class MathUtils:

#     @staticmethod
#     def average(a, b):
#         return a + b / 2

# print(MathUtils.average(2, 1))

# def intersection(names1, names2):
#   return list(set(names1)& set(names2))
    

# if __name__ == "__main__":
#   names1 = ["Ava", "Emma", "Olivia"]
#   names2 = ["Olivia", "Sophia", "Emma"]
  
    
    
# print(intersection(names1, names2))


# class IceCreamMachine:
    
#     def __init__(self, ingredients,toppings):
#         self.ingredients = ingredients
#         self.toppings = toppings

    # @property
    # def output(self):
    #     return '{} {}'.format(self.ingredients,self.toppings)
    # @property
    # def toppings(self):
    #     return (self.toppings)


    # @property
    # def toppings(self):
    #     return (self.toppings)    

#     def scoops(self):
#       a= []
#       for i in self.ingredients:
#         for j in self.toppings:
#              a.append([i,j])
#       return a  
        

# if __name__ == "__main__":
#     machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
#     # print(machine.output)
#     print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
############################################################################
    # class MathUtils:
    #  @staticmethod
    #  def average(a, b):
    #     return (a + b )/ 2

    # print(MathUtils.average(2, 1))

################################################################################
# import cmath


# def find_roots(a, b, c):
#     d = (b**2) - (4*a*c) # 2x^2 + 10x + 8 
   
#     sol1 =  (-b-cmath.sqrt(d))/(2*a)
#     sol2 =  (-b+cmath.sqrt(d))/(2*a)
#     print('The solution are {0} and {1}'.format(sol1,sol2))        
# print(find_roots(2, 10, 8))
##############################################################################
# c = 10**2
# print(c)

# def group_by_owners(files):
#     # for i in files:
#     #   files = print(i,files[i])
#     #df = pd.DataFrame(files)
#     # x = ['k1','k2','k3']
#     # y = ['v1','v2','v3']
#     #files = dict.get()
#     #for 
    #  df =  dict.items(files)
#     #df1 = dict.values(files)
#    # df = pd.DataFrame(files)
    
    
#     # files = {a:index[0],
#     #          b:index[1],
#     #          c:index[2],
#     #         }
#     # df = pd.DataFrame(files)
    #  return df

# if __name__ == "__main__":    
#     files = {
#         'Input.txt': 'Randy',
#         'Code.py': 'Stan',
#         'Output.txt': 'Randy'
       
#     }   
#     print(group_by_owners(files))

# def is_adult(age):
#         if age >=16:
#           print("adult :)")
#         else:
#             print("not yet an adult:(")
# is_adult(45)    

##########################################################################
# def is_adult(age):
#     if age >= 16:
#         return True
#     else:
#         return False
# result = is_adult(45)
# print(result)            
#######################################################################
# def is_adult(age): # auto return true or false
#     return age >=16
# result = is_adult(80)
# print(result)   
# ################################################################
# def ConvertGender(gender = "unknown"):
#     if gender.upper() == "M":
#         return "Male"
#     elif gender.upper() == "F":
#         return "Female"
#     else:
#         return(f"The Gender {gender} is unknown")
# print(ConvertGender("F"))
# print(ConvertGender("M"))
# print(ConvertGender("f"))
# print(ConvertGender("m"))
# print(ConvertGender("hello"))    
# 
# ################################################################################     
# [].    # build.in funtion in python for list
# "".    # build.in funtion in python for string
# for _ in range(10):
#     print("Test")

#############################underscore (_) in python

#####single Underscore
#a In Interpreter
# b After a name
# c Before a name

#####Double Underscore
# 1. __leading_double_underscore
# 2. __Before_After__


# __Before_After__

# Name with start with __ and ends with same considers special methods
# in python.python provides these methods to use it as 
# the operator overloading depending on the user.

# import math

# print(math.isqrt(25))

# class Myclass():
#     def __init__(self):
#         self.__variable = 10

###############################################################################
# class Phone:  # object has attribute and behaviour.

#     def __init__(self, brand, price):    # init is actually is a constructor ,
#                                           # Class is a blue print to create phones
#         self.brand = brand                # self is current instance of the current class   
#         self.price = price # this is a attributes and method is the behaviour

    # def call(self,phone_number):  # Behaviour
    #     print(f"{self.brand} is calling {phone_number}")  

          # Object is iphone and samsung instance 
         

        
             
    
# if __name__ == "__main__":
#     iphone = Phone("Iphone_7", 300)
#     samsung = Phone("Samsung S", 1400)     
#     print(iphone.brand)
#     print(iphone.price)
#     iphone.call("999")

#############################################################################    
# class Phone:  # object has attribute and behaviour.



#     def __init__(self, brand, price):    # init is actually is a constructor ,
#                                           # Class is a blue print to create phones
#         self.brand = brand                # self is current instance of the current class   
#         self.price = price # this is a attributes and method is the behaviour


    # def __str__(self) -> str:
    #      return f"Brand = {self.brand}\n Price = {self.price} "
          

    # def call(self,phone_number):  # Behaviour
    #     print(f"{self.brand} is calling {phone_number}") 
     
     
    

    



      # Object is iphone and samsung instance 
         


        
             
    
# if __name__ == "__main__":
#     iphone = Phone("Iphone_7", 300)
#     samsung = Phone("Samsung S", 1400)     
#     print(iphone.brand)
#     print(iphone.price)
#     iphone.call("999")
#     print(iphone) 

##################################################################
# print(datetime.datetime.now())
# w writing a appending r reading r+ reading/writing
# file = open("./data.csv","r+")
# file.write("id,name,email\n")
# file.write("1,tanveer,tanveer.ansari@gmail.com\n")
# file.write("2,taha,taha.ansari@gmail.com\n")
# file.close()
#########################################################################
# filename = "data.csv"

# if os.path.isfile(filename):
#     with open (filename, "r") as file:
#         print(file.read())

# else:
#     print(f"file {filename} does not exist")
                                          # with keyword we do not need to put
#print(file.read())                        # the code file.close() it automatically does that  

##################################################################
# r = request.urlopen("http://www.google.com")
# print(r.getcode())
# print(r.read())
#######################################################################
# http://official-joke-api.appspot.com/random_joke

# from types import SimpleNamespace
#people = []
# url = "http://api.open-notify.org/astros.json"
# r = request.urlopen(url)
# print(r.getcode())
#data = requests.get('http://api.open-notify.org/astros.json')
# data = r.read()
# jsonData= json.loads(data)
#print(jsonData)
# a=dict.items(jsonData)
#print(a)
# class People:
#     def __init__(self, name,craft,) -> None:
#         self.name = name
#         self.craft = craft
        #self.people = people
    #def __str__(self) -> str:
     #   return f"joke {self.people} "      
        
# for j in jsonData['people']:
#     name = j["name"]
#     craft = j["craft"]

    #people = People(name,craft)
# if __name__ == "__main__":
#     print(jsonData['people'])
#     print(len(jsonData['people']))    
     

#if __name__ == "__main__":
  #  print(jsonData)
 #jsonData = json.loads(data.text, object_hook=lambda d: SimpleNamespace(**d))
# #data = json.loads()
# print(jsonData.message)
# print(jsonData.people)
# class Joke:
#      def __init__(self,people):
#        self.people = people
#        #self.craft = craft

# #     def __str__(self) -> str:
# #         return f" name = {self.name} craft = {self.craft}  "


#    jokes = []
# for j in jsonData.people:
#      people = j["people"]
#      #dict.craft = j["craft"]
    
# joke = Joke(people)
# # #jokes.append(joke)

# # #print(len(jokes))

# # #for joke in jokes:
# print(joke)

# x = np.zeros([5,5])
# print(x)
####################################
# df = pd.read_csv("mydata.csv")
# print(df)

# df = pd.read_csv("mydata.csv")
# print(df)
############################################################

# df = pd.DataFrame()

# cars = ["Honda", "Maruti", "BMW"]
# bikes = ["bajaj", "Peiggo", "vespa"]

# d = {"Cars": cars, "Bikes": bikes}
# df = pd.DataFrame(d)
# print(df)

# df1 = pd.DataFrame()

# cars = ["Ferrari", "Audi","Mercedes"]
# cycle = ["BMW","Mercedes","vespa"]

# d1 = {"Cars":cars,"Cycles": cycle}

# df1 = pd.DataFrame(d1)
# print(df1)
# a= df.join(df1,lsuffix='_caller',rsuffix='_other')
# print(a)
# o/p

#    Cars   Bikes
# 0   Honda   bajaj
# 1  Maruti  Peiggo
# 2     BMW   vespa
#        Cars    Cycles
# 0   Ferrari       BMW
# 1      Audi  Mercedes
# 2  Mercedes     vespa
#   Cars_caller   Bikes Cars_other    Cycles
# 0       Honda   bajaj    Ferrari       BMW
# 1      Maruti  Peiggo       Audi  Mercedes
# 2         BMW   vespa   Mercedes     vespa
##########################################################################
# df = pd.DataFrame({'key':['k0','k1'],'A':['A0','A1']})
# print(df)
# other = pd.DataFrame({'key':['k0','k1'], 'B':['B2','B2']})

# a= df.join(other,lsuffix='_caller',rsuffix='_other')
# print(a)
# b = df.set_index('key').join(other.set_index('key'))    
# print(b)
# series1 = pd.Series(['g', 'e', 'e', 'k', 's'])
# print("Series 1:")
# print(series1)
# series2 = pd.Series([9, 8, 7, 6, 5])
# print("Series 2:")
# print(series2)
   
# # stacking the series horizontally
# df = pd.concat([series1, series2], axis = 1)
# print("\nStack two series horizontally:")
# print(df)
# Stack two series horizontally:
#    0  1
# 0  g  9
# 1  e  8
# 2  e  7
# 3  k  6
# 4  s  5

# importing the module

  
# creating the series
# series1 = pd.Series(['g', 'e', 'e', 'k', 's'])
# print("Series 1:")
# print(series1)
# series2 = pd.Series([9, 8, 7, 6, 5])
# print("Series 2:")
# print(series2)
   
# # stacking the series vertically
# df = pd.concat([series1, series2], axis = 0)
 # print("\nStack two series vertically:")#######print(df)

 ################################################
# class Foo(object):
#     def __init__(self):
#         self.x = 10

# if __name__ == "__main__":
#     bar = Foo()
# print(bar.x)

#o/p 10

###########################################################
# arr = pd.Series([2,33,66], index =['a','e','i'])
# print(arr)
# print(arr.index)
##################################################################
# a = [1,2,3]
# a.insert(1,5)
# print ("Final a", a)
#################################################################
# def tri_recursion(k):
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(k)
#     print(result)
#   else:
#       result =0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6) 
##########################################################
# fruits = ["apple","banana","cherry","kiwi","mango"]
# newlist = [x for x in fruits if "a"in x]
# print(newlist) 
# fruits = ["apple","banana","cherry","kiwi","mango"]
# newlist = []

# for x in fruits:
#   #if "a" in x:
#  newlist.append(x)

# print(newlist)

# def my_function():
#   """ Demon"""
#   return None

# print("using __doc__:")
# print(my_function.__doc__)  

# triple = lambda x: x * 3 

# print(triple(9))
# df = pd.read_csv("data.csv")
# print(df)

# gk = df.groupby('id')
# a=gk.first()
# print(a)
# b = gk.get_group(1)
# print(b)
# df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
# df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])
# print(df1)
# print(df2)

# df2 = df2.reindex_like(df1)
# print(df2)
#######################################################
# g = "  The Geet.  "
# d = ",,,,,,,,,,,,,,,,rrrrrtttggg.....banana........rrrrrrr"
# print(g)
# f = g.strip()
# print(f)
# x = d.strip(",.grt")
# print(x)
# y = replace(g)
# print(y)

##########################################################################
# empty class in python
# 
# class Geek:
#     pass

# if '__init__' == '__main__':
#     obj = Geek()
# print(obj)

# class Emp:
#     pass

    # def call(self,number):
    #  print (f"{number} called")




# if '__init__' == '__main__':
    # Object one 
# obj = Emp()
# obj.name = 'Tanveer'
# obj.office = 'teaching'
    
    # Object second
# obj2 = Emp()
# obj2.name = 'Taha'
# obj2.office = 'MBA'
# obj2.phone = 1234567
# obj2.number = 123

    

# print the details
# print("Object One to Print")
# print("Name = ", obj.name) 
# print("Office = ", obj.office)
# print("Object Second to Print")
# print("Name = ", obj2.name)
# print("Office = ", obj2.office)
# print("Phone = ", obj2.phone)
# obj2.call(999)

################################################################################
# A decorator in Python is a function that takes another function as 
# its argument, and returns yet another function. Decorators can be extremely 
# useful as they allow the extension of an existing function, without 
# any modification to the original function source code. 

# def decorative_list(fnc):
#     def inner(list_of_tuples):
#         return [fnc(val[0], val[1]) for val in list_of_tuples]
#     return inner    


# @decorative_list
# def add_together(a,b):
#     return a + b
# #print(add_together(1,3))  
# # 
# print(add_together([(1,3),(3,17),(5,5),(6,7)]))  

# #add_together = decorative_list(add_together)

# print(add_together)

##########################################################################
# def decor1(func):
#     def inner():
#         x = func()
#         return x * X
#     return inner    

# @decor1
# pass

  ### program to make the numerator greater then the denominator


def smart_div(func):
    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return inner


@smart_div #same as code "div=smart_div(div)"   
def div(a,b):
    print(a/b)

div(3,21)

# def f():
#    try:
#       return(1)
#    finally:
#       return(2)
# k=f()
# print(k)
# o/p 2
######################################
# n = 5.55
# m = 5

# print(n//m)
#######################################
# z = "Best website is Tutorials Point"
# print (z.find("Tutorials"))
###o/p 16
####################################################
# tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
# print (tuple[1:3])
# o/p (786, 2.23)
# print (random.random())
##############################################################
# Ans: title() − Returns "titlecased" version of string, that is, 
# all words begin with uppercase and the rest are lowercase

##########################################################
# S = [['him', 'sell'], [90, 28, 43]]
# print(S[0][1][1])

# S[0] take as S[[0][1]] So S[0] print [him,sell] then [0] = [him,sell] and [1]= [90,28,43]
# S[0][1] so amonge [him,sell] it print sell 
# S[0][1][1] so amonge [sell] it print e
########################################################################
# colors = ["white", "Black", "Grey"]
# x = "Red" not in colors
# print(x)
###############################################################################
# Which of the following operator in python evaluates
#  to true if it does not finds a variable in
#  the specified sequence and false otherwise?
# not in

############################################################
#What is the following function compares elements of both lists?
#cmp(list1, list2)

# l = 1
# l1 = 2
# print(cmp(l,l1))
#########################################################################
#Files can be deleted in python by using either of the following command:
# filename = "matches.csv"

# if os.path.isfile(filename):
#     print("File do exist")
#     os.unlink(filename) or os.remove(filename)

###############################################################################
# Early Binding 

# The Early Binding occurs at compile time 
# while the Late Binding occurs at runtime. 
# The key difference between Early and Late Binding is that Early Binding
#  uses the class information to resolve method calling
#  while Late Binding uses the object to resolve method calling

# The compiler performs a process called binding 
# when an object is assigned to an object variable.
# The early binding (static binding)
#  refers to compile time binding and late binding (dynamic binding) 
# refers to runtime binding.

##########################################################
#OOP programming and functional programming and Procedure Oriented Programming 
# all supported by python
# 
# __name__ is inbuilt special variable for example
# 
# Consider two separate files File1 and File2.

# File1.py 
  
# print ("File1 __name__ = %s" %__name__) 
  
# if __name__ == "__main__": 
#     print ("File1 is being run directly")
# else: 
#     print ("File1 is being imported") 

# File2.py 
  
# import File1 
  
# print ("File2 __name__ = %s" %__name__) 
  
# if __name__ == "__main__": 
#     print ("File2 is being run directly")
# else: 
#     print ("File2 is being imported")

# Now the interpreter is given the command to run File1.py.
# python File1.py
# Output :
# File1 __name__ = __main__
# File1 is being run directly

# File2 __name__ = __main__
# File2 is being run directly
# As seen above, when File1.py is run directly,
#  the interpreter sets the __name__ variable as __main__ and 
#  when it is run through File2.py by importing, the __name__
#   variable is set as the name of the python script, i.e. File1.
#    Thus, it can be said that if __name__ == “__main__” is
#     the part of the program that runs when the script is 
#     run from the command line using a command like python File1.py.
# __init__ method is auto call once for each instance of the Object

# class Computer: # OOP

#     def __init__(self) -> None:
#         print("In IT called ")

#     def config(self):
#         print("1TB")

# com1 = Computer()
# com2 = Computer()

# com1.config()
# com2.config()

# O/p :
# In IT called 
# In IT called 
# 1TB
# 1TB
##################################################################################
# class Computer:

#     def __init__(self,cpu,ram) -> None:
#         self.cpu = cpu
#         self.ram = ram

#     def config(self):
#         print("config is", self.cpu, self.ram)

# com1 = Computer("i5", 16)
# com2 = Computer("Ryzen 3", 8) 

# com1.config()
# com2.config()

##################################################################################

# class Computer:
#     pass

# c1 = Computer() # bracket () is nothing but constructor which decide how much space 
#                 # should be alocated to the object. This () calls in the init function 
#                 # internally. 

# print(id(c1)) # address of that memory 


###################################################################################
# class Car:
    # wheels = 4  # class variables/Static variable , Class namespaces
    # def __init__(self) -> None:
    #       self.mil = 10      # instance variables , Instance namespaces
    #       self.com = "BMW"   # instance variables , Instance namespaces

# c1 = Car()
# c2 = Car()

# c1.mil = 8

# print(c1.com, c1.mil, c1.wheels)
# print(c2.com, c2.mil, c2.wheels)

# print(c1.com, c1.mil, Car.wheels)
# print(c2.com, c2.mil, Car.wheels)
# print(id(c1))  # id prints the address of the object

# namespaces is an area where you create and store Class/object Variable
# class namespaces
# Object / Instance namespaces

#################################################################################
#Class Methods,Instance Method, Static Methods

# class Student:
#     school = "Tanveer"
#     def __init__(self,m1,m2,m3) -> None:
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3


#     def avg(self):   # this instance method as we passing the Object/instance variables Or
#                                                             # Object/instance namespace   
#         return (self.m1 + self.m2 + self.m3)/3


# s1 = Student(34,45,67)
# s2 = Student(89,34,28)        

# print(s1.avg())

################################################################################
# instance method are of two type Accessor Methods and Mutator Methods
# to access the value of the Object use Accessor Methods and to modify
# the object value we use Mutator methods
# instance/Object variable work with instance method
# class method work with class variable/static variable  

# class Student:
#     school = "Tanveer"
#     def __init__(self,m1,m2,m3) -> None:
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     def get_m1(self):   
#         return self.m1  # Accessor Method which just fetch the value of the instance 
#                         # Object


#     def set_m1(self, value): # Mutator Methods which change of the value of the instance
#         self.m1 = value      # Object
#         return value

# s1 = Student(34,47,32)

# a= s1.get_m1()
# print(a)
# value = input("The change value of m1 :")

# b = s1.set_m1(value)
# print(b)
# print(a)

#############################################################################
#class method work with class variable/static variable  @classmethod

# class Student:
#     school = "Tanveer"

#     def __init__(self,m1,m2,m3) -> None:
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
#     def avg(self):
#         return (self.m1 + self.m2 + self.m3)/3

#     @classmethod
#     def getSchool(cls): # This is Class method using Class variable
#         return cls.school    

# s1 = Student(34,47,32)

# print(Student.getSchool())

#####################################################################################
# static Method as @staticmethod
# class Student:
#     school = "Tanveer"

#     def __init__(self,m1,m2,m3) -> None:
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
#     def avg(self):
#         return (self.m1 + self.m2 + self.m3)/3

#     @staticmethod
#     def info(): # static method
#         print("This is Student class.. in abc module") # nothing to do with class variable
#                                                        # instance variable then can use static method  

#     @classmethod
#     def getSchool(cls): # This is Class method using Class variable
#         return cls.school    

# s1 = Student(34,47,32)

# print(Student.getSchool())

# Student.info()

#################################################################################
#inner class
# class Student: # outer Class

    # def __init__(self,name,rollno) -> None:
    #     self.name = name
    #     self.rollno = rollno
        #self.lap1 = self.Laptop() # Object of Class laptop declare in outer class or 
                                  # outside class we can create a object 

    # def show(self):
    #     print(self.name, self.rollno)
    #     #self.lap1.show()

    # class Laptop: # inner Class


        # def __init__(self) -> None:
        #     self.brand = "HP"
        #     self.cpu = 'i5'
        #     self.ram = 8

        # def show(self):
        #     print(self.brand,self.cpu,self.ram)



# s1 = Student("Navin", 2)
# s2 = Student("Jenny", 3)

# s1.show()

# lap1 = Student.Laptop()

# lap1.show()

#######################################################################################
#OOP
# Inheritance in python  single level Inheritance and multilevel inheritance

# class A:
#     def feature1(self):
#         print("Feature 1 is working")

#     def feature2(self):
#         print("Feature 2 is working")

# class B(A): # single level inheritance B can inherit A method
#     def feature3(self):
#         print("Feature 3 is working")

#     def feature4(self):
#         print("Feature 4 is working")

# class C(B): # multilevel level inheritance C can inherit B and A both
#     def feature5(self):
#         print("Feature 5 is working")


# a1 = A()

# a1.feature1()
# a1.feature2()

# b1 = B()

# b1.feature2()

# c1 = C()

# c1.feature1()
#####################################################################################
# Multiple Inheritance

# class A:
#     def feature1(self):
#         print("Feature 1 is working")

#     def feature2(self):
#         print("Feature 2 is working")

# class B: 
#     def feature3(self):
#         print("Feature 3 is working")

#     def feature4(self):
#         print("Feature 4 is working")

# class C(A,B): # Multiple inheritance 
#     def feature5(self):
#         print("Feature 5 is working")


# a1 = A()

# a1.feature1()
# a1.feature2()

# b1 = B()

#b1.feature2()
# b1.feature3()
# c1 = C()

# c1.feature1()

###################################################################################
# Constructor in Inheritance in Python
# sub class can access all the features of super class
# but, super class cannot access any features of sub class
# If you create object of sub class it will first try find init of
# sub class 
# If it is not found then it will call init of super class

# class A:

#     def __init__(self) -> None:
#         print(" Init of A ")

#     def feature1(self):
#         print("Feature 1 is working")

#     def feature2(self):
#         print("Feature 2 is working")

# class B(A):

#      def __init__(self) -> None:
#             super().__init__() 
#             print("Init of B")   # init not there here then A init is called
#             super().__init__()

#      def feature3(self):
#         print("Feature 3 is working")

#      def feature4(self):
#         print("Feature 4 is working")


# a1 = B()

####################################################################################
# Constructor in Inheritance in Python
# Method Resolution Order(MRO) is from left to right 

# class A:

#     def __init__(self) -> None:
#         print(" Init of A ")

#     def feature1(self):
#         print("Feature 1-A is working")

#     def feature2(self):
#         print("Feature 2 is working")

# class B:

#      def __init__(self) -> None:
#         print("Init of B")   # init not there here then A init is called
            

#      def feature1(self):
#         print("Feature 1-B is working")

#      def feature4(self):
#         print("Feature 4 is working")


# class C(A,B): # class C(B,A)

#     def __init__(self) -> None:
#         super().__init__()
#         print("in C init")
#         super().__init__()

#     def feat(self):
#         super().feature2()

# a1 = C() 
# a1.feature1()
# a1.feat()       

######################################################################################
# Poly -- Many Morphism -- Form --- PolyMorphism 
# Types 1.Duck Typing 2. Operator Overloading 3. Method OverLoading 4. Method Overriding
# loose Coupling , Dependency Injection , Interface

# Duck Typing # having same method name in different class is nothing but Duck typing

# class PyCharm:
#     def execute(self):
#         print("compiling")
#         print("Running")

# class Laptop:

#     def code(self,ide):
#         ide.execute()

# class MyEditor:

#     def execute(self):
#         print("Spell Check")
#         print("Convention Check")
#         print("Compiling")
#         print("Running")



# #ide = MyEditor() 
# ide = PyCharm()

# lap1 = Laptop()
# lap1.code(ide)

#################################################################################
# OPerator overloading __add__() , __sub__() , __mul__()

# a = '5'
# b = '6'

# print(a + b) # in  runtime the a and b is calling the below __add__ method

# print(str.__add__(a,b))

# class Student:
    

#     def __init__(self,m1,m2) -> None:
#         self.m1 = m1
#         self.m2 = m2

#     def __add__(self,other):   #operator Overloading
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s3 = Student(m1,m2)
#         return s3

    # def __gt__(self,other):
    #     r1 = self.m1 + self.m2
    #     r2 = other.m1 + other.m2
            
    #     if r1 > r2:
    #         return True
    #     else:
    #         return False  

#     def __str__(self) -> str: # Operator overloading
#         return '{} {}'.format (self.m1,self.m2)
#         # return '{} {}'.format(other.m1,other.m2)    
           
    
# s1 = Student(58,69) # 127
# s2 = Student(69,65) # 134       

# s3 = s1 + s2      # Student.__add__(s1,s2)  s1 is self and s2 is other in __add__ method        
# print(s3.m1)  # 56 + 98

# if s1 > s2:
#     print("s1 wins")
# else:
#     print("s2 wins")    


# a = 9 
# print(a.__int__()) # runtine __int__ function or method is called

# print(s1) # __str__ OPerator overloading
# print(s2)

# print(np.zeros([5,5]))
# print(np.diag([1,2,3,4,5]))
#######################################################################
# method overloading not supported in python lets see

# def avg(a,b)
# def avg(a,b,c)

# class Student:

# #     def __init__(self,m1,m2) -> None:
# #         self.m1 = m1
# #         self.m2 = m2

# # 
#       def sum(self,a=None,b=None,c=None): # method overloading is not supported 
#           s = 0                           # but just 
#           if a != None and b != None and c != None:
#               s = a + b + c
#           elif a != None and b != None:
#               s = a + b
#           else:
#               s = a
#           return s
# s = Student()

# print(s.sum(2,3))

#############################################################################
# Method overriding

# class A:
#     def show(self):
#         print("in A show")

# class B(A):
#     # pass if the class B do not have show method it prints class A show method
#     # once class B has a show method it overide the class A show method with class B
#     def show(self):
#         print("in B show") 

# a1 = B()
# a1.show()
################################################################################

# Python program showing
# abstract base class work
 
# from abc import ABC, abstractmethod
# class Animal(ABC):
 
#     @abstractmethod
#     def move(self):
#         pass
 
# class Human(Animal):
 
#     def move(self):
#         print("I can walk and run")

# class Snake(Animal):
 
#     def move(self):
#         print("I can crawl")
 
# class Dog(Animal):
 
#     def move(self):
#         print("I can bark")
 
# class Lion(Animal):
 
#     def move(self):
#         print("I can roar")
         
# # Driver code
# R = Human()
# R.move()
 
# K = Snake()
# K.move()
 
# R = Dog()
# R.move()
 
# K = Lion()
# K.move()
# o/p

# I can walk and run
# I can crawl
# I can bark
# I can roar
# a = list1 = (2,2)    #list,tuple allow duplicate set not allow duplicate 

# print(a)
































###########################################################################
# Dilnawaz requirement.

# filename = "data1.csv"

                                      #if os.path.isfile(filename):
                                       #with open (filename, "r") as file:
# df = pd.read_csv(filename)
# print(df)
# total = df['id'].sum()
# print(total)
# print(df['total'].values[2])

# if df['total'].values[2] == total:
#    print("The value is equal") 
# else:
#     print("The value is not equal")

# print(f"The Correct sum total should be : {total}")    
#if df.iloc[1,0] == total:
 #   print("The value is equal")
#else:
 #   print("The value is not equal")    
#a = df.sum(axis=0,skipna= True)
#print(a)

#total = a



#sum(df[:,:])
        #print(file.read())

######################################################################################
# g = "Tanveer"

# a = min(g)  # min string value 
# print(a)
################################################################################
from tkinter import *
# frame = Frame() # creating Frames in Python
# a = Canvas.create_rectangle(50,50,50,70)
# print(a)
# root = Tk()
# root.geometry("500x900")
# canvas = Canvas(root, width=550, height=820)
# canvas.pack()
# png = PhotoImage(file = r'example.png') # Just an example
# canvas.create_image(0, 0, image = png, anchor = "nw")

# a = canvas.create_rectangle(50, 0, 50, 0, fill='red')
# canvas.move(a, 20, 20)
# Canvas.bind("<key>",p)

#####################################################################
# seta = {"a","b", "c"}
# setb = {"1","2"}

# if len(seta) > len(setb):
#     print ("O My god")
# else:
#     print ("H")  

#####################################################################################
# text = 'bat ball'
# r = text.replace('b', 'c')
# print(r) 

# B - strip([chars])

# C - swapcase()

# D - title()
# ################################################################################# 
# L = [1,2,3]
# print(L[2]) o/p = 3

################################################################################
# tinytuple = (123, 'john')
# print(tinytuple*2)
# print(['Hi'] * 4 )
# print(len([1,2,3])) # o/p is 3
# print(1%2)
################################################################
# str = 'Hello World!'
# print(str)
#####################################################################################
# class B:
#     print("Hello hi")

# O = B()

# isinstance(O,B) # How can we check whether the object is instance of class or not. 
#                 #    Let us consider an object O which is instance of class B. 
###################################################################################
# num=3
# while True:
#    if (num%0o12 == 0):
#       break
# print(num)
# num += 1
#########################################################################
# def rev_func(x,length): 
#    print(x[length-1],end='' '') 
#    rev_func(x,length-1) 
# x=[11, 12, 13, 14, 15] 
# rev_func(x,5)
#o/p
# 15141312111514131211Traceback (most recent call last):
# IndexError: list index out of range
########################################################################
# a = random.random()
# print(a)
# b = random.randint(1,2)
# print(b)
# c = random.uniform(3,4)
# print(c)

# tuple = ()
# set = {}
# list = []
# dict = {key:value}
##############################################################################
# list = [78,67,90]
# print(max(list))
# a=set(list)
# print(a)
# print('hijk'.partition('ab'))

# b = ord(X)
# X
# print(b)

###############################################################################
# list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# print(list[2:])
# df = pd.DataFrame()

# bikeslist = ["Bajaj","TVS"]
# carslist = ["Ford","BMW"]

# df["cars"] = carslist
# df["bikes"] = bikeslist 
# print(df)
########################################################
# x = np.diag([1,2,3,4,5])
# print(x)
#####################################################################
##### INTIALIZATION #####

# #STRING SERIES
# fruits = pd.Series(["apples", "oranges", "bananas"])

# print("MY FRUIT SERIES")
# print(fruits, "\n")

# #FLOAT SERIES
# temperature = pd.Series([32.6, 34.1, 28.0, 35.9], index = ["a","b","c","d"])

# print("TEMPERATURE IN CELSIUS")
# print(temperature, "\n")

# #INTEGER SERIES
# factors_of_12 = pd.Series([1,2,4,6,12], name = "factors of 12")

# print("FACTORS OF 12 SERIES")
# print(factors_of_12, "\n")

# ##### QUERY #####

# #USING INDEX
# print ("2nd fruit: ", fruits.iloc[1])
# #OR
# print ("2nd fruit: ", fruits[1], "\n")

# #USING KEY
# print ("temperature at key \"b\": ", temperature.loc["b"])
###########################################################################
# data = ["1","three",4.0]

# series = pd.Series(data)
# print(series)
# print(type(series))
################################################
# df = pd.DataFrame({'Vehicle':['kia','Lambagoni','KTM RC','Pulsar'],'Type': ["car","car","Motor","Motor"]})
# print(df)
# d =df.groupby('Type').count() # groupby function in python
# print(d)
############################################################
# df = pd.DataFrame({'Vehicle':['Kya','BMW'],'Type':["car","car"]})
# print(df)
######################################################################
# df = pd.DataFrame({'animal':['snake', 'bat', 'tiger', 'lion',
#                    'fox', 'eagle', 'shark', 'dog', 'deer']})
# #df = pd.read_csv("C:\\Users\\tanveer.ansari_quali\\Documents\\matches.csv")
# print(df.head(2)) # df.head(n) number of row datas 
###############################################################
# df=pd.DataFrame()
# print(df) # empty Dataframe
# bikes=["Bajaj","TVS","Honda","Kawa","BMW"]  # list
# cars= ["Lam","Masserati","Ferra","Hyundai","Ford"]

# d = {"cars":cars,"bikes":bikes} # dictionary
# df = pd.DataFrame(d)
# print(df)
######################################################################
# df=pd.DataFrame() # empty Dataframe
# bikes=["Bajaj","TVS","Honda","Kawa","BMW"]  # list
# cars= ["Lam","Masserati","Ferra","Hyundai","Ford"]

# d = {"cars":cars,"bikes":bikes} # dictionary
# df = pd.DataFrame(d)
# print(df)
# df1=pd.DataFrame()
# colours=["yellow", "Red","White","Black","Purple"]
# model1 = ["normal","SUV","Jeep","HunchBack","Lumosieon"] 
# d1 ={"Colours":colours,"model1":model1}
# df1 = pd.DataFrame(d1)
# print(df1)
# df2 = pd.DataFrame()
# d2 = {df.index, df1.index}
# # df2 = pd.DataFrame(d2)
# df2 = pd.DataFrame(d2)
# print(df2)
# df2 = pd.DataFrame(d2)
# print(df2)
######################################################################
# df=pd.DataFrame() # empty Dataframe
# bikes=["Bajaj","TVS","Honda","Kawa","BMW"]  # list
# cars= ["Lam","Masserati","Ferra","Hyundai","Ford"]

# d = {"cars":cars,"bikes":bikes} # dictionary
# df = pd.DataFrame(d)
# a=[10,20,30,40,50]
# df.index=a

# print(df.loc[50])
####################################################################
# cars = ["BMW","Ford","Log","Talk"]
# bikes = ["pulse","TVS","N","M"]

# d = {"Cars": cars, "Bikes": bikes}

# df = pd.DataFrame(d)
# print(df)
# x = [20,30,40,50]
# df.index = x

# print(df.loc[30])
##############################################################################
# n1 = np.array([10,20,30,40,50,60]) # 10+20+30+40+50+60/6 = mean of the number
#                                    # median 1,3,3,6,7,8,9 middle number 6 is median
#                                    # median 1,2,3,4,5,6,8,9 then 4+5/2 is median i.e 4.5  
# print(np.mean(n1)) # mean is nothing but add all number divide by how many number there
# print(np.median(n1))
# print(np.std(n1))
############################################################################
# dict = {1:'a',2:'b',3:'c'}
# print(dict.keys())
# dict = {1:'a',2:'b', 3: 'c'}
# print(dict.keys())

# n = "tanveer"
# print(n.capitalize())
# ####################################################################
# list = [0,1,2,3,4,5,6,7,8,9]      insert update remove in list set dictionary
# list.insert(6,10) # Insert 10 at 6th index
# print(list)

# list1 = [0,1,2]
# list1.insert(1,10) # list
# print(list1)
###################################################################
# my_list = ["a","b","c","c","d","e","e","f","u","v"] 
# my_list1 = list(set(my_list))
# my_list2 = list(dict.fromkeys(my_list))
# print(my_list1)
# print(my_list2)
# my_list.remove("a") # list use remove pop(int) and append to add 
# my_list.pop(8)
# my_list.append("z")
# print(my_list)

# d = {"s": 1,"h":2}
# m = list(dict.items(d))
# print(m)

# f = {9,8} # set use remove and add
# f.remove(9)
# f.add(4)
# print(f)

# c = {"a": [], "b":[]} # dictionary
# c["a"].append(3)
# c["b"].append(4)
# print(c)
 ###########################################################################
 # list comprehension
# list = [i for i in range(1000)]
# print(list)

# l = [a for a in range(100)]
# print(l)
##########################################################################
def add_func(n):
    return n * 3
nb = (1,2,3,4,5,6,7,8)   
result = map(add_func,nb)
print(list(result))    
# # var = copy.copy(nb)
# # print(var)
# var = copy(nb)
# print(var)
##########################################################
# a_dictionary = {"name" : "John", "name" : "20"}
# a_dictionary = {"name" : "John", "age" : "20"} # appending empty list from dictionary
# a_list = []
# dictionary_copy = a_dictionary.copy()
# a_list. append(dictionary_copy)
# print(a_list)
# ########################################################
# n=10
# print(type(n))
# new_n = str(n)
# print(type(new_n))
########################################################
# letters = ("A,B,C")
# n = letters.split("")
# print(n)

#string.split(separator, maxsplit)
# Split a string into a list where each word is a list item:
# Parameter	Description
# separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
# maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"


# txt = "welcome to the jungle"
# x = txt.split("#")
# print(x)
###########################################################################
# def factorial (a):
#     if a==1:
#         return 1
#     else:
#         return (a * factorial(a - 1))

# input_number = input ("Enter the factorial number :  ")
# n= int(input_number)
# print(f"The factorial of ", {n},"is",{factorial(n)})
#############################################################################
# a = "Hello"
# b = 15
# c = 1               # 0 or empty array is false
# sample_list = [1]
# print(bool(a))
# print(bool(b))
# print(bool(c))
# print(bool(sample_list))

#######################################################################
# d1 = {"k1":10,"k2":20,"k3":30}
# for i in d1.keys():
#     d1[i] = d1[i] + 1
#     print(d1[i])
# print(d1.values())

####################################################
# a=[1,2,3]
# b=[2,3,4]

# d = {"col1":a,"col2":b}
# df= pd.DataFrame(d)
# print(df)
# df["Sum"] = df["col1"]+df["col2"]

# df["Difference"] = df["col2"]-df["col1"]

# print(df)
############################
# data = {"col1":[1, 2, 3], "col2":[4, 5, 6], "col3":[7, 8, 9]}
# df = pd. DataFrame(data)
# selected_Columns = df[["col1","col2"]]
# new_df =  selected_Columns.copy()
# print(new_df)
##########################################
# d = {"col1":[1,2,3],"col2": ["A","B","C"], "col3":["A1","B2","C3"]}

# df=pd.DataFrame(d)
# print(df)
# df=df.drop(['col2','col1'],axis=1)
# #df=df.drop([1,2],axis=0)
# # df=df.drop([0,2],axis=0)
# print(df)

# a = {'col1':[0,1,2], 'col2': ["A", "B", "C"], "col3":["A1","B1","C1"]}

# df = pd.DataFrame(a)
# b = [ 10,20,30]
# df.index = b
# print(df)
# df = df.drop(['col1','col2'],axis=1)
# print(df)
##############################################################
# n = random.random()
# print(n)  # generate random number
######################################################
# df = {"k1":1,"k2":2}
# for i in df.keys():
#     df[i] = df[i] + 1
#     print(df[i])
# print(df.keys())  
# print(df.values())
# print(df.items())       
#############################

# def tri_recursion(k):
#     if (k>0):
#         result = k + tri_recursion(k-1)
#         print(k)
#         print(result)
#     else:
#         result = 0    
#     return result
# print("The Recursive funtion result")
# tri_recursion(6)        
################################################################################
# def factorial(n):
#    if n == 1:
#       return 1
#    else:
#      return (n * factorial(n-1))
# input_number = input ("Enter the number for the Factorial :")
# n = int(input_number)
# print(f"The factorial number of  {n} , is, {factorial(n)}") 
#################################################
# n = random.randint(10,20) # give random number in the range of 10 to 20
# print(n)
###############################################
# sequ = [5,8,10,20,50,100]          
# sum =  reduce(lambda x,y: x+y,sequ)  
# print(sum)
############################################################
#Pass by value and Pass by Reference

# def check_pass(arr):
#     arr.append(4)
# arr = [1,2,3]
# 
# print(arr) # Call by value memory address remain the same 
# 
# check_pass(arr) # pass the memory location of the value where it is stored so the changes is reflected everywhere
# print(arr) # Call by Reference sending the memory location where the value is stored so if append  
# 
# o/p
# [1, 2, 3]
# [1, 2, 3, 4]
# [1, 2, 3, 4, 5]
# Now present code
# [1, 2, 3, 4]
# [1, 2, 3, 4, 4]
# [1, 2, 3, 4, 4, 5]

###################################################################
# def set_list(list): call by value and Call by Reference
#     list = ["A", "B", "C"]
#    
#     return list
# my_list = ["E"]

# def add(list):
#     list.append("D")
#     return list
  

# print(set_list(my_list))
# print(add(my_list))
##################################################################
# first_list = [1,2,3,4,5]
# second_list = first_list
# print(first_list)
# second_list.append(6)
# print(first_list)
# print(second_list) 
#######################################################
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)
##################################################
# for x in range(2, 6):
#   print(x)
# for x in range(2, 30, 2):
#   print(x)

# def set(list):
#     list = ["A","B", "C"]
#     return list
    
# My_List = ["E"]

# def add(list):
#     list.append("D")
#     return list

# print(set(My_List)) # Call by Value
# print(add(My_List)) # Call by Reference
##########################################################################

#######################################################
# #CRUD

# # Create posts @app.post("/posts")

# # Read   get   /posts/:id  @app.get("/posts/{id}")

# # Read   get   /posts      @app.get("/posts")

# # Update Put/Patch  /posts/:id @app.put("/post/{id}")

# # delete  delete /posts/:id  @app.delete("/posts/{id}")


# # @app.post("/createposts")
# # def create_posts(payload: dict = Body(...)):
# #      print(payload)
# #      return ("new_post": f"title {payload['title']} content: {payload['content']}")

# get
# api_url = "https://jsonplaceholder.typicode.com/todos"
# response = requests.get(api_url)
# response.json()

# post
# api_url = "https://jsonplaceholder.typicode.com/todos"
# todo = {"userId": 1, "title": "Buy milk", "completed": False}
# response = requests.post(api_url, json=todo)
# response.json()

# put
# #import requests
# api_url = "https://jsonplaceholder.typicode.com/todos/10" 
# response = requests.get(api_url)
# response.json()
# #{'userId': 1, 'id': 10, 'title': 'illo est ... aut', 'completed': True}

# todo = {"userId": 1, "title": "Wash car", "completed": True}
# response = requests.put(api_url,json=todo)
# response.json()
# {'userId': 1, 'title': 'Wash car', 'completed': True, 'id': 10}

# Patch 
# {'userId': 1, 'title': 'Wash car', 'completed': True, 'id': 10}
# api_url = "https://jsonplaceholder.typicode.com/todos/10"
# todo = {"title": "Mow"}
# response = requests.patch(api_url, json=todo)
# response.json()
# {'userId': 1, 'id': 10, 'title': 'Mow lawn', 'completed': True} 


# delete
# api_url = "https://jsonplaceholder.typicode.com/todos/10"
# response = requests.delete(api_url)
# response.json
# {}

#insert into table_name (column1,column2,...) VALUES (value1,values2,....)
# update table_name set column1 = , column2 = , where condition

#################################################################################
# Test Strategy 
# The components to be covered in test strategy
# 1. Scope and Evironment
# 2. Testing Approach
# 3. Test Evironment Specification
# 4. Testing tools
# 5. Release Management 
# 6. Risk Analysis
# 7.Reviews and Approvals

# Test Strategy is the general way how the testing will be approached....Test Strategy is independent
#  of project and is dependent on the organization general approach for Testing Software project.
# Test Strategy is organization level...Test Plan is individual to each and 
# every project.Most of the organization Test Plan for each and every project gets 
# aligned with the Organizational Test Strategy.
# Its takes care of what all artifacts are coming of the the project like 
# Test Cases report, Test summary report, Test Plan, 
# Test Strategy is the Base line for all the Project in the Organization.
# Test Approach gets enhance in test Plan as per each and every project.

# ###########################################################################################
# Test Plan
# 1. Test Plan Identifier
# 2.Indroduction
# 3.Test items
# 4.Feature to be tested
# 5.Feature not to be tested
# 6.Approach
# 7 Item Pass/Fail criteria
# 8.Suspension /Resumption Crieria
# 9 Test Deliverables
# 10 Testing Task
# 11 Environment Needs
# 12 Responsibiles
# 13 Staffing and Training Needs
# 14 Schedule
# 15 Risk Mitigation and contigency plan
# 16 Approvals


# Test items login, Registration , 


###################################################################################################
# Test Approach:
# A test approach is the test strategy implementation of a project, defines how testing would be carried out. Test approach has two techniques:

# Proactive - An approach in which the test design process is initiated as early as possible in order to find and fix the defects before the build is created.

# Reactive - An approach in which the testing is not started until after design and coding are completed.

# Different Test approaches:
# There are many strategies that a project can adopt depending on the context and some of them are:

# Dynamic and heuristic approaches

# Consultative approaches

# Model-based approach that uses statistical information about failure rates.

# Approaches based on risk-based testing where the entire development takes place based on the risk

# Methodical approach, which is based on failures.

# Standard-compliant approach specified by industry-specific standards.

# Factors to be considered:
# Risks of product or risk of failure or the environment and the company.

# Expertise and experience of the people in the proposed tools and techniques.

# Regulatory and legal aspects, such as external and internal regulations of the development process.

# The nature of the product and the domain.  
# #########################################################################################
# 
# # ##############################
# Exit Criteria
# Set of a condition agreed upon with the stakeholders for permitting a process to be officially completed.The purpose of exit criteria is to preventing the 
# task from being considered completed if there are still outstanding task which is not finished.Exit criteria are used to report against and to plan when
#  to stop testing.
 
#  Set of condition should be met before concluding(ending) the testing process.
 
 
# ####################################################
# Entry criteria It is a set of condition for permitting a process to go forward
#  with defined task e.g test phase.The purpose of entry criteria is to prevent 
# the task from geting started which may entail more effort compared to the effort needed to remove the failed entry criteria.
  
#  prerequiste condition must be achieved before commencing(starting) the testing process.
 
# ################################################################

# Test Principle 
# ###########


# Testing shows presence of defect
# Exhaustive testing is impossiable
# Early Testing
# defect clustering
# Pesticide Paradox
# Testing is context dependent
# absence of errors fallacy   
# 
# ###########################################################
# second largest salary of the employee
# select max(salary) from employee where
# salary < (select max(salary) from employee);
# 
# insert into employee values (1,'Mandy', 12000)
# create table table_name (column1_name_Constraint,)
# create database database_name
# Select TOP,LIMIT and ROWNUM command to specify
# number of records to return
# sql server uses SELECT TOP , MySql uses LIMIT, and Oracle
# uses ROWNUM
# 
# SELECT TOP 3 * FROM customers
# select * from customers limit 3;
# select * from customers where rownum <=3;
#####################################################
# third largest salary sql query

# using Top

# SELECT TOP 1 salary from 
# (select TOP 3 Salary from table_name order by salary desc) as comp
# order by salary asc


##################################
# using LIMIT

# select salary from table_name 
# order by salary desc
# limit 2,1

##########################################
# using subquery
#select salary
# from (select salary from table_name order by salary desc
# limit 3) as comp
# order by salary 
# LIMIT 1
###########################################################
# name = "Bob"
# #greeting = f"Hello, {name}"

# print(f"Hello, {name}")

# name = "tanveer"

# print(f"Hello, {name}")

############################################
# f string 
# name  = "Bob"
# greeting = "Hello, {}"
# #with_name = greeting.format(name)
# name = "Tanveer"
# welcome = "Welcome to Flight "
# name = "Talha"
# print(f"{welcome} {greeting.format(name)}")
##############################################
# longer_phrase = "Hello, {}. Today is {}."

# formatted = longer_phrase.format("Rolf","Monday")
# print(formatted)
#########################################################  
# user_age = int(input("Enter the user age :"))
# months = user_age * 12
# print(f"Your age, {user_age}is equal to {months} months." )

########################################################################
# create a list, call my_list , with three number.The total of
# the numbers added together should be 100 
# answer my_list = [100,0,0]
###############################################################
# create a tuple , called my_tuple , with a single value in it
# answer my_tuple = (25,) or 25,  comma should be added or else it takes mathmatical brackets
                                  # bracket is not compulsary in tuple just that python should know it's tuble.
####################################################################
# modify set2 so that set1.intersection(set2) return {5,77,9,12}
# set1 = {14,5,9,31,12,77,67,8}
# answer set2 = {5,77,9,12}
###################################################################
# is keyword
#####################################
# The is keyword is used to test if two variables refer to the same object.
#  The test returns True if the two objects are the same object. 
#  The test returns False if they are not the same object, even if the two objects
#   are 100% equal. Use the == operator to test if two variables are equal.
# friends = ["Rolf", "Bob"]
# abroad = ["Rolf", "Bob"]
# print( friends == abroad)
# # print(friends is abroad) not proper
# print(friends is friends)
#####################################################################
# number = 7 
# user_input = input ("Enter'y' if you would like to play:") or use lower()
##  user_input = input ("Enter'y' if you would like to play:").lower()

# if user_input in ('y', 'Y'):
#     user_number = int(input("Guess our number"))
#     if user_number == number:
#         print("WOW You win the Game Price")
#     elif abs(number - user_number) == 1:
#         print("You were off by one. Sorry")
#     else:
#         print("Sorry, it's Wrong! You Loss")   
# #################################################################### 
# #########################################################################
# number = 7  # while loop
# user_input = input ("Enter'y' if you would like to play:") or use lower()
##  user_input = input ("Enter'y' if you would like to play:").lower()
# number = 8
# user_input = input("would you like to play?(Y/n)")

# while user_input != "n":
#     user_number = int(input("Guess our number"))
#     if user_number == number:
#         print("WOW You win the Game Price")
#     elif abs(number - user_number) == 1:
#         print("You were off by one. Sorry")
#     else:
#         print("Sorry, it's Wrong! You Loss")     
#     user_input = input("would you like to play?(Y/n)") # to terminate the loop
#############################################################################
# number =  7
# while True:
#     user_input = input("would you like to play?(Y/n)").lower()
#     if user_input == "n":
#        break
#     user_number = int(input("Guess our number"))
#     if user_number == number:
#         print("WOW You win the Game Price")
#     elif abs(number - user_number) == 1:
#          print("You were off by one. Sorry")
#     else:
#          print("Sorry, it's Wrong! You Loss")
################################################################
# friends = ["R","J","B","A"]

# for friend in range(4): # instead of friends can use range(4)
#     print(f"{friend} is my friend")    

#################################################################
# grades = [35,75,78,89,90]
# total = 0
# amount = len(grades)       

# for grade in grades:
#     total += grade
# print(total/amount)  
##############################################################
#using sum function

# grades = [35,75,78,89,90]
# total = sum(grades)
# amount = len(grades)
# print(total/amount)
###################################################################
# numbers = range(20)

# evens = []
# for number in numbers:
#     if number % 2 == 0:
#         evens.append(number)
# print(evens)    
######################################################################
#list comprehensions
# 
# numbers = [1,2,5]
# doubled = []
# for num in numbers:
#     doubled.append(num * 2)
# print(doubled)  

##################################################################

# def get_num(n):
#     return n * 2
# num = [1,2,5]
# u = map(get_num,num)
# print(tuple(u)) # set,list,tuple needs to be added   

#########################################################################
# list comprehension

# numbers = [1,2,5]
# doubled = [num * 2 for num in numbers] # list comprehension
# print(doubled)

# friends = ["Rat", "Bat","Sat", "Tat"]
# # start_s = [friend for friend in friends if friend.startswith("S")  ] # list comprehension
# # print(start_s)

# # same as below 

# start_s = []

# for friend in friends:
#     if friend.startswith("S"):
#         start_s.append(friend)
# print(start_s)

######################################################
# friends = ["Sat"]
# start_s = [friend for friend in friends if friend.startswith("S")]
# print(friends is start_s) # answer is False coz the it is the two different list with 
#                           # same value in the memory
# print(friends[0] is start_s[0])  # answer True coz the value of both is same 
# print("friends", id(friends), "start_s", id(start_s)) #  id locates the memory address
##################################################################
#dictionaries
# student_ad = {"R": 30 , "S": 50,"Y": 45}
# for student in student_ad:
#     print(f"{student}:{student_ad[student]}") 

# #    or 
# for student,attend in student_ad.items(): # dictionaries
#     print(f"{student}:{attend}")
# ###############################################################
# student_ad = {"B": 10}

# if "B" in student_ad:
#     print(f"B: {student_ad['B']}")
# else:
#     print("B is in the list") 


# a = student_ad.values()
# print(a)
################################################################
# x,y = 5,11  # x = 5 and y = 11

# people = [("Bob",42, "Teacher"), ("Alam",34, "Mechanic"), ("Tanveer",42, "IT")]

# for name,age,profession in people:
#     print (f"name: {name}, Age : {age}, Profession :{profession}") # destructuring variable or 
                                                                   # unpacking variable
                                                                   # destructuring the code makes the code quality nice

#Or

# people = [("Bob",42, "Teacher"), ("Alam",34, "Mechanic"), ("Tanveer",42, "IT")]

# for person in people:
#     print(f"Name : {person[0]}, Age :{person[1]}, Profession : {person[2]}")
##############################################################
# people = [("Bob",42, "Teacher")]

# name,_,profession = people # this is where the _ meaning is you do not care about the variable

# print(name,profession)
##################################################################
# spilt with head and tail
# *head,tail = [1,2,3,4,5,6]  # * meaning the maximum value is taken by the variable
# print(*head)
# print(tail)
# #or else 

# head,*tail = [1,2,3,4,5,6]
# print(head)
# print(*tail)
################################################################
# function in python

#do not define or reuse function name such as 

# def print(): wrong to reuse print() function

# def print():
#     print("Hello world ")

# print() # TypeError: print() takes 0 positional arguments but 1 was given
        # as it do not call the build in function but def print() function 
        # Error TypeError: print() takes 0 positional arguments but 1 was given

##############################################################################
# friends = ["Rof", "Bob"] # Global variable

# def add_friends():
#     friend_name = input("Enter your friend name:")
#     friends = friends + [friend_name]    # "this friends ="  is again declare under the function
#                                          # and it is different from the global variable friend
#                                          # as in function you are declaring and using the 
#                                          # "friends =" in the function and "friends = "  is again as
#                                          # local variable.Do not use this way 
# add_friends()                              

# Error :
#friends = friends + [friend_name]    # "this friends ="  is again declare under the function
#UnboundLocalError: local variable 'friends' referenced before assignment

# we are shadowing the variable by redefining it 
# shadowing the variable is a valid python code...
##############################################################

# say_hello()


# def say_hello():
#     print("Hello")

    # Declaring the function before its definition gives error 

#     # Error    say_hello()
# NameError: name 'say_hello' is not defined 

#########################################################
# friends = []
# def add_friend():
#     friends.append("Rolf")


# # friends = [] #   it will work but should be declare before the function. 
# add_friend()

# print(friends) # [Rolf]
##########################################################################
# def add(x,y): # x and y is parameters
#     pass # python pass mean do nothing just require something as indentment


# add(5,3)    # 5 and 3 are argument  i.e argument provides a value to the parameter

#############################################################
# def say_hello():
#     print("Hello!")

# say_hello("Bob")

# Error as the parameter is not provided in the function and we are 
# supplying a argument as BOb
# TypeError: say_hello() takes 0 positional arguments but 1 was given
##################################
#so the proper program is

# def say_hello(name):
#     print(f"Hello! {name}")

# say_hello("Bob")
##################################
# def say_hello(name, surname):
#     print(f"Hello! {name} {surname}")

# say_hello("Bob","Sharma") # is call positioning the argument
# Or
# say_hello(surname ="Bob",name = "Sharma") # is call keyword or named urguments

##############################################
# def divide(dividend, divisor):
#     if divisor != 0:
#         print(dividend/divisor)
#     else:
#         print("You Fool!")


# divide(15,divisor=0) # positining argument is always first
# divide(dividend=15,0) # python gives eeror positioning arugment after keyword argument not allowed
# divide(dividend=15,divisor=0)
#######################################################################
#Default Parameter Values

# def add(x,y=8):  # y=8 is default parameter value
#     print(x+y)
# add(5)
# add(x=5)
# add(y=5)  # Error
# add(x=5,y=5)
# add(x=5,y)  posiotioning arugment cannot appear after keyword argument  Errpr 

# def add(x=5,y):  # Error dafault value must be  specified here

##########################################################################
# default_y = 3

# def add(x,y=default_y):
#     sum = x + y
#     print(sum)


# add(2)  # would print 5 i.e is 2+3

# default_y = 4
# add(2) # would print 5 i.e is 2+3 coz the value default_y value 3 is assigned it 
#        #the var default_y. 
######################################################################
#Functions Returning Values

# def add(x,y):    # x and y are parameter values
#     print(x + y)  #first and second "13" is due to this print  

# add(5,8)   # 5 and 8 are argument values 
# result = add(5,8) # As function return "None" by default the result variable takes "None"
#                   # value and so the Last Print of "None" is due to this. 
# print(result) 

# O/p 
# 13
# 13
# None
#####################################################################
# def add(x,y):
#     return x + y # return stmt exit the function hence the next print stmt do not print.
#     print(x + y)


# result = add(5,8)
# print(result)   # print 13 due to this print 

#o/p 
#13 

####################################################################
# def add(x,y):
#     return #  as return stmt return "None" here 
#     print(x + y)
#     return x + y


# result = add(5,8)
# print(result)
# # o/p 
# # None 
##############################################################################
# def divide(dividend, divisor):
#     if divisor != 0:
#         return dividend/divisor
#     else:
#         return "You fool!"

# result = divide(15,3) # divide (15, divisor = 3) # wrong divide(dividend = 15,3) 
######################################################################
# 
# def smart_div(func):
#     def inner(a,b):
#         if a < b:
#            a,b = b,a
#         return func(a,b)
#     return inner    
# @smart_div # same as div = smart_div(div)
# def div(a,b):
#     print(a/b)

# div(2,10)


#Question.1 Complete the function return_42 , by making it return 42

# def return_42():
#     return 42

#Question.2
# Create a function , which must be called my_function, which takes two arguments 
# and returns the result of its two arguments multiplied together
# 

# def my_function(x,y): # where x and y is parameter values
#     return x * y

# result = my_function(2,3)   # where 2 and 3 is argument values 
# print(result)

###############################################################################

# def smart_div(func):

#     def inner(a,b):
#         if a < b:
#             a,b = b,a
#         return func(a,b)
#     return inner


# @smart_div #same as code "div=smart_div(div)"   
# def div(a,b):
#      print(a/b)           
# div(5,10)

###############################################################
#lambda function
 #lambda function is a function which do not have a name and which only return values 
#  function perform some actions or operating on values and returning them such as the 
#  sum function or both 

# lambda function is used to operate on input and return output they are never used
# to perform actions.

# print((lambda x, y: x+y)(4, 5))
#####################################################################


# sequence = [1,3,4,6,7]
# doubled = [x for x in sequence ]
# print(doubled)

# o/p is 
# [1, 3, 4, 6, 7]


# def double(x):
#     return x * 2
# sequence = [1,3,4,6,7]
# doubled = [double(x) for x in sequence] # list comprehension
# or
# doubled = map(double, sequence)
# print(list(doubled))
#or
# doubled = list(map(double, sequence))
# print(doubled)
#or
# doubled = [(lambda x: x * 2)(x) for x in sequence]
# print(doubled)
#or
# doubled = list(map(lambda x: x * 2 , sequence)) # map function return map object hence
#                                                 # need list to convert the Object to list 
# print(doubled)

#lambda function is without any name and we can name them by assigning to variable.

##############################################################################
#dictionaries comprehensions

# users = [
#     (0,"username1", "password1"),
#     (1,"username2","password2"),
#     (2,"username3","password3"),
# ]

# username_mapping = {user[1]: user for user in users} # "user[1]" is the key,dictionaries comprehensions
# o/p : {'A': (0, 'A', 'I'), 'B': (1, 'B', 'II'), 'C': (2, 'C', 'III')}
# print(username_mapping["B"]) 
# username_mapping = {user[0]: user for user in users} # ": user" is the value, dictionaries comprehensions
# o/p : {0: (0, 'A', 'I'), 1: (1, 'B', 'II'), 2: (2, 'C', 'III')}
# print(username_mapping) 

#"user[0]"  takes the first value i.e 0 as a key , as array start with zero
#"user[1]"  takes the second value i.e A as a key , as array start with zero,1,2

# username_input = input("Enter the username: ")
# password_input = input("Enter the password: ")

# _, username, password = username_mapping[username_input]

# if password_input == password:
#     print("Your details are correct")
# else:
#     print("Your details are not correct! Sorry")


###########################################################################
#need to ask
# student = {'name':"Tanveer","School":"Computing","grades":(66,77,88)}

# def average_grade(data):
#     grades = data["grades"]
#     print(sum(grades))
#     print(len(grades))
#     return sum(grades) / len(grades)

# average_grade(student)


#need to ask
# def average_grade_all_student(student_list):
#     total = 0 
#     count = 0

#     for student in student_list:
#         total += sum(student['grades'])
#         count += len(student['grades'])
#         print(total/count) 
#     average_grade_all_student(student)
#     print(student_list)


#############################################################################
# unpacking function arguments
#*args # multiple argument in single variable
# The special syntax *args in function definitions in python is used to pass a 
# variable number of arguments to a function.
#  It is used to pass a non-key worded, variable-length argument list.
#   The syntax is to use the symbol * to take in a variable number of arguments;
#    by convention, it is often used with the word args


# def multiply(*args):
#     print(args)
#     total = 1
#     for arg in args:
#         total = total * arg
#     return total
# print(multiply(1,3,5))
# # o/p
# # (1, 3, 5)
# # 15
# print(multiply(-1))
# # (-1,)
# # -1

############################################################################
#unpacking function arguments
# 
# **kwargs or **nums
# The special syntax **kwargs in function definitions in python is used to
#  pass a keyworded, variable-length argument list.
#   We use the name kwargs with the double star.
#    The reason is that the double star allows us to pass through keyword arguments
#     (and any number of them).



# def add(x,y):  # x and y is parameters  unpacking function arguments
#     return x + y 
# nums = [3,5]
# add(*nums)  # *nums send the value x=3 and y=5 if add(nums) (*nums) we are sending arguments 
#             #it sends the value [3,5] as one value

# def add(x, y):
#     return x + y


# nums = {"x": 15, "y": 25}

# print(add(**nums))
############################################################################
# def multiply(*args): # complex function
#     print(args)
#     total = 1
#     for arg in args:
#         total = total * arg
#     return total

# def apply(*args,operator):
#     if operator == "*":
#         return multiply(*args)
#     elif operator == "+":
#         return sum(args)  
#     else:
#         return " No valid  operator provided to apply()."


# print(apply(1,3,6,7,operator="*"))
#######################################################################
#unpacking Keyword arguments

# def named(**kwargs): # you can take any def named(**nam): no issues
#     print(kwargs)   # ** collects the Keyword or named argument

# named(name= "Bob", age = 25) #     
#O/p {'name': 'Bob', 'age': 25} as dictionaries output Key and value pair 

# def named(name,age):
#     print(name,age)

# details = {"name": "Bob", "age": 25}

#named(details) # details act as positional argument hence the error 
#named(details,25)
#o/p {'name': 'Bob', 'age': 25} 25
# named(**details)
# o/p  Bob 25

# def named(**nam):
#     print(nam)

# details = {"name": "Bob", "age": 25}


# named(**details)

###########################################################################
#unpacking Keyword arguments

# def named(**nam):  #unpacking Keyword arguments
#     print(nam)


# def print_nicely(**kwargs):   #unpacking Keyword arguments
#     named(**kwargs)
#     for args,value in kwargs.items():
#         print(f"{args}: {value}")

# print_nicely(name = "Bob", age = 25)    

#o/p
#{'name': 'Bob', 'age': 25}
# name: Bob
# age: 25

#############################################################################
# def both(*args,**kwargs):  #unpacking positional and Keyword/named arguments
#     print(args)
#     print(kwargs)

# both(1,2,4,5,6,name="Tanveer",age= 25)

#o/p
####(1, 2, 4, 5, 6) tuple of argument
####{'name': 'Tanveer', 'age': 25}  dictionaries of argument
###
##
##
##############################################################################
"""
def post(url,data= None,json=None, **kwargs):
    return request('post',url,data=data.json=json,**kwargs) # adds an extra argument the post
"""

################################################################################
#OOPs concept Object oriented Programmimg

# student = {"name": "tanveer","grades":(66,77,99,44,99)}


# def average(sequence):
#     return sum(sequence)/len(sequence)


# print(average(student["grades"]))

###########################################################################
#OOPs concept Object oriented Programmimg

# class Student:
#     def __init__(self):   ## function inside a class is called method
#         self.name = "Tanveer"
#         self.grades = (90,90,93,78,90)


# student = Student() ### Instance of a Object class Student or you can say a container
# print(student.name)
####################################################################
#OOPs concept Object oriented Programmimg   
# in Python Method with __{}__ is call special method or magic method
class Student:
    def __init__(self, name, grades) -> None:
        self.name = name
        self.grades = grades


    def average_grades(self):
        return sum(self.grades)/len(self.grades)


student = Student("Bob",(20,30,60,80,97))
print(student.name)
print(student.average_grades())
##################################################################################
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         #self.age = age


# #Person() # in Python Method with __{}__ is call special method or magic method
#          # Here as soon as you declare Person()(class name) it calls __init__ Method

#     #if __name__ == '__main__':
# bob = Person("Bob",35)
# print(bob.name) 
#######################################################################
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self): # convert the Object in string 
#         return f"Person {self.name}, {self.age} years old." 

#     def __repr__(self):
#         return  f"<Person ({self.name}, {self.age} )>"      #  Generate output for developer  


# #Person() # in Python Method with __{}__ is call special method or magic method
#          # Here as soon as you declare Person()(class name) it calls __init__ Method

#     #if __name__ == '__main__':
# bob = Person("Bob",35)
# print(bob)  # Error <__main__.Person object at 0x000002573B53A200>
#             # only bob is a Object and it has string and numbers
#             # print(bob) is calling for a string representation
# #manual calling
# print(bob.__repr__())

# >>> import datetime
# >>> now = datetime.datetime.now()
# >>> str(now)
# '2019-03-29 01:29:23.211924'
# >>> repr(now)
# 'datetime.datetime(2019, 3, 29, 1, 29, 23, 211924)'
# In above output, the str(now) computes a string containing 
# the value of now 
# whereas repr(now) again returns the python code needed to rebuild our now object.
# Key differences
# str()
#                                                                repr()
# Make object readable
#                                                 Required code that reproduces object
# Generate output to end user
#                                                     Generate output for developer  
# 
# 
# 
# 
# Now if you go by the official python documentation
#  – the __str__ is used to find the 
# “informal”(readable) string representation of an object 
# whereas __repr__ is used to find the “official” string representation of an object. 
# 
# ############################################################################
# solved
# class Store:

#     def __init__(self,name):
#         self.name = name
#         self.items = []

#     def add_item(self, name, price):
#         item = {'name':name, 'price':price }
#         self.items.append(item)

#     def stock_price(self):
#         return sum([item['price'] for item in self.items])
        #Or
        # total = 0
        # for item in self.items:
        #     total += item['price']
        # return total   
        # 
        # 
        # 
        # 
        # ######################################################################
# class composition 

# class BookShelf:
#     def __init__(self,*books):  # class composition is class containing bunch of other class
#         self.books = books      # Inheritance mean Book is a BookShelf which is not the case 
                                # class Composition mean BookShelf has many book 

#     def __str__(self):
#         return f"BookShelf with {len(self.books)} books."

# class Book:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"Book {self.name}"

# book = Book("Harry Potter")
# book1 = Book("Python 101")

# shelf = BookShelf(book, book1)

# print(shelf)

# Information In addition, you can now access shelf.books and that
# gives you all the books stored within the bookshelf, whereas
# earlier you would not have had access to that.

##############################################################################
#Type hinting in python 3.5+

# from typing import List

# def list_avg(sequence: List) -> float:  # float: will return a string sequence is a :List
#     return sum(sequence)/ len(sequence)

# print(list_avg([1,2,3])) 
# o/p 2.0  
############################################################################
# from typing import List,Tuple,Set # , Tuple, Set, etc
# class Book:
#     pass


# class BookShelf:
#     def __init__(self, books: Set(Book)):
#         self.books = books


#     def __str__(self) -> str:
#         return f"BookShelf with {len(self.books)} books."
                 

################################################################
# class Book:
#     TYPES = ("hardcover", "paperback")

#     def __init__(self,name: str, book_type:str, weight: int):
#         self.name = name
#         self.book_type = book_type
#         self.weight = weight 

#     def __repr__(self) -> str:
#         return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"


    # @classmethod
    # def hardcover(cls,name:str,page_weight:int) -> "Book": # If declare in same class
    #     return cls(name,cls.TYPES[0],page_weight + 100)  # hence return type in "Book"         

    # @classmethod
    # def paperback(cls,name:str,page_weight: int) -> "Book":
    #     return cls(name,cls.TYPES[1],page_weight)  
#############################################################################
#classmethod and staticmethod    
# class ClassTest:
#     def instance_method(self): # all the method which uses first parameter as Object instance method
#         print(f"Called instance_method of {self}")


#     @classmethod
#     def class_method(cls): # no need to create a instance here in classmethod
#         print(f" Called class_method of {cls}")

#     @staticmethod
#     def static_method(): # staticmethod do not have any information on class or Object
#         print("called static_method")    

# test = ClassTest()
# test.instance_method()
# ClassTest.instance_method(test)

# ClassTest.class_method() # python will automatically pass as ClassTest.class_method(ClassTest)

# instance_method are used for most things you want produce an action which data you want change/modify
# inside the Instance_method
# 
# 
# class_method are use as factories 
# 
# static_method is used to place the method inside the class
# 
# ####################################################
# class Book:
#     TYPES = ("hardcover","paperback") # acts a property(factory) by using classmethod


#     def __init__(self,name,book_type,weight): # __init__ create a instance and return an Object
#         self.name = name
#         self.book_type = book_type
#         self.weight = weight 

#     def __repr__(self):
    #     return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g"


    # @classmethod
    # def hardcover(cls,name,page_weight):
    #     return Book(name,Book.TYPES[0],page_weight + 100)
    #    #Or
    #    # return cls(name,cls.TYPES[0],page_weight + 100) same as above cls is class name


#     @classmethod
#     def paperback(cls,name,page_weight):
#         return Book(name,Book.TYPES[1],page_weight)
#         #Or
#        # return cls(name,cls.TYPES[1],page_weight) same as above cls use cls helps in inheritance           
            

# #book = Book("Harry Potter", "hardcover", 1500)

# book = Book.hardcover("Harry",1568)
# light = Book.paperback("Python 101", 600)

# #print(book.name)
# print(book) 
# print(light) 
###################################################################################
# import sys
# print(sys.path) 
#print(sys.modules) 
# Dunder or magic methods in Python are the methods having two prefix and 
# suffix underscores in the method name.
#  Dunder here means “Double Under (Underscores)”.
#   These are commonly used for operator overloading.
#    Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.

# The __init__ method for initialization is invoked without any call,
#  when an instance of a class is created,
#   like constructors 
#   in certain other programming languages such as C++, Java, C#, PHP etc. 
#   These methods are the reason we can add two strings with
#    ‘+’ operator without any explicit typecasting.

#__name__ is global variable and used as dunder meaning it takes from where the file is run

# def divide(dividend, divisor):
#     return dividend / divisor


# print("t.py:", __name__)

################################################################
#  Error in Python Error is used for flow control 

# def divide (dividend, divisor):
#     if divisor == 0:
#         raise ZeroDivisionError("Divisor cannot be zero/0.")                          #print("Divisor cannot be zero. ")
#     return dividend/divisor  # This divide function is concern about the Mathematic of
#                              # of the function 

# grades = [66,77,54,78]

# print("Welcome to the average grade program.")
# try:
#     average = divide(sum(grades),len(grades)) # try and except how to handle the mathematic
# except ZeroDivisionError as e: # create a variable e put value of error  # in the context of your program 
#     print(e)
#     print("There are no grades yet in your list.")

# print(f"The average grade is {average}.")
#####################################################################################
#custom Error classes

# Error classes ZeroDivisionError,RuntimeError,ValueError 

#ValueError
# import math
# try:
#     print(math.sqrt(-1))
# except ValueError:
#     print('You can not get take the square root of a negative number ')

#(As seen from the output of our code above, 
# there is a ValueError arising from an invalid input in the code.
#  This is so because, mathematically,
#  there is nothing like the square root of a negative integer (-0).)
#######exception BaseException
# The base class for all built-in exceptions.
#  It is not meant to be directly inherited by user-defined classes
#   (for that, use Exception).
#    If str() is called on an instance of this class,
#     the representation of the argument(s) to the instance are returned,
#      or the empty string when there were no arguments.
#with_traceback(tb)

#######exception Exception
# All built-in, non-system-exiting exceptions are derived from this class. 
# All user-defined exceptions should also be derived from this class.
######exception ArithmeticError
# The base class for those built-in exceptions that are raised
#  for various arithmetic errors:
#  OverflowError, ZeroDivisionError, FloatingPointError.
#####exception BufferError
#Raised when a buffer related operation cannot be performed.
#####exception LookupError
# The base class for the exceptions that are raised when a key or 
# index used on a mapping or sequence is invalid:
#  IndexError, KeyError. This can be raised directly by codecs.lookup().
######exception AssertionError
#Raised when an assert statement fails
######exception AttributeError
######exception EOFError
#####exception ImportError
#####exception GeneratorExit
#####exception ImportError
#####exception ModuleNotFoundError
#####exception IndexError
#####exception KeyError
#####exception KeyboardInterrupt
# exception MemoryError
# exception NameError
# exception NotImplementedError
# exception OSError
# exception RecursionError
# exception OverflowError
# exception ReferenceError
# exception RuntimeError
# exception StopIteration
# exception StopAsyncIteration
# exception SyntaxError
# exception SystemError
# exception SystemExit

#################################################################################
# First Class Function is nothing but function can be pass as an variable and used
# in below operator takes divide as a value and call the divide function
# i.e calculator(20,4, oprator=divide) unpacks the call by "return operator(*value) change to
# = (operator = divide)(*value unpacked to 20,4) which inturn calls divide(20,4)

# def divide(dividend,divisor):
#     if divisor == 0:
#         raise ZeroDivisionError("Divisor cannot be 0.")

#     return dividend / divisor


# def calculator(*values,operator):
#     return operator(*values)


# result = calculator(20,4,operator=divide)
# print(result)
###########################################################################
from operator import itemgetter
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"could not find an element with {expected}.")


friends = [

  {"name":"Rolf Smith", "age": 24},
  {"name":"Adam Wool", "age": 30},
  {"name":"Anne Pun", "age": 27},


]  

# def get_friend_name(friend):
#     return friend["name"]

#print(search(friends,"Tanveer Ansari",get_friend_name)) 

#print(search(friends,"Adam Wool",lambda friend: friend["name"])) 

print(search(friends,"Adam Wool",itemgetter("name"))) 
#######################################################################################
#simple decorators in python --- they allow us to modify functions
# import functools # this lib secure the documentation of both the function i.get and secure
# user = {"username": "jose", "access_level": "guest"}

# def make_secure(func):
#     @functools.wraps(func)
#     def secure_function():
#         if user["access_level"] == "admin":
#           return func()
#         else:
#             return f"No admin permissions for {user['username']}."  
#     return secure_function


# @make_secure  #get_admin_password = make_secure(get_admin_password)  # @make_secure
# def get_admin_password():   # secure the get_admin_password() function 
#     return "1234"           # /decorator allow as modify this function

# # if user["access_level"] == "admin":  # This code is secure 
# #     print(get_admin_password())

# #print(get_admin_password())    # but the below code is not secure 
# print(get_admin_password.__name__)
                            # loophole in decorator function is now get_admin_password 
                            # is replace with secure_function, get_admin_password is not 
                            # registered as function in python instead secure_function 
                            # is replaced.Using the Lib functools it register as it is.


########################################################################################
# decorating Functions with parameters
# import functools
# user = {"username":"jose", "access_level": "guest"}

# def make_secure(func):
#     @functools.wraps(func)
#     def secure_function(*args,**kwargs):
#         if user["access_level"] == "admin":
#             return func(*args,**kwargs)
#         else:
#             return f"No admin permission for {user['username']}."
#     return secure_function

# @make_secure
# def get_password(panel):
#     if panel == "admin":
#         return "1234"
#     elif panel == "billing":
#         return "super_secure_password"    

# print(get_password("billing"))  # get_password is now related to the inner function 
                       # secure_function 

###########################################################################################
# Decorators with Parameters
# import functools
# user = {"username": "jose", "access_level": "guest"}


# def make_secure(access_level):  # this a factory to create a decorator
#     def decorator(func):       # {
#         @functools.wraps(func)
#         def secure_function(*args,**kwargs):
#             if user["access_level"] == access_level:
#                 return func(*args,**kwargs)
#             else:
#                 return f"No {access_level} permission for {user['username']}."
#         return secure_function
#     return decorator           # }

# @make_secure("admin")   # Order is important function call happens here # {} will run
# def get_admin_password(): # This function is for admin level
#     return "admin: 1234"

# @make_secure("user")
# def get_dashboard_password(): # This function is for user level
#     return "user: user_password"

# print(get_admin_password())
# print(get_dashboard_password())


# user = {"username": "anna", "access_level": "admin"}

# print(get_admin_password())
# print(get_dashboard_password())


# user = {"username": "Tanveer", "access_level": "user"}

# print(get_admin_password())
# print(get_dashboard_password())
###########################################################################################
# Mutability in python

# a = [] # empty list and list is mutable as you can change it 
# b = a

# print(id(a)) # a and b refering to the same object as memory are some
# print(id(b))
# #o/p
# #2552347925824
# #2552347925824

# a.append(35)

# print(a)
# print(b)
# o/p 
# [35]
# [35]
#############################################################################
# a = ()
# b = () # empty tuple

# a = a + (15,)  # this creating a new tuple 

# print(b)
# print(a)
####################################################################
# a = 8567 # integers are immutable can change once created that 
# b = 8567 # here a and b are pointing to same memory location  

# print(id(a))
# print(id(b))
#o/p
# 2415425149136
# 2415425149136
# tuple,string,integers,float,boolean are immutable

#list,dictionary, set are mutable 
####################################################################################
#Mutable Default Parameters (and Why They're a Bad Idea)

# from typing import List, Optional

# class Student:
#     def __init__(self, name:str, grades: Optional[List[int]] = [] ): # This is bad default
#         self.name = name
#         self.grades = grades

#     def take_exam(self, result: int):
#         self.grades.append(result)

# bob = Student("Bob")
# rolf = Student("Rolf")
# bob.take_exam(90)
# print(bob.grades)
# print(rolf.grades)   # eventhought rolf has not given the exam the score is appended due to Default value
# o/p
# [90]
# [90]

#To Avoid the above code of default with modified new code


from typing import List, Optional

class Student:
    def __init__(self, name:str, grades: Optional[List[int]] = None ): # This is bad default
        self.name = name
        self.grades = grades or [] # define inside the function not in the parameter list





    def take_exam(self, result: int):
        self.grades.append(result)

bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)

# O/p 
# [90]
# []   # 
# The End of Oreilly Course Online
#################################################################################
# a = "hello"
# b = a

# print(id(a))
# print(id(b))

# a += "world"

# print(a)
# o/p
# 2397646124016
# 2397646124016
# helloworld


###########################################################################################
# def f():
#    try:
#       return(1)
#    finally:
#       return(2)
# k=f()
# print(k)
#################################################

# name = ("Tanveer").lower()
# print(name)

# L = [1,2]
# g = []
# g=random.shuffle(L)
# print(g)

#################################################################
# def total(initial = 5, *num, **key):
#    count = initial
#    for n in num:
#       count+=n
#    for k in key:
#       count+=key[k]
#    return count
# print(total(100,2,3, clouds=50, stars=100))
###################################################################
# x = '' in 'python'
# print(x)
############################################
# d = (1,2)
# print(set(d))
################################################
# c = ~~~~19
# print(c)
##############################################
# print(0.1+0.2==0.3)
###################################################
# set(s1={1,2,3})
# v= 2 * s1
# set = {1,2}
#O/p Error

#############################################################
# Rate-Limit in FastAPI
# pip install fastapi-limiter

# FastAPI-Limiter is simple to use, which just provide a dependency RateLimiter,
#  the following example allow 2 times request per 5 seconds in route /.

# import aioredis
# import uvicorn
# from fastapi import Depends, FastAPI

# from fastapi_limiter import FastAPILimiter
# from fastapi_limiter.depends import RateLimiter

# app = FastAPI()


# @app.on_event("startup")
# async def startup():
#     redis = await aioredis.create_redis_pool("redis://localhost")
#     await FastAPILimiter.init(redis)


# @app.get("/", dependencies=[Depends(RateLimiter(times=2, seconds=5))])
# async def index():
#     return {"msg": "Hello World"}


# if __name__ == "__main__":
#     uvicorn.run("main:app", debug=True, reload=True)

# Usage
# There are some config in FastAPILimiter.init.

# redis
# The redis instance of aioredis.

# prefix
# Prefix of redis key.

# identifier
# Identifier of route limit, default is ip, you can override it such as userid and so on.

# async def default_identifier(request: Request):
#     forwarded = request.headers.get("X-Forwarded-For")
#     if forwarded:
#         return forwarded.split(",")[0]
#     return request.client.host + ":" + request.scope["path"]
# callback
# Callback when access is forbidden, default is raise HTTPException with 429 status code.

# async def default_callback(request: Request, response: Response, pexpire: int):
#     """
#     default callback when too many requests
#     :param request:
#     :param pexpire: The remaining milliseconds
#     :param response:
#     :return:
#     """
#     expire = ceil(pexpire / 1000)

#     raise HTTPException(
#         HTTP_429_TOO_MANY_REQUESTS, "Too Many Requests", headers={"Retry-After": str(expire)}
#     )


##################################################################################
# IP Level throttling # Postgresql Has pg_hba.conf File where subnet Mask is configuted to take the Local network IP address 
# The accepted answer makes use of the TrustedHostMiddleware but that can be easily spoofed using a reverse proxy, i.e. using NGINX or using any other technique. In my opinion, validating IP address in a custom middleware is more secure:

# from fastapi import FastAPI, Request, status
# from fastapi.responses import JSONResponse


# app = FastAPI()

# # Whitelisted IPs
# WHITELISTED_IPS = []

# @app.middleware('http')
# async def validate_ip(request: Request, call_next):
#     # Get client IP
#     ip = str(request.client.host)
    
#     # Check if IP is allowed
#     if ip not in WHITELISTED_IPS:
#         data = {
#             'message': f'IP {ip} is not allowed to access this resource.'
#              }
#         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=data)

#     # Proceed if IP is allowed
#     return await call_next(request)
#     I'd maintain a list of whitelisted IPs and then I'd compare the client IP to the list and will return a 400 Bad Request error if 
#     the IP is not in the whitelisted IPs list.

#     FastAPI provides a TrustedHostMiddleware that:

# Enforces that all incoming requests have a correctly set Host header, in order to guard against HTTP Host Header attacks.

# from fastapi import FastAPI from fastapi.middleware.trustedhost import TrustedHostMiddleware

# app = FastAPI()

# app.add_middleware(
#     TrustedHostMiddleware, allowed_hosts=["example.com","*.example.com"] 
# )


# @app.get("/") async def main():
#     return {"message": "Hello World"}
# 
# The following arguments are supported:

# allowed_hosts - A list of domain names that should be allowed as hostnames.
#  Wildcard domains such as *.example.com are supported for matching subdomains
#   to allow any hostname either use allowed_hosts=["*"] or omit the middleware.
# If an incoming request does not validate correctly then a 400 response will be sent.
##############################################################################
#   concurrent connection limit: You have lot of client or lot of user 
# who try to connect to your database/ api concurrent you limit the client.  
# ##################################################################
# How to secure a restful  api

# 1.HTTPS
# 2.Hashing 
# 3.Never expose in URL never expose the parameter such as Username,email.
# 4.Oauth to protect

#############################################################################
# REGEXP in mysql

## ^ beginning of a string
## $ end of a string
## | pipe which logical Or we can supply multiple search pattern
## [ab]e
## [a-j]h

# select * 
# from customers
# where first_name REGEXP 'elka|ambur'

# select * 
# from customers
# where first_name REGEXP 'ey$|on$'

# select * 
# from customer
# where first_name REGEXP '^my|se'



# select * 
# from customer
# where first_name REGEXP 'b[ru]' or 'br|bu'

###############################################
# Is NULL Operator


# select * 
# from customer
# where phone IS NULL

################################################
#Order By Clause


# select * , quantity * unit_price As total_price
# from Order_Item
# where order_id = 2 
# Order by total_price desc
#######################################################
# Limit Clause

# select * 
# from customers
# Limit 3

# select * 
# from customers
# limit 6,3 ### skips first record and and print the next 3 records


#  select * 
#  from customer
#  where 
#  order by points desc
#  Limit 3

 ############################################################################
 # inner join
# select * 
# from orders
# join customers 
# on orders.customerid = customers.customerid 


# SELECT OrderDetailID,o.orderid, ProductID,Quantity
# from orderDetails oI
# join orders o on oI.orderid = o.orderID order by orderdetailID desc
# #########################################################################
# join across databases

# select * 
# from order_items oi 
# join sql_inventory.products p  # different DB 
# on oi.product_id = p.product_id 

#####################################################################
#self join
# user sql_hr;


# select *
# from employees e
# join employees m
#  on e.reports_to = m.employee_id

#  same
 
#  select e.employee_id,
#         e.first_name,
#         m.first_name As Manager
# from employees e
# join employees m
# on m.reports_to = m.employee_id    
# 
# ################################################################################
# joining multiple tables
# 
# select * 
# from orders o
# join customers c
# on o.customer_id = c.customer_id
# join order_statuses os
# on o.status = os.order_status_id 
# 
# same 

# select 
#   o.order_id.
#   o.order_date,
#   c.first_name,
#   c.last_name,
#   os.name as STATUS
#   from orders o 
#   join customers c
#   on o.customer_id = c.customer_id
#   join order_statuses os
#   on o.status = os.order_status_id

##########################################################################
# payment
# payment_id , client_id, invoice_id, date, amount, payment_method      
#payment_method
# payment_method_id, name

# select *
# from payment p
# join clients c
# on p.client_id = c.client_d
# join payment_method pm
# on p.payment_method = pm.payment_method_d

# same

# select
#  p.date,
#  p.invoice_id,
#  p.amount,
#  c.name,
#  pm.name,
#  from payment p
# join clients c
# on p.client_id = c.client_d
# join payment_method pm
# on p.payment_method = pm.payment_method_d
##########################################################################
#compound join condition
# composite columns that is the table contains two column as Primary key and 

# example 
# Order table
# order_id,product_id, quality, unit_price 
# customer table
# customer_id, first_name, last_name, birth_date, phone, address

# So in above order_id, and product_id as primary key....Both the column uniquely identify the Row.

# "order_item_notes" table
# note_id, order_id, product_id, note 
# 
#"order_items" table
# order_id, product_id, quantity, unit_price


#"orders" table
# order_date , order_id , first_name,shipper, status

# 
# So,
# select * 
# From order_items oi
# join order_item_notes oin
# on oi.order_id = oin.order_id
# and oi.product_id = oin.product_id # compound join condition
##########################################################################
#implicit join syntax
#
# select *
# from orders o, customers c
# where o.customer_id = c.customer_id
# 
# ########################################
# cross join 
# select * 
# from orders o, customers c
# ##########################################################
# outer join
# 
# 
# 
# This below is inner join
# select 
# c.customer_id,
# c.first_name,
# o.order_id 
# from customers c 
# join orders o # this is inner join
# on c.customer_id = o.customer_id 
# order by c.customer_id


# Left outer join
# select 
# c.customer_id,
# c.first_name,
# o.order_id
# from customers c
# left join orders o
#   on c.customer_id  = o.customer_id
# order by c.customer_id 
# #######################################
# Right outer join
# select 
# c.customer_id,
# c.first_name,
# o.order_id
# from  orders o
# right join customers c 
#   on c.customer_id  = o.customer_id
# order by c.customer_id
# 
# #################################################################
# select 
#  p.product_id,
#  p.name,
#  oi.quality
# from products p
# left join order_items oi
# on p.product_id = oi.product_id 
# 
# ##########################################################
# outer joins between Multiple tables
# 
# select 
# c.customer_id,
# c.first_name,
# o.order_id
# from customers c
# left join orders o
# on c.customer_id = o.customer_id
# join shippers sh  # inner join
#  on o.shipper_id = sh.shipper_id 
# order by c.customer_id    
# 
# same
# # select 
# c.customer_id,
# c.first_name,
# o.order_id,
# sh.name as shipper
# from customers c
# left join orders o
# on c.customer_id = o.customer_id
# left join shippers sh  # inner join
#  on o.shipper_id = sh.shipper_id 
# order by c.customer_id  
# 
# 
# 
# select 
# o.order_id,
# o.order_date,
# c.first_name as customer
#sh.name As   shipper
# from orders o
# join customers c
#    on o.customer_id = c.customer_id
# join shippers sh
#    on o.shipper_id = sh.shipper_id
# 
# 

# select 
# o.order_id,
# o.order_date,
# c.first_name as customer
# sh.name As   shipper
# os.name As status
# from orders o
# join customers c
#    on o.customer_id = c.customer_id
# Left join shippers sh
#    on o.shipper_id = sh.shipper_id
#join order_statuses os
#    on o.status = os.order_status_id   
# 
# ##################################################################
# self outer join
# 
# Use sql_hr
# 
#select 
#  e.employee_id,
#  e.first_name,
#  m.first_name As manager
# from employees e
# Left join employees m # Every employees who has manager, no manager
#   on e.reporting_to = m.employee_id 
# 
# #################################################################
# Using Clause
# 
# select 
# o.order_id,
# c.first_name,
# sh.name As shipper
# From orders o
# join customers c
# using (customer_id)
# Left join shipper sh
# using (shipper_id)
# 
# 
# composite key using clause
# 
# select *
# from order_items oi
# join order_item_notes oin
#    using(order_id,product_id)
# 
# payment table
# date, client, amount, name
# 
# 
# select 
# p.date
# c.name As Client
# p.amount,
# pm.name as payment_method
# from payments p
# join clients c using (client_id)
# join payment_methods pm 
#      on p.payment_method = pm.payment_method_id 

##########################################################################
#Natural Join
# select
# o.order_id,
# c.first_name
# from orders o
# natural Join customers c # both the table should have one common column_name with the same datatype

##################################################
#cross join

# select c.first_name as customer
#        p.name as product 
# from customers c
# cross join products p
# order by c.first_name

# same result

# select c.first_name as customer
#        p.name as product 
# from customers c,product p   # same as cross join result also called implicite syntax
# order by c.first_name

#########################################
#Union clause we can combine multiple queries

# select 
#  order_id,
#  order_date,
#  'Active' As Status
#  From   Orders
#  where order_date >= '2019-01-01'
#  Union
#  select 
#  order_id,
#  order_date,
#  'Archives' As status
#  from orders
#  where order_date <= '2019-01-01'

#
# select first_name,last_name # is wrong union stmt
# from customers
# union
# select name 
# from shippers

# select first_name 
# from customers
# union
# select name 
# from shippers

#output with column name first_name as from first query

# select 
# customer_id,
#  first_name,
#   points,
#    'Bronze' as Type
# from customers
# where points < 2000
# Union
# select 
# customer_id,
#  first_name,
#   points,
#    'Silver' as Type
# from customers
# where points Between 2000 and 3000
# Union
# select 
# customer_id,
#  first_name,
#   points,
#    'Gold' as Type
# from customers
# where points > 3000
# Order by first_name

#####################################################################
#column attributes




###############################################################
#inserting rows in multiple table 
# parent and child relation

# insert into orders (customer_id, order_date, status)
# values(1,'',1)   # parent table

# insert into order_items
# values
#       (last_insert_id(), 1,1, 2.95),
#       (last_insert_id(), 2, 1, 3.95)   # child table
##############################################################
#creating a copy of table

# create table orders_archives as
# select * from orders  # attribute that is primary key is not added in the table.

# insert into orders_acheived   # this subquery within insert stmt
# select *
# from orders
# where order_date < '2019-01-01'

# create table invoice_archived as
# select 
# i.invoice_id,
# i.number,
# c.name as client,
# i.invoice_total,
# i.payment_total,
# i.invoice_date
# i.payment_date,
# i.due_date
# from invoices i 
# join clients c
#      using (client_id)
# where payment_date IS NOT NULL 
# ################################################################
# update invoice 
# set payment_total = 10,payment_date = '2019-01-01'
# where     invoice_id = 1
# ########################################################
# subqueries in update invoice
# 
# update invoices
# set
# payment_total = invoice_total * 0.5
# payment_date = due_date
# where client_id = (select client_id
#from clients
#where name = 'Myworks'
# )    

# update invoices
# set
# payment_total = invoice_total * 0.5,
# payment_date = due_date
# where client_id in 
#                 ( select client_id
#                    from clients
#                    where state in ("CA", "NY"))

####################################
# update invoices 
# set
#    payment_total = invoice_total * 0.5,
#    payment_date = due_date
# where payment_date IS NULL  
# 
#
#
#

# # update orders
#   set comments = 'Gold customers'
#   where customer_id IN 
# #                (select * 
# #                from customers
# #                 where points > 3000)             
############################################################
# Delete from invoices
# where invoice_id = 1

# Or 
# Delete from invoices
# where client_id = (
#     select * 
#     from clients
#     where name = 'Myworks'
# )

####################################################################
# A PL/SQL procedure is a reusable unit that encapsulates specific business logic of the application.
#  Technically speaking, a PL/SQL procedure 
#  is a named block stored as a schema object in the Oracle Database.

# What is the difference between PL SQL function and PL SQL procedure?
# A function returns a value and control to calling function or code.
#  A procedure returns the control but not any value to calling function or code. 
#  A procedure has support for try-catch blocks.
#   A select statement can have a function call.

#   Similar to a procedure, a PL/SQL function is a reusable program unit stored 
#   as a schema object in the Oracle Database.

#PL/sql function
# create or replace function get_total_sales(
#     in_year pls_integer
# )
# return number
# Is 
#     Is_total_sales Number := 0
# BEGIN
#      ## get total sales
#      select  sum(unit_price * quantity)
#      into l_total_sales
#      from  order_items
#      inner join orders using (order_id)
#      where status = 'shipper'
#      group by extract(year from order_date)
#      Having extract(year from order_date) = in_year;
# ### return 1_total_sales;
# END  
# Rowtype
# The %ROWTYPE attribute provides a record type 
# that represents a row in a database table.
#  The record can store an entire row of data selected from 
# the table or fetched from a cursor or cursor variable.
# 
# PL/SQL has two types of subprograms called procedures and functions.
#  Generally, you use a procedure to perform an action and 
# a function to compute a value.   
# 
# "A procedures or function is a group or 
# set of SQL and PL/SQL statements that perform a specific task."  
# A function and procedure is a named PL/SQL Block which is similar .
#  The major difference between a procedure and a function is,
#  a function must always return a value, 
#  but a procedure may or may not return a value

# PL/SQL procedure 
# CREATE OR REPLACE PROCEDURE greetings 
# AS 
# BEGIN 
#    dbms_output.put_line('Hello World!'); 
# END; 
# /
# PL/sql Function
# CREATE OR REPLACE FUNCTION totalCustomers 
# RETURN number IS 
#    total number(2) := 0; 
# BEGIN 
#    SELECT count(*) into total 
#    FROM customers; 
    
#    RETURN total; 
# END; 
# / 
########################################################################
# Group by clause is pending

# SELECT COUNT(CustomerID), Country
# FROM Customers
# GROUP BY Country
# ORDER BY COUNT(CustomerID) DESC;

##################################################################
# #SELECT COUNT(CustomerID), Country
# FROM Customers
# GROUP BY Country
# HAVING COUNT(CustomerID) > 5;
#

# SELECT COUNT(CustomerID), Country
# FROM Customers
# GROUP BY Country
# HAVING COUNT(CustomerID) > 5
# ORDER BY COUNT(CustomerID) DESC;

###
#
# SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders
# FROM Orders
# INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
# WHERE LastName = 'Davolio' OR LastName = 'Fuller'
# GROUP BY LastName
# HAVING COUNT(Orders.OrderID) > 25;

###
#
# SELECT Employees.LastName, COUNT(Orders.OrderID) AS NumberOfOrders
# FROM (Orders
# INNER JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID)
# GROUP BY LastName
# HAVING COUNT(Orders.OrderID) > 10;

######################################
# synchronous Programming

# {def foo():
#     return

      
# foo()}  ### syn function is this part will execute first then it'll go to 
# # next stmt i.e  "print('tiim)"
# print('tiim')

###########################################
# async function uses coroutines
# import asyncio
# async def tan():
#     print('tan')
#     await foo('text')
#     print('finished')

# #asyncio.run(tan())  # we need to define async event-loop, then now adding asyncio.run it 
#                     # makes tan() as a coroutines asyncio creates a event-loop  


# async def foo(text):
#     print(text)
#     await asyncio.sleep(1)  # await should be used within async def here await makes 
#                              # coroutine  
# asyncio.run(tan())
# o/p
# tan
# text
# finished

#####################################################
#While the async is sleep we can do other task program below

#async function uses coroutines
# import asyncio
# async def tan():
#     print('tan')
#     task = asyncio.create_task(foo('text'))#instead of this line ==> await foo('text')
#     print('finished')

# #asyncio.run(tan())  


# async def foo(text):
#     print(text)
#     await asyncio.sleep(1)

# asyncio.run(tan())
# o/p
# tan
# finished
# text

###
# import asyncio

# async def fetch_data():
#     print('start fetching')
#     await asyncio.sleep(2)
#     print('done fetching')
#     return {'data': 1}

# async def print_number():
#     for i in range(10):
#         print(i)
#         await asyncio.sleep(0.25)

# async def tan():
#     task1 = asyncio.create_task(fetch_data())
#     task2 = asyncio.create_task(print_number())

#     value = await task1
#     print(value)
    #  #await task2 #o/p
#     start fetching
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# done fetching
# {'data': 1}


# asyncio.run(tan())   

# o/p
# start fetching
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# done fetching
# {'data': 1}
# 8
# 9
##################################################
# tan1 = [1,2]
# print(sum(tan1))

# tan1 = "tanveer"
# print("tanveer" [::-1])
################################################################
# several function  makes a module
# several module consolidate in a directory makes a package
# several package consolidate in a directory makes a library

# def reverse(s):   
#     result = ""
#     for i in s:
#         result = i + result    # first iteration it'll store 't',2 iteration 'at'  
#         """print (result)"""   # 3 iteration 'nat'................last iter 'reevnat' 
#     return result

# s = "tanveer"
# print("orginal string: ", s)
# print("reversed string:", reverse(s))

### in-build function

# s = "intellegent"
# result = "".join(reversed(s))
# print(result)

# s= "thant"
# print(s[::-1])
##############################
#### Prime number
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

############################################################################
# JWT Token Authentication ====JSON Web Token ==> JWT
# 
# One is session base authentication 
# 
# Client                                    API           
### Other is JWT Token Base Authenication 
# stateless base authentication in JWT i.e we have no idea about the user login or
# logout , 
# The Token is not stored in the database or in the api
# what happens in 
# Client                                    API 
#step1. /login (username + password)[IF credentials are valid sign  JWT Token]
#Client ===========================>>>API
# IF credentials are valid sign  JWT Token
#step2.{Token} send back to client 
#Client <<<===========================API
#          {Token} send back to client 
#step3.Now, With Request /posts header contain too {token}
#Client ===========================>>>API
#        With Request /posts header contain too {token} 
#        header meaning in the Payload of the request
#step4.Then, API checks the or verify token is valid or not
#step5. Data is send back to the client 
#Client <<<===========================API
#          Data is send back to the client 
# No Information is store in the API here                

# JWT Deep Dive 
# Token is divide into three segment 
# 1.Header Algorithm and Token Type  # This is metadata
# {
#     "alg": "HS256",
#     "typ": "JWT"
# }
# 2.PAYLOAD:DATA # Payload shouldnt be containing password or any restricted Data 
# {              # It should contain the UserId
#     "sub": "123456789",
#     "name": "John Doe"
#     "iat": 15678964 
# }
# 3.verify Signature  # Signature is combination of 3 thinks , 1.Header, 2.Payload, 
# HMACSHA256 (                          #3. Special password secret                          
#      base64UrlEncode(header) + "." +        or simple call secret code
#      base64UrlEncode(payload),      # Sinature is simply for data integrity
#      your-256-bit-secret            # signature is kept in API server


# )



#Logging in User


#Chrome                        API                                Database
# step1.
# /login (email,Passord)
# Chrome=======================>>>API============================>>>Database
#                                     Find user by email  
#                                 API<<<=============================Database
#                                       User{password(hashed)}
# 
#                                    unhashed password agained is hashed and
#                                               compare with hashed password 
#                                                if True
# Chrome<<<=======================API  
            # API send back {token}
################################################
# 7:27:59 Protecting Routes
# 7:36:17 Test Expired Token
# 7:42:47
# important#######     QKNB2952
# import mathx = '{1} is greater than {0}'.format(7,42)print(x)


# www.yelp.com/search?find_desc=&find_loc=Maime%2C+FL&ns=1


# www.yelp.com/search is the endpoint

# find_desc=&find_loc=Maime%2C+FL&ns=1 is query parameter, filter the request, pagenation

#%20 in the URL is considered as spaces

# 8:42:29
#9:04:02
#9:16:02
#9:21:02
#######################################################################################
# aList = [123, 'xyz', 'zara', 'abc']
# aList.insert( 3, 2009)
# print ("Final List :"  f"{aList}")

fruits = ["apple","banana","cherry","kiwi","mango"]

newlist = [x for x in fruits if "a" in x]
print(newlist)

triple = lambda x:x*3
print(triple(100))
#####################################################################################
#Types of inheritance 
#single interitance 
# Base class
# class Parent:
#     def func1(self):
#         print("This function is in parent class.")
 
# # Derived class
 
 
# class Child(Parent):
#     def func2(self):
#         print("This function is in child class.")
 
 
# # Driver's code
# object = Child()
# object.func1()
# object.func2()

#multiple inheritance   C(A,B) ===> Son (mother,father)

# Python program to demonstrate
# multiple inheritance
 
# Base class1
# class Mother:
#     mothername = ""
 
#     def mother(self):
#         print(self.mothername)
 
# Base class2
 
 
# class Father:
    # fathername = ""
 
    # def father(self):
    #     print(self.fathername)
 
# Derived class
 
 
# class Son(Mother, Father):
#     def parents(self):
#         print("Father :", self.fathername)
#         print("Mother :", self.mothername)
 
 
# Driver's code
# s1 = Son()
# s1.fathername = "RAM"
# s1.mothername = "SITA"
# s1.parents()

#Multilevel Inheritance :
# Python program to demonstrate
# multilevel inheritance
 
# Base class
 
 
# class Grandfather:
 
#     def __init__(self, grandfathername):
#         self.grandfathername = grandfathername
 
# Intermediate class
 
 
# class Father(Grandfather):
    # def __init__(self, fathername, grandfathername):
    #     self.fathername = fathername
 
        # invoking constructor of Grandfather class
        # Grandfather.__init__(self, grandfathername)
 
# Derived class
 
 
# class Son(Father):
    # def __init__(self, sonname, fathername, grandfathername):
    #     self.sonname = sonname
 
        # invoking constructor of Father class
        # Father.__init__(self, fathername, grandfathername)
 
    # def print_name(self):
    #     print('Grandfather name :', self.grandfathername)
    #     print("Father name :", self.fathername)
    #     print("Son name :", self.sonname)
 
 
#  Driver code
# s1 = Son('Prince', 'Rampal', 'Lal mani')
# print(s1.grandfathername)
# s1.print_name()

#Hierarchical Inheritance: 

#  Python program to demonstrate
# # Hierarchical inheritance
 
 
# # Base class
# class Parent:
#     def func1(self):
#         print("This function is in parent class.")
 
# # Derived class1
 
 
# class Child1(Parent):
#     def func2(self):
#         print("This function is in child 1.")
 
# # Derivied class2
 
 
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child 2.")
 
 
# # Driver's code
# object1 = Child1()
# object2 = Child2()
# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()
####################################################################################################
#9:27:34
#9:38
#10:09
#10:23
#11:17
#checked vote and oauth2

########################################################################################################
#CORS
#fetch('http://192.168.1.32:8000').then(res => res.json()).then(console.log)
#fetch('http://localhost:8000').then(res => res.json()).then(console.log)

# Cross Origin Resource sharing(CORS) allows you to make
# requests from web broswer on one domain to a server on
# a different Domain

# By dafault our API will only allow web browsers running
# on the same domain as our server to make requests to it
# pip install -r requirement.txt # command

####################################################################################################

