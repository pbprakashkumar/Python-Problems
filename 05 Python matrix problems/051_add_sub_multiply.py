#051.	Python Program to Add , Subtract and Multiply Two Matrices

X =      [[1,2,3],  
         [4,5,6],  
         [7,8,9]]  

Y =      [[10,11,12],  
         [13,14,15],  
         [16,17,18]]  

sum_res= [[0,0,0],  
         [0,0,0],  
         [0,0,0]]  

sub_res= [[0,0,0],  
         [0,0,0],  
         [0,0,0]]  

mul_res= [[0,0,0],  
         [0,0,0],  
         [0,0,0]]  
# iterate through rows  
for i in range(len(X)):  #len(X) is 3
   # iterate through columns  
   for j in range(len(X[0])):  #len(X[0]) is 3 (3x3 matrix)
       sum_res[i][j] = X[i][j] + Y[i][j]  
       sub_res[i][j] = X[i][j] - Y[i][j]  
       for k in range(len(Y)):    
               mul_res[i][j] += X[i][k] * Y[k][j]
print("____________________")
print("sum")
for r in sum_res: 
    print(r)
print("____________________")
print("sub")
for r in sub_res: 
    print(r)
print("____________________")
print("mul")
for r in mul_res: 
    print(r)
print("____________________")