# 020) 	Python Program to Check Armstrong Number

num=int(input("Enter a number:"))
order=len(str(num))
temp=num
sum=0
if num>0:
    while temp>0:
        a=temp%10
        temp=temp//10
        sum=sum+(a**order)
    if sum==num:
        print("It is an armstrong number!")
        print("The armstrong value is: ",sum)
    else:
        print("Not an armstrong number")
else:
    print("Enter a number greater than zero")
