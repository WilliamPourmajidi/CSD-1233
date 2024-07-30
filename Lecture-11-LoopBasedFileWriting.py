data = ["Line 1", "Line 2", "Line 3"]
with open('output.txt', 'w') as file:
    for line in data:
        file.write(line + "\n")
    print("writing to file is now completed!")
