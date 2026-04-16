text = input("Enter a word or sentence: ")
clean_text = text.replace(" ", "").lower()

is_palindrome = True

for i in range(len(clean_text) // 2):
    if clean_text[i] != clean_text[-i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
