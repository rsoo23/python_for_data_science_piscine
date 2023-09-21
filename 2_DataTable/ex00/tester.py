
from load_csv import load

print("Invalid file name")
print(load("life_expectancy.csv"))
print()

print("Incorrect data type")
print(load(None))
print(load(1))
print()

print("Valid file name")
print(load("life_expectancy_years.csv"))
print()
