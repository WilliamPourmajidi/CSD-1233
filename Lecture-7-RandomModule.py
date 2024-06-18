import random

# Generate a random integer between 1 and 10
rand_int = random.randint(1, 10)
print(f"Random integer between 1 and 10: {rand_int}")

# Choose a random element from a list
choices = ['apple', 'banana', 'cherry']
rand_choice = random.choice(choices)
print(f"Random choice from list: {rand_choice}")

# Shuffle a list
deck = list(range(1, 11))
print(f"list: {deck}")
random.shuffle(deck)
print(f"Shuffled list: {deck}")

