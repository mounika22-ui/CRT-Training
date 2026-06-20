n = int(input())
arr = list(map(int, input().split()))
k = int(input())
first = arr[0]
rest = arr[1:]
m = len(rest)
k = k % m
rest = rest[-k:] + rest[:-k]
result = [first] + rest
print(*result)