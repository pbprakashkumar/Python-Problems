# 004)	Python program to solve quadratic equation 
""" 
Quadratic equation is ax2+bx+c=0
The quadratic formula is x=(-b±√(b²-4ac))/(2a)
"""
#importing complex math module
import cmath
#Getting coefficients
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
#Calculating the quadratic equation
d=(b**2)-(4*a*c)
sol_1= (-b+cmath.sqrt(d))/(2*a)
sol_2= (-b-cmath.sqrt(d))/(2*a)
#Printing the solutions
print("The solutions for the quadratic equation are {},{}".format(sol_1,sol_2))



