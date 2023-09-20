
from give_bmi import give_bmi, apply_limit

print("Normal test:")
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
print()

# Expected Output
# [22.507863455018317, 29.0359168241966] <class 'list'>
# [False, True]

print("Negative values:")
height = [-2.71, 1.15]
weight = [165.3, -38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
print()

print("Different list size:")
height = [2.71, 1.15]
weight = [165.3, 38.4, 2349]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
print()

print("Different data type:")
height = [2.71, 1.15]
weight = "string"
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
print()

print("One is none:")
height = [2.71, 1.15]
weight = None
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
print()

print("Different element data type:")
height = [2.71, 1.15]
weight = [165.3, "sdf"]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
print()

print("Wrong dimension:")
height = [[2.71, 3], [1.15, 6]]
weight = [[165.3, 34], [1.15, 6]]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
print()

print("Negative bmi limit:")
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, -3))
print()
