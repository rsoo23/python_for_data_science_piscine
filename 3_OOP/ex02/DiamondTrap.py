
from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''King class'''
    def __init__(self, first_name, is_alive=True):
        '''King class constructor'''
        super().__init__(first_name, is_alive)

    def set_eyes(self, new_eyes):
        '''Setter for eyes'''
        self.eyes = new_eyes

    def set_hairs(self, new_hairs):
        '''Setter for hairs'''
        self.hairs = new_hairs

    def get_eyes(self):
        '''Getter for eyes'''
        return self.eyes

    def get_hairs(self):
        '''Getter for hairs'''
        return self.hairs

    def die(self):
        '''The person dies'''
        self.is_alive = False
