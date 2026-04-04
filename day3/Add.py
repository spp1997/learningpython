#Program to add 2 numbers in python Using Arithmetic operator(+)

a=int(input("Enter the first input: "))
b=int(input("Enter the second input: "))
c=a+b
print("Addtion of two numbers {0} and {1} is {2}".format(a,b,c))

#Using functions

def add (a,b):
    sum=a+b
    return sum

a=int(input("Enter the first input: "))
b=int(input("Enter the second input: "))

print(add(a,b))
