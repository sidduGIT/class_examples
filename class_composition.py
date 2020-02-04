'''
In composition one of the classes is composed of one or more instance of other classes. In other words one class is container and other class is content and if you delete the container object then all of its contents objects are also deleted.'''

class Salary:

    def __init__(self,pay):
        self.pay=pay

    def total_salary(self):
        return (self.pay*12)

class Employee:
    
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
        self.obj_salary=Salary(self.pay)
    
    def anual_salary(self):
        return 'Total ='+str(self.obj_salary.total_salary()+self.bonus)

emp1=Employee(250000,300000)
print(emp1.anual_salary())
