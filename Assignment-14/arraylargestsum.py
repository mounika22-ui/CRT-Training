n=int(input())
l=list(map(int,input().split()))
k=int(input())
prefix=[0]*n
prefix[0]=l[0]
for i in range(1,len(l)):
    prefix[i]=prefix[i-1]+l[i]
total=prefix[-1]
ans=float('inf')
for i in range(n-1):
    left_sum=prefix[i]
    right_sum=total-prefix[i]
    largest=max(left_sum,right_sum)
    ans=min(ans,largest)
print(ans)