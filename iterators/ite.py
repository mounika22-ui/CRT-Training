'''




Python refers iterators:
memory efficiency
controlled access

Iterable:is an object can be looped
1.list
2.tuple
3.set
4.dict
5.string

Examplles:
nums=[10,20,30,40]
for x in nums:
    print(x)
#syntax:
iterable_object=[1,2,3,4]
it=iter(iterable_objectj)
print(it)

iterable--->iteration  
 '''
# iterable_object=[1,2,3,4]
# it=iter(iterable_object)
# print(it)
# print(next(it))
# #element printed and then pause 
# print(next(it))
# print(next(it))
# print(next(it))

'''
list
  |
iter()
  |
iterator

nums=[1,2,3,4] 
for x in nums:
    print(x)
it=iter(nums)
while True:
   try:
      x=next(it)
      print(x)
      except StopIteration:
        break     


how loop in python works internally
iterators---will be used internally
iter(),next()   
'''
# nums=[1,2,3,4] 
# for x in nums:
#     it=iter(nums)
# while True:
#     try:
#         x=next(it)
#         print(x)
#     except StopIteration:
#         break    
'''
nums=[2,3,4]
it=iter(nums)
'''
# name="python"
# it=iter(name)
# print(next(it))

# t=(1,2,3)
# it=iter(t)
# print(it)

# d={"a":10,"b":20}
# it=iter(d)
# print(next(it)) #a
# print(it) #dict_keyiterator object
'''
nums=[i for i  in range(100000)]
#huge memory
#iterator apporach
nums=iter(range(100000))
#only the current elements will processed
'''
# class Count:
#     #constructor
#     def __init__(self,limit):
#         self.num=1
#         self.limit=limit
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num>self.limit:
#             raise StopIteration
#         x=self.num
#         self.num+=1 
#         return x  
#     #object creation
# c=Count(5) 
# for i in c:
#     print(i)     

'''
create a custom iterator for even numbers
'''
class EvenNumbers:   #class name 1st letter should be capital
    #constructor
    def __init__(self,limit):
        self.num=2
        #max_limt
        self.limit=limit
        #this method makes the object iterable
        #it returns the iterator objeect itself
    def __iter__(self):
        return self
    #next value during iteration
    def __next__(self):
        if self.num>self.limit:
            raise StopIteration
        x=self.num
        self.num+=2
        return x
    
e=EvenNumbers(10)
for i in e:
    print(i)
       
