#Polymorphism allows us to define methods in the child class with the same name as defined in their parent class.

class Shape:

    def __init__(self,widt,hgt):
        self.widt=widt
        self.hgt=hgt

    def area(self):
        print('Parent class area')

class Triangle(Shape):

    def __init__(self,w,h):
        self.widt=w
        self.hgt=h

    def area(self):
        print('Child class Triangle Area is',1/2*self.widt*self.hgt)

class Rectangle(Shape):

    def __init__(self,w,h):
        self.widt=w
        self.hgt=h

    def area(self):
        print('Child class recatngle area is',self.widt*self.hgt)

tri=Triangle(10,20)
tri.area()

rect=Rectangle(10,20)
rect.area()
