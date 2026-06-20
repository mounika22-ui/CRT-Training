'''
kadane's algorithm :max sub arrays problem
arr=[2,-1,3,-2,4]
find the contigious sub array with max sum
subarray:[-1,3,-2]right
         [2,3]invaild

subarray       sum
[2]             2
[2,-1]          1
[2,-1,3]        4
[2,-1,3,-2]     2
[2,-1,3,-2,4]   6

i=1
[-1]                    1
[-1,3]                  2
[-1,3,-2]               0

kadanes algorithm main idea 

at every element we decide

Two choices:
1.continue previous subarray
        (or)
2.start a new subarray

current_sum=-5
next_element=10

-5+10=5 #discarding the previous(-ve)
next==10

arr=[2,-1,3,-2,4]
current_sum=2
max_sum=2

index:1
      -1
      choice-1:extend the array
      2+(-1)=1
      choice-2:start a new array
      -1

      current_sum = 1
      max_sum = 2

      index -2 :3 
      choice-1:extend the array 
      2+(-1)= 1+3 = 4

      choice-2 : start a new array 
      3

      
      current_sum=4
max_sum=max(2,4)=4

idex-3:-2
     choice-1:extend the  array
      2+(-1)=1+3=4+(-2)=2

     choice-2:start a new array
     -2

current_sum=2
max_sum=max(4,2)=4

index-4:4
      choice-1:extend the array
      2+(-1)=1+3=4-2=2+4=6
      
      choice-2:start a new array
      4
current_sum=6
max_sum=max(4,6)=6  

current_sum=max(arr[i],current_sum+arr[i])
max_sum=max(max_sum,current_sum)
'''
# arr=[2,-1,3,-2,4]
# current_sum=arr[0]
# max_sum=arr[0]
# for i in range(1,len(arr)):
#     current_sum=max(arr[i],current_sum+arr[i])
#     max_sum=max(max_sum,current_sum)
# print(max_sum)    

'''
problem:
A cricket player gains or loses
points in each match.
positive -> won points
negative ->lost points
The coach wants to find the longest continuous
winning streak with maximum  performance
but instead of returing the sum,
return the:

maximum score
starting index
ending index
Example:
input:
scores=[-2,4,-1,5,-3,2]
output:
maximum score=8
start index=1
end index=3
'''
# scores = [-2, 4, -1, 5, -3, 2]
# current_sum = scores[0]
# max_sum = scores[0]
# start = end = 0
# temp_start = 0
# for i in range(1, len(scores)):
#     if scores[i] > current_sum + scores[i]:
#         current_sum = scores[i]
#         temp_start = i
#     else:
#         current_sum += scores[i]
#     if current_sum > max_sum:
#         max_sum = current_sum
#         start = temp_start
#         end = i
# print(max_sum)
# print(start)
# print(end) 

'''
problem:
Maximum product subarray
input:[2,3,-2,4]
output:6  2*3
print(index)
'''
arr = [2, 3, -2, 4]
max_prod = arr[0]
min_prod = arr[0]
ans = arr[0]
start = end = temp_start = 0
for i in range(1, len(arr)):
    if arr[i] < 0:
        max_prod, min_prod = min_prod, max_prod
    if arr[i] > max_prod * arr[i]:
        max_prod = arr[i]
        temp_start = i
    else:
        max_prod = max_prod * arr[i]
    min_prod = min(arr[i], min_prod * arr[i])
    if max_prod > ans:
        ans = max_prod
        start = temp_start
        end = i
print(ans)
