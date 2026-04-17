#Create a program to manage student grades using a dictionary. The program should:

#Allow adding students with their grades (as a dictionary)
#Calculate the average grade for all students
#Find the student with the highest grade
#Find the student with the lowest grade
#Display all students and their grades


# Function to add students and grades
def add_students():
    students = {}
    n = int(input("Enter number of students: "))
    
    for i in range(n):
        name = input("Enter student name: ")
        grade = float(input("Enter grade: "))
        students[name] = grade
    
    return students

# Function to calculate average grade
def calculate_average(students):
    return sum(students.values()) / len(students)

# Function to find highest grade student
def highest_grade(students):
    return max(students, key=students.get)

# Function to find lowest grade student
def lowest_grade(students):
    return min(students, key=students.get)

# Function to display all students
def display_students(students):
    print("\nStudent Grades:")
    for name, grade in students.items():
        print(name, ":", grade)

# Main program
students = add_students()

display_students(students)

avg = calculate_average(students)
print("\nAverage grade:", avg)

top_student = highest_grade(students)
print("Highest grade student:", top_student, "-", students[top_student])

low_student = lowest_grade(students)
print("Lowest grade student:", low_student, "-", students[low_student])
