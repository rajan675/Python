class Employee:
    company="Google"
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
        print("Employee is created")
    def getDetails(self):
         print(f"The name is {self.name}")
         print(f"The salary is {self.salary}")
rajan=Employee("Rajan", 100, )
rajan.getDetails()