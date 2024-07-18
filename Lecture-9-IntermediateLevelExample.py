# Checking for multiple items in a list
fruits = ['apple', 'banana', 'cherry']
items_to_check = [ 'grape','cherry','apple']

for item in items_to_check:
    if item in fruits:
        print(f"{item} is in the list.")
    else:
        print(f"{item} is not in the list.")





