# read file notebook.txt
#  go into the file if the the line is empty, then delete it
from ast import While
import codecs
import io
from queue import Empty
import re
from tkinter import CURRENT, W
import os
import textwrap


# with open("notebook.txt", "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         if line == "\n":
#             lines.remove(line)
# f = io.open("notebook.txt", mode="r", encoding="utf-8")
# data=f.readlines()
# print(data)
# for line in data:
#     if line start with "In":
#         // delete the next 2 Empty lines
#         if line == "\n":
#             data.remove(line)
f = io.open("check.txt", mode="r", encoding="utf-8")
data = f.readlines()
# print(data)
count = 0
curr1 = 0
curr2 = 0
# while count < len(data):
# if "In" in data[count]:
#     count += 1
#     while data[count] == "\n":
#         print("Asdasd")
#         data.remove(data[count])
#         count += 1
#     curr1 = count

#     while data[count] != "\n":
#         count += 1
#     curr2 = count
#     for i in range(curr1, curr2):
#         data[i] = "#"+data[i]
# print( data[count] == "\n")
# if data[count] == "\n":
#     data.remove(data[count])
# count += 1
# data.pop(0)
# data.pop(1)


# while count < len(data):
# if data[count] == '\n':
#     data[count]=''
# count+=1


while count < len(data):

    if "In" in data[count] and "[" in data[count] and "]" in data[count]:

        data.pop(count)
        data.insert(count, "## %% \n")
        count += 1
        while data[count] == "\n":
            data.remove(data[count])
            count += 1
        curr1 = count

        while data[count] != "\n":
            count += 1
        curr2 = count
        for i in range(curr1, curr2-1):
            if re.match(r'\s', data[i]):
                data[i] = data[i][4:]
            data[i] = "#"+data[i]
        data.pop(curr2-1)
        data[curr2] = '## %% [markdown]\n'
        # curr1=0
        # curr2=0

    elif data[count] == '\n':
        data.pop(count)

    else:
        count += 1

# for line in data:
#     if line[0] == "#":
print(data)
file = codecs.open("lol.py", "w+", "utf-8")
for line in data:
    # file.write(line)
    if line[0] == "#":
        file.write(line[1:])
#     # elif line[len(line)-2] =='¶':
#     #     file.write("# "+line)
    elif line[len(line)-2] == '¶':
        file.write(" # "+line+"\n")
    else:
        file.write("#"+line+"\n")

file.close()
