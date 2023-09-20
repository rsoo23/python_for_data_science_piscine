
from load_image import ft_load

print("Valid file test: ")
print(ft_load("landscape.jpg"))
print()

print("Invalid file test: ")
print(ft_load("landscap.jpg"))
print(ft_load(2))
print()
