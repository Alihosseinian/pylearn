from statistics import mean 

def calculate_average_grades():
    grades = []

    while True:
        try:
            grade = float(input("Enter a student's grade (or type 'exit' to finish): "))
            if grade < 0 or grade > 20:
                print("Invalid grade! Grades should be between 0 and 20.")
                continue
            grades.append(grade)

        except ValueError:
            user_input = input("Invalid input! Please enter a valid number or type 'exit' to finish: ")
            if user_input.lower() == 'exit':
                break
            else:
                continue

    if grades:
        print(f"\nAverage grade: {mean(grades)}")
    else:
        print("No grades entered.")

calculate_average_grades()
