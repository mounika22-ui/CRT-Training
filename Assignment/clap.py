performances=int(input("enter number of performances:"))
total=0
for i in range(performances):
    claps=int(input("enter number of claps:"))
    total=total+claps
avg=total/performances
print("total claps",total) 
print("Average claps",avg)   


'''
list--->[10,20]
input--->user (string)
split()--->10200--->"10","200"
int--->10,200

'''

