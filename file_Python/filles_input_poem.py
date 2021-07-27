f=open('poem.txt')
content=f.read()
print(content)
if 'Twinkle' in content:
    print("Twinle is present!")
else:
    print("Twinkle is not present!")