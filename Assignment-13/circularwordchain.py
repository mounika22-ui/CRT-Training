n = int(input())
words = []
for i in range(n):
    words.append(input())
valid = True
seen = set()
for i in range(n):
    if words[i] in seen:
        valid = False
        break
    seen.add(words[i])
for i in range(n - 1):
    if words[i][-1] != words[i + 1][0]:
        valid = False
        break
if valid:
    print("VALID")
else:
    print("INVALID")