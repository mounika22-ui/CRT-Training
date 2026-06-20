n = int(input())
arr = list(map(int, input().split()))
count = 1
max_so_far = arr[0]
for i in range(1, n):
    if arr[i] > max_so_far:
        count += 1
        max_so_far = arr[i]
print(count)