'''
what is loop?
A loop is used to repeat the block of code
Instead of writing the logics again and again
we will repeat the code

print("Hello")
print("Hello")
'''
#looping ----2 types
#      /       \
#    for       while    
'''
for loop used when no.of iterations are known
while loop is used when the no.of iterations are unknown

Benifits:
1.Reduces the code duplication & complexities.
2.Saves time
3.make our programs very efficient.
4.Helps in the automation
      Execution flow of loops
             start
               |
            conition check
               |
            True---->Execute the block
               |
            Repeat
               |
            False--->stop      

'''
#for loop: it iterates on the sequences
#list,tuple,range,string
'''
C-Programming
for(i=0;i<n;i++){}
i=0--->initalization
i<n--->condition
i++--->increament
}
python:
list--->collection of ordered elements
list--->[,,,,]
list is mutable

'''
'''
frnds = ["Maggi","Tatiribitiri","penguin"]
#syntax:
#for var in sequence:
#statements
for frnd in frnds:
    print(frnd)
    
    #2nd way?
    #range(start,end-1,step)
    #range(1,11)
    
    for i in range(5):
        print(i)

for i in range(1,16):
    print(i)
    
 #task:multiplication table using 5
 
num=5 
for i in range(1,11):
    print(num,"x",i,"=",num*i)
    
    
#task: sum of numbers(1,6)   
i= sum(range(1,6))
print(i)

total=0
for i in range(1,11):
   total+=i
print(total) 
  
#task: s = " Mouni" now count the char using for loop
s="Mounika"
char_count={}
for i in s:
   if i in char_count:
       char_count[i]+=1
   else:
      char_count[i]=1
print(char_count)      


#use for loop and print only
#even numbers upto 20
#dont write even num logic
for i in range(2,21,2):
   print(i)
 
#Reverse of the sequence
#1,11---->11,1,-1
for i in range(11,1,-1):
    print(i)   
    
#while loop
#syntax:
#while condition:
#    statment
#example
# i=1
# while i<=5:
#    print(i)
#    i +=1   
# while True:
#    print("run forever")   
#sum of numbers--using while   
#do sum unntil the input is 0
'''
'''

num=input() 5
total = 0
while num !=0:
    total +=num
    num=input()
print(total)    
'''

num=int(input())
total=0
while num!=0:
   total=total+num
   num=int(input())
print(total) 

#example2
#print the even numbers from 2-20?
'''
      start from 2
           |
      check if num<=20
          |
      print(num)
          |
      increament the number by 2
          |
      repeat
          |
      stop after 2o
'''
i=2
while i<=20:
   if i%2==0:       #we can remove if i%2==0 the output will come
      print(i)
      i+=2
      
      
      
      
   
  
