
from S1E9 import Character


# super(): calls the constructor of the Character class, allowing
# 		   it to initialize its own attributes and perform any
#          necesaary setup, before any additional initialization
#          specific to the Baratheon class is performed
# - maintains proper inheritance hierarchy and avoids duplication of code

# str():
# - returns a human readable string representation of an object
# - used for creating user-friendly output and for displaying the object
#   as a string

# repr():
# - returns an unambiguous string representation of the object
# - used for debugging and development purposes to get the complete
#   information of the object
class Baratheon(Character):
    '''Baratheon class'''
    def __init__(self, first_name, is_alive=True):
        '''Baratheon class constructor'''
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = self.__class__.__name__
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        '''__str__ implementation'''
        return 'Vector: ' + \
            str((self.__class__.__name__, self.eyes, self.hairs))

    def __repr__(self):
        '''__repr__ implementation'''
        return 'Vector: ' + \
            repr((self.__class__.__name__, self.eyes, self.hairs))

    def die(self):
        '''The person dies'''
        self.is_alive = False


class Lannister(Character):
    '''Lannister class'''
    def __init__(self, first_name, is_alive=True):
        '''Lannister class constructor'''
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = self.__class__.__name__
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        '''__str__ implementation'''
        return 'Vector: ' + \
            str((self.__class__.__name__, self.eyes, self.hairs))

    def __repr__(self):
        '''__repr__ implementation'''
        return 'Vector: ' + \
            repr((self.__class__.__name__, self.eyes, self.hairs))

    def die(self):
        '''The person dies'''
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        '''Creates a Lannister class using a method'''
        return cls(first_name, is_alive)
