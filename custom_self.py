#creating our own self object

class Employee:

    def __init__(atharv,name,age):
        atharv.name=name
        atharv.age=age

    def display(atharv):
        print('Name=',atharv.name)
        print('Age=',atharv.age)

emp1=Employee('siddu',42)
emp1.display()
