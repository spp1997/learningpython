# Python Crash Course, Eric Matthes

# Louis Lozano
# 2-26-2019
# whitespace.py

# \t makes a tab.
# \n makes a newline.
print("Languages:\n\tPython\n\tC\n\tJava")

fav_lang = " Python "

# The rstrip() method gets rid of whitespace on right side.
# lstrip() for left side.
# strip() for both sides.
print(fav_lang)

print(fav_lang.rstrip())

print(fav_lang.lstrip())

# Strips whitespace from both sides and assigns new value to itself.
fav_lang = fav_lang.strip()

print(fav_lang)
