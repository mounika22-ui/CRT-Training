#calculate electricity bill using the conditions:
#conditions: First 100 units --->5/unit
#2.next 100 units--->7/units
#3. above 200 units --->10/unnits

units=int(input("Enter the units"))
if units <=100:
    bill = units*5
    print("electricity bill:",bill)
elif units<=200:
    bill=(100*5)+((units-100)*7)
    print("electricity bill:",bill) 
else:
    #first 100 units--5
    #next 100 units--7
    #above 200 units--10
    bill=(100*5)+(100*7) +((units-200)*10)
#display the final bill
print("Final bill:",bill)       
'''
units= 250
100*5=500
100*7=700
(units - 200)*10
250-200*10=>500
500+700+500==>1700
'''
