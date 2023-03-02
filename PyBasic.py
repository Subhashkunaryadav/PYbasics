# Importing  modules
import random
import time

# Defining functions
def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

def multiply_numbers(x, y):
    return x * y

def divide_numbers(x, y):
    return x / y

#  user input
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

#  operations
print("The sum of {} and {} is {}".format(x, y, add_numbers(x, y)))
print("The difference between {} and {} is {}".format(x, y, subtract_numbers(x, y)))
print("The product of {} and {} is {}".format(x, y, multiply_numbers(x, y)))
print("The quotient of {} and {} is {}".format(x, y, divide_numbers(x, y)))

# Generating random number
random_number = random.randint(1, 10)
print("Random number between 1 and 10 is {}".format(random_number))

# Pausing program for 2 seconds
print("Pausing for 2 seconds...")
time.sleep(2)

# Using conditional statements
if random_number > 5:
    print("The random number is greater than 5.")
else:
    print("The random number is less than or equal to 5.")

#  Using loops
for i in range(1, 11):
    print(i)

#  Using lists
fruits = ["apple", "banana", "cherry", "orange", "kiwi"]
print("My favorite fruit is {}".format(fruits[0]))
print("All fruits: {}".format(fruits))

#  Using dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print("Person's name is {}".format(person["name"]))
print("Person's age is {}".format(person["age"]))
print("Person's city is {}".format(person["city"]))

#  Using try-except blocks
try:
    result = x / y
    print("The division of {} and {} is {}".format(x, y, result))
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print("Error occurred: {}".format(e))

#  Using file operations
file_name = "test.txt"
with open(file_name, "w") as file:
    file.write("Hello, world!")

with open(file_name, "r") as file:
    content = file.read()
    print(content)

#  Using classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print("Hello, my name is {} and I am {} years old.".format(self.name, self.age))

person = Person("John", 30)
person.say_hello()
