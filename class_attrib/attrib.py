class Employee:
    company="Google"


rajan= Employee()
arvind= Employee()
print(rajan.company)
Employee.company="Youtube"
print(arvind.company)