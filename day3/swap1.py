#swap two numbers using functions

def swap(a,b):
    t=a
    a=b
    b=t
    return (a,b)

a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
a,b=swap(a,b)
print("Swaped value of x is %d & y is %d" %(a,b))
