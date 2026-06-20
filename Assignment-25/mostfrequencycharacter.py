s = input()
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
max_count = max(freq.values())
ans = min(ch for ch in freq if freq[ch] == max_count)
print(ans)