# 076.    Selection Sort in Python
"""
In selection sort we start by finding the minimum value in a given list and move it to a sorted list. 
Then we repeat the process for each of the remaining elements in the unsorted list. 
The next element entering the sorted list is compared with the existing elements 
and placed at its correct position.So, at the end all the elements from the unsorted list are sorted.
"""
#sorting by finding min_index
def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
 
arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)