#divisible by 5
#if any number is given by user check whether the number is divisible by 5

a=int(input("Enter the number"))
if a%5==0:
    print("divisible by 5")
else:
    print("not divisible  by  5")    
    
#Leap year
#1.divisible by 400 or 4
#and should not divisible by 100

a= int(input("Enter the number"))
if a%400==0 or a%4==0 and a%100!=0:
    print("Leap year") 
else:
    print("Not a leap year")          