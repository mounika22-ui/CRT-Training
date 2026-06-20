'''
4. Find the frequency of the characters
'''
s="banana"
target="a"
frequency=s.count(target)
print(frequency)

s=input("enter some text")
target=input("enter the target")
count=0
for i in s:
    if i==target:
        count+=1
print(count)        