import random

# Generate a random integer between 1 and 10
rand_int = random.randint(1, 10)
print(f"Random integer between 1 and 10: {rand_int}")

# Choose a random element from a list
choices = ['apple', 'banana', 'cherry', 'Tomato', 'Orange']
rand_choice = random.choice(choices)
print(f"Random choice from list: {rand_choice}")

# Shuffle a list
deck = list(range(1, 11))
print(f"list: {deck}")


count = 0
for i in range(1, random.randint(100, 100000)):
    random.shuffle(deck)
    print(f"Shuffled list: {deck}")
    count += 1
    print(count)
