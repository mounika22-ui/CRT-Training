'''
problem:23
print the elements greater than previous elements
input:2 5 3 8 6
5>2--->yes
3>5--->no
8>3--->yes
6>8--->no
output:5,8
'''
# n=int(input())
# l=list(map(int,input().split()))
# for i in range(1,n):
#     if l[i]>l[i-1]:
#         print(l[i],end=" ")
        
'''
problem-24
count the multiples of 3
'''
# n=int(input())
# l=list(map(int,input().split()))
# count=0
# for i in range(n):
#     if l[i]%3==0:
#         count+=1
# print(count)            

'''
problem-25
find the absolute diff blw first and last element in a list
input:[10,25,-30,-40]
output:10-(-40)
'''
# n=int(input())
# l=list(map(int,input().split()))
# s=abs(l[0])-abs(l[-1])
# print(abs(s))

'''
problem-26
elements which appears only once 
input:[1,2,2,3,4,4]
output:[1,3]
'''
# n=int(input())
# l=list(map(int,input().split()))
# count=0
# for i in l:
#     if l.count(i)==1:
#         print(i,end="")
'''
problem-27
move all the negative numbers to the left given a list of integers ,move all the negative to the beginning of the list
note:maintain the order
'''
# l=list(map(int,input().split()))
# negative=[]
# positive=[]
# for i in l:
#     if i<0:
#         negative.append(i)
#     else:
#         positive.append(i)
# result=negative+positive            
# print(*result)                 #unpacking of list
'''
find the frequency of the element
ex:
input:[1,2,2,3,3,3]
output:[1,2,3]
'''
    
# n=int(input())
# l=list(map(int,input().split()))
# freq = {}
# for i in l:
#     if i in freq:
#         freq[i]=freq[i]+1
#     else:
#         freq[i] = 1       
# print(*freq.values()) 
'''
rotate list by k positions 
given a list and k integer, rotate the list to the left by k positions
examples:input[1,2,3,4,5]
k=2
output=[3,4,5,1,2]
'''
# n=int(input())
# l=list(map(int,input().split()))
# k=int(input())
# k=k%n
# for i in range(k):
#     last=l[-1]
#     for j in range(n-1,0,-1):
#         l[j]=l[j-1]
#     l[0]=last
# print(*l)
#using slicing
# n=int(input())
# l=list(map(int,input().split()))
# k=int(input())
# k=k%n
# result=l[-k:]+l[:-k]
# print(result)
#using built in function
# n=int(input())
# l=list(map(int,input().split()))
# k=int(input())
# k=k%n
# for i in range(k+1):
#     first=l.pop(0)
#     l.append(first)
# print(l)
'''
Operations:
swapping
Moves towards the center
arr=[1,2,3,5,7,10,11,15]

1+2-->3
1+3-->4
1+5-->6 upto 1+15-->16
'''
# n=int(input())
# l=list(map(int,input().split()))
# target=15
# for i in range(len(l)):
#     for j in range(len(l)):
        
#         if l[i]+l[j]==target:
#             print(l[i],l[j])

# arr=[1,2,3,5,7,10,11,15]
# n=len(arr)
# target=15
# for i in range(n):
#     for j in range(i+1,n):
#         current_sum=arr[i]+arr[j]
#         if current_sum==target:
#             print("pair found",current_sum) 
#2-pointer