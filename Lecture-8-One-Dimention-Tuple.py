# Creating a one-dimensional tuple
one_d_tuple = (1, 2, 3, 4, 5)

# Printing the tuple
print("One-Dimensional Tuple:", one_d_tuple)

# Accessing elements in the tuple
first_element = one_d_tuple[0]
print("First Element:", first_element)

# Note: Tuples are immutable, so you cannot modify elements directly.
# However, you can create a new tuple with the desired changes.

# Creating a modified tuple
modified_tuple = one_d_tuple[:2] + (10,) + one_d_tuple[3:]
print("Modified Tuple:", modified_tuple)
