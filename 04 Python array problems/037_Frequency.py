#037.	Python program to find the frequency of each element in the array
# Array Initialization
arr = [11, 11, 22, 22, 22, 33, 22, 33, 33, 44, 44, 44]

# store frequency of each element
frequency = {}

# iterating over the array elements for frequency
for element in arr:

   # checking whether it is in the dict or not
   if element in frequency:
      # incerementing the frequency count by 1
      frequency[element] += 1
   else:
      # setting the count to 1
      frequency[element] = 1

# printing the elements frequencies
for key, value in frequency.items():
   print(f"{key} = {value}")