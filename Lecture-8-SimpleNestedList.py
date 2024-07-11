# Creating a two-dimensional list (matrix)
two_d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(two_d_list)
print(two_d_list[0])
print(two_d_list[1])
print(two_d_list[2])

two_d_list[0][1] = 2024
print(two_d_list)

two_d_list[2][0] = 2027
print(two_d_list)

for item in two_d_list:
    print(f"Here im inside a loop showing you the {item}")




