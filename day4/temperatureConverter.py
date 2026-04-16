#Write a program with functions to convert temperatures between:

#Celsius to Fahrenheit: F = (C × 9/5) + 32
#Fahrenheit to Celsius: C = (F - 32) × 5/9
#Celsius to Kelvin: K = C + 273.15


# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(c):
    return c + 273.15

# Main program
print("Temperature Conversion Menu")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    print("Fahrenheit:", celsius_to_fahrenheit(c))

elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Celsius:", fahrenheit_to_celsius(f))

elif choice == 3:
    c = float(input("Enter temperature in Celsius: "))
    print("Kelvin:", celsius_to_kelvin(c))

else:
    print("Invalid choice!")
