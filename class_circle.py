class Circle():
    def __init__(self,rad):
        self.rad=float(rad)

    def get_rad(self):
        self.rad=float(input('enter radius'))

    def area(self):
        self.area=float(3.142*self.rad*self.rad)
        print(self.area)

    def perimeter(self):
        self.perimeter=float(2*3.142*self.rad)
        print(self.perimeter)

obj=Circle(4)

#obj.get_rad()
obj.area()
obj.perimeter()

obj.get_rad()
obj.area()
obj.perimeter()

