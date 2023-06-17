#doesnt work
text=input("Enter a string")
count=0
flag=0
for i in text:
    if i==" ":
        flag=1
        if flag==1:
            count+=1
            flag=0
        else:
            flag=1                       
print(count+1)    