class SmartLocker:
    def __init__(self,locker_id,owner_name,pin):
        self.locker_id=locker_id
        self.owner_name=owner_name
        self.__pin=pin
        self.__access_count=0
    def verify_pin(self,entered_pin):
        return entered_pin==self.__pin
    def access_locker(self,entered_pin):
        if self.verify_pin(entered_pin):
            self.__access_count+=1
            print("Access granted")
        else:
            print("invalid pin")
    def change_pin(self,old_pin,new_pin):
        if self.verify_pin(old_pin):
            self.__pin=new_pin
            print("PIN changed successfully")
        else:
            print("Incorrect old pin")
    def display_details(self):
        print("Locker ID:",self.locker_id)
        print("Onwer:",self.owner_name)
        print("AccessCount:",self.__access_count)
locker_id,owner_name,pin=input().split()
l=SmartLocker(locker_id,owner_name,pin)
q=int(input())
for i in range(q):
    operation=input().split()
    if operation[0]=="ACCESS":
        l.access_locker (operation[1])
    elif operation[0]=="CHANGE":
        l.change_pin(operation[1],operation[2])
    elif operation[0]=="DETAILS":
        l.display_details()