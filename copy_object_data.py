# how to copy object data from other objects

class Test:

    def __init__(self,a,b):
        self.a=a
        self.b=b

t1=Test(5,10)
print(t1.a)
print(t1.b)
t2=Test(5,10)
t1.a=100
t1.b=200
t2.__dict__.update(t1.__dict__)
print(t2.a)
print(t2.b)
t2.a=400
t2.b=500
print(t1.__dict__)
print(t2.__dict__)
