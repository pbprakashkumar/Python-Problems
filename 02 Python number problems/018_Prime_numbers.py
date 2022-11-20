# 018) 	Python Program to Check Prime Number

a=int(input("Enter a value"))
count=0
if a>1:
    for i in range(1,a+1):
      if (a%i==0):
        count+=1 #count=count+1
    if count==2:
        print("{} is a prime number".format(a))
    else:
        print("{} is a composite number".format(a))
else:
    print("{} is neither prime nor a composite number".format(a))
