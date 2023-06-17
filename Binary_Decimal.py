bin=int(input("Enter a binary number "))
pow=0
dec=0
num=bin
while(bin!=0):
    dig=bin%10
    dec=dec+dig*(2**pow)
    pow+=1
    bin=bin//10
print(dec)    