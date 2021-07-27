class Employee:
    Salary=1000
    Increment=1.5
    @property
    def salaryAfterincrement(self):
        return self.Salary*self.Increment
    @salaryAfterincrement.setter
    def salaryAfterincrement(self, salaryAfterincrement):
        self.Increment=salaryAfterincrement/self.Salary
e=Employee()
print(e.salaryAfterincrement)
print(e.Increment)