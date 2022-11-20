# 026) Python program to check if the given number is Happy Number

""" 
yields 1 when replaced by the sum of squares of its digits repeatedly.
Number = 32
3 power 2+ 2 power 2 = 13
1 power 2 + 3 power 2 = 10
1 power 2 + 0 power 2 = 1
"""

def sum_n(n):
    sum=0
    while(n>0):
        rem=n%10 
        sum=sum+(rem**2)
        n//=10
    return sum

def happy(n):
    if (n==1):
        print("Happy Number")
    elif (n==4):
        print("Unhappy Number")
    else:
        return happy(sum_n(n))

n=int(input("Enter a number"))
happy(n)