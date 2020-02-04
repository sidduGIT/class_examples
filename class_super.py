'''
In a class hierarchy with single inheritance, super can be used to refer to parent classes without naming them explicitly, thus making the code more maintainable. This use closely parallels the use of super in other programming languages'''

class A:

    def __init__(self,profession):
        self.profession=profession
        print(self.profession)

class B(A):

    def __init__(self):
        print('siddu bagewadi')
        super().__init__('python developer')

b=B()

class Father:

    def __init__(self,surname):
        self.surname=surname
        print(self.surname)

class Child(Father):

    def __init__(self,name):
        self.name=name
        print(self.name)
        super().__init__('bagewadi')

ch1=Child('Atharv')
