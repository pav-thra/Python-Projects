s=input("Enter main string")
sub=input("Enter substring")
p=int(input("Enter index to inset"))
print(s[:p]+sub+s[p:])