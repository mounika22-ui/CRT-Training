n = int(input())
arr = list(map(int, input().split()))
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
result = []
for num in freq:
    if freq[num] == 1:
        result.append(num)
result.sort()
print(*result)