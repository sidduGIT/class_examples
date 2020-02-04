#Write a Python program to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
#for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid^.

class Validate:

    def validate(self,str1):
        stack=[]
        pchar={'(':')','{':'}','[':']'}
        for i in str1:
            if i in pchar:
                stack.append(i)
            elif len(stack)==0 or pchar[stack.pop()]!=i:
                return False
        return len(stack)==0

print(Validate().validate('(){}[]'))
print(Validate().validate('({})'))
print(Validate().validate('[{}])'))

#Write a Python class to get all possible unique subsets from a set of distinct integers.

class Class_subsets:

    def subsets(self,lst):
        subset=[]
        for i in range(len(lst)+1):
            for j in range(i+1,len(lst)+1):
                subset.append(lst[i:j])
        return sorted(subset)

print(Class_subsets().subsets([4,5,6]))

#Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number. - Go to the editor
#Input: numbers= [10,20,10,40,50,60,70], target=50
#Output: 3, 4

from itertools import combinations
class Pair:
    def pair_elements(self,lst):
        combi=[]
        for n in combinations(lst,2):
            if n[0]+n[1]==60:
                #print(n)
                combi.append(n)
        return combi
print(Pair().pair_elements([10,20,10,40,50,60,70]))

from itertools import combinations
lst=[10,20,10,40,50,60,70]
print(list(combinations(lst,2)))
for n in combinations(lst,2):
    if n[0]+n[1]==60:
        print(n)

for n in combinations(lst,3):
    if n[0]+n[1]+n[2]==70:
        print(n)

#Write a Python class to find the three elements that sum to zero from a set of n real numbers.

class Sumtozero:

    def sumtozero(self,lst):
        combi=[]
        for n in combinations(lst,3):
            if n[0]+n[1]+n[2]==0:
                combi.append(n)
        return combi

print(Sumtozero().sumtozero([-25, -10, -7, -3, 2, 4, 8, 10]))

#Write a Python class to reverse a string word by word

class Reverse:

    def reverse(self,str1):
        words=str1.split()
        words=words[::-1]
        return ' '.join([word[::-1] for word in words])

print(Reverse().reverse('siddu bagewadi from bijapur'))

#Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.

class Strings:
    
    def __init__(self,str1):
        self.str1=str1

    def get_string(self):
        self.str1=input('enter string')
    
    def print_string(self):
        print(self.str1.upper())

obj=Strings('Atharv')
print('getting user string')
obj.get_string()
print('printing user string in upper')
obj.print_string()

#Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.

class Rectangle:

    def __init__(self,leng,bred):
        self.leng=leng
        self.bred=bred

    def get_params(self):
        self.leng=float(input('enter leng'))
        self.bred=float(input('enter bred'))

    def area(self):
        print('area=',self.leng*self.bred)

obj=Rectangle(10,20)
obj.get_params()
obj.area()
    
#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle. 

class Circle:

    def __init__(self,rad):
        self.rad=rad

    def perimeter(self):
        print('perimeter=',2*3.142*self.rad)
    
    def area(self):
        print('area=',3.142*self.rad*self.rad)

obj=Circle(2.5)
obj.perimeter()
obj.area()






