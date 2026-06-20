'''
Method Overriding?
Redefining a parent class metthod inside the child class

-same method name
-same parameters

child class method changes the behaviour of parent class method
speak()
'''
# class Animal:
#     def sound(self):
#         print("Animal makes sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# d1=Dog()
# d1.sound()             

'''
Dog object calls sound()
    |
python will serches inside the dog class
    |
method found
    |
parent ignored

Animal
    sound()
    | overriding by
   Dog
     sound()

#important rule:methods names should be same

'''  
'''
super():super function

Accessing the parent class methods
'''
# class Parent:
#     def show(self):
#         print("Parent method")
# class Child(Parent):
#     def show(self):
#         #call the parent method
#         super().show()
#         print("child method")
# c1=Child()
# c1.show()

# class Parent:
#     def show(self):
#         print("Parent method")
# class Child(Parent):
#     def show(self):
#         print("Child method")
# class GrandChild(Child):
#     def show(self):
#         #call the parent method
#         super().show()
#         print("Grandchild method")
# c1=GrandChild()
# c1.show()
#is it possible to override the constructor?
# class Parent:
#     def __init__(self):
#         print("Parent constructor")
# class Child(Parent):
#     def __init__(self):
#         print("Child constructor")
# c1=Child()

# class Parent:
#     def __init__(self,name):
#         self.name=name
# class Child(Parent):
#     def __init__(self,name):
#         super().__init__(name)
#         print(self.name)
#         print("Child constructor")
# c1=Child("mouni")
# print(c1.name)    

'''
MRO:Method Resolution Order 
order in which python searches method
'''
class A:
    def show(self):
        print("class A") 
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
d=D()                
d.show()
print(D.mro())