#self is passed as implicit parameter to class methods

class Test:

    def __init__(self):
        self.data=5

    def add(self,x):
        print(self.data+x)

    def mul(self,x):
        print(self.data*x)

    def sub(self,x):
        print(self.data-x)

    def div(self,x):
        print(self.data/x)

t1=Test()
print(t1.data)

t1.add(10)  
t1.mul(10)  
t1.sub(10)  
t1.div(10)  

