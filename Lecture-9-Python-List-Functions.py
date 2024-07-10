# Create a sample list of numbers
numbers = [3, 1, 4, 1, 5, 9]

# append() - Add an element to the end of the list
numbers.append(2)
print("List after append(2):", numbers)  # Expected output: [3, 1, 4, 1, 5, 9, 2]

# extend() - Add all elements from another iterable (list) to the end
more_numbers = [6, 7, 8]
numbers.extend(more_numbers)
print("List after extend([6, 7, 8]):", numbers)  # Expected output: [3, 1, 4, 1, 5, 9, 2, 6, 7, 8]

# insert(index, element) - Insert an element at a specific index
numbers.insert(2, 0)
print("List after insert(2, 0):", numbers)  # Expected output: [3, 1, 0, 4, 1, 5, 9, 2, 6, 7, 8]

# remove(element) - Remove the first occurrence of a specific element
numbers.remove(1)
print("List after remove(1):", numbers)  # Expected output: [3, 0, 4, 1, 5, 9, 2, 6, 7, 8]

# pop(index=-1) - Remove and return the element at a specific index (default: last)
last_item = numbers.pop()
print("Removed item using pop():", last_item)  # Expected output: 8 (Removes and prints the last element)
print("List after pop():", numbers)  # Expected output: [3, 0, 4, 1, 5, 9, 2, 6, 7]


# sort() - Sort elements in ascending order (in-place modification)
numbers.sort()
print("List after sort():", numbers)  # Expected output: [0, 1, 2, 3, 4, 5, 6, 7, 9x`]

# reverse() - Reverse the order of elements in-place
numbers.reverse()
print("List after reverse():", numbers)  # Expected output: [9, 7, 6, 5, 4, 3, 2, 1, 0]

# Common Functions

# len(list) - Get the length (number of items) of the list
list_length = len(numbers)
print("Length of the list:", list_length)  # Expected output: 9

# max(list) - Get the element with the highest value
highest_number = max(numbers)
print("Highest number:", highest_number)  # Expected output: 9

# min(list) - Get the element with the lowest value
lowest_number = min(numbers)
print("Lowest number:", lowest_number)  # Expected output: 0

# sum(list) - Get the sum of all elements (works for numeric lists)
total_sum = sum(numbers)
print("Sum of all elements:", total_sum)  # Expected output: 47 (assuming integers)

# list(iterable) - Convert an iterable (like a string) to a list
string_of_numbers = "12345"
number_list = list(string_of_numbers)
print("List from string:", number_list)  # Expected output: ['1', '2', '3', '4', '5']


