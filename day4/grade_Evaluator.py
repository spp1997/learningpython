# Ask the user to enter the test score
score = float(input("Enter your test score (0-100): "))

# Check the grade using if-elif statements
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score <= 89:
    grade = 'B'
elif 70 <= score <= 79:
    grade = 'C'
elif 60 <= score <= 69:
    grade = 'D'
elif 0 <= score < 60:
    grade = 'F'
else:
    grade = 'Invalid'

# Display the grade
if grade != 'Invalid':
    print("Grade:", grade)

    # Check pass or fail
    if score >= 60:
        print("Status: Passed")
    else:
        print("Status: Failed")
else:
    print("Invalid score! Please enter a value between 0 and 100.")
