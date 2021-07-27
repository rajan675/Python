class Programmer:
    company= "Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getInfo(self):
        print(f"The name of programmer is {self.name}")
        print(f"The product of programmer is {self.product}")
        print("\n")
rajan=Programmer("Rajan","Skype")
murari=Programmer("murari","Gethub")
rajan.getInfo()
murari.getInfo()