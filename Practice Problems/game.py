# p=input()
# u=l=d=s=0
# for i in p:
#     if "A"<=i<="Z":
#         u=1
#     if "a"<=i<="z":
#        l=1
#     if "0"<=i<="9":
#         d=1
#     else:
#         s=1
# if len(p)>=8 and u and l and s:
#     print("Valid password")
# else:
#     print("invald password")
    
    

s=input()
result=""
count=0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        if count>1:
            result=result+s[i]+str(count)
        else:
            result=result+s[i]
        count=1
if count>1:
    result = result+s[-1]+str(count)
else:
    result=result+s[-1]
print(result)   
    