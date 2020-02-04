class Employee:

    def __init__(self,first,last,pay,empid):
        self.first=first
        self.last=last
        self.pay=pay
        self.empid=empid
        self.email=first+'.'+last+'@company.com'

    def display(self):
        print('the details of an employee')
        print('Name = {} {}\npay = {}\nempid = {}\nemailid = {}'.format(self.first,self.last,self.pay,self.empid,self.email))


emp1=Employee('siddu','bagewadi',50000,1000)
emp1.display()

emp2=Employee('santu','bagewadi',80000,5000)
emp2.display()
