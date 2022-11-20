# 025)	Python program to print all disarium numbers between the given interval

num1=int(input("Enter a number in lower interval:"))
num2=int(input("Enter a number in upper interval:"))
if num2>num1:
    for num in range(num1,num2+1):
        sum=0
        temp=num
        if num==0:
            continue
        for i in range(len(str(num)),0,-1):
            rem=temp%10
            temp//=10
            sum=sum+(rem**i)
        if (sum==num):
            print(num)
