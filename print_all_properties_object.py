class Animal:

    def __init__(self):
        self.legs=4
        self.eyes=2
        self.name='Dog'
        self.color='Brown'
        self.age=10
        self.kids=0

animal=Animal()
animal.tail=1

temp=vars(animal)

for i in temp:
    print(i,':',temp[i])
