message = input()
k = int(input())
result = ""
for ch in message:
    if 'A' <= ch <= 'Z':
        result += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
    elif 'a' <= ch <= 'z':
        result += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
    else:
        result += ch
print(result)