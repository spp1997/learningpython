# Dictionary to store student data
students = {}

# Function to add student
def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter grade: "))
    students[name] = grade
    print("Student added successfully!\n")

# Function to display students
def display_students():
    if not students:
        print("No student records found.\n")
        return
    print("\nStudent Grades:")
    for name, grade in students.items():
        print(name, ":", grade)
    print()

# Function to calculate average
def calculate_average():
    if not students:
        print("No data available.\n")
        return
    avg = sum(students.values()) / len(students)
    print("Average grade:", avg, "\n")

# Function to find highest grade
def highest_grade():
    if not students:
        print("No data available.\n")
        return
    top = max(students, key=students.get)
    print("Highest grade student:", top, "-", students[top], "\n")

# Function to find lowest grade
def lowest_grade():
    if not students:
        print("No data available.\n")
        return
    low = min(students, key=students.get)
    print("Lowest grade student:", low, "-", students[low], "\n")


# Main loop
while True:
    print("===== Student Grade Manager =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Calculate Average Grade")
    print("4. Find Highest Grade")
    print("5. Find Lowest Grade")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        calculate_average()
    elif choice == '4':
        highest_grade()
    elif choice == '5':
        lowest_grade()
    elif choice == '6':
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.\n")
