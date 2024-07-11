# Creating a one-dimensional list
one_d_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
# index        0   1   2   3   4   5   6   7  8   9     10   11   12   13   14   15
# Printing the list

print("One-Dimensional List:", one_d_list)

# Accessing elements in the list
first_element = one_d_list[0]
print("First Element:", first_element)

# Example of Slicing
sliced_list = one_d_list[1:-1]
sliced_list_2 = one_d_list[1:]   # start is inclusive , stop is exclusive
sliced_list_3 = one_d_list[1:14:3]  # start, stop(end), step


print("Sliced List:", sliced_list)
print("Sliced List_2:", sliced_list_2)
print("Sliced List_3:", sliced_list_3)

# Modifying an element in the list
one_d_list[2] = 2024
print("Modified List:", one_d_list)

# Adding a new element to the list
one_d_list.append(170)
print("List after Adding an Element:", one_d_list)
#
# Removing an element from the list
one_d_list.remove(150)
print("List after Removing an Element:", one_d_list)


