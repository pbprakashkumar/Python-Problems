# 007) Python program to generate a random number

import random as r
a=int(input("Enter Opening Range:"))
b=int(input("Enter Closing Range:"))
number=r.randint(a,b)
print("The random number is:",number)