'''
An ecommerce company wants to validate order processing
The sytem should accept:
1.product stock
2.payment status
3.delivery address
raise exception if:
1.stock unavailable
2.payment failed
3.address is empty
if all validation pass:
print("Order succesfully placed")

'''
# '''class OutOfStockError(Exception):
#     pass
# class PaymentFailedError(Exception):
#     pass
# class InvalidAddressError(Exception):
#     pass
# class Ecommerce:
#     def __init__(self,stock,payment_status,address):
#         self.stock=stock
#         self.payment_status=payment_status
#         self.address=address
#     def place_order(self):
#         try:
#             if self.stock<=0:
#                 raise OutOfStockError("Product unavaliable")
#             if not self.payment_status:
#                 raise PaymentFailedError("Payment is failed")
#             if self.address.strip()=="":
#                 raise InvalidAddressError("Address cannot be empty")
#             print("Order placed Sucessfully")
#         except OutOfStockError as e:
#             print(e)
#         except PaymentFailedError as e:
#             print(e)
#         except InvalidAddressError as e:
#             print(e) 
# stock=int(input("Enter stock:"))
# payment=input("Payment Successful(Yes/NO):").lower()
# address=input("Enter address")
# payment_status=payment =="yes"                     
# obj=Ecommerce(stock,payment_status,address)
# obj.place_order()

'''
problem-3:
A company wants to create a file analyzer tool
The program should acccept:
1.Accept the filename from user
handle:
1.file not found
2.permission denied
3.empty file
Display:
number of lines:len(file.splitlines())
number of words:len(file.split)
number of characters:len(file)
'''
class EmptyFileError(Exception):
    pass
class FileAnalyzer:
    def analyze(self,filename):
        try:
            file=open(filename)
            content=file.read()
            
            if content.strip()=="":
                raise EmptyFileError("file is empty")
            lines=len(content.splitlines())
            words=len(content)
            characters=len(content)
            #display the outputs
            print("Lines:",lines)
            print("Words",words)
            print("Characters:",characters)
            file.close()
        except FileNotFoundError as e:
            print(e)
        except PermissionError as e:
            print(e)
        except EmptyFileError as e:
            print(e)  
        finally:
            print("analysis completed")  
filename=input("Enter the file name")
obj=FileAnalyzer()
obj.analyze(filename)
