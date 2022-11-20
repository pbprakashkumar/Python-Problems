# 027.    Python program to print all happy numbers between the given interval


""" 
yields 1 when replaced by the sum of squares of its digits repeatedly.
Number = 32
3 power 2+ 2 power 2 = 13
1 power 2 + 3 power 2 = 10
1 power 2 + 0 power 2 = 1
"""
def check_happy_number(n):
    while True:
        result = sum([int(a) ** 2 for a in str(n)])
        if result == 1:
            return True
        elif result == 4:
            return False
        else:
            n = result

for i in range(1,1000 + 1):
    if check_happy_number(i):
        print(i, end=", ")
