n=int(input())
arr=list(map(int,input().split()))
k=int(input())
w=[]
s=sum(arr[:k])
w.append(s)
for i in range(k,n):
    s+=arr[i]-arr[i-k]
    w.append(s)
m=len(w)
left=[0]*m
best=0
for i in range(m):
    if w[i]>w[best]:
        best=i
    left[i]=best
right=[0]*m
best=m-1
for i in range(m-1,-1,-1):
    if w[i]>=w[best]:
        best=i
    right[i]=best
ans=[-1,-1,-1]
max_sum=0
for j in range(k,m-k):
    i=left[j-k]
    l=right[j+k]
    total=w[i]+w[j]+w[l]
    if total>max_sum:
        max_sum=total
        ans=[i,j,l]
print(*ans)