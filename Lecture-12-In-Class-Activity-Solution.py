def read_grades(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            grades = []
            for line in lines:
                name, grade = line.split()
                grades.append((name, int(grade)))
            return grades
    except Exception as e:
        print("An error occurred:", e)

def calculate_average(grades):
    total = sum(grade for name, grade in grades)
    return total / len(grades)

def print_above_average(grades, average):
    for name, grade in grades:
        if grade > average:
            print(name, grade)

grades = read_grades("students.txt")
if grades:
    average = calculate_average(grades)
    print("Average Grade:", average)
    print("Students above average:")
    print_above_average(grades, average)
