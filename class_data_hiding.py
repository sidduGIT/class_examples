class Counter:
    __hiddencounter=0

    def count(self):
        self.__hiddencounter += 1
        print(self.__hiddencounter)

c=Counter()
c.count()
c.count()
#print(c.__hiddencounter) #this produces an error to print its value

print(c._Counter__hiddencounter)
