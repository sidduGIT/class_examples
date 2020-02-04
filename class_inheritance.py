class Parent:

    parentattr=100

    def __init__(self):
        print('calling parent constructor')

    def set_parent_attr(self,attr):
        Parent.parentattr=attr

    def calling_parent(self):
        print('calling parent')

    def get_parent_attr(self):
        print('parent attribute',Parent.parentattr)

class Child(Parent):

    def __init__(self):
        print('calling child constructor')

    def child_method(self):
        print('calling child method')

c1=Child()
c1.child_method()
c1.calling_parent()
print('calling sett attr for parent')
c1.set_parent_attr(200)
print('calling get attr for parent')
c1.get_parent_attr()
p1=Parent()

print('is Child is subclass of Parent',issubclass(Child,Parent))
print('is c1 is object of Child',isinstance(c1,Child))
print('is p1 is object of Parent',isinstance(c1,Parent))

