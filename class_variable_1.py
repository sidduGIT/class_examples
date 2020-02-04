class Employee:
    empcount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empcount +=1

    def emp_count(self):
        print('Total number of employees %d'%Employee.empcount)
    
    def display_emp(self):
        print('Name =',self.name)
        print('salary =',self.salary)

emp1=Employee('siddu',200000)
emp2=Employee('Atharv',500000)
emp1.display_emp()
emp2.display_emp()
emp1.emp_count()
emp1.age=40
emp2.age=5
print('emp1 age is %d'%emp1.age)
print('emp2 age is %d'%emp2.age)

#del emp1.age
#del emp2.age
#print('emp1 age is %d'%emp1.age)
#print('emp2 age is %d'%emp2.age)


print('Employee.__doc__     ',Employee.__doc__)
print('Employee.__name__    ',Employee.__name__)
print('Employee.__bases__   ',Employee.__bases__)
print('Employee.__module__  ',Employee.__module__)
print('Employee.__dict__    ',Employee.__dict__)
