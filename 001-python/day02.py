# Exception Handling in Python
# try:
#     num = int(input("Enter a number:"))
#     print(10 / num)

# except:
#     print("Something went wrong")


# try:
#    num = int(input("Enter a number: "))
#    result = 10 / num
#    print(result)
# except ValueError:
#    print("Please enter a valid number")
# except ZeroDivisionError:
#    print("Cannot devide by zero")
# except TabError:
#    print("wrong data type")


# ValueError
try:
    num = int("hello")

except ValueError:
    print("ValueError: Invalid value")


# TypeError
try:
    result = 10 + "20"

except TypeError:
    print("TypeError: Wrong data type")


# ZeroDivisionError
try:
    result = 10 / 0

except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero")


# IndexError
try:
    numbers = [10, 20, 30]
    print(numbers[5])

except IndexError:
    print("IndexError: Invalid list index")


# KeyError
try:
    user = {"name": "Abhishek"}
    print(user["email"])

except KeyError:
    print("KeyError: Dictionary key does not exist")


# FileNotFoundError
try:
    with open("unknown.txt", "r") as file:
        data = file.read()

except FileNotFoundError:
    print("FileNotFoundError: File does not exist")


# NameError
try:
    print(username)

except NameError:
    print("NameError: Variable does not exist")
