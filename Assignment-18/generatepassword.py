class PasswordGenerator:
    def generate(self, s, k):
        password = ""

        for i in range(k):
            password += s[i % len(s)]

        return password


t = int(input())

for _ in range(t):
    s = input()
    k = int(input())

    obj = PasswordGenerator()
    print(obj.generate(s, k))