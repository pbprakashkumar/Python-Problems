# 023)	Python program to print all Perfect numbers between the given interval

num1=int(input("Enter a number of lower interval"))
num2=int(input("Enter a number of upper interval"))
if (num2>num1):
    for num in range(num1,num2): 
        sum=0
        if num==0:
            continue # 0 is not a perfect number
        for i in range(1,num): #num+1 is not possible (6=1+2+3)
            if(num%i==0):
                sum+=i
        if sum==num:
            print(sum)
else:
   print("Enter a valid range")
   
