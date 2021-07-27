file1 = poem.txt
file2 = sample.txt

with open(file1) as f:
    f1=f.read()

with open(file) as f:
   f2= f.read()

if f1 == f2 :
    print("These file are identical")

else:
    print("These files arae not identical")