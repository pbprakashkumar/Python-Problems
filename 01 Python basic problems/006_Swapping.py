# 006) Python program to swap two variables without using third variable
"""
By using comma operator                ,
By using arithmetic operator      +,-(or)*,/
"""

# 1 By using comma operator
'''
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("The values before swapping are a={} and b={}".format(a,b))
a,b=b,a
print("The values after swapping are a={} and b={}".format(a,b))
'''

# 2 By using arithmetic operator +,-
'''
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("The values before swapping are a={} and b={}".format(a,b))
a=a+b
b=a-b
a=a-b
print("The values after swapping are a={} and b={}".format(a,b))
'''

# 3 By using arithmetic operator *,/
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("The values before swapping are a={} and b={}".format(a,b))
a=a*b
b=a/b
a=a/b
b=int(b)
a=int(a)
print("The values after swapping are a={} and b={}".format(a,b))