# Simple example to check if an item is in a list
fruits_list = ['apple', 'banana', 'cherry', 12, 3.14]

# Creating a tuple from a list using tuple function
fruits_tuple = tuple(fruits_list)

# Showing the type
print(type(fruits_list))
print(type(fruits_tuple))

# Showing the content
print(fruits_list)
print(fruits_tuple)

# Changing the content
# Lists are mutable
fruits_list[0] = "orange"
fruits_list.append("apple")
print(fruits_list)

# Tuples are immutable so the following line will cause the application to
# throw an error of TypeError: 'tuple' object does not support item assignment
# fruits_tuple[0] = "orange"


# Accessing elements
print(f"My Favorite Fruit from our list is {fruits_list[0]}")
print(f"My Favorite Fruit from our tuple is {fruits_tuple[0]}")

#
print('apple' in fruits_list)
print('apple' in fruits_tuple)
print('grape' in fruits_list)  # Output: False
print('grape' in fruits_tuple)  # Output: False


