n = int(input())
sum_divisors = 0
for i in range(1, n):
    if n % i == 0:
        sum_divisors += i
if sum_divisors == n:
    print("Perfect")
else:
    print("Not Perfect")