fruits = ['apple', 'banana', 'cherry', 'date']

# Search using list comprehension
search_item = 'banana'
found = any(fruit == search_item for fruit in fruits)

print(found)  # Output: True
