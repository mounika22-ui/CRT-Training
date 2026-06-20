n = int(input())
l= list(map(int, input().split()))
k = int(input())
k = k % n
for i in range(k):
    last=l[-1]
    for j in range(n-1,0,-1):
        l[j]=l[j-1]
    l[0]=last
print(*l)   