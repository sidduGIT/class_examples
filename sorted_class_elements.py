class Employee:
    
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    
    def display(self):
        return ('\nName ={}\nAge ={}\nSalary =${}'.format(self.name,self.age,self.salary))

e1=Employee('siddu',40,150000)
e2=Employee('atharv',4,180000)
e3=Employee('karu',6,160000)
e4=Employee('gundya',8,190000)

employees=[e1,e2,e3,e4]

def s_sort(e):
    return e.name

print('\nsorting based on names')
sorted_employees=sorted(employees,key=s_sort)
for e in sorted_employees:
    print(e.display())

def s_sort(e):
    return e.age

print('\nsorting based on ages')
sorted_employees=sorted(employees,key=s_sort)
for e in sorted_employees:
    print(e.display())

def s_sort(e):
    return e.salary

print('\nsorting based on salary')
sorted_employees=sorted(employees,key=s_sort)
for e in sorted_employees:
    print(e.display())
