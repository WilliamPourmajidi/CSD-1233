
try:
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    result = num1 / num2
    print('Result:', result)
except ZeroDivisionError:
    print('Error: Cannot divide by zero.')
except ValueError:
    print('Error: Invalid input. Please enter a valid number.')
finally:
    print('Execution completed.')
