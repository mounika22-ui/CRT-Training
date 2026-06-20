'''
what is function?
function is a block of reusable code. performs specific tasks

why functions?
1. avoid repetition
2.improves readability
3.easy debug
4.modular programming

#function definition

def function_name(parameters):
    """Doc strings"""--->it is a type of comment in functions
    statements
    return value


    def-->keyword
    function_name-->identifiers
    parameters-->input(passed inside the function)
    return-->output

#function calling:executing the code

function name()

functions are         two types
                      /       \
                built IN     userdefined functions

BuitIN functions: which are already defined
example: print()
input()
sum()
mean()
max()
user defined functions: we will create oue logic as per our requirement
 
'''
#create a function
# def hello():
#     print("Hello World")

# #call the function
# hello()

#parameters:variable passed during the function definition
# def add(a,b):#a,b are parameters
#     print(a+b)

#arguments = values passed during the function call
#calling the functions
# add(2,3)#2,3-->arguments

'''
types of arguments:
1.positional arguments:
arguments passed in order

ex:
def muliply(a,b):
    return a*b

#call the function
mulptiply(2,3)

task:create a function to calculate
simple interest using positional args (ptr/100)
'''

# def interest(p,t,r):
#     print((p*t*r)/100)
# interest(2,3,5)
'''
2.keyword arguments:no need of order
'''
#keyword arguments
# def sub(a,b):
#     return a-b
# sub(b=5,a=10)#no order
# #task : call the simple interest fun using keyword arguments
# def interest(p,t,r):
#     print((p*t*r)/100)
# interest(p=2,r=3,t=5)

'''
3. default arguments:used when value is not provided

example:
def student(name="megha"):
    print(f"student name is {name}")


'''
# def student(name,branch="CSE"):
#     print(f"student name is {name} and branch is {branch}")
# student("Rajesh")

#task: creat a function to cal squares by default parameters
# def squares(a,b=2):
#     print(a**b)
# squares(3)
'''
4.variable length arguments

def total(*args):
    print(args)
#call the function
total(10,20,30,40)

'''
# def total(*args):
#     print(args)
#     print(sum(args))
# #call the function
# total(10,20,30,40)
#task:create a function to find the sum of any no of values
# def total(*args):
#     print(sum(args))
# total(1,2,3,4)

'''
5.keyword arguments(kwargs)
def student_details(**kwargs):
    print(kwargs)
student_details(name="megha",branch="CSE",roll=9)

'''
# def student_details(**kwargs):
#     print(kwargs)
# student_details(name="megha",branch="CSE",roll=9)
# #task:create a function to print employee details
# def employee_details(**kwargs):
#     print(kwargs)
# employee_details(name="megha",department="production",employee_id=9)
#task: write args and kwargs together 
# def together(*args,**kwargs):
#     print(args,kwargs)
# together(10,20,30,name="megha",department="production",employee_id=9)

'''
return statement:send the value back to caller

def add(a,b):
    return a+b

result=add(10,20)
print(result)

print                     return
display the output        send the value
cannot reuse              can reuse

multiple return values:

def calculate(a,b):
    return a+b,a-b,a/b

format:tuple 

s,sub,div=calculate(20,30)
'''
# def calculate(a,b):
#     return a+b,a-b,a/b

# #format:tuple 

# s,sub,div=calculate(20,30)
# print(s,sub,div)

#task: create a function that returns
#1.min 2.max 3.avg
# def function(a,b):
#     return min(a,b),max(a,b),((a+b)/2)
# small,large,avg=function(20,30)
# print(small,large,avg)

'''
#function doc strings

doc strings describes:
1.what function does
2.parameters
3.return value

def add(a,b):
    """This function add two numbers and returns results"""
    return a+b
'''
# def add(a,b):
#     """This function add two numbers and returns results"""
#     return a+b
# print(add.__doc__)
# print(help(add))

#task: write a docstring for the simple interest program
# def interest(p,t,r):
#     """ this function will find the interest and return results"""
#     print((p*t*r)/100)
#     print(interest.__doc__)
#     print(help(interest))
# interest(2,3,5)

'''
variable scope
local variable:
variables declared inside the functions

def test():
    x=100
test()

global scope:
variables declared outside the functions
x=200
def show():
    print(x)
show()

'''
# def test():
#     x=100 #local variable
#     print(x)
# test()

# x=200 #global variable
# def show():
#     print(x)
# show()

#accessing the local var outside the function

# x=0
# def update():
#     global x
#     x=x+5
# update()
# print(x)  #5 this tells that we can access local variable outside the code

#task: try without using the global and tell the error
# x=0
# def update():
#     x=x+5
# update()
# print(x)

'''
task:
create a function bank_transaction()
which accepts:
1.account holder(string)
2.balance
3.transaction_type(deposite/withdraw)
4.amount

use:
default args
return statements
global balance
print updated balance
'''
# balance=30000
# def bank_transaction(account_holder,transaction_type,amount,bank_name="xyz bank"):
#     global balance  #to modify balance
#     if balance==0:
#         print("Insufficient funds")
#     else:
#         if transaction_type=="withdraw":
#            print(f"{account_holder} updated balance=",balance-amount)
#         else:
#             print(f"{account_holder} updated balance=",balance+amount)
# bank_transaction("megha","deposit",10000)

'''
lambda function: is a small and anonymous function 
# function without name
# defined using lambda
can pass any number of args
can have only one expression 
return the value automatically(no return keyword)

normal function:
def add(a,b):
    return a+b
add(10,20)

#write using lambda 
add =lambda a,b:a+b
#calling the function
add(10,20)

#task: write a normal function to square of num convert the normal fun to lambda

''' 
#using normal function   
# def squares(a,b=2):
#     print(a**b)
# squares(3)

# #using lambda function
# print((lambda x:x*x)(5))

#max number in 2
#c-programming
#ternary: ? :
#python: a if a>b else b
# max_num=lambda a,b:a if a>b else b

'''

arr=list(map(int,input().split()))

#map(): applies the function each element of iterable


map(function,iterable)

example:
def square(x):
    return x*x
nums=[1,2,3,4]
result=list(map(square,nums))
print(result)

'''
# def square(x):
#     return x*x
# nums=[1,2,3,4]
# result=list(map(square,nums))
# print(result)

#using lambda
# nums=[1,2,3,4]
# result=list(map(lambda x:x*x,nums))
# print(result)
'''
task: given a list of numbers 
convert each number into cubes
using map() and lambda
'''
# nums=[1,2,3,4]
# result=list(map(lambda x:x**3,nums))
# print(result)

'''
what is filter?
selects the elements based upon the condition

syntax:
filter(function,iterable)

example:
def is_even(x):
    return x%2==0
list=[1,2,3,4,5]
result=filter(is_even,list)
print(result)
'''
# def is_even(x):
#     return x%2==0
# list=[1,2,3,4,5]
# result=list(filter(is_even,list))
# print(result)

#using lambda
# l=[1,2,3,4,5]
# result=list(map(lambda x:x%2==0,l))
# print(result)

#task:given with a list with frnds names
#filter the names letter starting with A
#use filter with lambda
# names=["Akanksha","Anu","Rajesh"]
# result=list(filter(lambda x:x.startswith("A"),names))
# print(result)

'''
what is reduce?
repeatedly applies function
reduces the iterable to single value

syntax:
reduce(function,iterable)
'''
#functools--->module
# from functools import reduce
# nums=[1,2,3,4,5]
# result=reduce(lambda a,b:a+b,nums)
# print(result)

#without using lambda
from functools import reduce
nums=[1,2,3,4,5]

result=reduce(lambda a,b:a+b,nums)
print(result)