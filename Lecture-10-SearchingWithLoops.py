# Example when search does return any match
fruits = ['apple', 'banana', 'cherry', 'date']

# Search using loop
search_item = 'banana'
found = False

for fruit in fruits:
    if fruit == search_item:
        found = True
        break

print(found)

# Example when search does not return any match
fruits = ['apple', 'banana', 'cherry', 'date']

# Search using loop
search_item = 'grape'
found = False
for fruit in fruits:
    if fruit == search_item:
        found = True
        break

print(found)
