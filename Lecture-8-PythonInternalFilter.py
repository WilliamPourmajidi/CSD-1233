nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)


def is_odd(num):
    for x in range(2, num):
        if (num % 2) == 0:
            return False
        return True


odds = list(filter(is_odd, nums))
print(odds)
