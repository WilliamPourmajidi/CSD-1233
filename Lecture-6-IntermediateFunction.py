def calculate_factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input number.
    """
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


# Example usage
number = 10
result = calculate_factorial(number)
print(f"The factorial of {number} is {result}")

