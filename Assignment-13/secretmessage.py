s = input()
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
count = list(freq.values())
if len(set(count)) == 1:
    print("YES")
else:
    ok = False
    for i in range(len(count)):
        temp = count[:]
        temp[i] -= 1
        if temp[i] == 0:
            temp.remove(0)
        if len(temp) > 0 and len(set(temp)) == 1:
            ok = True
            break
    if ok:
        print("YES")
    else:
        print("NO")