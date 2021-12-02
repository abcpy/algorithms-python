# To heapify subtree rooted at index i.
# n is size of heap

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i    # left = 2 * i
    r = 2 * i + 1 # right = 2 *i + 1

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[r] > arr[largest]:
        largest = r

    # change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Heapify the root
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Sorted array is: ")
for i in range(n):
    print(arr[i])



