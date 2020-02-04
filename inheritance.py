class Mammal:
    def walk(self):
        return('walk method from parent class')

class Dog(Mammal):
    def bark(self):
        return 'Bow bow method from dog child class'

    

class Cat(Mammal):
    def mew(self):
        return 'mew mew method from cat child class'

dog1=Dog()
print(dog1.walk())
print(dog1.bark())

cat1=Cat()
print(cat1.walk())
print(cat1.mew())
