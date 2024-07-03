# Creating a three-dimensional tuple (tensor)
three_d_tuple = (
    (
        (1, 2, 3),
        (4, 5, 6)
    ),
    (
        (7, 8, 9),
        (10, 11, 12)
    )
)

# Printing the three-dimensional tuple
print("Three-Dimensional Tuple (Tensor):")
for matrix in three_d_tuple:
    for row in matrix:
        print(row)
    print()  # Newline for better readability

# Accessing an element in the tensor
element = three_d_tuple[1][0][2]  # Accessing the element in the second matrix, first row, third column
print("Element at [1][0][2]:", element)

# Note: Tuples are immutable, so you cannot modify elements directly.
# However, you can create a new tuple with the desired changes.

# Creating a modified tensor
modified_matrix = three_d_tuple[0][:1] + ((4, 5, 13),) + three_d_tuple[0][2:]
modified_tensor = (modified_matrix,) + three_d_tuple[1:]
print("Modified Tensor:")
for matrix in modified_tensor:
    for row in matrix:
        print(row)
    print()  # Newline for better readability
