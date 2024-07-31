sales_data = [
    {'date': '2023-01-01', 'amount': 100},
    {'date': '2023-01-01', 'amount': 150},
    {'date': '2023-01-02', 'amount': 200},
    {'date': '2023-01-02', 'amount': 250}
]

current_date = None
subtotal = 0

for entry in sales_data:
    if entry['date'] != current_date:
        if current_date is not None:
            print(f'Subtotal for {current_date}: {subtotal}')
        current_date = entry['date']
        subtotal = 0
    subtotal += entry['amount']
print(f'Subtotal for {current_date}: {subtotal}')

