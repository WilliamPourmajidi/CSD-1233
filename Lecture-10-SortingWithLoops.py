fruits = ['cherry', 'apple', 'banana', 'date']
numbers = [8, 5, 3, 1, 4, 7, 9]

# Bubble sort
for i in range(len(fruits)):
    for j in range(0, len(fruits) - i - 1):
        if fruits[j] > fruits[j + 1]:
            fruits[j], fruits[j + 1] = fruits[j + 1], fruits[j]

print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# Bubble sort
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)  # Output: [1, 2, 3, 5, 8, 9, 11]

