# Initialize variables to store the sum of grades and the number of grades entered
total_grades = 0
count_grades = 0
print("Enter your course grades one by one. Type 'done' to finish and calculate the average GPA.")
# Loop to collect grades until the user types 'done'
while True:
    grade_input = input("Enter a course grade (or 'done' to calculate): ")

    # Check if the user wants to stop entering grades
    if grade_input.lower() == 'done':
        break
    # Validate the input to ensure it's a numeric value
    try:
        grade = float(grade_input)

        # Check if the grade is within the valid  range
        if 0.0 <= grade <= 100:
            total_grades += grade
            count_grades += 1
        else:
            print("Please enter a valid grade between 0.0 and 100.0.")
    except ValueError:
        print("Invalid input. Please enter a numeric grade or 'done' to finish.")
# Calculate the average GPA if grades were entered
if count_grades > 0:
    average_gpa = total_grades / count_grades
    print(f"Your average GPA is: {average_gpa:.2f}")
else:
    print("No valid grades were entered.")
