class Vector:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return('vectors {} {}'.format(self.a,self.b))

    def __add__(self,other):
        return('vectors {} {}'.format(self.a+other.a,self.b+other.b))

v1=Vector(10,5)
v2=Vector(6,-2)
print(v1+v2)
