#creating data attributes dynamically with setattr

class Employee:
    
    def display(self,name,age,salary):
        print(self.name,self.age,self.salary)

emp1=Employee()
setattr(emp1,'name','siddu')
setattr(emp1,'age',42)
setattr(emp1,'salary','1.5lakh')
emp1.display(emp1.name,emp1.age,emp1.salary)

