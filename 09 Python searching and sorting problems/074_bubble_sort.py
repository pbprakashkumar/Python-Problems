# 074.    Bubble Sort in Python
'''
1.  Compare and Swap: - Compare the first and second items starting with the first index. 
    The first and second elements are switched if the first is bigger than the second. 
    Compare the second and third items now. 
    If they aren't in the right sequence, swap them. 
    The procedure continues until the last item is added.
2.  Remaining Iteration: - For the remaining iterations, the same procedure is followed. 
    The biggest element among the unsorted items is placed at the conclusion of each iteration.
3.  The result after each operation is a sorted array.
'''
def bubbleSort(array):
  # loop to access each array element
  for i in range(len(array)):
    # loop to compare array elements
    for j in range(0, len(array) - i - 1):
      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:
        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
data = [-2, 45, 0, 11, -9]
bubbleSort(data)
print('Sorted Array in Ascending Order:')
print(data)