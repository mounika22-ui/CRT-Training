'''
logic for password verifier
             |
    store the  original password
             |
    Ask the user for input
             |
    compare the entered password with original pass
             |
        if Wrong:
        Show error message
        ask again
             |
        if correct:
        stop loop
        login successful
'''      
crtpin="Mouni22"
password=""
while crtpin!=password:
    password=input()
    if crtpin!=password:
        print("password is incorrect")
        print("Try Again")
print("login Successful")
    