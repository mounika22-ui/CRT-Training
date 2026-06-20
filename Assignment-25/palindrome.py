a, b = map(int, input().split())
found = False
for i in range(a, b + 1):
    if str(i) == str(i)[::-1]:
        print(i, end=" ")
        found = True
if not found:
    print("No Palindromes")