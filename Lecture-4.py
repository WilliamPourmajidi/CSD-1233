#### While loop

count = 0
while count < 5:
    print(count)
    count += 1


### For loop

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

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





