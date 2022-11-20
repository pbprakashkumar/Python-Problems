# 066.    Python Program to reverse a string
def reverse(str):   
    str = str[::-1]   
    return str   
    
s = "Prakash"  
print ("The original string  is : ",s)   
print ("The reversed string using extended slice operator  is : ",reverse(s))  