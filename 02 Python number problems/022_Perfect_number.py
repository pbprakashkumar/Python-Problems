# 022)	Python program to check if the given number is a Perfect Number or not

"""

6 is a perfect number
Factors of 6 = 1, 2,3
Sum of Factor = Given number

"""

num=int(input("Enter a number"))
sum=0
temp=num
for i in range(1,num): #num+1 is not possible (6=1+2+3)
    if(temp%i==0):
        sum+=i
        print(sum)
if sum==num:
    print("Perfect number")
else:
    print("Not a perfect number ")    
