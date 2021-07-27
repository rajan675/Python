def farenhiet(cel):
    return (cel*9/5)+32
c=37
temp= farenhiet(c)
print("Farenhiet temperature of given celsius value is = " + str(temp))

# for celsius
def celsius(far):
    return (far - 32)*5/9

f=98.6
temp1=celsius(f)
print("Celsius temperature of given farenhiet value is = "+ str(temp1))