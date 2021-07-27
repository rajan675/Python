print("                Arithmetic Operators      \n")
a=float(input("Enter frist Number"))
b=float(input("Enter second Number"))
c = float(input("Enter which Arithmetic Operation you want to preform +,-,*,/"))

if c=='+':
    d=(a + b)
    print("Sum= " + d)
elif c=='-':
    e=(a-b)
    print("Subtraction= "+ e)
elif c== '*':
    f=(a*b)
    print("Multiplication= "+ f)
elif c=='/':
    g=(a/b)
    print("Divide= "+ g)


