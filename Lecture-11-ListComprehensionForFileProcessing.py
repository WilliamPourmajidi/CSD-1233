# List comprehension
with open('info.txt', 'r') as file:
    lines = [line.strip() for line in file]
    print(lines)

# Expanded version
my_line_list = []
with open('info.txt', 'r') as file:
    for line in file:
        my_line_list.append(line.strip())
print(my_line_list)

