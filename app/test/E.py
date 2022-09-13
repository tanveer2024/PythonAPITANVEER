class E:
    """A Sample Employee class"""

    # The __init__ method is the Python equivalent of the C++ constructor 
    # in an object-oriented approach. The __init__ function 
    # is called every time an object is created from a class. 
    # The __init__ method lets 
    # the class initialize the object's 
    # attributes and serves no other purpose. It is only used within classes.

    # Python programming provides us with a built-in
    #  @property decorator which makes usage of getter and setters much easier
    #  in Object-Oriented Programming.


    raise_amt = 1.05
    def __init__(self,first,last,pay): 
        self.first = first
        self.last = last
        self.pay = pay


    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)        


