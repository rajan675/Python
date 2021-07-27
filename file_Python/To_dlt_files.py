import os 
dlt= 'dlt.txt'
with open('dtl1.txt') as f:
    content= f.read()
print(content)
os.remove(content)