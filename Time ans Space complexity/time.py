'''
Analogy:
You are given with 2 programs where it is generating the same output
how will you decide which one to use?
1.Faster program
2.less memory
3.efficient
#algorithm complexity == efficient

two types:
1.Time complexity:faster results in google
2.Space complexity: 
                        Mark-Zukerberg--->CSS 20kb
                        /          \
                        A=19kb           B=18kb    
                           |               |
                         10LPA            30LPA               

           DAU===>200cr
           70 Lakhs--20 Lakhs--50lakhs
           
Time Complexity?
Time Complexity measures how the runninng time grows as the size of input   
3-Techniques to measure time complexity    


'''
#Stop watch method
import time
start=time.time()
for i in range (1,1001):
    print(i)
print(time.time()-start)

'''
#problems in above technique
1. different systems diff time
2.different compilers/different interpreters
3.background apps effect time
4.internet/cpu/Gpu affect the performance    
'''    
#Techinque -2 counting the number of operations
#not measure the time in seconds but counts operations

def c_to_f(c):
    return c*9/5+32
#mul = 1
#div = 1
#add = 1  Operations = 3

#Example-2
def mysum(x):
    total=0      #-->1 op
    for i in range(x+1):  #1 op
        total=total+i    #2 op
    return total  
   #x--->input
   #1+2x x=10--->21 operations

#Techniques 3 order of growth
'''
Notations:
asympotic notations
1.big oho():calc the upper bound(worst time complexity)
2.Omega Notation: Best case complexity
3.Theta:avg case complexity

#Example:Linear search
arr=[1,2,3,4,5,6,7]
arr[0]==target #best case
arr[4]==target #avg case
arr[last]==target # worst case complexity

Big Oh: worst time growth
Focus:
1.Measuring the scalability
2.Machine Independent
3.Focuses on growth
4.ignores the hardware

def mysum(n):
    total=0  #-->1 op
    for i in range(n+1):
      total=total+i #2 op
    return total
#n--->input
  #num operations 1+2n n=10-->21 operations
Big oh(rules)
1.additive constants(remove)
    #1+2n--->2n
2.multiplicative constans(remove)
   #2n-->n
   time complexity-->O(n)
   
a=10
b=20
c=a+b
for i in range(1,101):
O(n)

Nested loops:
for i in range(1,n+1):
    for j in range(i):
    print(i)

Equation:n^2+n+10--->n^2+n--->time complexity=O(n^2)

for i in range(1,100):
    print(i)
for j in range(1,50):
    print(j) 
    n+n--->2n
    time compllexity=O(n)
    
#Practice:
1.n^2+10000n+3^1000
O(n^2)
2.log(n)+n+4
O(n)
3.0.0001*n*log(n)+300n
O(nlog(n))
4.2n^30+3^n
O(3^n) 

#Complexity Classes
1.Constant Time--->O(1)
_>same time always
arr=[10,20,20] 
arr[i] 
--->Input increase and time stays cinstant

2.Linear time--->O(n)
for i in arr:
    print(i)
#Grows along with input

3.Quadratic time --->O(n^2)
-->in nested loops
Nested loops:
 for i in range(1,n+1):
   for j in range(i):
     print(i)

#outer loop runs n times and
inner loops runs n time with outerloops

4.logarithmic time-->O(log(n))

Best example:
Binary search:
arr =[1,6,8,3,7,10]
arr=[1,3,6,7,8,10]
n/2
#Large input:smaller growth
#very efficient

5.Linearithmic-->O(nlog(n))

#better then quadratic
#used in industry

6.Exponential:-->O(2^n)

very slow,not much used

example: recursive fibonacii

Dangerous for Large input

while n>1:
    n=n//2

#space complexity:measures memory used by the alogithm
1.input space
2.Auxillary space

Example:
a=10
b=20
constant space--->O(1)

Example-2:
arr[0]*n
liner space--->O(n)
    
'''
      