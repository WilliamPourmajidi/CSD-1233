# Creating a three-dimensional list (tensor)
three_d_list = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]

# Printing the three-dimensional list
print("Three-Dimensional List (Tensor):")
for matrix in three_d_list:
    for row in matrix:
        print(row)
    print()  # Newline for better readability

# Accessing an element in the tensor
element = three_d_list[1][0][2]  # Accessing the element in the second matrix, first row, third column
print("Element at [1][0][2]:", element)

# Modifying an element in the tensor
three_d_list[0][1][2] = 13
print("Modified Tensor:")
for matrix in three_d_list:
    for row in matrix:
        print(row)
    print()  # Newline for better readability

# Adding a new matrix to the tensor
new_matrix = [
    [13, 14, 15],
    [16, 17, 18]
]
three_d_list.append(new_matrix)
print("Tensor after Adding a New Matrix:")
for matrix in three_d_list:
    for row in matrix:
        print(row)
    print()  # Newline for better readability
