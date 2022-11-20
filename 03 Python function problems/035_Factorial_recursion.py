#035)	Python Program to Find Factorial of Number Using Recursion

def recur_factorial(n):  
    if n == 1:  
       return n  
    elif num < 0:  
        print("Sorry, factorial does not exist for negative numbers")  
    elif num == 0:  
        print("The factorial of 0 is 1") 
    else:  
       return n*recur_factorial(n-1)  
# take input from the user  
num = int(input("Enter a number: "))  
print("The factorial of",num,"is",recur_factorial(num))  