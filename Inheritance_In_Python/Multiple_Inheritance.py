class Employee:
    company = "Visa"
    def getDetails(self):
        print("This is parent class of Employee!")
class Freelancer:
    company = "Rupay"
    def getDetails(self):
        print("This is also the Parent class of Employee!")
class Programmer(Employee, Freelancer):
    def getInfo(self):
        print("This is the Child class Inherits from Employee and Freelancer")
e=Employee()
f=Freelancer()
p=Programmer()
p.getDetails() #Inherits Employee Parent because in Child Employee is written first