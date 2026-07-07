# Strings are Arrays
#Strings in python are arrays of unicode characters

a= "hello, World!"
print(a[1])

#Loopin through a string 

for x in "banana":
    print(x)

#String lrngth 
a= "Hello, World!"
print(len(a))

#Checkstring 

txt= "The best things in life are free!"
print("free" in txt)

txt= "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# Check  if NOT
txt= "The best things in life are free!"
print("expensive" not in txt)

txt= "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")



