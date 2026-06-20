#largest of 4 numbers:
#logical operators and conditionals

a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
d=int(input("Enter the number:"))
if a>=b and a>=c and a>=d:
    print("a is larger")
elif b>=c and b>=a and b>=d:
    print("b is larger") 
elif c>=d and c>=a and c>=b:
    print("c is larger")
else:
    print("d is larger")  
    
#Task: Write the Pseudocode for above

'''
START
Input a,b,c,d
IF a is largest
    Dispaly a
ELSE IF b is largest
    Dispaly b
ELSE IF c is largest
    Display c
ELSE 
    Display d
END                
'''
           
#Truly or Falsy statements
if 0:
    print("hello")    
# It will not execute

#Short circuit evaluation

if True or 10/0:
    print("safe")

#No -error and print safe
if True:
    print("hello")    