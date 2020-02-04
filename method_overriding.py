'''Sometimes the class provides a generic method, but in the child class, the user wants a specific implementation of the method.
Example
Classes Triangle, Rhombus, Pentagon and Hexagon have the same methods area() and perimeter() with different implementations:'''

import math

class Polygons:

    def number_of_sides(self):
        return 0

    def area(self):
        return 0

    def perimeter(self):
        return 0

class Triangle(Polygons):

    def number_of_sides(self):
        return 3

    def area(self,b,h):
        return 1/2*b*h

    def perimeter(self,a,b,c):
        if a+b>c:
            return a+b+c
        else:
            return 'invalid input'

class Rhombus(Polygons):

    def number_of_sides(self):
        return 4

    def area(self,p,q):
        return (p*q)/2

    def perimeter(self,p):
        return 4*p

class Pentagon(Polygons):
    def number_of_sides(self):
        return 5
 
    def area(self, a):
        return 1 / 4 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * a ** 2
 
    def perimeter(self, a):
        return 5 * a

# Hexagon class inherits from Polygons
class Hexagon(Polygons):
    def number_of_sides(self):
        return 6

    def area(self, a):
        return (3 * math.sqrt(3) / 2) * a ** 2

    def perimeter(self, a):
        return 6 * a

tri=Triangle()
print('Triangle area is ',tri.area(10,20))
print('Triangle perimeter is ',tri.perimeter(10,20,10))
print('-'*20)

rho=Rhombus()
print("Rhombus Area:", rho.area(15, 25))
print("Perimeter:", rho.perimeter(30))
print('-'*20)

pent = Pentagon()
print("Pentagon Area:", pent.area(15))
print("Perimeter:", pent.perimeter(25))
print("-----------------")

hex = Hexagon()
print("Hexagon Area:", hex.area(15))
print("Perimeter:", hex.perimeter(25))
print("-----------------")





class Parent:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print('Parent Name=',self.name)
        print('Parent Age=',self.age)

class Child(Parent):

    def __init__(self,name,age):
        Parent.__init__(self,name,age)

    def display(self):
        print('Child Name=',self.name)
        print('Child Age=',self.age)

ch1=Child('Atharv',4)
ch1.display()
ch1.display()


