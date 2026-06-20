'''
Youtube: does not load the whole video
lods by:
small chunks
when needed
simply generators work in the same format

problem with list:
list=[1,2,3,4,5]
entire list is stored in memory
nums=[i for i in range(100000)]

Python consumes:
high memory
slower
Generator:
produces values one at  a time
only when it  is needed
saves memory

Yield keyword:
yield pauses the function
and remembers the state
return: ends the function
yield:pauses the function
'''
# #example:
# def numbers():
#     yield 1
#     yield 2
#     yield 3
# x=numbers()
# print(x)    #generator object

# #access the numbers
# print(next(x))
# print(next(x))
# print(next(x))

'''
numbers() #call
|
generator created
|
1. first next()
yield 1-->1
function paused

2.second next()
resume from previous position
yield 2-->2
function pause

3.third next()
resume from previous position
yield 3-->3
pause again
generators:
remembers the variables
remember line position
continue from the same place

#diff between return and yield
return                       yield
ends the function      pauses the funtion 
returns single value   will return multiple values
by one value
no state memory         remembers the state
'''
# def test():
#     return 1
#     return 2

# print(test())

# #with yield
# def numbers():
#     yield 1
#     yield 2
# for i in numbers():
#     print(i)

#for loop uses  iter(),next() internally
#create a generator for even numbers
# def even_numbers(limit):
#     num=2
#     while num<=limit:
#         yield num
#         num+=2
# x=even_numbers(10)
# for i in x:
#     print(i)
    
'''
num=2-->yield 2 ->2
pause
resume 
num=4-->yield 4 ->4
pause
resume
num=6-->yield 6 ->6
pause
#Memory Efficiency
nums-[i for i in range(100000)]
only the current value

#lazy evalution
values are generated when needed
generators are lazy 

#write a program for fibonacci using geneators
'''
def fibonacci(limit):
    
    #first two numbers
    a=0
    b=1
    #loop until the limit
    while a<=limit:
        #generate the current value
        yield a
        #update the values
        a, b=a+b 
x=fibonacci(20)    
for i in x:
    print(i)       
    
            
    
        
