# 071.    Python Program to convert Bytes to string
byteData = b"Lets eat a \xf0\x9f\x8d\x95!"  
# Let's check the type  
print(type(byteData))  
str1 = byteData.decode('UTF-8')  
print(type(str1))  
print(str1)  