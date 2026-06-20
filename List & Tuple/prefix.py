'''
Prefix sum:one of the most important technique
used to solve sub array problems
1.Fast range sum queries
2.Optimization
3.sliding window's alternative
4.sub array problems
5.competitive programming

if reduce the repeated calculations and
improves the time complexity

what is prefix sum?
stores the cumulative sum of the elements
from the beginninng of the array to every  index

arr=[a0,a1,a2,a3....]
then:
prefix[i]=arr[0]+arr[1]+arr[2]+.....arr[i]

problem:
arr=[2,4,1,7,3]
     0 1 2 3 4
find the sum from index 1-3
'''
# arr=[2,4,1,7,3]
# sum=0
# for i in range(1,4):
#     sum+=arr[i]
# print(sum)   
# #solve in brute force--->use pointers
# arr=[2,4,1,7,3]
# l=1
# r=3
# total=0
# for i in range(l,r+1):
#     total+=arr[i]
# print(total)   
'''
i=1 total=4--->O(n) 
i=2 total=5--->O(n)
i=3 total=12
sum(1,3)
sum(0,3)
sum(2,3)complexity increases

prefix sum--->
arr=[2,4,1,7,3]
     0 1 2 3 4
calculate the prefix:

prefix[i]=prefix[i-1]+arr[i]

index    arr[i]     prefix[i]
0          2            2
1          4           2+4=6
2          1           6+1=7
3          7           7+7=14
4          3           14+3=17
prefix of [i]=[2,6,7,14,17]
prefix[0]=2 sum from 0 to 0
prefix[1]=6  sum from 0 to 1
prefix[2]=7 sum from 0 to 2
prefix[3]=14 sum from 0 to 3
prefix [4]=17 sum from 0 to 4         

prefix sum formula:
sum=prefix[R]-prefix[L-1]
special case:
if L==0
sum=prefix[R]
find the sum from 1 to 3

R=3
L=1
sum=prefix[3]-prefix[0] #[l-1=0]
sum=14-2=12
'''
# arr=[2, 4, 1, 7, 3]
# n=len(arr)
# prefix=[0]*n
# prefix[0]=arr[0]
# for i in range(1,n):
#     prefix[i]=arr[i]+prefix[i-1]
# print(prefix)    
# l=1
# r=3
# if l==0:
#     total=prefix[r]
# else:
#     total=prefix[r]-prefix[l-1]
# print(total) 

'''
problem: find the multiple range queries
1-4  sum
2-5
0-3
all queriess in a single program

'''
arr=[2,4,1,7,3,9]
n=len(arr) 
prefix=[0]*n
prefix[0]=arr[0]
L=[(1,4),(2,5),(0,3)]
for i in range(1,n):
    prefix[i]=arr[i]+prefix[i-1]
print(prefix)    
for l,r in L:      
  if l==0:
    total=prefix[r]
  else:
    total=prefix[r]-prefix[l-1]
  print(total) 

'''
Problem-3
find the equilibrium index using prefix sum
arr=[1,3,5,2,2]
     0 1 2 3 4
left sum=1+3=4
right sum=2+2=4     
'''
arr=[1,3,5,2,2]
n=len(arr)  
prefix=[0]*n
prefix[0]=arr[0]
for i in range(1,n):
    prefix[i]=prefix[i-1]+arr[i]
total_sum=prefix[-1]
for i in range(n):
    if i==0:
        left_sum=0
    else:
        left_sum=prefix[i-1]
    right_sum=total_sum-prefix[i]
    if left_sum==right_sum:
        print("Equilibrium index",i)           
  

         
        
