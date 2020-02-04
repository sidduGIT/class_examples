class Employee:

    def __init__(self,name,empid,salary):
        self.name=name
        self.empid=empid
        self.salary=salary

    def display(self):
        print('details of a employee')
        print('Name= ',self.name)
        print('Empid= ',self.empid)
        print('salary= ',self.salary)

    def get_info_from_user(self):
        print('Get details of a employee')
        self.name=input('enter name ')
        self.empid=input('enter empid ')
        self.salary=int(input('enter salary '))
