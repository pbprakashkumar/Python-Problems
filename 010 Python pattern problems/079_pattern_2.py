#079) Pattern 2
'''
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
'''
rows = 6
# if you want user to enter a number, uncomment the below line
# rows = int(input('Enter the number of rows'))
# outer loop
for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')