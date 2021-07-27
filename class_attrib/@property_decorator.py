class Employee:
    salary= 100
    bonusSalary= 50
    @property
    def totalSalary(self):
        return self.salary + self.bonusSalary
e=Employee()
print(e.totalSalary)