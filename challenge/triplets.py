'''
nums=[-1,0,1,2,-1,-4]
       i L         R
       left=i+1
       right=n-1
nums.sort()
nums=[-4,-1,-1,0,1,2]
       i L         R  left=i+1  right=n-1
redult=-1,0,1
        -1,-1,2
two pointers approach:
iteration-1:
i=0

nums[i]=-4
left=1
right=5
total=nums[i]+left+right
      -4+(-1)+2=-3
sum<0
-3<0
move left
left=2
total=-4+(-1)+2=-3
sum<0
left=3
total=-4+0+2=-2
sum<0
left=4
total=-4+1+2=-1
sum<0
left=5==right stop iteration
no triplets were found

iteration-2:
i=1
nums[i]=-1
left=2
right=5
total=-1+(-1)+2=0
#triplet found
[-1,-1,2]

move both pointers
left=3
right=4

total=-1+(0)+1=0
tiplet found
[-1,0,1]

move both pointers
left=4  left>right-->stop
right=3

iteration=3
i=2
nums[i]=-1
check duplicate:
nums[i]==nums[i-1]

-1==-1
skip


'''
# if sum<0:
#     left+=1
# if sum>0:
#     right-=1

n=int(input())
nums=list(map(int,input().split()))
nums.sort()
for i in range(n-2):
    #skip the duplicate elements
    if i>0 and nums[i]==nums[i-1]:
        continue
    left=i+1
    right=n-1
    while left<right:
        total=nums[i]+nums[left]+nums[right]
        if total==0:
            print(nums[i],nums[left],nums[right])
            left+=1
            right-=1
            #skip the duplicates
            while left<right and nums[left]==nums[left-1]:
                left+=1
            while left<right and nums[right]==nums[right+1]:
                right-=1
        elif total<0:
            left+=1
        else:
            right-=1

