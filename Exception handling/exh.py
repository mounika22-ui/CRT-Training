'''
Error:
an error is a problem in the program causing abnormal termination
1.Syntax error
2.Run tine error---->exception
--->occurs while executing the program

Example:
a=10
b=0
c=1a/b --->ZeroDivisionError

3.logic error:
program runs but gives wrong ouput
Example:
print(2*(3+5))

What  is exception handling?
Exception handling is a mechanism to handle run time errors gracefully without stopping the program

without exception:
1.program may crashes
2. poor user experince
3. data loss possible

with exception:
1.program will execute normally
2.proper error message
3.safer application

#Basic xception:
syntax:
keywords:try,catch,finally,raise,else

try:
    risky code
except:
    handlin code        
'''
#lets write our first program

# try:
#     num=int(input("Enter a number:"))
#     print(10/num)
# except:
#     print("Some error occcured")    
    
#Risky code will be inside try
#if exception occurs --->except exception
#above is not a good practice
#Hides actual problem
#diificulty to debug
# try:
#     num=int(input("Enter a number:"))
#     print(10/num)
# except ZeroDivisionError:
#     print("cannot divide with 0")
# except ValueError:
#     print("Input should not be string")
            
'''
Common python exceptions:
1.ZeroDivisionError--->Divide with 0
2.ValueError--->Invaild input
3.TypeError--->wrong datatype
4.IndexError--->Invaild Index
5.KeyError--->Ivaild dictionary key
6.FileNotFoundError--->File Missing
7.AttributeError--->Invaild Attribute
8.NameError--->Variable is not defined
'''
#Example:
# try:
#     lst=[10,20,30]
#     index=int(input("Enter the index:"))
#     print(lst[index])
# except IndexError:
#     print("Index out of range") 
# except ValueError:
#     print("Please enter integer")       
    
#Else: if no exception occurs 
'''
try:
    code
except:
    handling
else:
    success block        
'''
                
# try:
#     lst=[10,20,30]
#     index=int(input("Enter the index:"))
#     print(lst[index])
# except IndexError:
#     print("Index out of range") 
# except ValueError:
#     print("Please enter integer")    
# else:
#     print("No exception occured")       

#another example by using else

# try:
#     num=int(input("Enter number:"))
#     result=100/num
# except ZeroDivisionError:
#     print("Zero")
# else:
#     print(result)    
    
'''
finally block executes always
used for:
1.closing files
2.closing database connections
3.cleanup activities

try:
    code
except:
    handling
finally:
    cleanup code
'''
# try:
#     file=open("data.txt")
# except FileNotFoundError:
#     print("File not found") 
# finally:
#     print("Execution completed")           
        
#ATM Machine
# try:
#     print("transaction is processing")
# except:
#     print("transaction failed")
# finally:
#     print("Thanks for using atm")              

# try:
#     a=10/0
# except ZeroDivisionError as e:
#     print("error:",e)   
    
#Nested try blocks
# try:
#     print("outer try")
#     try:
#         num=int(input("Enter number:"))     
#         print(10/num)
#     except ZeroDivisionError as e:
#         print("Error:",e)
# except:
#     print("Outer Exception")       
    
#raise: used to manually
#generate exceptions

# age=int(input("Enter the age:"))
# if age<18:
#     raise ValueError("Age should be 18 or greater")
# print("Eligible")       

#why custom exceptions;

# class MyException(Exception):
#     pass

#Bank application:
# class  InsufficientBalance(Exception):
#     pass
# balance=5000
# withdraw=int(input("Enter the amount"))
# if withdraw > balance:
#     raise InsufficientBalance ("Not enough balance")
# print("Withraw succesful") 

#Task:
# class Panner(Exception):
#     pass
# panner=140
# eat=int(input("Enter the amount"))
# if eat>panner:
#     raise Panner("Not enough")
# print("Panner is avaliable")

#Student Result System
# class Student:
#     def __init__(self,marks):
#         self.marks=marks
#     def calculate_result(self):
#         try:
#             average=sum(self.marks)/len(self.marks)
#             print(average)
#         except ZeroDivisionError as e:
#             print("Error:",e)  
# s1=Student([])  
# s1.calculate_result()              

#login system:
# class LoginSystem:
#     def login(self,username,password):
#         try:
#             if username !="admin":
#                 raise ValueError("Invalid username")
#             if password !="admin123":
#                 raise ValueError("Invaild password")
#             print("Login succesful")
#         except ValueError as e:
#             print("Error:",e)
            
#Generic Exception:
try: 
    print(10/0) 
except Exception as e:
    print(e)                          
    
'''
Accept account balance
nd withdrawl amount
Raise Exception if:
1.withdrawl amount is -ve
2.withdrawl amount exceeds balance
3.withdrawl amount exceeds daily
limit pf 25000
display remaining balance
if transcation succesful
'''

# class InsufficientBalance(Exception):
#     pass
# class WithdrawlLimit(Exception):
#     pass
# class InvalidInput(Exception):
#     pass
# class ATM:
#     def __init__(self,balance):
#         self.balance=balance
#     def withdraw(self,amount):
#         try:
#             if amount<=0:
#                 raise InvalidInput("No negative")
#             if amount>25000:
#                 raise WithdrawlLimit("No more than 25000")
#             if amount>balance:
#                 raise InsufficientBalance("Insufficient ")
#             self.balance-=amount
#             print("Transaction is successful")
#             print("Balance:",self.balance)
#         except InsufficientBalance as e:
#             print(e)
#         except InvalidInput as e:
#             print(e)
#         except WithdrawlLimit as e:
#             print(e)
# balance=int(input())
# amount=int(input())
# obj=ATM(balance)
# obj.withdraw(amount)    

'''
A university wants to automate students result processing
The program should accept:
1.marks of 5 subjects
2.raise exception
if
1.marks are negative
2.marks exceed 100
3.non-numeric input
4.calculate average and grade

rules:
avg>=75 ->distiction
avg>=60 ->first class
avg>=40 ->pass

'''
# class InvalidMarksError(Exception):
#     pass
# class StudentResult:
#     def __init__(self):
#         self.marks=[]
#     def input_marks(self):
#         try:
#             for i in range(5):
#                 mark=int(input(f"Enter subject{i+1}marks")) 
#                 if mark<0 or mark>100:   
#                     raise InvalidMarksError("Marks should be between 0 and 100") 
#                 self.marks.append(mark)  
#             average=sum(self.marks)/5
#             print("Average:",average) 
#             if average >=75:
#                 print("Distintion")
#             if average>=60:
#                 print("First class")
#             if average>=40:
#                 print("Pass")
#             else:
#                 print("Fail")
#         except ValueError:
#             print("Only numerics are allowed") 
#         except InvalidMarksError as e:   
#             print(e) 
# obj=StudentResult()
# obj.input_marks()            


                     