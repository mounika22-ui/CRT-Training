'''
loop control:
Break:it stops the execution of the loop immediately
(Terminate the loop immediately)
continue: skips the current iteration
pass:do's nothing
'''
#Example: Break
i=1
while i<=10:
    if i ==5:
        break    #Terminates at 5
    print(i)
    i+=1
    
#example : continue
for i in range(1,11):
    if i==5:
        continue
    print(i) 
    
#pass : do's nothing (provides the placeholderfor the code) 

for i in range(1,11):
    pass   

#example include break,continue,pass in the  program
for i in range(20,40):
    pass
    if i==25:
        continue
    if i==35:
        break
    print(i)
    
 #summary:
'''
diff btw for and while
for: used when num of iterations are known
Best for iterating over the sequences

while:unkown num of iterations
best for conditions controlled loops
best  for conditions based repetition
it executes until the condition is true

Q2:what makes the loop infinite?
when  condition never mets false becomes an infinite loop

Q3:can we use else withh while?
i=1
while i<=3:
    print(i)
    i+=1
else:
    print("loop is finished")
Note: Else wont work if there is a break statement        
'''

    
