'''
what is abstraction?
hiding the internal implementation details
showing the essential features to the user
            or
what operation is done ?
But not:
how operstion is working internally
-->complexity is hidden form the user

what use abstraction?
1.reduces the complexity
2.improvers the security
3.better maintenance
4.cleaner code 
5.standardization

#Abstraction in python:
Python supports abs using:
abstract classses
abstract methods

#ABC Module
ABC--Abstract Base Class

Abstract class
blueprinnt of a class
cannot create objects directly

#defines basic common structure

abstract can have:
1.abs methods
2.normal methods

#Abs Method
Methods declared but:
    implementation not provided
child class must implement it

Example:
vechile
->start()    
'''
#ABC -->Abstract Base Class
# from abc import ABC,abstractmethod
# #abstract class
# class Vehicle(ABC):
#     #abstract method
#     @abstractmethod
#     def start(self):
#         pass
# class Car(Vehicle):
#     def start(self):
#         print("Car started")
# c1=Car()
# c1.start()

# #Example-2
# from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#       print("dog barks")
# d1=Dog() 
# d1.sound()  

# #multiple abstract methods
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
# class Rectangle(Shape):
#     def area(self):
#         print("Area Formula")
#     def perimeter(self):
#         print("Perimeter formula")
# r=Rectangle()
# r.area()
# r.perimeter() 

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
#     #normal method
#     def sleep(self):
#         print("sleeping")
# class Dog(Animal):
#     def sound(self):
#         print("bark")
# d2 = Dog()
# d2.sound()
# d2.sleep()    
        
        
#Payment system:
#pay()
# class PaymentGateway(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
# class Phonepe(PaymentGateway):
#     def pay(self):
#         print("Paid using phonepe")
# class Paytm(PaymentGateway):
#     def pay(self):
#         print("Paid using paytm")
# pp=Phonepe()
# pt=Paytm()
# pp.pay()
# pt.pay()   

'''
TAsk:create an abstarct class paymentgateway
with two abs methods
1.pay
2.refunf
but amount--:param
create child class implementation
1.creditcardpay
2.UPI pay
'''
# from abc import ABC, abstractmethod
# class paymentgateway(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass
#     @abstractmethod
#     def refund(self, refund):
#         pass
# # Child 1
# class creditcardpay(paymentgateway):
#     def pay(self, amount):
#         print(f"pay {amount} using credit card")
#         def refund(self, refund):
#             print(f"refund {refund} using credit card")
# # Child 2
# class UpiPay(paymentgateway):
#     def pay(self, amount):
#         print(f"pay {amount} using UPI")
#         def refund(self, refund):
#             print(f"refund {refund} using UPI")
# c1 = creditcardpay()
# c2 = UpiPay()
# c1.pay(5000)
# c2.refund(6000)                

'''
Create an abstract class Employee
with abs methods:
calculate
'''
from abc import ABC, abstractmethod 

class Employee(ABC):
    @abstractmethod
    def calaculate_salary(self):
        pass
#child 1
class FullTimeEmployee(Employee):
    def calaculate_salary(self):
        return 50000
class partTimeEmployee(Employee):
    def  __init__(self,hour):
        self.hour = hour
    def calaculate_salary(self):
        return self.hour*500
c1 =FullTimeEmployee()
c2 = partTimeEmployee(40)
print(c1.calaculate_salary())
print(c2.calaculate_salary())

'''
Food delivery system:
create an abstract class restaurtant
with methods:
prepare_food()
delivary_time()
 create  child  classes:
 1.Pizzashop
 2.BurgerShop
 display:
 food preparation message
dleivery_time()
'''

