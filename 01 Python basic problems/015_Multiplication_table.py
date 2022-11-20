# 015)	Python Program to Display the multiplication Table
num=int(input("Enter a number:"))

#Multiplication table for 10 times
print("Multiplication table of",num)
print("____________________________")
for i in range(1,11):
    product=num*i
    print("{} x {} =".format(num,i),product)