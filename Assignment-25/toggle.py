n = int(input())
binary = bin(n)[2:]
toggled = ""
for bit in binary:
    if bit == '0':
        toggled += '1'
    else:
        toggled += '0'
print(int(toggled, 2))