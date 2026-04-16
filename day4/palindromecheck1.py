# Take input from user
text = input("Enter a word or sentence: ")

# Remove spaces and convert to lowercase
clean_text = text.replace(" ", "").lower()

# Reverse the string
reversed_text = clean_text[::-1]

# Check palindrome
if clean_text == reversed_text:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
