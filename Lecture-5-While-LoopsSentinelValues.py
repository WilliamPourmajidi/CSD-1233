# Example using 'end' as a sentinel value to terminate input collection
data_list = []
while True:
    data = input("Enter data ('end' to stop): ")
    if data.lower() == 'end':
        break
    data_list.append(data)
print("Data collected:", data_list)

