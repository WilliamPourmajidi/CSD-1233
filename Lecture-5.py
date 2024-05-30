
#Simple validation: Numeric input

while True:
    try:
        number = int(input('Enter an integer: '))
        print('Valid number entered:', number)
        break
    except ValueError:
        print('Invalid input. Please enter a valid integer.')


# Advanced validation: Date input using datetime module

from datetime import datetime

date_format = '%Y-%m-%d'
while True:
    date_input = input('Enter a date in YYYY-MM-DD format: ')
    try:
        valid_date = datetime.strptime(date_input, date_format)
        print('Valid date entered:', valid_date.strftime(date_format))
        break
    except ValueError:
        print('Invalid date. Please follow the YYYY-MM-DD format.')


# Example using 'end' as a sentinel value to terminate input collection
data_list = []
while True:
    data = input("Enter data ('end' to stop): ")
    if data.lower() == 'end':
        break
    data_list.append(data)
print("Data collected:", data_list)

