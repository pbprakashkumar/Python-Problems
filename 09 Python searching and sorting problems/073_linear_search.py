# 073.    Linear Search in Python
'''
Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
If x matches with an element, return the index.
If x doesn’t match with any of the elements, return -1.
'''
def LinearSearch(array, n, k):
    for j in range(0, n):
        if (array[j] == k):
            return j
    return -1
array = [1, 3, 5, 7, 9]
k = 7
n = len(array)
result = LinearSearch(array, n, k)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)