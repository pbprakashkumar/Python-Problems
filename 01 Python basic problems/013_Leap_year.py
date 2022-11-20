# 013) 	Python Program to Check Leap Year

"""
__Conditions__
1.The year is multiple of 400.
2.The year is multiple of 4 and not multiple of 100.
"""

a=int(input("Enter the year:"))
if (a%400==0) or (a%4==0 and a%100!=0):
    print("Leap year")
else:
    print("Not a leap year")