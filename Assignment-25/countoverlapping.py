d = input()
w = input()
count = 0
for i in range(len(d) - len(w) + 1):
    if d[i:i+len(w)] == w:
        count += 1
print(count)