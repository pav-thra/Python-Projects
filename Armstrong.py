n=int(input("Emter a number"))
num=n
sum=0
while(n!=0):
    d=n%10
    sum=sum+d**3
    n=n//10
if num==sum:
    print(num," is Armstrong number")    
else:
    print(num," is not an Armstrong number")    