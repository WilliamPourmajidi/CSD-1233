# Example 2: Two-Dimensional Tuple
# Creating a two-dimensional tuple (matrix)
two_d_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Printing the two-dimensional tuple
print("Two-Dimensional Tuple (Matrix):")
for row in two_d_tuple:
    print(row)

# Accessing an element in the matrix
element = two_d_tuple[1][1]  # Accessing the element in the second row, second column (index starts from 0!)
print("Element at [1][1]:", element)

# Note: Tuples are immutable, so you cannot modify elements directly.
# However, you can create a new tuple with the desired changes.

# Creating a modified matrix
modified_row = two_d_tuple[0][:2] + (10,) + two_d_tuple[0][3:]
modified_matrix = (modified_row,) + two_d_tuple[1:]
print("Modified Matrix:")
for row in modified_matrix:
    print(row)

