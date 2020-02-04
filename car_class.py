class Car:
    def __init__(self,modelname,price,yearm):
        self.modelname=modelname
        self.price=price
        self.yearm=yearm

    def display(self):
        print('information of car')
        print('model= ',self.modelname)
        print('price= ',self.price)
        print('year_of_manufatuare ',self.yearm)

    def increase_price(self):
        self.price=int(self.price*1.15)
        #print(self.price)

car1=Car('honda',1000000,2017)
car1.display()

car1.increase_price()
car1.display()

car2=Car('TATA',600000,2018)
car2.display()
