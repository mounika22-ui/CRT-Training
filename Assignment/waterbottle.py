n=int(input())
glasses=list(map(int,input().split()))
total=0
hours=0
for glass in glasses:
    total=total+glass
    hours+=1
    if total>8:
        break
print(hours)
print(total)