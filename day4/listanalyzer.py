# Take input from user
numbers = input("Enter numbers separated by commas: ")

# Convert input string into a list of integers
num_list = [int(num) for num in numbers.split(",")]

# Find largest and smallest numbers
largest = max(num_list)
smallest = min(num_list)

# Calculate average
average = sum(num_list) / len(num_list)

# Count even and odd numbers
even_count = 0
odd_count = 0

for num in num_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display results
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Average:", average)
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)
