s=input("Enter a stting")
vowels="aeiouAEIOU"
count=0
for i in s:
    if i in vowels:
        count+=1
print(count)        