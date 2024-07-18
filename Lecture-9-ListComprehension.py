# Using `in` with list comprehension
fruits = ['apple', 'banana', 'cherry', 'orange', 'grapefruit']
items_to_check = ['apple', 'grape', 'orange']

# check the following list comprehension
results = [item for item in items_to_check if item in fruits]

print("Items found:", results)  # Output: Items found: ['apple']
