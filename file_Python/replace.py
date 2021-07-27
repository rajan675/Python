words=["donkey","sala","kutta","kalu","harami"]
with open("replace.txt") as f:
     content=f.read()
for word in words:
    content=content.replace(word,"abuse")
with open('replace.txt','w') as f:
    f.write(content)