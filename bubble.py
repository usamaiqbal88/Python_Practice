
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Driver code to test above
if __name__ == "__main__":
  arr = [5, 1, 4, 2, 8]

  bubbleSort(arr)

  print("Sorted array is:")
  for i in range(len(arr)):
      print("%d" % arr[i], end=" ")

# Algorithm:
# Start with an array of unsorted numbers
# Define a function called “bubbleSort” that takes in the array and the length of the array as parameters
# In the function, create a variable called “sorted” that is set to true
# Create a for loop that iterates through the array starting at index 0 and ending at the length of the array - 1
# Within the for loop, compare the current element with the next element in the array
# If the current element is greater than the next element, swap their positions and set “sorted” to false
# After the for loop, check if “sorted” is false
# If “sorted” is false, call the “bubbleSort” function again with the same array and length as parameters
# If “sorted” is true, the array is now sorted and the function will return the sorted array
# Call the “bubbleSort” function with the initial unsorted array and its length as parameters to begin the sorting process.
