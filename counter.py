class Counter:

    def __init__(self,low,high):
        self.current=low
        self.high=high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current+=1
            return self.current-1

for num in Counter(0,15):
    print(num)


class Reverse:

    def __init__(self,str1):
        self.str1=str1
        self.index=len(str1)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index==0:
            raise StopIteration
        else:
            self.index-=1
            return self.str1[self.index]
test=Reverse('Python')
result=''
for ch in test:
    result+=ch
print(result)

class Reverse:

    def __init__(self,str1):
        self.str1=str1
        self.index=len(str1)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index<0:
            raise StopIteration
        else:
            self.index-=1
            return self.str1[self.index]
print('*'*20)
for ch in Reverse('Python'):
    print(ch)
