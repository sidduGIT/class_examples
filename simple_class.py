class Employee:
    name='siddu'
    age=42

emp=Employee()
print(emp.name,emp.age)
print(type(emp))

#class with __init__

class Employee:
    name='siddu'
    age=42

    def __init__(self,name,age):
        self.name=name
        self.age=age

print(emp.name,emp.age)
emp=Employee('santu',38)
print(emp.name,emp.age)

#class wih display() method

class Employee:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print('Employee name= {}'.format(self.name))
        print('Employee age= {}'.format(self.age))

emp=Employee('siddu',42)
emp.display()

#within class you can have self as anything like myself, ourself or any other variable general practice is having self

class Employee:
    
    def __init__(myself,name,age):
        myself.name=name
        myself.age=age

    def display(myself):
        print('Employee name= {}'.format(myself.name))
        print('Employee age= {}'.format(myself.age))

emp=Employee('shivu',52)
emp.display()

#deleting objects parameters in the case below name and age

class Employee:

    def __init__(myself,name,age):
        myself.name=name
        myself.age=age

    def display(myself):
        print('Employee name= {}'.format(myself.name))
        print('Employee age= {}'.format(myself.age))
    
    def display_age(myself):
        print('Employee age= {}'.format(myself.age))

    def display_name(myself):
        print('Employee name= {}'.format(myself.name))

emp1=Employee('surabhi',6)
emp2=Employee('atharv',4)
emp1.display()
emp2.display()

del emp1.name
del emp2.age
#emp1.display()
#emp2.display()
emp1.display_age()
emp2.display_name()

#empty class

class Employee:
    pass

emp1=Employee()
emp2=Employee()




