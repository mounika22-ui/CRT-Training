username = input("Enter the username:")
#First condition
if username == "admin":
    password = input("Enter the password:")
    #Nested condition
    if password=="1234":
        print("Login Sucessful")
    else:
        print("Wrong password") 
else:
    print("Invalid username")           