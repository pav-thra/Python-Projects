n=int(input("Enter a number"))
num=n
temp=0
for i in range(2,n//2):
    if n%i==0:
        temp+=1
if temp==0:
    print(n," is prime")
else:
    print(n," is not prime")    
