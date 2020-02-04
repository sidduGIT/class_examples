class Rectangle():

    def __init__(self,l,b):
        self.l=l
        self.b=b

    def getdata(self):
        self.l=int(input('enter length'))
        self.b=int(input('enter bredth'))

    def area(self):
        self.area=self.l * self.b
        print('area of rectangle is',self.area)

obj=Rectangle(0,0)
obj.getdata()
obj.area()
