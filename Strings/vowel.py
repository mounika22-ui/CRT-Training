'''
problem-3
count the vowels in a string:
'''
s="Durga Mani mounika"
count=0
for i in s:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count+=1
print(count) 

#or
s="Mounika"
count=0
for i in s:
    if i in "aeiou":
        count+=1
print(count)  

    

s = {1,2,3,4,4}
print(s)
     