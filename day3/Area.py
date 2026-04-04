#Program to find area of circle in python using math file 

import math
r=float(input("Enter the radius of the circle: "))
area=math.pi*r*r
print("%.2f"% area)

#Using PI
PI=3.142
r=float(input("Enter the radius of the circle: "))
area=PI*r*r
print("%.2f"% area)

#Using functions

import math 
def area_of_circle(r):
    a=r**2*math.pi
    return a

r=float(input("Enter the radius of the circle: "))
print("%.2f"% area_of_circle(r))

