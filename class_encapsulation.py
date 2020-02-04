'''
The wrapping up of data and functions into a single unit (called class) is known as encapsulation. Data encapsulation is the most striking feature of a class. The data is not accessible to the outside world, and only those functions, which are wrapped in the class, can access it. These functions provide the interface between the object’s data and the program. This insulation of the data from direct access by the program is called data hiding or information hiding.'''


class Encapsulation:
    __name=None
    emp_id=100887
    salary='1.5 lakh'

    def __init__(self,name):
        self.__name=name

    def display(self):
        print(self.__name)
name1=Encapsulation('Siddu')
#print(name1.__name)
print(name1.emp_id)
print(name1.salary)
name1.display()

