import csv

# Reading from CSV file
with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = [row for row in reader]

# Processing data
summary = []
for row in data:
    processed_row = [element.upper() for element in row]
    summary.append(processed_row)

# Writing summary to a text file
with open('summary.txt', 'w') as summaryfile:
    for row in summary:
        summaryfile.write(", ".join(row) + "\n")
