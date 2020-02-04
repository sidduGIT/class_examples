#Indexing and Slicing with __getitem__ and __setitem__ 

class Counter:

    def __init__(self,index):
        self.index=[None]*index

    def __setitem__(self,index_number,data):
        self.index[index_number]=data

    def __getitem__(self,index_number):
        return self.index[index_number]

index=Counter(4)
print(index)

index[0]='ABCD'
index[1]='EFGH'
index[2]='IJKL'
index[3]='MNOP'
print(index[2])
