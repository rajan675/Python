import random
import time
print("Dice Roll Game")
dice=input("Enter y to roll Dice!")
if dice=='y':
    random= str(random.randint(1,6))
    print("Rotating Dice")
    time.sleep(1)
    print("The value is = " + random)
