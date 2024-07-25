fruits = ['cherry', 'apple', 'banana', 'date']

# Using sorted()
sorted_fruits = sorted(fruits)
print(f"Here is the original fruit list : {fruits}")
print(f"Here is the sorted fruit list : {sorted_fruits}")

# Using .sort()
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# Breaking and fixing the sort!
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)