
from S1E9 import Character, Stark

print("Normal class tests:")
Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)
print()
print()

print("Abstract class instantiation test:")
hodor = Character("hodor")

# Expected Output
# {'first_name': 'Ned', 'is_alive': True}
# True
# False
# Your docstring for Class
# Your docstring for Constructor
# Your docstring for Method
# ---
# {'first_name': 'Lyanna', 'is_alive': False}
