'''
Strings: one of the most impotant topic
string are the sequence of characters:
Enclosed--->'',"",''''''
String is always Inmutable.
                              Mutability
                                /   \
                           Mutable   Inmutable
                              |         |
                             Change    Cant Change    

Example:
name= "Sounika"
name[0]="M"--->error (cant change)
                           
Memory space
"S T R I N G"
 0 1 2 3 4 5                          
#accessing the elements
str[0]
# '''
# name="M O U N I K A" 
#      #0 1 2 3 4 5 6
# print(name)
# #print (name[0])
# print(name[0:2])
# print(len(name))

# str="College"
# print(len(str))

# #string:
# #str[start,end,step]
# print(str[0:3])

'''
str=" C O L L E G E"
      0 1 2 3 4 5 6 
     -7-6-5-4-3-2-1
str[-1:-4]
str[6:3]
str[-1]--->last character
str[-2]--->second last character
str[10]--->inex error
#ommiting start
str[:3]--->col
str[3:]--->lege
#C O L L E G E
 0 1 2 3 4 5 6
 C     L     E
 C 
#STEP SLICING:
str[0:6:2]--->CLE
str[0:6:1]--->colleg
'''

#Reverse your name
# name="Mounika"
# #[::-1]-->Starts from -1 and goes upto end
# print(name[::-1])

# #string traversal:
# name="C h a l a p a t h i"
#      # 0 1 2 3 4 5 6 7 8 9 
# for i in name:
#     print(i)
'''
#Output:
C
h
a
l
a
p
a
t
h
i
'''  
'''
name="Chalapathi"
for i in range(len(name)):
    print(name[i])
''' 
# ch="Chalapathi"   
# for i in range(len(ch)):
#     print(ch,ch[i]) 
# print(ch.upper())  #Writes in upper case
# print(ch.lower())  #Writes in lower case
# print(ch.title())  #writes 1st letter in upper case and rest of them are lower case   
# print(ch.capitalize())  #Only first letter capital
# #strip--->removes the extra spaces
# print(ch.strip())
# text="I love programming"
# print(text)
# replaced_text=text.replace("love","hate")
# print(replaced_text)


# fruit="banana"
# #find the frequency of "a"
# print(fruit.count("a"))

#startswith--->checks if starting with "letter" 
# print(fruit.startswith("M"))
# #endswith-->
# print(fruit.endswith("na"))
# #split()
#text="Python C Java"

#separated=text.split()
# print(separated)
# print(type(separated))
# #Use join
# #python-C-Java
#new="-".join(separated)
# print(new)

# #searching inside the strings
# #find()--->
 #print(new.find("Python"))
# #using membership operator
# print("Python" in new)
# #index()
# text="Python"
# print(text.index("z"))
# #which is safe find() or index?
# #find() is safe to use 
# #string farmatting
# name="Vijay"
# age=20
# #f-string
# print(f"My name is {name} and age is {age}")
# #old college
# print("Name:",name ,"and age is :",age)
# #format()
# print("Welcom {}",format(name))
# #Escaping characters or sequence 
# print("hello \n world")
# print("Hello \t world")
# #R-strings(Regex-regular expressions)
# path=r"c://downloads/photos/pic.jpeg"
# print(path)
'''
r--> tells to your interpreter that there are no escaping characters in path

'''
#swapcase()---?
# text="PyThon"
# print(text.swapcase())
# #casefold()-->stronger lower conversion
# print(text.casefold())

# #center--?
# print(text.center(40))
#task:creat a string with your friends 
#name=mounika mona harika
#split the name to store in the list
#join the string "_"
#Traverse over the string and find the index
#of the person name starting with "A"
#print the person name
#count the len of the name & check "a" occurances
#print the frnd name with 30 space in center

# names="megha mona hari anjali"
# a=names.split()
# print("_".join(a))
# for i in a:
#     if i.startswith("a"):
#         print(i)
#         print(a.index(i))
# for i in a:
#     print(len(i))
#     print(i.count("a"))
# for i in a:
#     print(i.center(30))
    
    
#task : print the name in reverse
#slicing
# name="Mounika"
# print(name[::-1])#-->akinuoM
#without using slicing
'''
                            logic
                              |
                  read the characters from the end of the string       (traverse)    
                            |
                        start adding each char(from end) to a string   
                            |
                        print the var
'''
# s="HELLO"
# #start=4  
# #end=-1
# #step=-1
# reverse=""
# for i in range(len(s)-1,-1,-1):
#     reverse=reverse+s[i]
#     print("step:",i,"character:",s[i],"Reverse:",reverse) 
    
#problem-2 palindrom
'''
"Madam"==>"madam"
              logic
                |
             Input a word
                |
            reverse the word
                |
           compare original and reversed
                |
            palindrome or not          
'''
n = input()
reverse = ""
for i in range(len(n)-1, -1, -1):
    reverse= reverse + n[i]
if reverse==n:
    print("it is a palindrome")
    print(reverse)
else:
    print("it is not a palindrome")    
    
    #(or)
n=input()
reversed=n[::-1] 
if n==reversed:
    print("palindrome")
else:
    print("not a palindrome")       
    
    
 



