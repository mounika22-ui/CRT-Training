'''
Login Authentication System
A company wants to store user credentials
write a program:
1.Register users into users.txt
2.login using username and password
3.validate the credentials from file
4.handle invalid login attempts
'''
class LoginAuthentication:
    def register(self):
        username=input("Enter the username")
        password=input("Enter the password")
        with open("data.txt","a") as file:
            file.write(username+" "+password+"\n")
        print("Registration Successful")
    def login(self):
        try:
            username=input("Enter username:") 
            password=input("Enter the password:")
            found=False
            with open("data.txt","r") as file:
                for line in file:
                    u,p=line.strip().split()
                    if (username==u and password==p):
                        found=True
                        break
                    if found:
                        print("Login Successfull") 
                    else:
                        print("Invaild Credentials")
        except FileNotFoundError as e:
            print(e) 
obj=LoginAuthentication()
obj.register()
obj.login()            
                                  