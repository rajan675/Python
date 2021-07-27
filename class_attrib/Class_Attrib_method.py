class Doctor:
    Salary= 100
    # def __init__(self, sal):
    #     self.sal=sal
    @classmethod
    def changeSalary(cls, sal):
        cls.Salary=sal

d=Doctor()
print(d.Salary)
d.changeSalary(101)
print(d.Salary)