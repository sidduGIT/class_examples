class Print():
    
    def get_string(self):
        self.str1=input('enter a string')

    def put_string(self):
        print('string entered',self.str1)

    def reverse_string(self):
        print('reverse of a string',self.str1[::-1])

    def len_string(self):
        print('length of a entered string',len(self.str1))

    def caps_string(self):
        print('capitals of a string',self.str1.upper())

obj=Print()
obj.get_string()
obj.put_string()
obj.reverse_string()
obj.len_string()
obj.caps_string()
