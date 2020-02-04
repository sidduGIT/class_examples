#this example shows calling parent class constructor from child class constructor

class Family():

    def __init__(self,name):
        self.name=name

class Father(Family):

    def __init__(self,name,age):
        Family.__init__(self,name)
        self.age=age

    def display(self):
        print('Fathers name is {}'.format(self.name))
        print('Fathers age is {}'.format(self.age))

f=Father('siddu',42)
print(f.name)
print(f.age)
f.display()
