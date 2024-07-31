transactions = [
    {"type": "deposit", "amount": 100},
    {"type": "withdrawal", "amount": 50},
    {"type": "deposit", "amount": 200},
    {"type": "withdrawal", "amount": 30},
]

total_deposit = 0
total_withdrawal = 0

for transaction in transactions:
    if transaction["type"] == "deposit":
        total_deposit += transaction["amount"]
    elif transaction["type"] == "withdrawal":
        total_withdrawal += transaction["amount"]

print("Total Deposits:", total_deposit)
print("Total Withdrawals:", total_withdrawal)
