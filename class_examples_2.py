# class Number():
#     num=1234
#
# n1=Number()
# print(n1,type(n1),id(n1))
# print(n1.num)
#
# n2=Number()
# print(n2,type(n2),id(n2))
# print(n2.num)
#
#
# class simple:
#     company='Fungible'
#
#     def input(self):
#         self.name=input('enter name')
#         self.empid=int(input('enter empid'))
#         self.salary=int(input('enter salary'))
#
#     def output(self):
#         print('Name={} Empid={} Salary={}'.format(self.name,self.empid,self.salary))
#
# s1=simple()
# s1.input()
# s1.output()
# print('Company={}'.format(s1.company))

# class Message():
#
#     def __init__(self):
#         self.msg=None
#
#     def assignValue(self):
#         self.msg='Hello World'
#
#     def getValue(self,str1):
#         self.msg=str1
#
#     def printValue(self):
#         print('The message is={}'.format(self.msg))
#
# m1=Message()
# m1.printValue()
# m1.assignValue()
# m1.printValue()
# m1.getValue('Hello Siddu')
# m1.printValue()

#class Person:

    # def __init__(self):
    #     self.name='XYZ'
    #     self.age=0

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def display(self):
#         print('Name={}  Age={}'.format(self.name,self.age))
#
# # p1=Person()
# # p1.display()
# #
# # p1.name='Siddu'
# # p1.age=40
# # p1.display()
#
# p2=Person('Atharv',4)
# p2.display()

# class Employee:
#
#     def __init__(self,empid,name,dept,salary,city):
#         self.empid=empid
#         self.name=name
#         self.dept=dept
#         self.salary=salary
#         self.city=city
#
#     def setValue(self,empid,name,dept,salary,city):
#         self.empid = empid
#         self.name = name
#         self.dept = dept
#         self.salary = salary
#         self.city = city
#
#     def display(self):
#         print('Empid={}  Name={}  Dept={}   Salry={}   City={}'.format(self.empid,self.name,self.dept,self.salary,self.city)
#               )
#
# e1=Employee(1000,'siddu','symmetrix',150000,'Bangalore')
# e1.display()
# e1.setValue(1001,'santu','vmax',150000,'Bangalore')
# e1.display()

# class Employee:
#
#     def __init__(self): #Constructor
#         self.__id = 1000
#         self.__name = "siddu"
#         self.__gender = "Male"
#         self.__city = "Bangalore"
#         self.__salary = 150000
#
#     def setId(self,id):  #setters
#         self.__id=id
#
#     def  getId(self):   #getters
#         return self.__id
#
#     def setName(self,name):
#         self.__name=name
#
#     def getName(self):
#         return self.__name
#
#     def setGender(self,gender):
#         self.__gender=gender
#
#     def getGender(self):
#         return self.__gender
#
#     def setCity(self,city):
#         self.__city=city
#
#     def getCity(self):
#         return self.__city
#
#     def setSalary(self,salary):
#         self.__salary=salary
#
#     def getSalary(self):
#         return self.__salary
#
# def main():
#
#     print('Enter Employee data')
#     id=int(input('enter id'))
#     name=input('enter name')
#     gender=input('enter gender')
#     city=input('enter city')
#     salary=int(input('enter salary'))
#
#     e1=Employee()
#
#     e1.setId(id)
#     id1=e1.getId()
#
#     e1.setName(name)
#     name1=e1.getName()
#
#     e1.setGender(gender)
#     gender1=e1.getGender()
#
#     e1.setSalary(salary)
#     salary1=e1.getSalary()
#
#     e1.setCity(city)
#     city1=e1.getCity()
#
#     print('Employee data is as follows')
#     print('ID={}'.format(id1))
#     print('Name={}'.format(name1))
#     print('Gender={}'.format(gender1))
#     print('City={}'.format(city1))
#     print('Salary={}'.format(salary1))
#
# if __name__=='__main__':
#     main()

'''In this program, we are implementing Properties.
Python offers a better way to implement setters and getter with the help of properties by using attribute @property.
By default properties are getters so we have to declare setter part explicitly.'''

# class Employee:
#     def __init__(self): #Constructor
#         self.__id = 0
#         self.__name = ""
#         self.__gender = ""
#         self.__city = ""
#         self.__salary = 0
#
#     @property
#     def id(self):
#         return self.__id
#
#     @id.setter
#     def id(self,value):
#         self.__id=value
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def gender(self):
#         return self.__gender
#
#     @gender.setter
#     def gender(self, value):
#         self.__gender = value
#
#     @property
#     def city(self):
#         return self.__city
#
#     @city.setter
#     def city(self, value):
#         self.__city = value
#
#     @property
#     def salary(self):
#         return self.__salary
#
#     @salary.setter
#     def salary(self, value):
#         self.__salary = value
#
# def main():
#     print("Enter Employee Data:")
#     i = int(input("Enter Id\t:"))
#     n = input("Enter Name\t:")
#     g = input("Enter Gender:")
#     c = input("Enter City\t:")
#     s = int(input("Enter Salary:"))
#
#     e=Employee()
#     e.id=i
#     e.name=n
#     e.gender=g
#     e.city=c
#     e.salary=s
#     id2 = e.id
#     name2 = e.name
#     gender2 = e.gender
#     city2 = e.city
#     salary2 = e.salary
#
#
#     print("\nDisplaying Employee Data:")
#     print("Id\t\t:", id2)
#     print("Name\t:", name2)
#     print("Gender\t:", gender2)
#     print("City\t:", city2)
#     print("Salary\t:", salary2)
#
#
# if __name__=="__main__":
#     main()

'''In this program, we are implementing the concept of Interface using class. 
Here, Class Shape worked as Interface. In Interface all methods must be non-implemented 
it must be implemented in child class unlike abstract class, 
where we can have some implemented members.'''
# import math
#
# class Shape():
#
#     def input(self):
#         pass
#
#     def process(self):
#         pass
#
#     def output(self):
#         pass
#
# class Circle(Shape):
#
#     def __init__(self,rad=0.0):
#         self.__radius=rad
#         self.__area=0.0
#
#     def input(self):
#         self.__radius=float(input('enter radius'))
#
#     def process(self):
#         self.__area=math.pi*math.pow(self.__radius,2)
#
#     def output(self):
#         print('Area of a Circle is   {}'.format(self.__area))
#
# class Rectangle(Shape):
#
#     def __init__(self,l=0.0,b=0.0):
#         self.__len=l
#         self.__bred=b
#         self.__area=0.0
#
#     def input(self):
#         self.__len=float(input('enter length'))
#         self.__bred=float(input('enter breadth'))
#
#     def process(self):
#         self.__area=self.__len*self.__bred
#
#     def output(self):
#         print('Area of a rectanlge   {}'.format(self.__area))
#
# def main():
#     print("Circle Object:")
#     c=Circle()
#     c.input()
#     c.process()
#     c.output()
#
#     print("\nRectangle Object:")
#     r=Rectangle()
#     r.input()
#     r.process()
#     r.output()
# if __name__=="__main__":
#     main()

'''In this program, we have a parent class named Details and child class named Employee, 
we are inheriting the class Details on the class Employee. And, finally creating an object 
of Employee class and by calling the method setEmployee() – we are assigning the values to 
the class variables and printing the values using showEmployee() function.'''

# class Details:
#
#     def __init__(self):
#         self.__id='No id'
#         self.__name='No name'
#         self.__gender='No gender'
#
#     def setData(self,id,name,gender):
#         self.__id=id
#         self.__name=name
#         self.__gender=gender
#
#     def getData(self):
#         print("Id\t\t:", self.__id)
#         print("Name\t\t:", self.__name)
#         print("Gender\t\t:", self.__gender)
#
# class Employee(Details):
#
#     def __init__(self):
#         self.__company='No company'
#         self.__dept='No dept'
#
#     def setEmployee(self,id,name,gender,company,dept):
#         self.setData(id,name,gender)
#         self.__company=company
#         self.__dept=dept
#
#     def showEmployee(self):
#         self.getData()
#         print("Company\t\t:", self.__company)
#         print("Dept\t\t:", self.__dept)
#
# def main():
#     e1=Employee()
#     e1.setEmployee(1000,'Siddu','Male','Dell-Emc','Vmax')
#     e1.showEmployee()
#
# if __name__=='__main__':
#     main()

'''In this program, we have a parent class named Details and two child classes named Employee 
and Doctor, we are inheritance the class Details on the classes Employee and Doctor. 
And, finally creating two objects of Employee and Doctor classes and setting, 
showing the values using their methods.'''

# class Details:
#
#     def __init__(self):
#         self.__id=0
#         self.__name=''
#         self.__gender=''
#
#     def setDetails(self):
#         self.__id=int(input('enter id'))
#         self.__name=input('enter name')
#         self.__gender=input('enter gender')
#
#     def showDetails(self):
#         print('Id\t\t={}'.format(self.__id))
#         print('Name\t\t={}'.format(self.__name))
#         print('Gender\t\t={}'.format(self.__gender))
#
# class Engineer(Details):
#
#     def __init__(self):
#         self.__company=''
#         self.__city=''
#
#     def setEngineer(self):
#         self.setDetails()
#         self.__company=input('enter company name')
#         self.__city = input('enter city name')
#
#     def showEngineer(self):
#         self.showDetails()
#         print('Company\t\t={}'.format(self.__company))
#         print('City\t\t={}'.format(self.__city))
#
# class Docter(Details):
#
#     def __init__(self):
#         self.__hospital=''
#         self.__city=''
#
#     def setDoctor(self):
#         self.setDetails()
#         self.__hospital=input('enter hospital name')
#         self.__city=input('enter city name')
#
#     def showDoctor(self):
#         self.showDetails()
#         print('Hospital\t\t={}'.format(self.__hospital))
#         print('City\t\t={}'.format(self.__city))
#
# def main():
#     print('Enter Engineer details')
#     e=Engineer()
#     e.setEngineer()
#     print('Engineer details are')
#     e.showEngineer()
#
#     print('Enter Doctor details')
#     d=Docter()
#     d.setDoctor()
#     print('Doctor details are')
#     d.showDoctor()
#
# if __name__=='__main__':
#     main()

'''Multiple inheritance
When we have one child class and more than one parent classes then it is called multiple inheritance 
i.e. when a child class inherits from more than one parent class.

In this program, we have two parent classes Personel and Educational and one child class named 
Student and implementing multiple inheritance.'''

# class Personnel:
#
#     def __init__(self):
#         self.__id=0
#         self.__name=''
#         self.__gender=''
#
#     def setPersonnel(self):
#         self.__id=int(input('enter id'))
#         self.__name=input('enter name')
#         self.__gender=input('enter gender')
#
#     def showPersonnel(self):
#         print('Id\t\t={}'.format(self.__id))
#         print('Name\t\t={}'.format(self.__name))
#         print('Gender\t\t={}'.format(self.__gender))
#
# class Educational:
#
#     def __init__(self):
#         self.__stream=''
#         self.__year=''
#
#     def setEducational(self):
#         self.__stream=input('enter stream')
#         self.__year = input('enter stream')
#
#     def showEducational(self):
#         print('Stream\t\t={}'.format(self.__stream))
#         print('Year\t\t={}'.format(self.__year))
#
# class Student(Personnel,Educational):
#
#     def __init__(self):
#         self.__address=''
#         self.__contact=0
#
#     def setStudent(self):
#         self.setPersonnel()
#         self.setEducational()
#         self.__address=input('enter address')
#         self.__contact = input('enter contact number')
#
#     def showStudent(self):
#         self.showPersonnel()
#         self.showEducational()
#         print('Address\t\t={}'.format(self.__address))
#         print('Contact\t\t={}'.format(self.__contact))
#
# def main():
#     s=Student()
#     print('enter student details')
#     s.setStudent()
#     print('show student details')
#     s.showStudent()
#
# if __name__=='__main__':
#     main()

'''Multilevel inheritance
When we have a child class and grandchild class – it is called multilevel inheritance i.e. 
when a class inherits on second class and second class further inherits on another class.

In this program, we have a parent class named Details1 which is inheriting on class 
Details2 and class Details2 further inheriting on the class Details3.'''

# class Details1:
#
#     def __init__(self):
#         self.__id=0
#
#     def setDetails1(self):
#         self.__id=int(input('enter id'))
#
#     def showDetails1(self):
#         print('Id\t\t={}'.format(self.__id))
#
#
# class Details2(Details1):
#
#     def __init__(self):
#         self.__name = ''
#
#     def setDetails2(self):
#         self.setDetails1()
#         self.__name = input('enter name')
#
#     def showDetails2(self):
#         self.showDetails1()
#         print('Name\t\t={}'.format(self.__name))
#
#
# class Details3(Details2):
#
#     def __init__(self):
#         self.__gender = ''
#
#     def setDetails3(self):
#         self.setDetails2()
#         self.__gender = input('enter gender')
#
#     def showDetails3(self):
#         self.showDetails2()
#         print('Gender\t\t={}'.format(self.__gender))
#
# class Employee(Details3):
#
#     def __init__(self):
#         self.__dept=''
#         self.__stream=''
#
#     def setEmployee(self):
#         self.setDetails3()
#         self.__dept=input('enter dept')
#         self.__stream = input('enter stream')
#
#     def showEmployee(self):
#         self.showDetails3()
#         print('Dept\t\t={}'.format(self.__dept))
#         print('Stream\t\t={}'.format(self.__stream))
#
# def main():
#
#     e1=Employee()
#     print('setting employee details')
#     e1.setEmployee()
#     print('showing employee details')
#     e1.showEmployee()
#
# if __name__=='__main__':
#     main()

'''In this program, we are implementing the concept of Abstraction using Abstract Class. 
Here, VEHICLE is Abstract Class and CAR and BIKE are Child Classes. 
VEHICLE class have two unimplemented methods, which are implemented in child Classes.'''

# class Vehicle:
#
#     def start(self,name=''):
#         print(name,'is started')
#
#     def accelerate(self,name=''):
#         pass
#
#     def park(self,name=''):
#         pass
#
#     def stop(self,name=''):
#         print(name,'is stopped')
#
# class Bike(Vehicle):
#
#     def accelerate(self,name=''):
#         print(name,'is accelerating at 60KMPH speed')
#
#     def park(self,name=''):
#         print(name,'is parked at basement')
#
# class Car(Vehicle):
#
#     def accelerate(self,name=''):
#         print(name,'is accelerating at 90KMPH speed')
#
#     def park(self,name=''):
#         print(name,'is parked at basement')
#
# def main():
#
#     print('Bike object')
#     b=Bike()
#     b.start('Bike')
#     b.accelerate('Bike')
#     b.park('Bike')
#     b.stop('Bike')
#
#     print('Car object')
#     c = Car()
#     c.start('Car')
#     c.accelerate('Car')
#     c.park('Car')
#     c.stop('Car')
#
# if __name__=='__main__':
#     main()

'''Total number of objects created using class counter variable'''
#
# class Student:
#
#     counter=0
#
#     def __init__(self,name='',age=0):
#         self.name=name
#         self.age=age
#
#         Student.counter+=1
#
#     def display(self):
#         print('Name\t\t={}'.format(self.name))
#         print('Age\t\t={}'.format(self.age))
#
# def main():
#
#     s1=Student('siddu',40)
#     s2 = Student('santu', 35)
#     s3 = Student('suraj', 20)
#     s4 = Student('suman', 14)
#
#     print('Total number of objects created  {}'.format(Student.counter))
#
# if __name__=='__main__':
#     main()

# class Palindrome:
#
#     def __init__(self,str1):
#         self.str1=str1
#
#     def Palincheck(self):
#         if self.str1==self.str1[::-1]:
#             print('Palindrome')
#         else:
#             print('Not Palindrome')
#
# p=Palindrome('nitin')
# p.Palincheck()
# p1=Palindrome('nitin1')
# p1.Palincheck()
#
# class Check:
#
#     def __init__(self,num):
#         self.num=num
#
#     def Ispalindrome(self):
#         orig=self.num
#         rev=0
#         while(self.num!=0):
#             rem=self.num%10
#             rev=rev*10+rem
#             self.num=self.num//10
#         if orig==rev:
#             print(orig, 'is palindrome')
#         else:
#             print(orig, 'is NOT palindrome')
#
# c=Check(1234321)
# c.Ispalindrome()
#
# c=Check(1234)
# c.Ispalindrome()

'''Building Restaurant Menu using Class in Python
Here, we try to use class in python to build a Menu for the restaurant. 
The Menu will contain the Food Item and its corresponding price. This program aims to 
develop an understanding of using data abstraction in general application.'''
#
# class Food:
#
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#
#     def getprice(self):
#         return self.price
#
#     def __str__(self):
#        return self.name + ' : ' + str(self.getprice())
#
# def buildmenu(items,price):
#     menu=[]
#     for i in range(len(items)):
#         menu.append(Food(items[i],price[i]))
#     return menu
#
# # items
# names = ['Coffee', 'Tea', 'Pizza', 'Burger', 'Fries', 'Apple', 'Donut', 'Cake']
#
# # prices
# costs = [250, 150, 180, 70, 65, 55, 120, 350]
#
# # building food menu
# Foods = buildmenu(names, costs)
#
# n=1
# for item in Foods:
#     print(n,'.',item)
#     n+=1

'''Program to manage a phone store (mobile shop) record using class in Python'''

# class Mobile:
#
#     def __init__(self,phname,model,price):
#         self.phname=phname
#         self.model=model
#         self.price=price
#
#     def getPrice(self):
#         return self.price
#
#     def getModel(self):
#         return self.model
#
#     def __str__(self):
#         return self.phname + ' : ' + str(self.getModel()) + '  ::' + str(self.getPrice())
#
# def prices(rec,phname,model,price):
#     rec.append(Mobile(phname,model,price))
#     return rec
#
# Record=[]
# x='y'
#
# while(x=='y'):
#     phname=input('enter phone name')
#     model = input('enter phone model name')
#     price = input('enter phone price')
#     Record=prices(Record,phname,model,price)
#     x=input('enter another item, y/n')
#
# n = 1
# print("---The list of the phone that store have---")
# for el in Record:
#     print(n,'. ', el)
#     n = n + 1

# Definig a class student, which contain
# name and Roll number and marks of the student
#
# class Student(object):
#     def __init__(self, name, roll, marks):
#         self.name = name
#         self.roll = roll
#         self.marks = marks
#
#     def getmarks(self):
#         return self.marks
#
#     def getroll(self):
#         return self.roll
#
#     def __str__(self):
#         return self.name + ' : ' + str(self.getroll()) + '  ::' + str(self.getmarks())
#
#
# # Defining a function for building a Record
# # which generates list of all the students
# def Markss(rec, name, roll, marks):
#     rec.append(Student(name, roll, marks))
#     return rec
#
#
# # Main Code
# Record = []
# x = 'y'
# while x == 'y':
#     name = input('Enter the name of the student: ')
#     height = input('Enter the roll number: ')
#     roll = input('Marks: ')
#     Record = Markss(Record, name, roll, height)
#     x = input('another student? y/n: ')
#
# # Printing the list of student
# n = 1
# for el in Record:
#     print(n, '. ', el)
#     n = n + 1
#
# class Person(object):
#
#     def get_gender(self):
#         return 'Unknown'
#
# class Male(Person):
#
#     def get_gender(self):
#         return 'Male'
#
# class Female(Person):
#
#     def get_gender(self):
#         return 'Female'
#
# aMale=Male()
# print(aMale.get_gender())
# aFemale=Female()
# print(aFemale.get_gender())
#
# import re
# str1='1234-5678-8910*1112'
# if(re.match('\d{4}-\d{4}-\d{4}-\d{4}',str1)):
#     print('pass')
# else:
#     print('no pass')
#
# str1=list('ABCD')
# for i in range(3):
#     last=str1.pop()
#     str1.insert(0,last)
# print(''.join(str1))
#
#
# class Person:
#
#     species='Homo sapient'
#
#     def __init__(self,name):
#         self.name=name
#
#     def display(self):
#         print('My name is {}'.format(self.name))
#
#     def renamed(self,other):
#         self.name=other
#         print('My changed name is {}'.format(self.name))
#
# obj1=Person('siddu')
# print(obj1.species)
# print(obj1.display())
# print(obj1.renamed('Atharv'))
#
# def fun(n):
#     if n in range(10,20):
#         return True
#     else:
#         return False
# print(fun(15))
# print(fun(12))
# print(fun(5))
#
# #Create a Vehicle class with max_speed and mileage instance attributes
# class Vehicle:
#     maxspeed=0
#     mileage=0
# modelx=Vehicle
# print(modelx.maxspeed,modelx.mileage)
#
# class Vehicle:
#     def __init__(self,maxspeed,mileage):
#         self.maxspeed=maxspeed
#         self.mileage=mileage
# modelx=Vehicle(150,25)
# print(modelx.maxspeed,modelx.mileage)
#
# #Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#     pass
#
# busobj=Bus('Volvo',200,12)
# print('Name of the bus:  {}  Max speed:  {}  Mileage:  {}'.format(busobj.name,busobj.max_speed,busobj.mileage))
#
# class Car(Vehicle):
#     pass
# carobj=Car('Benz',250,15)
# print('Name of the Car:  {}  Max speed:  {}  Mileage:  {}'.format(carobj.name,carobj.max_speed,carobj.mileage))


#Create a Cricle class and intialize it with radius. Make two methods getArea and getCircumference inside this class.
#
# class Circle:
#
#     def __init__(self,radius):
#         self.radius=radius
#
#     def getArea(self):
#         print('Area of a circle is',3.142*self.radius*self.radius)
#
#     def getCircumferance(self):
#         print('Circumferance is',2*3.142*self.radius)
#
# c1=Circle(20.5)
# #c1.radius=20.5
# c1.getArea()
# c1.getCircumferance()
#
# c2=Circle(50.5)
# c2.getArea()
# c2.getCircumferance()
#
# #Create a Student class and initialize it with name and roll number. Make methods to :
# # 1. Display - It should display all informations of the student.
# # 2. setAge - It should assign age to student
# # 3. setMarks - It should assign marks to the student.
#
# class Student:
#
#     def __init__(self,name,rolln):
#         self.name=name
#         self.rolln=rolln
#
#     def display(self):
#         print('Name of the student',self.name)
#         print('Age of the student', self.age)
#         print('Roll number of student',self.rolln)
#         print('Marks of the student',self.marks)
#     def setAge(self,age):
#         self.age=age
#
#     def setMarks(self,marks):
#         self.marks=marks
#
# s1=Student('siddu',100)
# s1.setAge(42)
# s1.setMarks(98)
# s1.display()

# Create a class, Triangle. Its __init__() method should take self, angle1, angle2, and angle3 as arguments. Make sure to set these appropriately in the body of the __init__()method.
# Create a variable named number_of_sides and set it equal to 3.
# Create a method named check_angles. The sum of a triangle's three angles is It should return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.
# Create a variable named my_triangle and set it equal to a new instance of your Triangle class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).
# Print out my_triangle.number_of_sides and print out my_triangle.check_angles().

# class Triangle:
#
#     number_of_sides=3
#
#     def __init__(self,angle1, angle2, angle3):
#         self.angle1=angle1
#         self.angle2 = angle2
#         self.angle3 = angle3
#
#     def check_angles(self):
#         if (self.angle1+self.angle2+self.angle3)==180:
#             return True
#         else:
#             return False
#
# t1=Triangle(90,60,30)
# print(t1.number_of_sides)
# print(t1.check_angles())
#
# t1=Triangle(90,60,20)
# print(t1.number_of_sides)
# print(t1.check_angles())

# Define a class called Songs, it will show the lyrics of a song. Its __init__() method should have two arguments:selfanf lyrics.lyricsis a list. Inside your class create a method
# called sing_me_a_songthat prints each element of lyricson his own line. Define a varible:
#
# happy_bday = Song(["May god bless you, ",
#                    "Have a sunshine on you,",
#                    "Happy Birthday to you !"])
# Call the sing_me_songmehod on this variable.
#
# class Songs:
#
#     def __init__(self,lyrics):
#         self.lyrics=lyrics
#
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)
#
# s1=Songs(["May god bless you, ",
#                    "Have a sunshine on you,",
#                    "Happy Birthday to you !"])
# print(s1.sing_me_a_song())
#
# s2=Songs([1,2,3,4,5,6,7,8,9])
# print(s2.sing_me_a_song())
#
# Define a class called Lunch.Its __init__() method should have two arguments:selfanf menu.Where menu is a string.
# Add a method called menu_price.It will involve a ifstatement:
#
# if "menu 1" print "Your choice:", menu, "Price 12.00", if "menu 2" print "Your choice:", menu, "Price 13.40", else print "Error in menu".
# To check if it works define: Paul=Lunch("menu 1") and call Paul.menu_price().
#
# class Lunch:
#
#     def __init__(self,menu):
#         self.menu=menu
#
#     def menu_price(self):
#         if self.menu=='menu 1':
#             print('Your choice: menu 1')
#             print('Price 12.00')
#         elif self.menu=='menu 2':
#             print('Your choice: menu 2')
#             print('Price 13.40')
#         else:
#             print('Error in menu')
#
# l1=Lunch('menu 1')
# print(l1.menu_price())
#
# l2=Lunch('menu 2')
# print(l2.menu_price())
#
# l3=Lunch('menu 3')
# print(l3.menu_price())
#
# Define a Point3D class that inherits from object Inside the Point3D class, define an __init__() function that
# accepts self, x, y, and z, and assigns these numbers to the member variables self.x,self.y,self.z.
# Define a __repr__() method that returns "(%d, %d, %d)" % (self.x, self.y, self.z).
# This tells Python to represent this object in the following format: (x, y, z). Outside the class definition,
# create a variable named my_point containing a new instance of Point3D with x=1, y=2, and z=3. Finally, print my_point.
#
# class Point3D:
#
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __repr__(self):
#         print("(%d, %d, %d)" % (self.x, self.y, self.z))
#
# p1=Point3D(x=1, y=2,z=3)
# p1.__repr__()
#
# # Define a new class named "Car". For now, since we have to put something inside the class, use the pass keyword.
# #
# # We can use classes to create new objects, which we say are instances of those classes.
# #
# # Below your Car class, create a new object named my_car that is an instance of Car.
#
# class Car(object):
#     pass
# my_car=Car()
#
# # Inside your Car class, replace the pass statement with a new member variable named `condition and give it an
# # initial value of the string "new".
# # At the end of your code, use a print statement to display the condition of my_car.
#
# class Car:
#     condition='new'
# my_car=Car()
# print(my_car.condition)
# #
# # Define the __init__() function of the Car class to take four inputs: self, model, color, and mpg.
# # Assign the last three inputs to member variables of the same name by using the self keyword.
# #
# # Then, modify the object my_car to provide the following inputs at initialization:
# #
# # model = "DeLorean"
# # color = "silver"
# # mpg = 88
#
# class Car:
#
#     condition='new'
#
#     def __init__(self,model,color,mpg):
#         self.model=model
#         self.color=color
#         self.mpg=mpg
#
# my_car=Car("DeLorean","silver",88)
# print(my_car.condition)
#
# # Now that you've created my_car print its member variables:First print the model of my_car. ' \
# # 'Then print out the color of my_car.Finally, print out the mpg of `my_car.
#
# class Car:
#
#     condition='new'
#
#     def __init__(self,model,color,mpg):
#         self.model=model
#         self.color=color
#         self.mpg=mpg
#
# my_car=Car("DeLorean","silver",88)
# print(my_car.condition)
# print(my_car.model)
# print(my_car.color)
# print(my_car.mpg)
#
# # Inside the Car class, add a method named display_car() to Car that will reference the
# # Car's member variables to return the string, "This is a [color] [model] with [mpg] MPG." You can use the str() ' \
# # 'function to turn your mpg into a string when creating the display string.
# # Replace the individual print statements with a single print command that displays the result
# # of calling my_car.display_car().
#
# class Car:
#
#     condition='new'
#
#     def __init__(self,model,color,mpg):
#         self.model=model
#         self.color=color
#         self.mpg=mpg
#
#     def display_car(self):
#         print('This is a {} {} with {} MPG'.format(self.color,self.model,self.mpg))
#
# my_car=Car("DeLorean","silver",88)
# print(my_car.condition)
# my_car.display_car()
#
# # Inside the Car class, add a method drive_car()that sets self.condition to the string "used".
# # Remove the call to my_car.display_car() and instead print only the condition of your car.
# # Then drive your car by calling the drive_car() method.
# # Finally, print the condition of your car again to see how its value changes.
#
# class Car:
#
#     condition='new'
#
#     def __init__(self,model,color,mpg):
#         self.model=model
#         self.color=color
#         self.mpg=mpg
#
#     def display_car(self):
#         print('This is a {} {} with {} MPG'.format(self.color,self.model,self.mpg))
#
#     def drive_car(self):
#         self.condition='used'
#
# my_car=Car("DeLorean","silver",88)
# print(my_car.condition)
# my_car.drive_car()
# print(my_car.condition)
#
# # Create a class ElectricCar that inherits from Car. Give your new class an __init__() method of that includes
# # a "battery_type" member variable in addition to the model, color and mpg.
# # Then, create an electric car named "my_car" with a "molten salt" battery_type. Supply values of your choice for
# # the other three inputs (model, color and mpg).
#
# class Car:
#
#     condition='new'
#
#     def __init__(self,model,color,mpg):
#         self.model=model
#         self.color=color
#         self.mpg=mpg
#
#     def display_car(self):
#         print('This is a {} {} with {} MPG'.format(self.color,self.model,self.mpg))
#
#     def drive_car(self):
#         self.condition='used'
#
# class ElectricCar(Car):
#
#     def __init__(self, model, color, mpg, battery_type):
#         self.model = model
#         self.color = color
#         self.mpg = mpg
#         self.battery_type = battery_type
#
# my_car=ElectricCar('Tesla','Blue','100',"molten salt")
# my_car.display_car()
#
# # Inside ElectricCar add a new method drive_car() that changes the car's condition to the string "like new".
# # Then, outside of ElectricCar, print the condition of my_car.
# # Next, drive my_car by calling the drive_car() function.
# # Finally, print the condition of my_car again
# class Car:
#
#     condition='new'
#
#     def __init__(self,model,color,mpg):
#         self.model=model
#         self.color=color
#         self.mpg=mpg
#
#     def display_car(self):
#         print('This is a {} {} with {} MPG'.format(self.color,self.model,self.mpg))
#
#     def drive_car(self):
#         self.condition='used'
#
# class ElectricCar(Car):
#
#     def __init__(self, model, color, mpg, battery_type):
#         self.model = model
#         self.color = color
#         self.mpg = mpg
#         self.battery_type = battery_type
#
#     def drive_car(self):
#         self.condition='like new'
#
# my_car=ElectricCar('Tesla','Blue','100',"molten salt")
# print(my_car.condition)
# my_car.drive_car()
# print(my_car.condition)
#
# class Jets:
#
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#
# first_item = Jets("F16", "USA")
# print(first_item.name)
# print(first_item.origin)
#
# names=['F14', 'SU33', 'AJS37', 'Mirage2000', 'Mig29', 'A10']
# obj=[0]*len(names)
# for i,v in enumerate(names):
#     #print(i,v)
#     obj[i]=Jets(v,'USA')
# for i in obj:
#     print(i.name,i.origin)
#
#
# class Student:
#
#     def __init__(self,name,rolln):
#         self.name=name
#         self.rolln=rolln
#
#     def display(self):
#         print('Name={}  RollN={}'.format(self.name,self.rolln))
#
#     def setage(self,age):
#         self.age=age
#         print('Age=',self.age)
#
#     def setmarks(self,marks):
#         self.marks = marks
#         print('Marks=', self.marks)
#
# s1=Student('siddu','100')
# s1.setage(42)
# s1.setmarks(98)
# s1.display()
#
# s2=Student('santu','101')
# s2.setage(40)
# s2.setmarks(95)
# s2.display()

# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of
# ​the rectangle.
# Create a method display() that display the length, width, perimeter and area of an object created using an
# instantiation on rectangle class.
# Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and
# another Volume() method to calculate the volume of the Parallelepiped.
#
# class Rectangle:
#
#     def __init__(self,leng,widt):
#         self.leng=leng
#         self.widt=widt
#
#     def Perimeter(self):
#         return 2*self.leng+2*self.widt
#
#     def Area(self):
#         return self.leng*self.widt
#
#     def Display(self):
#         print('Length of Rectanlge',self.leng)
#         print('Width of Rectanlge', self.widt)
#         print('Area of Rectanlge', self.Area())
#         print('Area of Rectanlge', self.Perimeter())
#
# r1=Rectangle(20,40)
# r1.Display()
#
# class Parallelepipede(Rectangle):
#     def __init__(self,leng,widt,hgt):
#         Rectangle.__init__(self,leng,widt)
#         self.hgt=hgt
#
#     def Volume(self):
#         print('Volume of parallelpoid=',self.leng*self.widt*self.hgt)
#
# p1=Parallelepipede(50,60,70)
# p1.Volume()

# Create a Python class Person with attributes: name and age of type string.
# Create a display() method that displays the name and age of an object created via the Person class.
# Create a child class Student  which inherits from the Person class and which also has a section attribute.
# Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
# Create a student object via an instantiation on the Student class and then test the displayStudent method.
#
# class Person:
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def display(self):
#         print('Name=',self.name)
#         print('Age=',self.age)
#
# class Student(Person):
#
#     def __init__(self,name,age,section):
#         Person.__init__(self,name,age)
#         self.section=section
#
#     def display_student(self):
#         print('Student name=',self.name)
#         print('Student age=',self.age)
#         print('Student section=',self.section)
#
# s1=Student('siddu',42,'F')
# s1.display_student()
#
# p1=Person('santu',40)
# p1.display()

# Create a Python class called BankAccount which represents a bank account, having as attributes:
# accountNumber (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method  which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details.
# Give the complete code for the  BankAccount class.
#
# class BankAccount:
#
#     def __init__(self,ac,name,balace):
#         self.ac=ac
#         self.name=name
#         self.balance=balace
#
#     def Deposit(self,deposit):
#         self.balance=self.balance+deposit
#         return self.balance
#
#     def Withdrawal(self,withdraw):
#         self.balance=self.balance-withdraw
#         return self.balance
#
#     def Bankfees(self):
#         self.bankfees=self.balance*.05
#         print('Bank Fees',self.bankfees)
#         self.balance=self.balance-self.bankfees
#         return self.bankfees,self.balance
#
#     def Display(self):
#         print('Name=',self.name)
#         print('Account=',self.ac)
#         # print('Deposit=',self.Deposit())
#         # print('Withdrwal=',self.Withdrawal())
#         print('balance={}'.format(self.balance))
#
# b1=BankAccount('123456','siddu',5500)
# b1.Display()
# b1.Deposit(2000)
# b1.Display()
# b1.Withdrawal(1500)
# b1.Display()
# b1.Bankfees()
# b1.Display()

# In this Python exercise, write a Python program that can define a class with a minimum of two methods.
# Have a user provide input via prompt and then print that input in uppercase in the second method.
# The input can be anything, but the second method must take the input and make the first method input in all
# uppercase with a print statement.
#
# class Simple:
#
#     def __init__(self):
#         pass
#
#     def Method1(self):
#         input1=input('enter name')
#         self.input1=input1
#
#     def Method2(self):
#         print('output: ',self.input1.upper())
#
# s1=Simple()
# s1.Method1()
# s1.Method2()

#Building ATM functionality with python
# from random import randint
#
# class ATM:
#     balance=0
#     current_pin=1234
#
#     def __init__(self):
#         pass
#
#     def Deposit(self,amount):
#         #print('Depositing {} amount'.format(amount))
#         self.balance+=amount
#         print('Balance after Depositing amount: {}  Balance: {}'.format(amount, self.balance))
#
#     def GetPin(self):
#         return self.current_pin
#
#     def Withdraw(self,amount):
#         print('Withdrawing {} amount'.format(amount))
#         self.balance -= amount
#         print('Balance after withdrawing Withdraw amount: {}  Balance: {}'.format(amount,self.balance))
#
#     def PIN_authenticate(self,pin):
#         if self.current_pin==pin:
#             print('User athenticated')
#         else:
#             print('Wrong PIN, please use correct pin')
#
#     def Balance(self):
#         #print('Current balance',self.balance)
#         return self.balance
#
#     def Interest(self):
#         interest=self.balance*.05
#         print('Interest creited',interest)
#         self.balance+=interest
#
#     #def Transaction_ID(self):
#         #randint
#
# # a1=ATM()
# # print('Initial balance',a1.balance)
# # a1.Deposit(2000)
# # a1.Balance()
# # a1.Deposit(5500)
# # a1.Balance()
# # a1.Deposit(2200)
# # a1.Balance()
# #
# # a1.PIN_authenticate('1234')
# # a1.PIN_authenticate('1243')
# #
# # a1.Interest()
# # a1.Balance()
# #
# # a1.Withdraw(500)
# # a1.Balance()
#
# import random
# a1=ATM()
# while True:
#     # Reading id from user
#     pin=int(input('Enter the PIN'))
#     if a1.GetPin() == pin:
#         while True:
#                 # Printing menu
#                 print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")
#
#                 # Reading selection
#                 selection = int(input("\nEnter your selection: "))
#                 #if # View Balance
#                 if selection == 1:
#                    # Printing balance
#                    print(a1.Balance())
#
#                 # Withdraw
#                 elif selection == 2:
#                    # Reading amount
#                    amt = float(input("\nEnter amount to withdraw: "))
#                    ver_withdraw = input("Is this the correct amount, Yes or No ? " + str(amt) + " ")
#
#                    if ver_withdraw == "Yes":
#                        print("Verify withdraw")
#                    else:
#                        break
#
#                    if amt < float(a1.Balance()):
#                       # Calling withdraw method
#                       a1.Withdraw(amt)
#                       # Printing updated balance
#                       print("\nUpdated Balance: " + str(a1.Balance()) + " n")
#                    else:
#                        print("\nYou're balance is less than withdrawl amount: " + str(a1.Balance()) + " n")
#                        print("\nPlease make a deposit.");
#
#                        # Deposit
#                 elif selection == 3:
#                    # Reading amount
#                    amt = float(input("\nEnter amount to deposit: "))
#                    ver_deposit = input("Is this the correct amount, Yes, or No ? " + str(amt) + " ")
#
#                    if ver_deposit == "Yes":
#                        # Calling deposit method
#                        a1.Deposit(amt)
#                        # Printing updated balance
#                        print("\nUpdated Balance: " + str(a1.Balance()) + " n")
#                    else:
#                        break
#
#                 elif selection == 4:
#                    print("nTransaction is now complete.")
#                    print("Transaction number: ", random.randint(10000, 1000000))
#                    #print("Current Interest Rate: ", a1.Interest())
#                    print("Thanks for choosing us as your bank")
#                    exit()
#
#                    # Any other choice
#                 else:
#                    print("nThat's an invalid choice.")
#                 # Loop till id is valid
#     else:
#         print('Invalid PIN, Retry')

#
# from random import choice
#
# class My_list:
#     from random import choice
#
#     def __init__(self,lst):
#         self.lst=[]
#
#     def add_list(self,element):
#         self.lst.append(element)
#
#     def display(self):
#         for i in self.lst:
#             print(i)
#
#     def contains(self,element):
#         if element in self.lst:
#             return True
#         else:
#             return False
#
#     def getRandom(self):
#
#         if not self.lst:
#             return random.choice(self.lst)
#
#
# from random import choice
# lst=My_list([])

