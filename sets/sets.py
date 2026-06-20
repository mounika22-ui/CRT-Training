'''
what is a set?
Collection of unnordered unique elements
-->unordered
-->unique(never allows duplicates)
why?
->fast searching-->O(1)
->duplicates removal
how to create a set?
numbers={1,2,3,4,5}
print(numbers)
'''
#creation of set
numbers={1,2,3,4,5}
print(numbers)
numbers={1,2,2,2,3,4,5}
print(numbers)
num=[1,2,3,3,4,4,5]
unique=set(num)
print(unique)
#checking the mutability
# numbers[0]=10
# print(numbers)
#set is unordered -->fixed indexing(no)
numbers.add(10)
print(numbers)

#1st way--->create
num={1,2,3,4,5}
#2nd way--->create
s=set([1,2,3,4,5])
#freq{}-->empty dict
#empty set-creation
s=set() 
s.add(1)
print(s)
#multiple elements:
s.update({2,3,4,5})
print(s)

#removing the element
s.remove(2)
print(s)

#discard:it returns none without getting any error
s.discard(1)
print(s)

#pop(): delets the  random element
s.pop()
print(s)

#clear():clear all elements

print(20 in s)

'''
what is hashing?
hashing will convert the data into unique hash values

python uses:
1.hash tables
2.hash functions
target=10
set={1,2,3,4,10}

unlike linear search it directly jumps to target/location
ex:hash(10)

search,insert,delete--->O(1):time complexity
time complexity of list O(n)

set operations:
1.union |
2.instersection 
3.difference

'''
a={1,2,3,4}
b={5,6,7,8}
#union
print(a|b)
print(a.union(b))
#intersection
print(a.intersection(b))
print(a&b)
#difference
print(a-b)
print(a.difference(b))

#symmetric difference
a={1,2,3}
b={2,3,4}
print(a^b)
print(a.symmetric_difference(b))

#subsset and superset
a={1,2}
b={1,2,3,4}
print(a.issubset(b))
print(b.issuperset(a))

#frozenset:immutable version of set
#cannot add 
#cannot delete
#cannot update
fs=frozenset([1,2,3,4,5])
print(fs)
'''
feature             list     tuple     dictionary          set
ordered             yes       yes       no                  no
mutability          yes       no       yes,no               yes
allow duplicates    yes       yes      keys:no val:allow    no
indexing            yes        yes      no                   no

can i store list inside the set?
1.list
2.dict
3.set

Task:
create a list with squares of a numbers
convert the list with
squares of a number to set
try to repeat the squares two times
add the multiples of 2 to the same set at a single time
--->separate the set with 2 diff sets
multiples of 2
squares
now perform all the set operations on both
'''
s= [1, 4, 9, 16, 25]
s_set = set(s)
s_set.add(4)
s_set.add(9)
multiples = {2, 4, 6, 8, 10}
print("S:", s_set)
print("Multiples:", multiples)
print("Union:", s_set | multiples)
print("Intersection:", s_set & multiples)
print("Difference:", s_set - multiples)
print("Symmetric Difference:", s_set ^ multiples)

'''
problem:
find the length of longest consecutive sequence
input:[100,4,200,1,3,2]
output:[4]
'''
a=[100,4,200,1,3,2]
s=set(a)
longest=0
for i in s:
    if i-1 not in s:
        length=1
    while i+length in s:
        length+=1
    longest=max(longest,length)
print(longest)        
            
        
    
