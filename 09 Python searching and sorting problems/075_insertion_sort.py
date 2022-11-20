# 075.    Insertion Sort in Python
"""
1. Create a function insertion_sort that takes a list as argument.
2. Inside the function create a loop with a loop variable i that counts from 1 to the length of the list – 1.
3. Set temp equal to the element at index i.
4. Set j equal to i – 1.
5. Create a while loop that runs as long as j is non-negative and temp is smaller than the element at index j.
6. Inside the while loop, set the element at index j + 1 equal to the element at index j and decrement j.
7. After the while loop finishes, set the element at index j + 1 equal to temp.
"""
def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1      
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        # Place key at after the element just smaller than it.
        array[j + 1] = key
data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)