'''
Recursion is a programming technique where a function calls itself to solve smaller
version of the same problem

function -->calls itself-->again--->again

def function_name(parameters):
    """Docstring"""
    statements
    return statement


    def-->keyword
    function_name-->identifier
    parameters-->input
    return-->output

def hello():
    print("Hello")

#calling the function
hello()


#sum of two numbers
def add(a,b): #parameters
    return a+b
#call
add(2,3)#arguments


Recursion is a programming technique where a function calls itself to solve smaller
version of the same problem

function -->calls itself-->again--->again

1.Base case
condition where the recursion stops

2.Recursive case
function calls itself with a smaller input


'''
# def hello(n):
#     if n==0:   #base condition
#         return
#     print("Hello")
#     #recursive case or recursive call
#     hello(n-1)
# hello(5)

# hello(5)->hello
# hello(4)->hello
# hello(3)->hello
# hello(2)->hello
# hello(1)->hello
# hello(0)->stops the execution

'''
call stack:LIFO(last in first out)
stores function calls in memory 

every function call:

gets added to stack
removed after the completion

def fun1:
    print("Fun1")
    fun2()

def fun2():
    print("func2")

fun1()

main
   fun1
   fun2
'''

# def count(n):
#     if n==0:
#         return
#     print("Before :",n)
#     count(n-1)
#     print("After:",n)
# count(5)

'''
count(5) count(4)-->count(3)-->count(2)-->count(1)-->count(0)
fact(5)=fact(n-1)


'''
'''
added in stack and removed from stack if work is done
    0 count(0) #pop #base condition 
    1|count(1)|  #pop After:1
    2|count(2)|  #pop After:2
    3|count(3)|  #pop After:3
    4|count(4)|  #pop After:4
    5|count(5)|  #pop Afer:5


 Before:5 #topbtm flow(going down)
 befor:4
 before:3
 befor:2
 before:1
After:1 #returning phase
After:2
After:3
After:4
After:5

code befor recursive call:
--->executes while going down
code after recursive call
--->executes whike returning

'''
'''
5!=5x4x3x2x1
  =(n-1)!*(n-2).........n

fact(n)=fact(n-1)*n

def factorial(n):
    if n==0 or  n==1:
      return 1
    return n*factorial(n-1)
print(factorial(5))

call stack
|  fact(1)    |pop 1 
| fact(2)     |pop 1*2
| fact(3)     |pop 1*2*3
| fact(4)     |pop 1*2*3*4
| fact(5)     |pop 1*3*4*5=120
factorial(5)=factorial(4)*n
factorial(4)=factorial(3)*n
factorial(3)=factorial(2)*n
factorial(2)=factorial(1)*n
factorial(1)=1

'''
#task :sum of N numbers
# def sum_n(n):
#     if n==0:      #time complexity and space compllexity O(n)
#       return 1
#     return n+sum_n(n-1)
# print(sum_n(5))

# sum(5)=5+sum(4)
# sum(4)=4+sum(3)
# sum(3)=3+sum(2)
# sum(2)=2+sum(1)
# sum(1)=1+sum(0)  #base condition

#fibonacci:
#fib(n)=fib(n-1)+fib(n-2)
#fib(5)=fib(4)+fib(3)
# fib(4)=fin(3)+fib(2)
# fib(3)=fib(2)+fib(1)
# fib(2)=fib(1)+fib(0)

# def fib(n):
#    if n<=1:
#       return n
#    return fib(n-1)+fib(n-2)
# print(fib(5))

#problem:3
#reverse a string
'''
rev of string = reverse of rest+ first element

call       s        s[1:]   s[0]  it returns 
1        "hello"    "ello"   "h"   reverse("ello")+"h"
2        "ello"     "llo"    "e"   reverse("llo")+"e"
3        "llo"      "lo"     "l"   reverse("lo")+"l"
4        "lo"        "o"     "l"   reverse("o")+"l"
5        "o"         ""      "o"   reverse("")+"o"
#unwinding-->returning phase
6 .returns""
5.returns""+"o"="o"
4.returns"o"+"l"="ol"
3.returns"ol"+"l"="oll"
2.returns"oll"+"e"="olle"
1.returns"olle"+"h"="olleh"

'''
# def reverse_string(n):
#     if len(n)==0:
#       return ""
#     return reverse_string(n[1:])+n[0]
# print(reverse_string("hello"))

'''
#problem:4
given with n=1234
perform the sum of all the digits
1234=1+2+3+=10
1234%10-->4

remove last digit 
1234//10-->123

1234
|
4 +sum_digit(123)
then:
123
|
3+sum_digit(12)
then:
12
|
2+sum_digit(1)
then:
1
|
1+sum_digit(0)  #base case

#unwinding phase:

1+sum_digit(0)  1
2+sum_digit(1)  2+1=3
3+sum_digit(2)  3+2+1=6
4+sum_digit(3)  4+3+2+1=10

time complexity:
if number of digits has d
t.c=O(d)
space:each call uses stack
becomes total number of digits
s.c=O(d)
'''
# def sum_digits(n):
#     if n==0:
#         return 0
#     return (n%10)+sum_digits(n//10)
# print(sum_digits(1234))

'''
problem:5
check palindrome string using recursion
input:madam
output:True

first check first and last char
and the remaining characters
s[0]==s[-1] AND s[1:-1]

s="madam"
call=1
s[0]==s[1]
True   1:-1
is_palindrome("ada)
call=2
s="ada"
a==a
call==3
True
is_palindrome("d")
True

#stack unwinding starts
is_palindrome("d")=True
is_palindrome("ada")=true
is_palindrome("madam")=true

final output:True

'''
# def palindrome(s):
#    if s==s[::-1]:
#       return True
#    return False
# print(palindrome("madam"))
# def is_palindrome(s):
#     if len(s)<=1:
#         return True
#     if s[0]!=s[-1] :
#         return False
#     return is_palindrome(s[1:-1])
# print(is_palindrome("madam"))

'''
problem-6:print the numbers from N to 1
n=5
5 4 3 2 1
'''
'''
problem:7-find the largest element in an array
input:[3,9,2,15,7]
output:15


main idea:
compare current element with max of remaining array 
arr=[3,9,2,15,7]
     0 1 2 3 4
call n arr[n-1]  what it does                       returns
 1   5 arr[4]=7   max(7,find_max(arr,4))              wait
 2   4 arr[3]=15  max(15,find_max(arr,3))             wait
 3   3 arr[2]=2   max(2,find_max(arr,2))              wait
 4   2 arr[1]=9   max(9,find_max(arr,9))              wait
 5   1 arr[0]=3   max(3,find_max(arr,3))

 unwinding:
 5.returns 5
 4.max(9,3)=9
 3.max(2,9)=9
 2.max(15,9)=15
 1.max(7,15)=15
 final output:15
 '''
# def find_max(arr,n):
#     if n==1:
#         return arr[0]
#     return max(arr[n-1],find_max(arr,n-1))
'''
problem:8:
check array is sorted or not using recursion

input:[1,2,3,4,5]
output:True
another example:
input:[1,5,3,4]
output:False
'''
'''
def is_sorted(arr, n):
      if n == 1:
            return True
      return arr[n-1] >= arr[n-2] and is_sorted(arr, n-1)
print(is_sorted([1,2,3,4,5],5))
'''