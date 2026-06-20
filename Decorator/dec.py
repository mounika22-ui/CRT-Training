'''
Decorators :
adds the extra functionality 
without changing  the original function
gift wrapper :
      wrappper adds :
      extra layer ,beauty
decorator=wrapped around the function

      # why decorators are needed ?
      logging :
      authentication ,
      timing
      validation
if no decorators
1.repeated code
2.messy programs
         
         
'''      
def greet():
    print("hello students")
#in python -- functions are treated as life variables

def greet():
    print("hello students")
x=greet
x()

#nested functions
def outer():
    def inner():
        print("Inner side") 
    return inner()       
x=outer
x() 

'''
outer()called
|
returns the inner
|
stored iin  x
|x()-->executes inner
'''
#simple decorator
def decorator_function(original_function):
    def wrapper():
        print("Before function call")
        original_function()
        print("After function call")   
    return wrapper
#original function
def greet():
    print("Hello students")

#apply manually
decorated=decorator_function(greet)
decorated()        
'''
greet()
|
decorator_function()
|
wrapped created
|
# extra functionality is added 


# specail symbol , @



# '''

# @decoration_function
# def greet():
#     print("Hello students")
# example 2 :
def smart_divide(func):
    def wrapper():
        print("Checking before div")
        func()
        print("Division is completed " )
    return wrapper
@smart_divide
def divide():
    print(10/2)

#example:3
def decorator_function(original_function):

    def wrapper(name):
        print("Before function call")
        original_function(name)
        print("After function call")
    return wrapper
@decorator_function
def greet(name):
    print("hello",name)
greet("megha")

#timer decorator
import time 
def timer(func):
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        print("Execcution time ",end-start)
    return wrapper
@timer
def test():
    for i in range(10000):
        pass
test()

#Example:2
def login_required(func):
    def wrapper():
        func()
    return wrapper 

@login_required
def dashboard():
    print("Welcome to dashboard")

