
import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''generates a random id (15 lowercase alphabets)'''
    return "".join(random.choices(string.ascii_lowercase, k=15))


# dataclass decorator simplifies the creation of the classes
@dataclass
class Student:
    '''Student class'''
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        '''initializatino for login and id'''
        self.login = self.name[0] + self.surname
        self.id = generate_id()
