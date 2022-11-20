# 072.    Binary Search in Python
'''
Compare x with the middle element.
If x matches with the middle element, we return the mid index.
Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.
'''
def binarySearch(arr, k, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
           low = mid + 1
        else:
            high = mid - 1
    return -1
arr = [1, 3, 5, 7, 9]
k = 5
result = binarySearch(arr, k, 0, len(arr)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")