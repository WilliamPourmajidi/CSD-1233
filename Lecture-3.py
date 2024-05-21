temperature = 32

if temperature > 30:
    print("It's a hot day!")


######

number = 5
if number > 0:
    print("Positive number")

#####
number = 4
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#####

score = 93
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
else:
    print("Grade C")

####
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

#####
light_color = input("Enter the traffic light color (red, yellow, green): ").lower()
if light_color == "red":
    print("Stop")
elif light_color == "yellow":
    print("Slow down")
elif light_color == "green":
    print("Go")
else:
    print("Invalid color entered")

