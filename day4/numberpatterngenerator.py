# Take input from user
n = int(input("Enter a number: "))

# Ask user to choose a pattern
print("\nChoose a pattern:")
print("1. Numbers from 1 to N")
print("2. Numbers from N to 1 (reverse)")
print("3. Multiplication table of N")

choice = input("Enter your choice (1/2/3): ")

# Pattern 1: 1 to N
if choice == '1':
    print("\nPattern 1:")
    for i in range(1, n + 1):
        print(i, end=" ")

# Pattern 2: N to 1
elif choice == '2':
    print("\nPattern 2:")
    for i in range(n, 0, -1):
        print(i, end=" ")

# Pattern 3: Multiplication Table
elif choice == '3':
    print("\nPattern 3:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Invalid choice
else:
    print("Invalid choice! Please select 1, 2, or 3.")
