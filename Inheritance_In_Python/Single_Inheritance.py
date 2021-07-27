class Parent:
    company="Google"
    def getDetails(self):
        print("This is the details of Parent Class")
class Child(Parent):
    lang= "Python"
    def getLanguage(self):
        print(f"The Language is {self.lang}")
p=Parent()
c=Child()
print(p.company)
print(c.company)
c.getLanguage()
c.getDetails()  #Inherits the property of Parent Class