mark1=int(input("Enter the marks of Physics \n"))
mark2=int(input("Enter the marks of Chemiatry \n"))
mark3=int(input("Enter the marks of Maths\n"))

total=(mark1+mark2+mark3)
avg=total/3
print(" Your Average= ",avg)
if(avg>40 and mark1>30 and mark2>30 and mark3>30):
    print("Congrates! You are passed")
else:
    print("Sorry! You are fail")
