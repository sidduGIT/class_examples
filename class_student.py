class Student():

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def display(self):
        print('initial value',self.name,self.roll)

    def setAge(self):
        self.age=int(input('enter age'))

    def setmarks(self):
        self.marks=int(input('enter marks'))

    def displayall(self):
        print(f'name={self.name} roll={self.roll} age={self.age} marks={self.marks}')

obj=Student('siddu',1008887)
obj.display()
obj.setAge()
obj.setmarks()
obj.displayall()
