num1=int(input("Enter num 1 "))
num2=int(input("Enter num 2 "))
num3=int(input("Enter num 3 "))
num4=int(input("Enter num 4 "))
if(num1>num4):
    f1=num1
else :
    f1=num4
if(num2>num3):
    f2=num2
else :
    f2=num3
if(f1>f2):
    print(f1, "is greatest")
else:
    print(f2,"is greatest")