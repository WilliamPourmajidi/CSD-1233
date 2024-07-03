# Creating a two-dimensional list (matrix)
two_d_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Printing the two-dimensional list
print("Two-Dimensional List (Matrix):")
for row in two_d_list:
    print(row)

# Accessing an element in the matrix
element = two_d_list[1][1]  # Accessing the element in the second row, second column
print("Element at [1][1]:", element)

# Modifying an element in the matrix
two_d_list[0][2] = 10
print("Modified Matrix:")
for row in two_d_list:
    print(row)

# Adding a new row to the matrix
new_row = [10, 11, 12]
two_d_list.append(new_row)
print("Matrix after Adding a New Row:")
for row in two_d_list:
    print(row)
