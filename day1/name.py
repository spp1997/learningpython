# Python Crash Course, Eric Matthes

# Louis Lozano
# 2-26-2019
# name.py

# Stores a string in a variable
first_name = "ada"
last_name = "lovelace"

# Adds strings together and stores as one string in a variable.
full_name = first_name + " " + last_name

# title() makes first letter of each word upper case.
# upper() makes every letter uppercase.
# lower() makes every letter lower case
print(full_name.title())
print(full_name.upper())
print(full_name.lower())

message = "Hello, " + full_name.title() + "!"
print(message)
