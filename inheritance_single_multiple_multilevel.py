#single,multiple and multilevel inheritance

class Father:
    pass

class Mother:
    pass

#single
class Child1(Father):
    pass

#multiple
class Child2(Father,Mother):
    pass

#multilevel
class Grandfather:
    pass

class Father(Grandfather):
    pass

class Child(Father):
    pass

ch1=Child1()
print(Child1.__bases__)
ch2=Child2()
print(Child2.__bases__)
ch=Child()
print(Father.__bases__)
print(Child.__bases__)
