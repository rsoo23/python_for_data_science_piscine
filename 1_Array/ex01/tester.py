
from array2D import slice_me

print("Normal test:")
family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
print()

# Expected output:
# My shape is : (4, 2)
# My new shape is : (2, 2)
# [[1.8, 78.4], [2.15, 102.7]]

# My shape is : (4, 2)
# My new shape is : (1, 2)
# [[2.15, 102.7]]

print("Wrong family data type:")
family = "hi"
print(slice_me(family, 0, 2))
print()

print("Wrong dimension:")
family = [1.80, 78.4, 33]
print(slice_me(family, 0, 2))
print()

print("Incorrect element dimension:")
family = [[1.80, 78.4], [[19, 23], [123, 33]], [2.10, 98.5], [1.88, 75.2]]
print(slice_me(family, 0, 2))
print()

print("Incorrect element shape:")
family = [[1.80, 78.4], [34, 4.3, 3.5], [2.10, 98.5], [1.88, 75.2]]
print(slice_me(family, 0, 2))
print()

print("Invalid start / end:")
family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
print(slice_me(family, 0, 's'))
print(slice_me(family, "sldkf", 2))
print()
