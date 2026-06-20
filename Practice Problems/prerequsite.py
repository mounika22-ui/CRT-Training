'''
count the frequency of the character
Example:
input:aaabc
output:
a:3
b:1
c:1
dict={'a':10,'b':3}
'''
# S=input()
# freq={}
# for i in range(len(S)):  
#     ch=S[i] 
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch]=1
# print(freq) 

'''
find the maximum freq character
input:aaabcd
a:3
b:1
c:1
d:1
'''       
S=input()
freq={}
for i in range(len(S)):  
    ch=S[i] 
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)              
        
        
               



