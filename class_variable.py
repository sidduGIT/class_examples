class Employee:

    raise_amount=1.05
    number_of_emps=0

    def __init__(self,first,last,pay,empid):
        self.first=first
        self.last=last
        self.pay=pay
        self.empid=empid
        self.email=first+'.'+last+'@company.com'
        Employee.number_of_emps+=1

    def display(self):
        print('\nthe details of an employee')
        print('Name = {} {}\npay = {}\nempid = {}\nemailid = {}'.format(self.first,self.last,self.pay,self.empid,self.email))
    
    def apply_raise(self):
        self.pay=self.pay*self.raise_amount

emp1=Employee('siddu','bagewadi',50000,1000)
emp1.display()
print('after pay raise\n')
emp1.apply_raise()
emp1.display()

emp2=Employee('santu','bagewadi',80000,5000)
emp2.display()
print('after pay raise\n')
emp2.apply_raise()
emp2.display()

emp3=Employee('atharv','bagewadi',10000,4000)
print(Employee.number_of_emps)
