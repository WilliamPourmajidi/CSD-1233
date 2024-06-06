# Number of rows and columns in the multiplication table
n = 10

# Using nested loops to print a multiplication table
for i in range(1, n + 1):
    # print("-------Outer Loop-------")
    for j in range(1, n + 1):
        # print("-------Inner Loop-------")
        print(f"{i * j}\t", end='')  # Multiplying and formatting the output
    print()  # New line after each row
