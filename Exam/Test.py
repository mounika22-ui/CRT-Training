'''
* problem statement:*
given a integer array arr of size N,
find the count of of elements whose values is
greater than all of its prior elements .
the 1st element is always considered in the count.

*Example:*
-Input:Arr={7,4,8,2,9}
            0 1 2 3 4 
            count=1
            max_so_far=7
            i=1
            4>7 false(ignore)
            count=1
            i=2
            8>7(yes)
            count=2
            max_so_far=8
            2>8 false(ignore)
            count=2
            max_so_far=8
            i = 4
            9>8 true
            count = 3
            max_so_far = 9
'''
# n=int(input())
# arr=list(map(int,input().split()))
# count=1
# max_so_far=arr[0]
# for i in range(1,len(arr)):
#     if arr[i]>max_so_far:
#         count+=1
#         max_so_far=arr[i]
# print(count)      

''''
n = int(input("Enter size: "))
arr = list(map(int, input("Enter elements: ").split()))

result = []

# Store non-zero elements
for num in arr:
    if num != 0:
        result.append(num)

# Count zeros
zeros = n - len(result)

# Add zeros at the end
for i in range(zeros):
    result.append(0)

print(*result)
'''
n = int(input())
arr = list(map(int, input().split()))
left = 0
for right in range(n):
    if arr[right] != 0:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
print(*arr)


          


