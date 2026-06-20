#Bitwise &
#1 only if both bits are 1
'''
A B A&B
0 0 0
0 1 0
1 1 1
1 0 0
'''
# 8 4 2 1

#5--> 0101
#3-->0011
#&-->0001--->1
print(5&3)
print(6&2)

'''
RealLife: 
Permission system, masking operations
Checking flags
'''

#Bitwise OR
#1 if any one bit is 1
'''
A B A|B
0 0 0
0 1 1
1 1 1
1 0 1
'''
# Example
'''
5 --->0101
3 --->0011
|--->0111--->7
'''

print(5|3)  #7
print(12|4)  #12

#Bitwise XOR --> IMP  interviews

#1 if both bits are different
'''
A B A^B
0 0 0
0 1 1
1 1 0
1 0 1
'''
'''
6--->0110
2--->0010
^--->0100---->4
'''

print(6^2) #4


# swap the numbers without using the third variable
input =  5,3
output = 3,5
a=3
b=5

a = a+b
#a = 3+5=8
b = a-b
# b = 8-5=3
a = a-b
# a=8-3=5
print(a,b)


a= a^b
#a =5^3--->6
b=a^b
#b=6^3--->5
a=a^b
#a=6^5--->3
print(a,b)


#Bitwise NOR
#0--->1
#1--->0
print(~5) #-6

#~n = -(n+1)
print(~10) #-11

#Low level memory operations

#<< left shift
#rule--> shift the bit to left

'''
5--->  0 1 0 1
<< --> 1 0 1 0---->10

'''

print(5<<1)#10

#formula ==> n<<k = n*2^k

#right shift: shift: shift the bits to right
'''
8--->1 0 0 0
>>--->0 1 0 0--->4

'''
# formula = n>>k = n/2^k
print(8>>1)

print(16>>2)#4

print(12>>6) 

print(13>>7)
'''
13--->1 0 1 1
>>--->0

'''

print(17>>8)












