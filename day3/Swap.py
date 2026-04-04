#python program to swap numbers using third varaible   

#taking input from the user
x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))

#Create a temporary variable and swap the values
temp=x
x=y
y=temp
print("Value of x is %d" %x)
print("Value of y is %d" %y)


#Swap two numbers using arithemetic operators + and -
#taking input from the user
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

#Create a temporary variable and swap the values
a=a+b
b=a-b
a=a-b

print("Swapped value of a is %d & b is %1.f " %(a,b))
