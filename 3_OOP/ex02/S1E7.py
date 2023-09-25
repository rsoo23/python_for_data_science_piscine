
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
    '''Constructor of a Baratheon class with params: \
first_name, is_alive (default: true)'''
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        return 'Vector: ' + \
            str((self.__class__.__name__, self.eyes, self.hairs))

    def __repr__(self):
        return 'Vector: ' + \
            repr((self.__class__.__name__, self.eyes, self.hairs))


class Lannister(Character):
    '''Constructor of a Lannister class with params: \
first_name, is_alive (default: true)'''
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        return 'Vector: ' + \
                str((self.__class__.__name__, self.eyes, self.hairs))

    def __repr__(self):
        return 'Vector: ' + \
            repr((self.__class__.__name__, self.eyes, self.hairs))

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)
