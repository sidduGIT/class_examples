# creating multiple class variables and pass it to as arguments

class Employee:

    def __init__(self,**kwargs):
        for key in kwargs:
            setattr(self,key,kwargs[key])
    def display(self):
        print('Name=',self.name)
        print('Age=',self.age)
        print('Salary=',self.salary)

e1=Employee(name='siddu',age=42,salary='1.5lakh')
e1.display()
