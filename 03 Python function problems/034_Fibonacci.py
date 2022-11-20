#034)	Python Program to Display Fibonacci Sequence Using Recursion
def recur_fibo(n):  
    if n <0:  
        print("Incorrect input")
    elif (n==0): 
        return 0
    elif (n==1) or (n==2):
        return 1
    else:
       return(recur_fibo(n-1) + recur_fibo(n-2))  
# take input from the user  
n = int(input("How many terms? "))  
# check if the number of terms is valid  
  
for i in range(n):  
    print(recur_fibo(i))  