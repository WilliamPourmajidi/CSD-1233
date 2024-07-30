# Reading a file line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Appending to a file (Writing to the end of it!, similar to append to a list)
with open('example.txt', 'a') as file:
    file.write("\nThis is an appended line.")


