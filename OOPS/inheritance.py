'''
what is inheritance?
a mecha ism where one class acquires the properties and methods of another class
                      or
one class reuses the features of another class

Simple understandinng:

a child class can

use variables
use methods
of parents class without
rewriting the code           
Example:
vechicles:
car,bike,bus

all vechiles have
start(),stop()
No need to repeated code
write code once
|
use num of times

Advantages or why?
1.Code reusability
2.Reducing the code duplication           
3.Better organization
4.Easy maintenance

Terms:
parent:Base or super class
child:sub class/derrived class
   
         parent
            |
         child
'''
#syntax:
# class Parent:
#     pass
# class Child(Parent):
#     pass

# #basic example:
# class Animal:
#     def eat(self):
#         print("Animal is eating")
# #child class
# class Dog(Animal):
#     pass

# d1=Dog()
# d1.eat()       

'''
Dog class does not contains eat() 
            |
python seaches in animal class
            |
method is found and executed
'''
#No Inheritance

# class Dog:
#     def eat(self):
#         print("eating")
# class Cat:
#     def eat(self):
#         print("eating")

#with inheritance
# class Animal:
#     def eat(self):
#         print("eating")
# class Dog(Animal):
#     pass
# class Cat(Animal):
#     pass
# c1=Cat()
# c1.eat()

#accessing the parent variables
# class Person:
#     def __init__(self):
#         self.name="Glory"
# class Student(Person):
#         pass
# s1=Student()
# print(s1.name)
'''
Type of inheritance in python
1.Single inheritance
2.Multiple inheritance
3.Multilevel inheritance
4.Hierarichal inheritance
5.Hybrid Inheritance

1.Single inheritance:
one child class inherits from one parent class
         parent
           |
        child
'''
#example:
# class Animal:
#      def eat(self):
#           print("eating")
# class Dog(Animal):
#      def bark(self):
#           print("Barking")
# d1=Dog()
# d1.eat()
# d1.bark()  
'''
2.multiple inheritance:
one child class inherits from multiple parents
            parent1     parent2
                 \      / 
                  child
            

'''
# #example:
# class Father:
#     def money(self):
#         print("Fther's money")
# class Mother:
#     def gold(self):
#         print("Mother's gold")
# class Child(Father,Mother):
#     pass
# c1=Child()
# c1.gold()
# c1.money()  

'''
#Multilevel inheritance
Inheritance chain of multiple level
             GrandParent
                  |
               parent
                  |
                child
'''
# class Grandparent:
#     def house(self):
#         print("Grand parents house")
# class Parent(Grandparent):
#     def car(self):
#         print("Parents car")
# class Child(Parent):
#     def bike(self):
#         print("child's bike")
# c1=Child()
# c1.house()
# c1.car()
# c1.bike()
'''
4.Hierarichal inheritance

Multiple child classes inherit from one parent
               parent
                /   \
            child1  child2

'''
# class Animal:
#     def eat(self):
#         print("Eating")
# class Dog(Animal):
#     def bark(self):
#         print("Barking")
# class Cat(Animal):
#     def meow(self):
#         print("meow")
# c1=Cat()
# c1.eat()        
'''
5.Hybrid inheritance:
two or more inheritancetypes:
1,hierarchial and multiple
           A
          /  \
        B     C
        \     /
           D
'''
# class A:
#     def show_a(self):
#         print("Class A")
# class B(A):
#     def show_b(self):
#         print("Class B")
# class C(A):
#     def show_c(self):
#         print("Class C")
# class D(B,C):
#     def show_d(self):
#         print("class D")
# d1=D()
# d1.show_a()
# d1.show_b()
# d1.show_c()
# d1.show_d()             

#Check the inheritance
# class Animal:
#     pass
# class Dog(Animal):
#     pass
# c1=Dog()
# print(isinstance(c1,Dog))
# print(issubclass(Dog,Animal))  
# class Parent:
#     def __init__(self):
#         print("constructor called")
# class Child(Parent):
#     pass
# c1=Child()

'''
1.methods
2.variables
3.constructor
'''
'''
problem-1
create a parent class Animal
with method sound()
that should print
Animal makes sound

Create a child class Dog()
that inherits the Animal
create object of Dog and call that inherits the Animal
'''
# class Animal:
#     def sound(self):
#         print("Animal makes sounds")
# class Dog(Animal):
#     def show(self):
#         print("dog barks")
# d=Dog()
# d.sound()                

'''
problem:2
student and college
create a parent class college
class var-->college name
create a child class student with:
instance var-->student_name
display
1.college_name
2.student_name
'''
# ''''''class College:
#     college_name="CITY"
# class Student(College):
#     def __init__(self,student_name):
#         self.student_name=student_name 
#     def display(self):
#         print(self.college_name)                      
#         print(self.student_name)
# s=Student("Mouni")
# s.display()        

'''
problem-3
create:
vehicle class with method start()
car class inheriting vechicles
sportscar class inheriting the car
add method:
speed()
inside the sports car:
call:
start()
speed()
using sportscar object
'''
# class Vechicle:
#     def start(self):
#         print("start")
# class Car(Vechicle):
#     pass
# class Sportscar(Car):
#     def speed(Self):
#         print("sportscar is too speed")
# s=Sportscar()
# s.start()
# s.speed()                   

'''
problem-4
Employee skills system
create:
class programmer with method coding()
class desinger with method designing()
create a child class employee inheriting
both classes
call both methods using employee objects
'''
# class Programmer:
#     def coding(self):
#         print("coding")
# class Designer:
#     def designing(self):
#         print("I am a designer")
# class Employee(Programmer,Designer):
#     pass
# e1=Employee()
# e1.coding()
# e1.designing()    

'''
problem-5
Employee Bonus Mgmt
A company wants to calc
yearly bonuses for 
different types of employees 

create a base class Employee:
with:
name , salary 
create method:
calculate bonus()

then create two child classes 
developer
Bonus = 20% of salary 
manager 
Bonus = 35% of salary 
write a program to:
1.Take employee details as input
2.create objects based on employee type
3.Display:
employee name 
role
Bonus amount 

input format:
role,name,salary

output format:
Name:<name>
Role:<role>
Bonus:<bonus>

Sample:
3
Developer Rahu1 50000
Manager   Sneha 80000
Developer Arjun 60000

output:
Name:Rahul
Role:Developer
Bonus:10000.00
'''
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def calculate_bonus(self):
#         return 0
# class Developer(Employee):
#     def calculate_bonus(self):
#         return self.salary*0.20
# class Manager(Employee):
#     def calculate_bonus(self):
#         return self.salary*0.35
# n=int(input())
# employees=[]
# for _  in range(n):
#     role,name,salary=input().split()
#     salary=int(salary)
#     if role=="Developer":
#         emp=Developer(name,salary)
#     elif role=="Manager":
#         emp=Manager(name,salary)
#     employees.append((role,emp))
# for role,emp in employees:
#     print(f"Name:{emp.name}")
#     print(f"Role:{role}")
#     print(f"Bonus:{emp.calculate_bonus()}")
#     print()
'''
online course access sytem
an online learning platfom provdes
different level of course access
create a parent class course with : 
---> Student_name
create a method :
access_level():
then create two child classes 
---> freecourse
Access level = "Limited Access"
write a program :
1.accepts student details
2.create objects using inheritance
3.print student access information

input :
course_type,st
sample :
4
Free Amit
premium Neha
Free Rohan
Premium Rakesh

output:
Student : Amit
Course_type:Free
Access : Limited Access
'''
class Course:
    def __init__(self,Student_name):
        self.Student_name=Student_name
    def access_level(self):
        return "No Access"
class FreeCourse(Course):
    def access_level(self):
        return "Limited Accesss"
class PremiumCourse(Course):
    def access_level(self):
        return "Full Access"
n=int(input())
students=[]
for _  in range(n):
    course_type,name=input().split()
    if course_type=="Free":
        student=FreeCourse(name)
    elif course_type=="Premium":
        student=PremiumCourse(name)
    students.append((course_type,student))
for course_type,student in students:
    print(f"Name:{student.Student_name}")
    print(f"Course_type:{course_type}")
    print(f"Access:{student.access_level()}")
    print()
    
     
        
