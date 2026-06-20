class DigitalWallet:
    def __init__(self,name,balance,password,):
        self.name=name
        self.__balance=balance
        self.__password=password
        self.__Transaction_count=0
    def deposit(self,amount):
        self.__balance+=amount
        self.__Transaction_count+=1
        print("Deposit successful")
    def withdraw(self,amount,password):
        if password!=self.__password:
            print("Incorrect password")
            
        elif amount>self.__balance:
                print("Insufficient balance")
        else:
                self.__balance-=amount
                self.__Transaction_count+=1
                print("Withdrawal successful")
    def balance(self,password):
        if password==self.__password:
           print(self.__balance)
        else:
            print("Incorrect password")
    def display_details(self):
        print("Transaction count:",self.__Transaction_count)
name,balance,password=input().split()
w=DigitalWallet(name,int(balance),password)
n=int(input())
for i in range(n):
    operation=input().split()
    if operation[0]=="DEPOSIT":
        amount=int(operation[1])
        w.deposit(amount)
    elif operation[0]=="WITHDRAW":
        amount=int(operation[1])
        password=operation[2]
        w.withdraw(amount,password)
    elif operation[0]=="BALANCE":
        password=operation[1]
        w.balance(password)
    elif operation[0]=="HISTORY":
        w.display_details()