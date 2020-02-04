#accessing private members in a child class

class Human:

    __privatevar='I am private variable'

    def __init__(self):
        self.classname='Human class constructor'
        self.__privatevar='redefined private variable'

    def showname(self,name):
        self.name=name
        return self.__privatevar+self.name

    def __private_method(self):
        return 'Human class private method'

    def show_private(self):
        return self.__private_method()

    def show_protected(self):
        return self._protected_method()

class Male(Human):
    
    def show_class_name(self):
        return 'Male child class from Human parent class'

    def show_private(self):
        return self.__private_method()

    def show_protected(self):
        return self._protected_method()

class Female(Human):

    def show_class_name(self):
        return 'FeMale child class from Human parent class'

    def show_private(self):
        return self.__private_method()

human=Human()
print(human.classname)
print(human.showname('Vasya'))
print(human.show_private())

male = Male()
print(male.classname)
print(male.show_class_name())

female = Female()
print(female.classname)
print(female.show_class_name())





