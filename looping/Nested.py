'''
nested loop: loop inside the loop
first loop:outer loop--->row
second loop:inner loop--->coloumn
'''
# #Example:
# i=1
# while i<=3:
#     j=1
#     while j<=2:
#         print(i,j)
#         j=j+1
#     i=i+1  

'''
for loop:
for outer in range():
    for inner in range():
        #code
for every row:
    for every student in that row:
       #greet the student
How nested loop works usinng for:
for i in range(1,4):i=1
    for j in range(1,3):j=2
        print(i,j) print(1,1)(1,2)
                   print(2,1)(2,2)
                   print(3,1)(3,2)
                   
outer loop runs once
   Inner loop runs completely
outer loop runs twice
   Inner loop runs completely
   
why  nested loops are used?
1.Pattern problems
2.Matrix operations
3.Tables
4.Games
5.Grid system
6.Comparing the elements 

Task: square-star pattern 

****
****
**** 
****                   
'''
# for i in range(1,5):
    
#     for j in range(1,5):
#         print("*",end="")
#     print()    
# 
'''
    Example :
    *
    * *
    * * *
    * * * *
    * * * * *
'''
# for i in range(6):
#     for j in range(i):
#          print("*",end=" ") 
#     print()
    
#example:3 Number pattern

# 1
# 1 2 
# 1 2 3 
# 1 2 3 4
# 1 2 3 4 5

    
# for i in range(6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print() 

# '''
# * * * * * 
# * * *
# * *
# *
# '''
    
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print() 
    
    
#Example-5
# '''
# 1
# 2 2 
# 3 3 3 
# 4 4 4 4
# 5 5 5 5 5
# '''
# n=int(input())
# for i in range(6):
#     for j in range(5,i-1):
#             print(j,end=" ")
#     print()  

'''
Example-6
5 4 3 2 1
5 4 3 2
5 4 3 
5 4
5
'''

# n=int(input())
# for i in range(n):
#     for j in range(n,i,-1):
#         print(j,end=" ")
#     print()        
      
'''
A
B C
D E F
G H I J
'''
# n=int(input())
# for i in range(1,5):
#     for j in range(i):
#         print(chr(n),end=" ")
#         n+=1
#     print() 
'''
A B C D E
A B C D
A B C
A B 
A
'''
# n=int(input())
# a=int(input())
# for i in range(n,0,-1):
#     for j in range(i):
#         print(chr(a+j),end=" ")
#     print()                  


'''
Example:
1
1 3
1 3 5
1 3 5 7
'''
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         odd=2*j-1
#         print(odd,end=" ")
#     print()  
    
'''  
    *
   * *
  * * *  
 * * * *
* * * * *      

Rows  | Spaces |Stars
1       4        1
2       3        2
3       2        3       
'''  

n=int(input())
for i in range(1,n+1):
    
    #leading spaces
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    print()          
    
      
      
