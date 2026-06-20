'''
OOPS:Object oriented programming (paradigm)

programs are organized using objects
objects contains:
1.data(variables)
2.behaviour(finctions/methods)

OOP not only focuses on functions but also real world entities

car->Object
student->object

Each object here:
will have properties and actions
              |              |
            variables       methods

Earlier the programming was written without oops

1.diificult to manage the large level projects
2.code duplication
3.less security
4.difficult maintenance

OOPs will sole the above problems :
1.classes
2.objests
3.encapsulation
4.Inheritance
5.Abstraction
6.polymorphism
'''

#procedural programming
# name="Ramya"
# marks=30
# def display():
#     print(name,marks)

# display()

#OOP approach:

# class Student:

#     def __init__(self,name,marks):
#          self.name=name
#          self.marks=marks
#     def display(self):
#         print(self.name,self.marks)

# #object
# s1=Student("megha",90)
# s1.display()

#data+functions-->
'''
advantages:
1.code reusability
2.better organization- modular and structure
3.security->encapsulation
4.easy maintenance:update,debug
5.real world modelling
6.scalability : large applications 

      full stack:frontend+backend+db
      mern stack--:
      m:mongodb-->db
      e:express-->framework
      r:react-->frontend
      n:node-->runtime environment

      frontend:html,css,js,react js
      backent:python,js,node,node+express
      database:Mysql,postgresql,oracle,mongodb
      python-flash,django,fastapi,streamlit(minimal interface),gradio
      
'''
'''
class:Blue print of an object
collection of variable and methods ??

blueprint: can be used to build many houses



'''
# class ClassName:
#     pass
'''
class:keyword creates class
classname:identifiers
pass:empty block
'''
#object:instance of a class
        #or
#actual memory representation of class

# class Student:
#     pass
# #create an object
# obj=Student()
# print(obj)

'''
obj-->instance name(object)
student-->class name
'''
# class Car:
#     brand="Audi"
#     #self refers to the current object
#     def start(self):
#         print("class started")
#create objects:
#both objects has different memory locations
# c1=Car()
# c2=Car()
# c1.start()
# c2.start()
# print(c1.brand)
# c1.brand #class-->obj searches for brand inside the class

#task:create a class named as employee
#create two var company name and name_emp
#create two methods to access name and comp_name
#create two objects and access var and methods
# class Employee:
#     cmp_name="CITY"
#     emp_name="manoranjan"
#     def name(self):
#         print("the company name is :",self.cmp_name)
#     def emp(self):
#         print("the employee name is:",self.emp_name)
# e1=Employee()
# e2=Employee()
# print(e1.cmp_name)
# print(e2.emp_name)
# e1.name()
# e2.emp()
# print(e1)
# print(e2)

'''
construstor:__init__()
special method 
automatically called when object is created

used: initializing the object data 
'''
class Student:
    def __init__(self):  #constructor
        print("constructor is called")
s1=Student()

'''
Student()
|
object created
|
__init__ automatically called

If no constructor
manually assign the value

if yes
automatic initialization

'''
# if no constructor
# manually assign the value   

# class Student:
#     pass
# s1=Student() 
# s1.name="megha"
# s1.branch="CSE"

#example with constructor

# class Student:
#     def __init__(self):
#         self.name="megha"
#         self.age=20
# obj1=Student()
# print(obj1.name)
# print(obj1.age)
'''
self-->current object(obj1)
self-->obj1


#constructor with parameters


'''
class Student:
    #constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj2=Student("megha",20)
print(obj2.name)
print(obj2.age)
'''
self-->obj2
name:"megha"
age:20

obj2_____
name="megha"
age=20

step by step
1.object memory allocated
2.__init__ is called automatically
3.self points to object
4.variables initialized
5.object returned

'''
'''
#default constructor
class Test:
    def __init__(self):
        print("default contructor")
t=Test()
parameterized constructor

class Test:
    def __init__(self,x):
      self.x=100
t=test()

constructor                 |   normal method
automatically called          manually called
name fixed:__init__              any name
used for initialization          used for operations
executes during object creation  execcutes when called


''' 
class Student:
    def __init__(self):
        print("constructor")
    #normal method
    def display(self):
        print("normal method")
c1=Student()
c1.display()
'''
Instance variables:
variables that belong to an object
seperate copy created for every object

They store:
object specific data
student  |name     |marks
s1        mouni      99
s2        kishore     98

each object stores its own data

'''
class Student:
    def __init__(self,name,marks):
        #instance variables
        self.name=name
        self.marks=marks

s1=Student("Mounika",99)
s2=Student("Kishore",98)
print(s1.marks)        
print(s2.marks)

'''
s1 object
---------
name="Mounika"
marks=99

s2 object
---------
name="Kishore"
marks=98

Objects do not store instance variables.
'''
class Student:
    def __init__(self,name,marks):
        #instance variables
        self.name=name
        self.marks=marks

    #instance method
    def display(self):
        print(self.name)
        print(self.marks)
s1=Student("Mouni",98)
s1.display()
'''
s1.display()
Student.display(self)
|
self ---> s

'''
'''
#dynamic object properties
adding the variables dynamically
class Students :
    pass
s1 = Student()
s1.name = "harii"
s1.age = 21
print(s1.name)

'''
'''
class variables  :shared among all the objects
      '''
class Student:
    #class Variable
    college_name  = "CITY"
    def __init__(self,Branch):
        #Instance variable
        self.Branch=Branch
#Normal Method
    def display(self):
        print(self.college_name)
s1=Student("cse")
s2=Student("csd")
print(s2.college_name) 
print(s1.college_name)

'''
self:refers to current object
          or
reference variable pointing to current object
'''
class Student:
    def display(self):
        print("hello")
s1=Student()
s1.display()
'''
s1.display()
|
student.display(s1)
|
self-s1(self points to s1)

'''
class Student:
    def show(self):
        print(self)
s1=Student()     
s2=Student()     
print(s1)
print(s2)
s1.show()

# s2.show()
'''
  student class
  -------------
  College=CITY  #stored in class memory
  -------------
     |     |
     s1    s2
class Employee:
     company="Google"
     def display(self):
         print(self.company)

e=Employee()
two ways access:
print(e.company)

#no object use
print(Employee.company)
'''
'''
#class methods
wprk with class variables
operate on class level data

@classmethod--decorator
'''
#Bsic example for class method
# class Student:
#     college="CITY"
    
#     @classmethod
#     def show_college(cls):
#         print(cls.college)

# Student.show_college()

'''
@classmethod:
decorator which tells python:
This method belongs to class not object


self->current object
cls-->current class
'''
#task:create a class named as employee
#create one class var
#use @classmethod to apply on method company_name
#print the company name
#using multiple objects
class Employee():
    name="Google"
    @classmethod
    def company_name(cls):
        print(Employee.name)
e=Employee()
e2=Employee()
e.company_name()
e2.company_name()

'''
diff between instance method  and class method
    instance method                |     class method
works on the object  data          |    works on class data
uses self                          |    cls - current class
 need object                       |     directly uses class
 access the instance var           |      access class variables 
'''
'''
class Student:
    college = "CITY"
    #instance method
    def instance_method(self):
        print("Instance method")
    #class method
'''
#Task:create a class named as student
#create constructor
#class variable
#instance variable
#instance method
#class method
#static method

class Student:
    #class var
    college="cITY"
    def __init__(self,name):
        self.name="Mouni"
        
        
        








    
       
        
        
        