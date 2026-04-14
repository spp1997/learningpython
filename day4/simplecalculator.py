#Simple calculator program
# Ask the user to enter the first number
num1 = float(input("Enter the first number: "))

# Ask the user to enter the second number
num2 = float(input("Enter the second number: "))

# Ask the user to choose an operation
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")


# Use if statements to perform the operation
if choice == '1':
    result = num1 + num2
    print("Result:", result)

elif choice == '2':
    result = num1 - num2
    print("Result:", result)

elif choice == '3':
        result = num1 * num2
        print("Result:", result)

elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Division by zero is not allowed.")

else:
        print("Invalid choice. Please select a valid operation.")
