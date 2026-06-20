'''
files helps store data permanently

File Handling:
is a process of:
1.creating files
2.reading files
3.writing files
4.updating files
using python

why file handling?
data disappears after  the program ends

with file:
1.store data perm
2.data sharing possible
3.reports/logs can be generated

Types of files???
1.Text files:
1. .txt
2. .csv
3. .py
4. .json
2.Binary Files:
1.Images
2.Videos
3.PDFs

#Opening the files
syntax:

file=open("Filename","mode")


'''
#r-will tell to python that line doesnot have any escaping characters
# file=open(r"C:\Users\Mounika\Desktop\python classes\file handling\data.txt","r")
# print(file)

'''
File Modes

Mode        Meaning
r            read
w            write
a            append
x            create
r+           read+write
w+           write+read
a+           append+read
rb           read binary
wb           write binary
'''
# try:
#     file=open(r"C:\Users\Mounika\Desktop\python classes\file handling\data.txt","r")
#     data=file.read()
#     print(data)
#     file.close()
# except FileNotFoundError as e:
#     print("No file found")

# #write mode-w
# file=open(r"C:\Users\Mounika\Desktop\python classes\file handling\data.txt","w")
# file.write("Hello students")
# file.close()

#Createsfiles if not exist 
#delete the old and add new content 

# append - mode
# file=open(r"C:\Users\Mounika\Desktop\python classes\file handling\data.txt","a")
# file.write("\nHow are you?")
# file.close()

# #create mode-x (creating a new file only)
# file=open("newfile.txt","x")
# #gives FileExistsError if already available

# #Read()
# file=open("newfile.txt","r")
# print(file.read())
# file.close()
# #readline()
# file=open("newfile.txt","r")
# print(file.readline())
# file.close()
#3.readlines()-reads multiple lines
# file=open("newfile.txt","r")
# lines=file.readlines()
# print(lines)
# file.close()

#readlines--> converts to list

#write()-->writes the data to file
# file=open("newfile.txt","w")
# file.write("megha\n")
# file.write("Rahu\n")
# file.close()

#writelines():writes list data 
# names=["Rahul\n","Anjali\n","Rajesh"]
# file=open("newfiles.txt","w")
# file.writelines(names)
# file.close()

#pointer method:returns the current cursor position
#tell()
# file=open("newfiles.txt","r")
# print(file.tell())
# file.read(5)
# print(file.tell())
# file.close()

#seek(): moves the cursor position
# file=open("newfiles.txt","r")
# file.seek(3)
# print(file.read())
# file.close()

#with open()
# with open("newfiles.txt","r") as file:
#     print(file.read())
    #automatic closing

#student record system
# name=input("Enter student name:")
# marks=input("enater marks")
# with open("newfile.txt","a") as file:
#     file.write(name +" "+ marks+ "\n")
# print("Record saved")

#list---employee details
# employees=["Rahul 50000","Anjali 60000","mounika 50000"]
# with open("newfile.txt","w") as file:
#     for emp in employees:
#         file.write(emp + "\n")
# print("Report Generated")

'''
CSV-->Comma Separated Values
used:excel,reports,databases

Example:
name,age,branch
meghana,20,cse
rahul,22,cse
'''
import csv
with open("students.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Age","Branch"])
    writer.writerow(["Rahul",23,"CSE"])
    writer.writerow(["Sravani",24,"CSE"])

#read CSV
with open("students.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
        
#binary file handling
file=open(r"C:\Users\Mounika\Desktop\python classes\krishna.jpeg.jpeg","rb")
data=file.read()
print(data)
file.close() 

'''
Task-1:count words in the file
with open(data.txt","r) as file:
'''
with open("first.txt", "r") as file:
    data = file.read()
    words = data.split()
    print("Word count:", len(words))
'''
Task-2 count the lines in the file
'''
with open("first.txt", "r") as file:
    lines =len(file.readlines())
    print(lines)     
        
'''
task-3:search the word in a file
'''
word = input("Enter word to search: ")
with open("first.txt", "r") as file:
    content = file.read()
if word in content:
    print("Word found")
else:
    print("Word not found")
    
'''
task-4: copy one file to another
'''
with open("first.txt", "r") as file1:
    content = file1.read()
with open("second.txt", "w") as file2:
    file2.write(content)
print("File copied successfully") 

'''
task-5:count the characters in a file
'''
with open("first.txt","r") as file:
    characters=len(file.read())
    print("Characters:",characters)    

'''
Student Record Management :
A college wants to maintain  student
records permentally
write a python program to
1.accept student_name and marks
2.store records in a file 
named students.txt
3.dispaly all records
4.handle file exceptions properly
'''
class StudentManager:
    def add_student(self):
        try:
            name = input("Name:")
            marks = input("Marks")
            with open("Students.txt","a") as file:
                file.write(name + " "+ marks)
            print("Records added")
        except Exception as e:
            print(e)
    def dsplay_records(self):
        try:
            with open("students.txt","r") as file:
                content = file.read()
                print("Students Records:")
                print(content)
        except FileNotFoundError as e:
            print(e)
obj = StudentManager()
obj.add_student()
obj.dsplay_records()