#String Format
# Python, we cannot combine strings and numbers like this

#age = 36
#This will produce an error:
#txt = "My name is John, I am "+ age
#print(txt)

#We can combine strings and numbers by using f-strings or the format(.) method!

#To specify a string as an f-string put an f in front of the of the string literal, and add curly brackets{} as placeholders for variables and other opeartions.

age= 36
txt = f"My name is John, I am {age}"
print(txt)

#A placeholder can contain varaibles, operations, functions and modifiers to format the value

price=59
txt=f"The price is {price} dollars"
print(txt)

#Modifier
#A placeholder can include a modifier to format the value 

price = 59
txt= f"The price is {price:.2f} dollars"
print(txt)


#A placeholder can contain python code, like math operator
txt=f"The price is {20*59} dollars"
print(txt)


