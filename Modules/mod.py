'''
Module:
a module is simply a python file containing code

why?
1.large file
2.hard to maintain
3.difficult to reuse

modules:
reusability
organization
readability
collabration
'''
import calculator
print(calculator.add(1,2))
print(calculator.sub(10,5))

#Task: create a module named as greeting 
import greeting
greet1=greeting.greet()
print(greet1)

#task
#from looping import new
#print(new.hello())

#built in modules:
import math
print(math.sqrt(33))
print(math.factorial(5))

#from import
# from math import sqrt,pow
# sqrt(3)
# pow(2,2)
# import math
# import random
#    #or
# import math,random
#all the attributes from math
# from math import *
# from looping import new
# new.hello()

#collection of modules is called package

import datetime as dt
print(dt.datetime.now())

'''
Module         Meaning
1.math         mathematics
2.random       random values
3.datetime     date & time
4.os           operating system
5.sys          python runtime
'''
# help("modules")

'''
#Package:
is a floder containing multiple modules
school/-->package
    student.py
    teacher.py
    managment.py
    
    main.py-->from school import student
    
__init__.py
Purpose:
special file used to identify package
1.marks directory as package
2.runs initialization code
3.controls the import    
'''
#Importing from package
#from School import student
#student.show_student()

#builtin methods
import math
#round upward
print(math.ceil(5.2))

#floor()-->
math.floor(5.2)
print(math.floor(5.2))

#constrants
print(math.pi)
print(math.e)

#task:Area of a circle
# import math
# r = float(input())
# p=math.pi
# print(p*r*r)

#Random builtin methods
#used for random values
import random
print(random.randint(1,100))

#choice()
fruits=["Apple","Banana","Mango"]
print(random.choice(fruits))

# random()-->0.0 -1.0
print(random.random())

#shuffle()
cards=[1,2,3,4]
random.shuffle(cards)
print(cards)

#Task: build the dice simulator
import math
print(random.randint(1,6))

#date
import datetime
print(datetime.date.today())

#custom date
d=datetime.date(2026,9,22)
print(d)

# build the age calculator
import datetime
currentyr=datetime.date.today().year
birthyr=2005
print(currentyr-birthyr)