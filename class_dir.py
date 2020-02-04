class Employee:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age

e1=Employee('siddu',42)
print(dir(e1))

print([i for i in dir(e1) if not i.startswith('__')])
