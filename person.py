class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print('Hi {}, How ar you?'.format(self.name))

person1=Person('Atharv')
person1.talk()
person1.name='Surabhi'
person1.talk()

