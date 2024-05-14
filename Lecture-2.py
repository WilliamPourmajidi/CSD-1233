# How to define and modify a global variable.


global_counter = 0
print(f"Value of global_counter before modification: {global_counter}")


def increment():
    global global_counter
    global_counter += 1

    print(f"Value of global_counter after modification: {global_counter}")


increment()  # calling the modification function

# Example working with constants

PI = 3.14159  # Defining the constant PI


def calculate_circle_area(radius):
    return PI * radius ** 2


radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print(f"The area of the circle is {area:.2f}")

# Asking for user input

user_input = input('Enter a number: ')
print(type(user_input))
number = int(user_input)
print(type(number))
print(f'You entered: {number}')

## boolean logic


# Define boolean variables
a = True
b = False

# Logical AND
print(a and b)  # Output: False

# Logical OR
print(a or b)  # Output: True

# Logical NOT
print(not a)  # Output: False

## Second example for boolean  Variables for comparison
age = 20
is_teenager = age > 12 and age < 20

# Conditional logic to check if the person is a teenager
if is_teenager:
    print("You are a teenager.")
else:
    print("You are not a teenager.")

## String manupulation

# Define a string
greeting = "Hello World!"

# Concatenate strings
full_greeting = greeting + " Have a nice day!"
print(full_greeting)  # Output: Hello World! Have a nice day!

# Slice the string
first_word = greeting[0:5]
print(first_word)  # Output: Hello

# Replace a substring
modified_greeting = greeting.replace("World", "Python")
print(modified_greeting)  # Output: Hello Python!

# Check for substring
contains_world = "World" in greeting
print(contains_world)  # Output: True

# Convert to uppercase
uppercase_greeting = greeting.upper()
print(uppercase_greeting)  # Output: HELLO WORLD!

# Find position of a substring
position = greeting.find("World")
print(position)  # Output: 6

# Split the string into words
words = greeting.split()
print(words)  # Output: ['Hello', 'World!']

# Join strings in a list
joined_string = ", ".join(["apple", "banana", "cherry"])
print(joined_string)  # Output: apple, banana, cherry

## Solution to in-class activity

# Explanation: Below is a step-by-step solution to check if a string is a palindrome.

user_string = input('Enter a string to check and see if it is a palindrome: ')

reversed_string = user_string[::-1]

if user_string == reversed_string:

    print('The string is a palindrome.')

else:

    print('The string is not a palindrome.')

# Solution for the homework
###
# Task Description: Write a program that prompts the user to enter their full name (first and last name).
# The program should then print the names in reverse order (last name followed by the first name).
###

# Ask the user to input their full name
full_name = input("Enter your full name: ")
# Split the name into parts and reverse the order
name_parts = full_name.split()
reversed_name = ' '.join(reversed(name_parts))
# Print the reversed name
print(f"Reversed name: {reversed_name}")
