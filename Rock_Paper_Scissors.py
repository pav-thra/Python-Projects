import random
print("Choices: 1-Rock, 2-Paper, 3-Scissors")
i=int(input("Enter your choice "))
r=random.randint(1,3)

print("User choice: ",i," Computer choice: ",r)
if i==r:
    print("Draw")
if (i==1 and r==2) or (i==2 and r==1):
    print("Paper wins Rock")    
elif (i==1 and r==3) or (i==3 and r==1):
    print("Rock wins Scissors")    
elif (i==2 and r==3) or (i==3 and r==2):
    print("Scissors wins Paper")        
else:
    print("Enter correct numbers")    