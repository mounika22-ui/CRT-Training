class InvalidUsernameError(Exception):
    pass
class UserNotFoundError(Exception):
    pass
class ShortUsernameError(Exception):
    pass
class LoginSystem:
    def __init__(self, users):
        self.users = users
    def login(self, username):
        if len(username) < 4:
            raise ShortUsernameError(
                "Username length must be at least 4."
            )
        if not username.isalpha():
            raise InvalidUsernameError(
                "Username must contain only alphabets."
            )
        valid_users = [user.lower() for user in self.users]
        if username.lower() not in valid_users:
            raise UserNotFoundError(
                "Username not found."
            )
        print("Login Successful")
n = int(input())
users = []
for i in range(n):
    users.append(input())
username = input()
obj = LoginSystem(users)
try:
    obj.login(username)
except InvalidUsernameError as e:
    print("InvalidUsernameError:", e)
except UserNotFoundError as e:
    print("UserNotFoundError:", e)
except ShortUsernameError as e:
    print("ShortUsernameError:", e)