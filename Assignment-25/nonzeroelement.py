n = int(input())
arr = list(map(int, input().split()))
product = 1
found = False
for num in arr:
    if num != 0:
        product *= num
        found = True
if found:
    print(product)
else:
    print(0)