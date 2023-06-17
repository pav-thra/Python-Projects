num=678
rev=0
while (num>0):
    d=num%10
    rev=rev*10+d
    num=num//10
print(rev)    