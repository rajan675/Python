import random
def gameWin(comp, you):
    if comp==you:
        return None
    elif comp == 's':
        if you=='g':
            return True
        elif you=='w':
            return False
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
random=random.randint(1,3)

if random==1:
    comp='s'
elif random==2:
    comp='g'
elif random==3:
    comp='w'

you=input("Your Turn:Snake(s), Gun(g), Water(w)\n")

print("Comp Choice= ",comp)
print("Your Choice= ",you)

a=gameWin(comp,you)
if a==None:
    print("This match is Tie!")
elif a:
    print("You win")
else:
    print("YOu lose ")

