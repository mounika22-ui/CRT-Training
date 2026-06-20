'''
what is polymorphism?
poly-->many
morphism-->forms
same method/operators will behave differnt behaviour

Example:
print(5+3)#8
print("Hello"+"world")#Hello world

      same operator
          |
    But different behaviours
types of polymirphism:
1.complie time 
2.Run time polymorphism

#complie time-- method overloading
#No method overloading in python 
Method overloading:
same method names
     +
different parameters

#*args-->var len arguments
#java-->add(int,int)
     -->addd(int,int,int)
python approach:
class Calculator:
     def add(self,a,b,c=0):
     print(a+b+c)
c1=calculator()
c1.add(10,20)
c1.add(10,20,30)          

#Run time polymorphism:
--->method overriding
'''
class Bird:
    def fly(self):
        print("Bird Flying")
class Eagle(Bird):
    def fly(self):
        print("Eagles is flying")
e1=Eagle()
#method is chossen during run time
e1.fly()
#duck typing in python

                