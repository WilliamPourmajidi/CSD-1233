
while True:
    try:
        number = int(input('Enter an integer: '))
        print('Valid number entered:', number)
        # break
    except ValueError:
        print('Invalid input. Please enter a valid integer.')
        break

