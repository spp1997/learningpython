# Take input from user
n = int(input("Enter a number: "))

# Ask user to choose a pattern
print("\nChoose a pattern:")
print("1. Numbers from 1 to N (using FOR loop)")
print("2. Numbers from N to 1 (using WHILE loop)")
print("3. Multiplication table of N (using FOR and WHILE)")

choice = input("Enter your choice (1/2/3): ")

# Pattern 1: FOR loop
if choice == '1':
    print("\nPattern 1 (FOR loop):")
    for i in range(1, n + 1):
        print(i, end=" ")

# Pattern 2: WHILE loop
elif choice == '2':
    print("\nPattern 2 (WHILE loop):")
    i = n
    while i >= 1:
        print(i, end=" ")
        i -= 1

# Pattern 3: Multiplication Table using FOR and WHILE
elif choice == '3':
    print("\nPattern 3 (Multiplication Table):")
    
    # Using FOR loop
    print("\nUsing FOR loop:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    
    # Using WHILE loop
    print("\nUsing WHILE loop:")
    i = 1
    while i <= 10:
        print(f"{n} x {i} = {n * i}")
        i += 1

# Invalid choice
else:
    print("Invalid choice! Please select 1, 2, or 3.")
