'''
check whether a  character is alphabet or not
logic flow:
read the character-->
ASCII--->chr(Ch)--->int--string
ord(ch)--->string--int
A-Z==>65-90
a-z==>97-122
'''
# s=input()
# ch=ord(s)
# if 65<=ch<=90 or 97<=ch<=122:
#     print("alphabet")
# else:
#     print("not alphabet")    
    
'''
Find the length of the string without using len()
logic:                   1.Initialize a count=0
                                    |
                         2.Traverse the string
                                    |
                         3.increment the counter for each other
                                     |
                         4.print(counter)                         
                                  
'''
# s=input()
# count=0
# for i in s:
#     count+=1
# print(count)    

'''
Toggle each character:
logic flow:
                  1.Traverse each character
                               |
                  2.if uppercase-->convert to lower
                               |
                  3.else lowercase-->uppercase                       

'''
# string=input()
# r=string.swapcase()
# print(r)

'''
Remove the total vowels from the string
Example: input:Hello
output:Hll
'''
# s=input()
# result=""
# for i in s:
#     if i.lower() not in ['a','e','i','o','u']:
#         result=result+i
# print(result)    

'''
problem-5
Remove all characters except alphabets
Example:
input:"hel23@lo"
output:"helo"
'''
# s=input()
# result=""
# for i in s:
#     if i.isalpha():
#         result+=i
# print(result)        
        
'''
problem-6
Remove spaces without using strip
Example:
input:Hello
output:Hello
'''
# s=input() 
# result=""
# for i in s:
#     if i !=" ":
#         result=result+i
# print(result)               
    
'''
problem-7
remove the brackets from algerbic expression
example:
input:(a+b)*{c+d}
output:a+b*c+d
'''    

# s = input()
# result = ""
# for i in s:
#     if i not in "{}()[]":
#         result =result+i
# print(result)      

'''
problemm-8
sum of numbers in a string:
input:hel123o
output:6
logic:traverse string-->
identify digits-->do sum and print
'''
# s = input()
# result= 0
# for i in s:
#     if i.isdigit():
#         result=result+int(i)
# print(result)

'''
problem-9
Capitalize the first and last character of a word
Example:
input:hello world
output:HellO WorlD
'''
# s = input().split()
# result=""
# for i in s:
#     word=i[0].upper()+i[1:-1]+i[-1].upper()
#     result=result+word+" "
# print(result)
 # (or)
# s=input().split()
# result=[]
# for i in s:
#     if len(i) == 1:
#         result.append(i.upper())
#     else:
#         word = i[0].upper() + i[1:-1] + i[-1].upper()
#         result.append(word)
# final = " ".join(result)
# print(final)  
'''
check anagram
input:SILENT--->LISTEN
'''
# s1=input()
# s2=input()
# if s1==s2:
#     print("anagram")
# else:
#     print("not anagram")    
    
    #(or)
s = input()
if sorted(s) == sorted("LISTEN"):
    print("LISTEN")
else:
    print("No match")    
