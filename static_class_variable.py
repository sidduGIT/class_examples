#creating static class variable accessing it

class Employee:
    age=42

print(Employee.age)

e1=Employee()
print(e1.age)

e1.age=43
print(Employee.age)
print(e1.age)
