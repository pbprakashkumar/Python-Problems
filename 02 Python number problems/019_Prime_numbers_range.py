# 019)  Python Program to Print all Prime Numbers in an Interval

a=int(input("Enter a starting value"))
b=int(input("Enter a ending value"))
print("The prime numbers between {} and {} are :".format(a,b))
for num in range(a,b+1):
    if num>1:
        count=0
        for i in range(1,num+1):
            if (num%i==0):
                count+=1 #count=count+1
        if count==2:
            print(num)
