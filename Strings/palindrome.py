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
    
    