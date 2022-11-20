# 009)	Python program to convert Celsius to Fahrenheit
'''
__Formulas__
Fahrenheit =(1.8*Celsius)+32
Celsius    =(Fahrenheit-32)/1.8
'''

#Celsius to Fahrenheit
"""
a=float(input("Enter value in celsius"))
F=(1.8*a)+32
print("Celsius value is {}°C".format(a))
print("Fahrenheit value is .{0:.2f}°F".format(F))
"""

#Fahrenheit to Celsius

a=float(input("Enter value in Fahrenheit"))
C=(a-32)/1.8
print("Fahrenheit value is .{0:.2f}°F".format(a))
print("Celsius value is {0:.2f}°C".format(C))
