#Take 3 sides from user and check
#whether triangle is
#1.Isosceles
#2.Equilateral
#3.Scalene

a= int(input("Enter the side"))
b= int(input("Enter the side"))
c= int(input("Enter the side"))
if a==b==c:
    print("It is a Equilateral Triangle")
elif a==b or b==c or a==c:
    print("It is a Isosceles Triangle")  
else:
    print("It  is a Scalene Triangle")
       