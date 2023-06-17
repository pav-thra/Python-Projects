dec=int(input("Enter a decimal number "))
num=dec
bin=''
while(dec>0):
    bin=str(dec%2)+bin
    dec=dec//2
print(bin)    

