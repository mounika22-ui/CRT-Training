class CyclicSum:
    def find_sum(self, arr, n, k):
        total = 0

        for i in range(k):
            total += arr[i % n]

        return total


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    obj = CyclicSum()
    print(obj.find_sum(arr, n, k))