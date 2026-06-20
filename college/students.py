# def show_student():
#     print("hello student")
    
# from looping import new
# new.hello()    




#Task: Display all the files in a dir
import os
files = os.listdir()
for file in files:
    print(file)
    
#Module - sys
#provides the information
#python interpreter    
import sys
print(sys.version)
print(sys.exit())