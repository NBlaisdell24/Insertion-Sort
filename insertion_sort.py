# Python program for implementation of Insertion Sort
 
# Function to do insertion sort
def insertionSort(A):
  count = 1
  for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:
      A[i + 1] = A[i]
      i = i - 1
    A[i + 1] = key
    print(f"{count}. {A}")
    count += 1

# Driver code to test above
arr = [12, 11, 13, 5, 6]
print("Initial Array: ", arr)
insertionSort(arr)
print("Final result: ", arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
