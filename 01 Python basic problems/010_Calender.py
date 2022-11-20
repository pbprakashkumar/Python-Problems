# 010)	Python program to display calendar

#Importing calender module
import calendar
#Getting year and month
y=int(input("Enter year:"))
m=int(input("Enter month:"))
print(calendar.month(y,m))