class Parent:

    def mymethod(self):
        print('calling parent method')

class Child(Parent):

    def mymethod(self):
        print('calling child method')

c=Child()
c.mymethod()
