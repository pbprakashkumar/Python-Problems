# 064.    Python Program to Sort Words in Alphabetic Order

my_str = input("Enter a string: ")  
# breakdown the string into a list of words  
words = my_str.split()  
# sort the list  
words.sort()  
# display the sorted words  
for i in words:  
   print(i)