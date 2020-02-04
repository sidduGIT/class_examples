#The type keyword used to create a new class on the fly and then instantiate it.

e1=type('Employee',(),{})()
print(e1)
e1.name='siddu'
e1.age=42
e1.salary='1.5 lakh'
print(e1.name,e1.age,e1.salary)

class Employee:

    def __init__(self,name,age):
        self.name=name
        self.age=age

e1=Employee('siddu',42)
print(e1.name)
print(e1.age)

e1.name='Atharv'
e1.age=4
print(e1.name)
print(e1.age)

del e1.name
#print(e1.name)
print(e1.age)

del e1
print(e1.name)
print(e1.age)




