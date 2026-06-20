#Decision makinng ability
#Control flow decides
#!. how many times to execute what to execute

#human anology:
'''
if it rains --> take umberlla
if marks is >40-->pass
if password correct-->login
'''

#program also needs ddecision making ability
#control flow: determines
#which statement to execute and in what order
'''
3-Types of control flow
1.Sequential : Top to Bottom
2.Conditional: decision making
3.Looping: Repeatiion
'''
#if 
#Syntax:
#if condition:
 #  statements
 
 #example:
age =21
if age > 20:
     print("Eligible")
     
'''
Execution flow
        condition true?
               |
        Execute the block

''' 
x = 10
if x>5:
    print("Hello")

#if-else:what if state becomes false

'''
Execution flow:
      condition?
      /       \
      True    False
       |        |
       Even    Odd

'''
#elif ladder
#Multiple conditions: multiple decisions

#if condition:
   #statement
#elif condition-2:
#    statement
#else:
#    statement

#Task:build a student gradinng system

a = int(input("enter the number"))
if a>=90:
    print("grade A")
elif a>=80:
    print("grade B")
elif a>=60:
    print("grade C")
elif a>=50:
    print("grade D")
else:
    print("Fail")

   
    
    






