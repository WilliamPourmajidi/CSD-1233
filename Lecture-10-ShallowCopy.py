# Shallow Copy Behaviour

# Original list with nested list
original_list = [1, 2, [3, 4], 5, 6, 7, 8, 9]
print("Original list:", original_list)
# Creating a shallow copy
shallow_copy = original_list.copy()

print("Shallow  (before changing the original_list):", shallow_copy)

# Modifying the nested list in the original list
original_list[2][0] = 'changed'

print("Original List(after change):", original_list)
print("Shallow  (after changing the original_list):", shallow_copy)
