'''
getting parent classes of a class'''

class A:
    pass

class B:
    pass

class C(A,B):
    pass

print(C.__bases__)
