# How to define and modify a global variable.


global_counter = 0
print(f"Value of global_counter before modification: {global_counter}")

def increment():
    global global_counter
    global_counter += 1

    print(f"Value of global_counter after modification: {global_counter}")

increment() # calling the modification function


