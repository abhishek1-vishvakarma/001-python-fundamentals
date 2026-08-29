# List / Dict / Set Comprehensions in Python

# Introduction: Comprehensions are a short and clean way to create collections using a loop in a single line.

# There are three important types:

# List Comprehension
# Dict Comprehension
# Set Comprehension

# 1. List Comprehension ⭐:

# A List Comprehension is used to create list:
# Syntaxt 1: [expression for item in iterable] --------- (1)
# Syntaxt 2: [expression for item in iterable if condition] --------- (2)
# Syntaxt 3: [expression for item in iterable if condition] --------- (3)
# Syntaxt 4: [expression_if_true if condition else expression_if_false for item in iterable] --------- (4)


# Normal For Loop:

numbers = []

for i in range(1, 6):
  numbers.append(i)

# print(numbers)

# Using List Comprehension:
numbers = [i for i in range(1,6)] # By equation ----- (1)

# print(numbers)


# 2. List Comprehension with Condition

# Normal:

numbers = []

for i in range(1, 6):
  if i % 2 == 0:
    numbers.append(i)

# print(numbers)

# With Condition:

even_numbers = [i for i in range(1,6) if i % 2 == 0]  # By equation --------- (2)
# print(even_numbers)


# 3. List Comprehension with expression:

# Square numbers:
squares = [i**2 for i in range(1, 6)]  # By equation --------- (3)
# print(squares)

# Another example:

names = ['Abhishek', 'Peter', 'Ava', 'MJ']

upper_names = [name.upper() for name in names]  # By equation --------- (3)
# print(upper_names)


# List Comprehension with if-else:

numbers = [ "even" if i % 2 == 0 else "odd" for i in range(1, 6)]  # By equation --------- (4)
# print(numbers)


# 5. Dictionary Comprehension ⭐:
# Introduction: Dictionary Comprehension is used to create dictionaries:
# Syntax1: {key: value for item in iterable} ----- (1)
# Syntax2: {key: value for item in iterable if condition} ------- (2)

# Normal Loop:

squares = {}

for i in range(1,6):
    squares[i] = i ** 2


# print(squares)


# Dictionary Comprehension:

squares = {i: i ** 2 for i in range(1,6)} # By equation ---- (1)
# print(squares)

# Dictionary Comprehension with condition:

squares = {i: i ** 2 for i in range(1, 6) if i % 2 == 0} # By equation ------ (2)

# print(squares)

# 7. Set Comprehension ⭐
# A Set comprehension creates a set.
# Syntax1: {expression for item in iterable} ----- (1)
# Syntax1: {expression for item in iterable if condition} ----- (2)

# Normal Loop:

numbers = {1, 2, 2, 3, 3, 4}
unique = set()

for num in numbers:
   unique.add(num)

# print(unique)

# Set Comprehension:

unique = {num for num in numbers} #By equation ------ (1)
# print(unique)


# 8. Set Comprehension with Condition

even_numbers = {num for num in numbers if num % 2 == 0} # By equation ------ (2)
# print(even_numbers)

# 10. Practical Examples:

# List --- Filter salaries:

salaries = [200000, 350000, 250000, 150000, 100000]
high_salaries = [salary for salary in salaries if salary > 200000]
# print(high_salaries)

# Dictionary — Create employee salaries:

employee = {name: 3000 for name in names}
# print(employee)


# Set — Extract unique values:

skills = ["Python", "FastAPI", "Python", "AI", "FastAPI"]

unique_skills = {skill for skill in skills}
# print(unique_skills)

# 11. Nested Comprehension:

result = []

for i in range(1,5):
   for j in range(1,5):
      result.append((i,j))

# print(result)

# Comprehension:

result = [(i,j) for i in range(1, 5) for j in range(1,5)]
# print(result)


# ⭐ Quick Revision
# COMPREHENSIONS
# │
# ├── List
# │   └── [expression for item in iterable]
# │
# ├── Dictionary
# │   └── {key: value for item in iterable}
# │
# └── Set
#     └── {expression for item in iterable}
# Most important examples:
# # List
# squares = [x ** 2 for x in range(1, 6)]

# # List + condition
# even = [x for x in range(1, 11) if x % 2 == 0]

# # Dictionary
# squares = {x: x ** 2 for x in range(1, 6)}

# # Set
# unique = {x for x in [1, 2, 2, 3, 3, 4]}

