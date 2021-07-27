class Employee:
    company="Google"
    salary= 100

rajan=
arvind= Employee()
arvind.salary= 200
print(rajan.company)
Employee.company="Youtube"
print(arvind.company)
print(rajan.salary)
print(arvind.salary)