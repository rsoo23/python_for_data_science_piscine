
from abc import ABC, abstractmethod


# ABC: abstract base class
# - a method with a declaration but not a definition / no implementation is an
# abstract method
# - you cannot instantiate abstract classes

class Character(ABC):
    '''Character class'''
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        '''Character abstract class constructor'''
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        '''The person dies'''
        self.is_alive = False


class Stark(Character):
    '''Stark class'''
    def __init__(self, first_name, is_alive=True):
        '''Stark class constructor'''
        super().__init__(first_name, is_alive)

    def die(self):
        '''The person dies'''
        self.is_alive = False
