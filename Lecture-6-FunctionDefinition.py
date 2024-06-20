# Void function  -- it has no return statement
# def summation(num_1, num_2):
#     print("I am inside the function")
#     print(f"This is your first number {num_1}")
#     print(f"This is your second number {num_2}")
#     print(num_1 + num_2)
#
#
# summation(10, 20)
###############################################
# Value-returning function - it has a return statement

#
# def summation_2(num_1, num_2):
#     return num_1 + num_2
#
# print(summation_2(15, 25))

####################################


def greeting(name):
    print(f"Hello {name}!")
    return (f"Hello {name}!")


# my_greeting = greeting("Neel")
my_team = ["John", "Prabodh", "Sharon", "Nisarg"]
for member in my_team:
    greeting(member)


