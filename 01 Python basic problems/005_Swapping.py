# 005) Python program to swap two variables using third variable

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("The values before swapping are a={} and b={}".format(a,b))
temp=a
a=b
b=temp
print("The values after swapping are a={} and b={}".format(a,b))
