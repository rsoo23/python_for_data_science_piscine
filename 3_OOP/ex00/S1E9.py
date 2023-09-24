from abc import ABC, abstractmethod

# ABC: abstract base class
# - a method with a declaration but not a definition is a
# abstract method
# - you cannot instantiate abstract classes

# - Character is a subclass of ABC
class Character(ABC):
    """Your docstring for Class"""
    @abstractmethod
    def Character(self):


class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, name):
        self.name = name