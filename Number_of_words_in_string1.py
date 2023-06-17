text=input("Enter a string")
temp=0
count=1
for i in text:
    if i==" ":
        temp+=1
        if temp==1:
            count+=1
        else:
            temp+=1
    else: 
        temp=0
if text[0]==" ":
    count-=1
print(count)    
        
