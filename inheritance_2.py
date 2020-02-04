class Parent:
    pname=''
    cname=''

    def show_parent(self):
        print('Parent name = {}'.format(self.pname))

class Child(Parent):

    def show_child(self):
        print('Child name = {}'.format(self.cname))

ch=Child()
ch.pname='siddu'
ch.cname='atharv'
ch.show_parent()
ch.show_child()

ch1=Child()
ch1.pname='santu'
ch1.cname='karu'
ch1.show_parent()
ch1.show_child()

#multiple child class

class Parent:
    pname=''
    cname=''

    def show_parent(self):
        print('Parent name = {}'.format(self.pname))

class Child1(Parent):

    def show_child1(self):
        print('Child1 name = {}'.format(self.cname))

class Child2(Parent):

    def show_child2(self):
        print('Child2 name = {}'.format(self.cname))

print('two Child classes from single parent')
ch1=Child1()
ch1.pname='siddu'
ch1.cname='surabhi'
ch1.show_parent()
ch1.show_child1()
ch2=Child2()
ch2.pname='siddu'
ch2.cname='atharv'
ch2.show_parent()
ch2.show_child2()

#multiple parent classes

class Father:
    fname=''

    def show_father(self):
            print('Father name is {}'.format(self.fname))

class Mother:
    mname=''

    def show_mother(self):
            print('Mather name is {}'.format(self.mname))

class Son(Father,Mother):
    sname=''

    def show_son(self):
        print('Sons name is {}'.format(self.sname))

class Daughter(Father,Mother):
    dname=''

    def show_daughter(self):
        print('Daughters name is {}'.format(self.dname))

print('Child classes from Multiple Parent class')
son1=Son()
son1.fname='siddu'
son1.mname='sunanda'
son1.sname='atharv'
son1.show_father()
son1.show_mother()
son1.show_son()
dtr1=Daughter()
dtr1.fname='siddu'
dtr1.mname='sunanda'
dtr1.dname='surabhi'
dtr1.show_father()
dtr1.show_mother()
dtr1.show_daughter()







