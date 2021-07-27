class Employee:
    company= "Google"
    def getSalary(self):
        print(f"Salary for Employee working in {self.company} is {self.salary}")
rajan= Employee()
rajan.salary=500
rajan.getSalary()
# Second metohd is 
# Employee.getSalary(rajan)