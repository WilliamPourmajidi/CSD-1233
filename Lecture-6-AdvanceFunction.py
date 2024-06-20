def find_primes_in_range(start, end):
    """
    Find all prime numbers within a specified range.

    Parameters:
    start (int): The starting integer of the range (inclusive).
    end (int): The ending integer of the range (exclusive).

    Returns:
    list: A list of all prime numbers within the specified range.
    """

    def is_prime(num):
        """Helper function to check if a number is prime."""
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True



    primes = []  # Start with an empty list to hold prime numbers
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)  # Add the number to the list if it is prime

    return primes

# Example usage
start_range = 10
end_range = 50
primes = find_primes_in_range(start_range, end_range)
print("Prime numbers between", start_range, "and", end_range, ":", primes)


