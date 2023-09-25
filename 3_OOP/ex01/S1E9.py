
from abc import ABC, abstractmethod


# ABC: abstract base class
# - a method with a declaration but not a definition / no implementation is an
# abstract method
# - you cannot instantiate abstract classes

class Character(ABC):
    '''Character class that inherits from the abstract base class'''
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        '''Constructor with params: first_name, is_alive (default: true)'''
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        '''The person dies'''
        self.is_alive = False


class Stark(Character):
    '''Stark class that inherits from the Character class'''
    def __init__(self, first_name, is_alive=True):
        '''Constructor of a Stark class with params: \
first_name, is_alive (default: true)'''
        super().__init__(first_name, is_alive)
