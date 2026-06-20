'''
what is list?
list: collection of ordered elements
                                     Mutability
                                      /      \
                                Mutable     Inmutable
                                   |           |
                                can modify    cant modify
list is mutable:
Allow's duplicates--->yes list allows duplicate
#dymanic in size.
#syntax:
list_name=[elements]
'''
# numbers=[10,20,30,40]
# print(numbers)
# print(type(numbers))
# data=[10,10.4,"python",True]
# print(data)
# #accessing the elements
# a=[10,20,30,40]
# print(a[0])
# #check mutability
# a[0]=60
# print(a)
# #negative indexing
# a=[10,20,30,40]
# print(a[-1])
# #slicing:
# #list[start:end:step]
# print(a[0:3])
# print(a[:3])
# print(a[::2])
# #list methods
# #append:adds at the end
# b=[10,20]
# b.append(30)
# print(b)
# #inset:adds multiple values
# b.extend([40,50,60])
# print(b)
# #insert-->add the elements at specific index
# b.insert(2,25)
# print(b)
# #remove:removes the elements
# b.remove(20)
# print(b)
# #pop:removes the elements with index
# b.pop(0)
# print(b)
# #clear()---->deletes all  elements
# # b.clear()
# # print(b)
# #index():returns the position
# print(b.index(25))
# #count: counts the occurances of the elements
# print(b.count(25))
# #reverse():
# b.reverse()
# print(b)
# #copy()
# c=b.copy()
# print(c)
# #sorting in list
# a=[5,0,2,4,3,1]
# #sort()--->sorts in ascending order
# a.sort()
# print(a)
# #descending order
# a.sort(reverse=True)
# print(a)
# #sort=sorts same list  vs sorted:creates a new list
# b=sorted(a)
# print(b)



# a=["sree","anu","nikki","lahari","harshi"]
# print(a)
# a.append("Hannu")
# print(a)
# a.remove("lahari")
# print(a)
# a.remove("anu")
# print(a)
# a.extend(["maggi","hari","mona"])
# print(a)
# a.sort()
# print(a)
# a.pop(4)
# print(a)

# #Nested list?
# a=[[1,2,3],[4,5,6]]
#     #   0       1
# print(a[0][0])
# print(a[1][1])
# #iterating 

    







# a = [1,2,3,4,5,6]
# count = 0
# for i in a:
#     if i % 2 == 0:
#         count += 1
# print(count)

# a = [1,2,3,4]
# reverse = a[::-1]
# print(reverse)

# a=[5,6,1,7,7,8]
# result=[]
# for i  in a:
#     if i not in result:
#         result.append(i)
# print(result)        

'''
find the second largest number in a list 
a=[10,40,80,90,30]
largest=80
'''
# a=[10,40,80,90,30]
# a.sort()
# print(a[-2])

a = [10, 40, 80, 90, 30]
largest = float('-inf')
second = float('-inf')
for i in a:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i
print(second)

'''
check if list is sorted
'''
a=[1,3,6,8,9]
sorted_list=True
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        sorted_list=False
if sorted_list:
    print("List is sorted")
else:
    print("List is not sorted")