n=int(input())
nums=list(map(int,input().split()))
k=int(input())
ans = []
for i in range(n - k + 1):
    window = nums[i:i + k]
    window.sort()
    if k % 2 == 1:
        median = window[k // 2]
    else:
        median = (window[k // 2 - 1] + window[k // 2]) / 2
    ans.append(median)
for x in ans:
    if x == int(x):
        print(int(x), end=" ")
    else:
        print(x, end=" ")