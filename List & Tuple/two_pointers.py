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

# arr = [1, 2, 3, 2, 1]
# left = 0
# right = len(arr) - 1
# while left < right:
#     if arr[left] != arr[right]:
#         print("Not Palindrome")
#         break
#     left += 1
#     right -= 1
# else:
#     print("Palindrome")



# arr = [1, 0, 0, 1, 1, 0, 1]
# left = 0
# right = len(arr) - 1
# while left < right:
#     if arr[left] == 0:
#         left += 1
#     elif arr[right] == 1:
#         right -= 1
#     else:
#         arr[left], arr[right] = arr[right], arr[left]
#         left += 1
#         right -= 1
# print(arr)

#solve the problem with two pointers

# n=int(input())
# arr=list(map(int,input().split()))
# k=int(input())
# arr.sort()
# left=0
# right=len(arr)-1
# pairs=set()
# while left<right:
#     sum=arr[left]+arr[right]
#     if sum==k:
#       pairs.add((arr[left],arr[right]))
#       left+=1
#       right-=1
#     elif sum<k:
#        left+=1
#     else:
#        right-=1
# print(len(pairs))