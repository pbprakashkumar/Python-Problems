# 016) 	Python Program to Print the Fibonacci sequence

num=int(input("Enter how many terms you want to print:"))
flag1=0
flag2=1
count=0
if num<=0:
    print("Please enter a number greater than zero ")
elif num==1:
    print("The fibonacci sequence of the number upto {} is ".format(num),flag1)
else:
    print("The fibonacci sequence of the number upto {} is:".format(num))
    while count<num:
        print(flag1)
        flag=flag1+flag2
        flag1=flag2
        flag2=flag
        count+=1

   
   
   
   
   

       