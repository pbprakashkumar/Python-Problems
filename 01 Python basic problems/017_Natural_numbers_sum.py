# 017) 	Python Program to Find the Sum of Natural Numbers

num=int(input("Enter a number:"))
sum=0
if num<0:
    print("Enter a positive number")
else:
    for i in range(0,num+1):
        sum=sum+i
    print("The sum of natural numbers upto {} is:".format(num),sum)
