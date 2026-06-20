'''
What is dictionary?
list--->collection of ordered elements.
mutable-->can be modified
tuple--->collection of ordered elements.
immutable-->cant be modified

Dict:collection of key value pairs
    key:valuues
    G1:"Mounika"
    dict::{}
#dict is mutable:can be modified
and it is also immutable : cant be modified  
#keys are immutable and values are mutable
Not  allows duplicates of keys.
values cant be duplicates.
no fixed indexing
ssearching is very efficient:O(1)
uses hashing technique to search hence O(1)


Why we use dict?
1.Labels
2.Properties
3.Mapping the releationships

'''
    
list=["Mounika","G1",20] 
#creation of dictionary
student={
    "Name":"Mounika",
    "Rollno":1,
    "Age":20
    }
print(student)

#2nd method
#student=dict(name="Mounika",age=20,branch="CSE")
#print(student)

#3rd method:empty dict
data={}
print(data)

#list=[10,20,30,40]
       #0 1  2   3
#list[0]
#print(student["Name"]) 
#print(student["Age"])
'''
feature             list       dict
ordered             yes         no
access(indexing)     yes        no
arr[0]               yes        no student["keys"]
'''
employee={}
employee["Name"]="lokesh"
employee["age"]=21
print(employee) 
#upadte the value
employee["age"]=24     
print(employee)
#delete the value
employee.pop("age")
print(employee)
#2nd method of delete
del student["Rollno"]
print(student)

#dictionary methods
#keys()--->return all the values
print(student.keys())
#values()-->return all the values
print(student.values())
#items()--->returns all the items in dict
print(student.items())
#print(student["Branch"])
#access the elements
print(student.get("Name"))
print(student.get("Branch"))
#None
student.update({"Branch":"CSE","College":"CITY"})
print(student)
#popitems:removes the last inserted pair
student.popitem()
print(student)

#looping on dictionary
for i in student:
    print(i)

#itearating on values
for value in student.values():
    print(value)    

for key,value in student.items():
    print(key,value)
    
#Nested dictionaries: dict inside the dict
students={
    "s1":{
        "Name":"Rajesh",
        "Branch":"AI"
        },
    "s2":{
        "Name":"Ravi",
        "Branch":"AIML"
    }
}        
print(students["s1"]["Name"])

#can i store list inside the dict?  --->yes
student={"Name":"Harish","Marks":[90,80,60,95]}
print(student)
#you can store multiple dict in list
students=[{"Name":"Rajesh","Branch":"CSE"},#0
          {"Name":"Praful","Branch":"CSD"}] #1
print(students[0]["Name"])

#dict comprehension
#{key:value for variable in iterable}
squares={x:x*x for x in range(1,11)}
print(squares)

#keys:Rules
'''
int
strings
tuple
list--->no  bez it is mutable
dict--->
student={
    1:"Mounika",
    ""Roll":1,
    (1,2):"tuple"
    [1,2,3]:"list" #mmutable
    {"Name":"Mounika"}:"hello"  #cant use
    }
'''
