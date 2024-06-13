from datetime import datetime

proper_date_format = '%Y-%m-%d'
while True:
    date_input = input('Enter a date in YYYY-MM-DD format: ')
    try:
        valid_date = datetime.strptime(date_input, proper_date_format)
        print('Valid date entered:', valid_date.strftime(proper_date_format))
        break
    except ValueError:
        print('Invalid date. Please follow the YYYY-MM-DD format.')
