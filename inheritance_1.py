class Parent:
    x=1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x,Child1.x,Child2.x)
Child1.x=2
print(Parent.x,Child1.x,Child2.x)
Child2.x=3
print(Parent.x,Child1.x,Child2.x)

def extendlist(val,list=[]):
    list.append(val)
    return list

lst1=extendlist(10)
lst2=extendlist(123,[])
lst3=extendlist('a')
print(lst1)
print(lst2)
print(lst3)


def extendlist1(val,list=None):
    if list is None:
        list.append(val)
    return list

lst4=extendlist(10)
lst5=extendlist(123,[])
lst6=extendlist('a')
print(lst4)
print(lst5)
print(lst6)


def multi():
    return [lambda x: i*x for i in range(4)]

print([m(2) for m in multi()])


lst=[[]]*5
print(lst)
lst[0].append(10)
print(lst)
lst[1].append(20)
print(lst)
lst.append(30)
print(lst)

