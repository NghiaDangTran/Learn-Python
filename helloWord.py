# 1 mutiple asignment

# name,age,sex="brp",231,True

# nam1=name2=name3mnam=namd1=30
# print(nam1)

# 2 function for string
# name="bro"
# print(len(name))
# print(name.find("b"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("o"))
# print(name.replace("o","A"))
# print(name*9)

# 3) type casting= convert the data type of a value to another data type.


# x=1
# y=2.0
# z="3"
# x=float(x)
# z=int(z)
# y=str(y)
# print(x)
# print(int(y))
# print(z*32)

# 4) user input


# name= input("what is ur name \n")
# print(name)

# 5) math import
# import math
# pi=3.14
# print(round(pi))
# print(math.ceil(pi)) # round up , floor round down
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(420))
# print(max(pi,12,19))
# print(min(pi,12,19))


# 6) slicing = substring indexong[] or slice()

# name ="nghia dang tran ngoc"
# first_name=name[0:5]
# print(first_name)

# from operator import indexOf


# wesbite="https://google.com"

# slice=slice(8,-4)
# indexOf
# print(wesbite[slice])

# 7) if
# age = int(input("how old are you"))

# if (age > 10 and age < 18):
#     print(age)
# else:
#     print("yes")
# if age > 10 and age < 90:
#         print("no")


#  8) logical thing
# 9) while loop

# i=1
# while(i<10):
#     print("hi")
#     i+=1

# 10) for loop\
# for i in range(10):
#     print(i)

# import time


# for i in range(10,0,-1):
#     print(i,end="")
#     time.sleep(1)


# import contextlib
# from itertools import count


# for i in range(10):
#     if i==5:
#         continue
#     else: print(i)

# 11) set = colection which is unordered, unindexed . no duplicate
# list=[]
# set1={"fork","spon","mad"}
# set1.add("napkin")
# set1.remove("mad")
# set1.clear()
# set2=["bow","plate","cup","mad"]
# set1.update(set2)
# set1= set1.union(set2)
# set1.difference(set2)
# print(set1.intersection(set2))


# for x in set1:
# print(x)

# * 12)     dictionary= a changeable, unordered collection with unique key:value paor , the same with hashing
# from asyncio.windows_events import NULL


# Contry = {
#     "vietNam": "hanoi",
#     "USA": "wassiton",
#     "india": "new dehli",
#     "china": "beijing",
# }
# # Contry.update({"germany":"berlin"})
# # Contry.update({"USA":"berlin"})
# Contry.pop("USA")# remove
# Contry.clear()
# # print(Contry["hey"])
# # print(Contry.get("vietNam")) # boolean value much safeer
# # print(Contry.keys()) # get all the key
# # print(Contry.values()) # get all the value
# # print(Contry.items())# print all


# for key,val in Contry.items():
#     print (key+" "+ val)

# *13) index operator : give access to any str,list,tuples

# name="Nghia Dang"
# if(name[0]=="N"):
#     print("yes yout name "+name[0])

# *14) function


# def hello(x):
#     for i in range(x):
#         print("hellp")


# hello(7)

# *15) return value

# def add(a,b):
#     return a+b

# print(add(5,5))

# 16) keywords argument

# def hello(first,middle,last):
#     print("hello /\\\\() \"{middle} {last}")

# hello("Nghia",last="Dang",middle="tran")

# 17) nested funciton
# num=input("Enter num\n")
# num=round(abs(float(num)))
# print(num)


# 18) scope of variable

# def changename(name):
#     name="nghia dfanhg"
#     print(name)

# myname="nghiadsadasd"
# changename(myname)
# print(myname)

# *19) *args = parameter that will pack all arguments into atuple
# useful so that a function can accept a varying amount of arguments
# * is make data into tuple if u want to get that data just use a for loop to add them again

# def add(*value):
#     sum=0
#     value=list(value)
#     for i in range(len(value)):
#         sum+=i
#     print(sum)

# add(1,2,3)

# *20) **args = make value into dictionary

# def hello(**value):
#     # print("hello "+ value["first"]+ " "+value["last"] )
#     for key,value1 in value.items():
#         print(value1+" ",end="")

# hello(first="nghia",middle="dang",last="anh")
# # *21) str.format

# print(" themoon{} {}".format("anh","em"))

# *22) random
# import random
# x= random.randint(1,6)
# list=["rock","paper","siccor"]
# z= random.choice(list)
# random.shuffle(list)
# random.random() # 0-1

# https://youtu.be/XKHEtdqhLK8?t=9403
# *23) excetion

# try:
#     num=21
#     denominotor=12
#     result =num/denominotor
# except ZeroDivisionError:
#     print("cant dive")
# except Exception:
#     print("wrong")
# else:
#     print("result")

# *24) file open
# import os

# path="C:\Huion Tablet"

# if os.path.exists(path):
#     print("ok")
#     if os.path.isfile(path):
#         print("that is a file")
#     else:
#         print("not")
# else:
#     print("not ok")
# *25) read file

# import os
# # will close automatic
# try:
#     with open("test.tt") as file:
#         print(file.read())
# except Exception:
#     print("file not found")

# *26) write file
# text="YOOOOOOO\n"
# name="r"


# with open ("test.txt",name) as file:
#     if(file.readline()==""):

#         name="w"
#         with open ("test.txt",name) as file1:
#             file1.write(text)
#     else:
#         print("yes")

#         name="a"
#         with open ("test.txt",name) as file1:
#             file1.write(text)


# # *27) copy file
# from cgitb import text
# import  shutil
# # remmber to check test is ava;liable and safe
# shutil.copy("test.txt","copy.txt")

# *28) move a file

# import os

# src="test.txt"
# des="newFolder"


# try:
#     if os.path.exists(des):
#         print("already a file")
#     else:
#         os.replace(src,des)
#         print(src+" moved")
# except Exception:
#     print(Exception+"at")

# *29) delete file
# os.remove(src)

# *30) module
# like java make in another py file then import it


# def hello():
#     print("have a nice day")
# def bye():
#     print("hi")

# *31) paper siccor

# import random

# choices = ["rock", "paper", "scissors"]
# comp = random.choice(choices)

# user = None


# while True:
#     while user != "1" or user != "2" or user != "3":
#         user = input("Pls pick 1 to 3 (rock, paper, scissors)\n")
#         if user == "" or user == "break" or user=="quit" or user == "1" or user == "2" or user == "3":
#             break

#     if (user == "1" or user == "2" or user == "3"):
#         user=int(user)
#         user_input = choices[user-1]

#         if (
#         (comp == choices[0] and user_input == choices[1])
#         or (comp == choices[1] and user_input == choices[2])
#         or (comp == choices[2] and user_input == choices[0])
#         ):
#             print("User win")
#         elif comp==user_input:
#             print("Draw")
#         else:
#             print("comp win")
#     next=input("Do you still want to play? (Yes or No)\n")

#     if next=="No":
#         print("the game Ended")
#         break


# *32) quiz game
# def new_game():

# *33) OOP in python


# class Car:
#     def __init__(self, make, model, year, color):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color

#     def drive(self):
#         print("this car is driving")
#     def stop(self):
#         print("this car is stoping")

#*34) super() calass

# class Rec:
#     def __init__(self,length,width)
#         self.length=length
#         self.width=width
# class square(Rec):
#     def __init__(self,length,width)
#     super.__init__(length,width)


#*35) abstract class abstract method ****
# from abc import ABC, abstractmethod
# class Rec:

#     @abstractmethod
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#         print("yes")
# class square(Rec):
#     def __init__(self,length,width):
#         super().__init__(length,width)
#         print("yes")

# num1=Rec(1,2)

# *36) pass object argumernt

# class Car:
#     color=None
# class moto:
#     color=None
# def change_color(Obj_car,color):
#     Obj_car.color=color

# moto1=moto()
# change_color(moto,"name")
# *37) duck typing = concept where the class of an obj is less important than the methods/attributes 
# *38) walrus operator:=

# print(happy=Ture)#cannot do
# print(happy:=True)# can do 

# foods=list()
# while food:=input("what food ?") !="quit":
#     foods.append(food)


#*39)

# def hello():
#     print("hello")


# # print(hello)
# # hi=hello
# # hi()
# say =print
# say("cant sav")

# #*40) high order function

# def loud(text):
#     return text.upper()
# def quite(text):
#     return text.lower()

# def hello(func,container):
#     text=func(container)
#     print(text)

# hello(loud,"HI evryone")

# *41) higher order function accept a function as an argument or returns a funciton
# def divisor(x):
#     def dividend(y):
#         return y/x
#     return dividend
# divdie=divisor(2) # call first then save the x value

# print(divdie(10)) # because the divisor function return dividen then when we call dividie(10)= call dividend(10) an with the saved value of x
# *42) lambda function
# double=lambda x: x*2
# mutiple=lambda x,y:x*y
# print(double(2))
# print(mutiple(2,3))
# *43  sort sorted map(function,data )   filter(age,data)
# reduce function
# import functools
# letter =["a","b","c","d"]
# word=functools.reduce(lambda x,y:x+y,letter)
# print(word)

# factorial=[5]
# result= functools.reduce(lambda x,y:x*y,factorial)
# print(result)
#*44 list comprehwnaion  = a way to creat a new list with less syntax
# square=[i*i for i in range(1,11)]
# print(square)
# student=[100,90,80,80,76,0,5,9,6,3,110,220,336,5,4,8,8,88,22,99]
# graded=[i for i in student if i>=60  ]
# #  if need else or move infort
# graded=[i if i>=60 else "Fail" for i in student   ]

# print(graded)
# *45 dic comprehantion
# city={"newyouir":32,"boston":75,"los":100}
# newCity={key:(value>10) for (key,value) in city.items()}
# print(newCity)
# *46 zip(*iterables) = aggregate elemets from 2 or more iterables

# user=["user1","user2","user3"]
# passWord=("password","123","456")
# login_date=["1/1/2021","1/2/2021","1/3/2021"]
# user_data=dict(zip(user,passWord))
# print(user_data)

# for key,value in user_data.items():
#     print(key +value)
# *47) main def
# def hello():
#     print("helelo")
# if __name__ =='__main__':
#     print("runioing")
# print(__name__)
# hello()


# *48) time module
# import time

# # print(time.ctime(10000))

# # print(time.time())

# print(time.ctime(time.time()))
# time_obj=time.localtime()

# *49) threading
# import threading
# import time
# # print(threading.active_count())
# # print(threading.enumerate())

# def eat_breafast():
#     time.sleep(3)
#     print("you eat breakfast")
# def drink_coffer():
#     time.sleep(4)
#     print("you drink coffee")

# def study():
#     time.sleep(5)
#     print("you start study")
    

# x=threading.Thread(target=eat_breafast)
# x.start()
# y=threading.Thread(target=drink_coffer)
# y.start()
# z=threading.Thread(target=study)
# z.start()
#*50 daemon thread
# import threading
# import time

# def timmer():
#     print()
#     count=0
#     while True:
#         time.sleep(1)
#         count+=1
#         print("loging in for: ",count,"second") 
# x=threading.Thread(target=timmer,daemon=True)
# x.start()
# anwer=input("do u want to exit")

# *60) mutiprocessing
# from multiprocessing import Process, cpu_count
# import time




# def counter(x):
#     count=0
#     while count<x:
#         count+=1


# def main():
#     print(cpu_count())
#     a=Process(target=counter,args=(10000000/4,))
#     b=Process(target=counter,args=(10000000/4,))
#     c=Process(target=counter,args=(10000000/4,))
#     d=Process(target=counter,args=(10000000/4,))
    
#     a.start()
#     b.start()
#     c.start()
#     d.start()


#     a.join()
#     b.join()
#     c.join()
#     d.join()

#     print("finish in:",time.perf_counter(),"seconds")



# if __name__=='__main__':
#     main()
# *61) GUI window
from tkinter import *
window=Tk() #iknstantiate an instance of awindow
window.geometry("500x500")
window.title("Hello words")
window.config(background="black")

window.mainloop() # place window on computer screen listen for events















