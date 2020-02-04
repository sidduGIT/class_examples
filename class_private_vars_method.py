'''
If the name of a Python function, class method, or attribute starts with (but doesn't end with) two underscores, it's private; everything else is public.'''

class Test:
    __private_var=100
    public_var=200

    def __private_func(self):
        print('I am private function')

    def public_func(self):
        print('I am public function')
        print('and my public variable is',self.public_var)

    def calling_private_var_func(self):
        self.__private_func()
        print('and my private variable is',self.__private_var)

t=Test()
t.calling_private_var_func()
t.public_func()
