#### While loop

count = 0
while count < 500000:
    print(count)
    count += 1
# output:
# 0
# 1
# 2
# 3
# 4

### For loop

my_list = ["apple", "banana", "cherry", 12,13,15, 3.14]
for item in my_list:
    print(item)

for character in "My String":
    print(character)


### For loop with break

fruits = ["apple", "banana", "cherry","melon"]
for x in fruits:
  print(x)
  if x == "cherry":
    break

## For and Range

for x in range(2, 6):
  print(x)


### Nested Loops
print("-------")
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j)
    print()


# Dealing with nested Lists!
not_nested_list = ["a", "b", "c"]
nested_list = ["a", "b", "c", ["d", "e"], "f", "g"]

for element in nested_list:
  print(f"This is our element {element}, and it has the variable {type(element)}")




