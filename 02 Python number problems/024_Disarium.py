# 024)	Python program to check if the given number is a Disarium Number

"""
1 power 1+ 7 power 2 + 5 power 3 = 1+ 49 + 125 = 175
"""
num=int(input("Enter a number:"))
sum=0
temp=num
if num>0:
    for len in range(len(str(num)),0,-1):
        rem=temp%10
        temp//=10
        sum=sum+(rem**len)
    if (sum==num):
        print("It is a disarium number")
    else:
        print("Not a disarium number")
else:
    print("Enter a valid number!")