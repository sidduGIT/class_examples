class Pet:
    num_pets=0

    def __init__(self,name):
        self.name=name
        Pet.num_pets+=1

    def show(self):
        print('My name is {} and I have {} pets'.format(self.name,Pet.num_pets))

dog=Pet('Dog')
cat=Pet('Cat')
dog.show()
cat.show()
