# 002) Python program to do arithmetical operations of 2 numbers

"""
__Arithmetic Operations__
1. Addition.        +           
2. Subtraction.     -
3. Multiplication.  *
4. Division.        /
5. Modulus.         %
6. Exponentiation.  **
7. Floor division.  //
"""
#Getting inputs
num1 = input("Enter number 1:")
num2 = input("Enter number 2:")
 #Performing operations
sum   = float(num1)  +  float(num2)
diff  = float(num1)  -  float(num2)
mul   = float(num1)  *  float(num2)
div   = float(num1)  /  float(num2)
mod   = float(num1)  %  float(num2)
exp   = float(num1)  ** float(num2)
floor = float(num1)  // float(num2)
#Printing outputs
print("Addition of {} and {} is {}".format(num1,num2,sum))
print("Subtraction of {} and {} is {}".format(num1,num2,diff))
print("Multiplication of {} and {} is {}".format(num1,num2,mul))
print("Division of {} and {} is {}".format(num1,num2,div))
print("Remainder of {} and {} is {}".format(num1,num2,mod))
print("Quotient of {} and {} is {}".format(num1,num2,floor))
print("Exponentiation of {} and {} is {}".format(num1,num2,exp))