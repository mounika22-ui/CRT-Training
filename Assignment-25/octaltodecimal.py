octal = input()
decimal = 0
power = 0
for digit in reversed(octal):
    decimal += int(digit) * (8 ** power)
    power += 1
print(decimal)