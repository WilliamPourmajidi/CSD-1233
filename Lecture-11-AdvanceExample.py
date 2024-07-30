# introduction to file handling and exception handling

try:
    with open('example.txt', 'r') as file:
        lines = file.readlines()
        print("File content:")
        for line in lines:
            print(line.strip())
except FileNotFoundError:
    print("File not found. Please check the file path.")
