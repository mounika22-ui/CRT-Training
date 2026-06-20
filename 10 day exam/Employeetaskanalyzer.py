# class Employee:
#     def __init__(self,emp_name,emp_task):
#         self.emp_name=emp_name
#         self.emp_task=emp_task
#     def get_emp_name(self):
#         return self.emp_name
#     def get_emp_task(self):
#         return self.emp_task
# n=int(input())
# emp_name,emp_task=input().split(":")
# count=0
# tasks=[]
# emp_name=emp_name.lower()
# max_count=0
# emp=Employee(emp_name,emp_task)
# tasks.append(emp)
# for ch in tasks:
#     if ch in tasks:
#         count+=1
#     else:
#         count=0
#     if count<=max_count:
#         max_count=count
#         emp.sort()
# print(f"{emp_name:{count}}")   

# (or) 
    
def productivity_report(activities):
    #dict to store employee task count
    count = {}

    #traverse each activity
    for activity in activities:
        #John:Login --> name = John
        #task = Login
        name,task = activity.split()
        name = name.lower()                         #case sensitive --> name.lower

        #check if employee
        #already exsits in dict
        if name in count:
            count[name] +=1
        else:
            #add a new employee with count 1
            count[name] = 1
    employees = list(count.items())

#sort alphabetically by name
    def sort_by_name(item):
    #(John,2) --> tuple format
    #  0   1
        return item[0]
        employees.sort(key = sort_by_name)

#sort by task count
    def sort_by_count(item):
        return item[1]
        employees.sort(key = sort_by_count,reverse = True)
#input section
n = int(input())
#list to store activities
activities = []
for i in range(n):
    activity = input()

    activities.append(activity)
productivity_report(activities)                
    
            