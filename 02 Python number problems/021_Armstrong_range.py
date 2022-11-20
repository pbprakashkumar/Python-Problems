# 021) 	Python Program to Find Armstrong Number in an Interval


num1=int(input("Enter the opening number of the interval"))
num2=int(input("Enter the ending number of the interval"))
for num in range (num1,num2+1):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        a=temp%10
        temp=temp//10
        sum=sum+(a**order)
    if sum==num:
        print(num)

 
    