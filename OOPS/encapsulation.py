'''
what is encapsulation?
binding data and methods together into a single unit

And:
restricting direct access to data 

Encapsulation protects the data from
1. unauthorized access
2. accidental modifications

similarly in oops:
data is hidden inside the class accessed using methods

key-idea:
data+methods
   |
combined into a single unit 
      |
controlled access 

Features of encapsulation:
1.security
2.data hiding
3.controlled access
4.Better maintenance
5.Better organization

'''
#no encapsulation
# balance=50000
# balance=-50000

#encaplsulation
# class Bank:
#     def __init__(self):
#         self.balance=10000

#     def deposite(self,amount):
#         self.balance+=amount

#     def show_balance(self):
#         print(self.balance)

# b1=Bank()
# b1.deposite(5000)
# b1.show_balance()  #data and methods are bound together
    
#data hiding
#restricting access to direct variables
'''

goal:prevent data modifications
misuse of data

access mofifiers in python:
1.public:default
2.protected:_single_ underscore
3.private:__double_underscore



'''
#1.:public:members can be accessible every where
#default access type in python

# class Student:
#     def __init__(self):
#         self.name="megha"

# s1=Student()
# print(s1.name)

'''
accessed anywhere
no restriction
default behaviour
'''

#protected:_single_underscore
#should no be accessed directly outside the class

# class Student:
#     def __init__(self):
#         self._marks=90
# s1=Student()
# print(s1._marks)
'''
python protected members are not exactly protected

_marks:protected by convention

please dont access it directly

where to use?
1.during inheritance
2.for internal usage

'''
'''
Private:__underscore

used for :strong data hiding
'''
# class Student:
#     def __init__(self):
#         self.__marks=90

# s1=Student()
# print(s1.__marks)  #cant access out of the class 

#reason:Name Mangling:
# __marks
#    |
# _Student__marks
'''
prevent:
accidental direct access
acciddental overriding

'''
#can i access private var inside the class ? yes u can
# class Student:
#     def __init__(self):
#         self.__marks=90
#     def show(self):
#         print(self.__marks)
# s1=Student()
# s1.show()# accessed within the same class

# #try to access using name mangling
# class Student:
#     def __init__(self):
#         self.__marks=90
# s1=Student()
# #i am using name mangling to access
# print(s1._Student__marks)

'''
self.__marks
     |
python will convert
      |
self._student__marks

'''
'''
Access modifiers           | syntax        | accessible outside
1.Public                     variable           yes
2.protected                  _variable        yes(convention only)
3.private                   __variable        no (directly)

#Task:create a class named "BankAccount"
#balance-->private
#deposite
#withdraw amount
#check for balance
#print balance using name mangling
'''
# class BankAccount:
#     def __init__(self):
#         #private variable
#         self.__balance=50000
#     def deposite(self,amount):
#         self.__balance+=amount
       
#     def withdraw(self,amount):
#         if amount<=self.__balance:
#             self.__balance-=amount
#         else:
#             print("insufficient amount")
#     def show_balance(self):
      
#         print(self.__balance)
# b=BankAccount()
# b.deposite(500)
# b.withdraw(200)
# b.show_balance()
# print(b._BankAccount__balance)

'''
Getters and setters:
getters-->read the data
setters-->modify/update the data

#why use?
student.marks=-90
no validation

'''
#without getters and setters
# class Student:
#     def __init__(self):
#         self.marks=90        
# s1=Student()
# s1.marks=-50  #accepted
# print(s1.marks)

# #using getters and setters
# class Student:
#     def __init__(self):
#         self.__marks=90
#     #getter method
   
#     def get_marks(self):
#         return self.__marks
#     #setter method
    
#     def set_marks(self,value):
#        if value>=0:
#           self.__marks=value
#        else:
#            print("invalid marks")

# b1=Student()
# print(b1.get_marks())
# b1.set_marks(95)
# print(b1.get_marks())
# b1.set_marks(-95)
# print(b1.get_marks())

#task :create a class BankAccount
#create getter for returning balance
#create setter for updating balance
#amount>=0

# class BankAccount:
#     def __init__(self):
#         self.balance=50000
#     def get_balance(self):
#         return self.balance
#     def deposite(self,amount):
#         self.balance+=amount
#     def set_withdraw(self,amount):
#         if amount<=self.balnace:
#             self.balance-=amount
#         else:
#             print("insufficient amount")
# b1=BankAccount()
# b1.get_balance   

    
'''
obj.setmarks
obj.getmarks


'''
# class Student:
#     def __init__(self):
#         self.__marks=90
#     #getters
#     @property
#     def marks(self):
#         return self.__marks
#     @marks.setter
#     def marks(self,value):
#         if value>=0:
#             self.__marks=value
#         else:
#             print("invalid marks")
# s1=Student()
# print(s1.marks)
# s1.marks=-50
# print(s1.marks)

'''
Student marks validator
Create a class Student:
Requirements:
Private var-->__marks
method set_marks(marks)
method get_marks()
rules:
Marks must be btw 0-100
otherwise print
invaild marks
Example:Input[85]-->85
            -104-->invaild marks
            205-->invaild marks
'''            
# class Student:
#     def __init__(self):
#         self.__marks=0
#     def set_marks(self,marks):
#         if 0<=marks<=100:
#             self.__marks=marks
#         else:
#             print("invalid marks")
#     def get_marks(self):
#         return self.__marks
# marks = int(input())
# s = Student()
# s.set_marks(marks)
# if 0 <= marks<=100:
#     print(s.get_marks())
    
'''
Employee salary manager
create a class named as employee
Requirements:
1.private var- __salary
2.salary should not be<15000
3.method  increase_salary(percent)

if invalid:
invalid salary
input:20000
'''
# class Employee:
#     def __init__(self):
#         self.__salary=0
#     def set_salary(self,salary):
#         if salary>=15000:
#             self.__salary=salary
#         else:
#             print("invalid salary")
#     def get_salary(self):
#         return self.__salary
#     def increase_salary(self, percent):
#         self.__salary += self.__salary * percent / 100    
# salary= int(input())
# percent=int(input())
# e = Employee()
# e.set_salary(salary)
# if salary>=15000:
#     e.increase_salary(percent)
#     print(e.get_salary())    
    
'''
password manager
create a class passwordmanager:
rules:1.minimum 8 character
2.one upper case
3.one lower case
4.one digit

if invaild 
weak password
else:
password set sucessfully
example:
input:"Mounika22"
output:password set succesfully
'''
# class PasswordManager:
#     def set_password(self,password):
#         upper=False
#         lower=False
#         digit=False
#         for ch in password:
#             if ch.isupper():
#                 upper=True
#             elif ch.islower():
#                 lower=True
#             elif ch.isdigit():
#                 digit=True
#         if len(password)>=8 and upper and lower and digit:
#             print("password set successfully")
#         else:
#             print("weak password")
# password=input()            
# p = PasswordManager()
# p.set_password(password)
    
'''
problem-4
e-Commerce shopping cart
Create a class Shopping cart
features:
1.private var- __total
2.add items
3.remove the items
4.apply discount

rules:
1.total should never become zero
2.discount only if total>1000
methods:
1.add_items(price)
2.remove_items(price)
3.apply_discount(percent)
4.get_total()
'''
class ShoppingCart:
    def __init__(self):
        self.__total=0
    def add_items(self,price):
        self.__total +=price
    def remove_items(self,price):
        if self.__total-price>0:
            self.__total -=price
        else:
            print("total should never become zero")
    
 
            
            
    