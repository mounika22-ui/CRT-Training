'''
text="apple banana pineapple strawberry banana apple"
find the frequency of the words?
'''
text = "apple banana pineapple strawberry banana apple"
words = text.split()
freq= {}
for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print(freq)          

#shallow copy:
student={
    "Name":"Mounika","Rollno":1
}
b=student.copy()
print(b)
student["Rollno"]=9
print(student)
print(b)
c=student
print(c)
student["Rollno"]=10
print(c)
#why dict is faster?
#hashing -- dict stores data in hashtable
#time complexity:O(1)
#searching--O(1)
#inserting,deleting-->O(1)
data={
    "a":1,
    "a":2
}
print(data)

'''
create a dict with employee details
now add branch and phone num at a time
fetch all the key and values using loop
pop the last added pair
print the pairs without deleting
addon:make the employee a nested dict with multiple employess
each employee has task with arr=[1,2,3]
now print key values using looping
'''
employee={"Name":"Mounika","Rollno":1}
employee.update({"Branch":"CSE","Phoneno":9876543210})
for key,value in employee.items():
    print(key,value)
emp=employee.copy()
print(emp)
employee.popitem()
print(employee)

'''
problem-2:
group anagram:
input:["eat","tea","tan","ate","nat","bat"]
output;[[eat,tea,ate],[tan,nat],[bat]]
'''

words=["eat","tea","tan","ate","nat","bat"]
dict={}
for word in words:
    key="".join(sorted(word))
    if key in dict:
        dict[key].append(word)
    else:
        dict[key] = [word]
print(list(dict.values()))

'''
problem:
Top k frequent elements
input[1,1,1,2,2,3]
k=2
ouput[1,2]
'''
nums = [1,1,1,2,2,3]
k = 2
freq = {}
for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
result = sorted(freq, key=freq.get, reverse=True)
print(result[:k])