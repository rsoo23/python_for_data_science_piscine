
from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''Constructor of a King class with params: \
first_name, is_alive (default: true)'''
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def set_eyes(self, new_eyes):
        self.eyes = new_eyes

    def set_hairs(self, new_hairs):
        self.hairs = new_hairs

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs
