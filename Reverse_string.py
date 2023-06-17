s=input("Enter a string ")
a=""
for i in s:
    a=i+a
print(a)
if a==s:    
    print("S")    
else:
    print("N")    
