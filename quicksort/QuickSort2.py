import random

def quickSort(arr, start, end):
    if start >= end:
        return
    left = start
    right = end
    index = partiton(arr, left, right)
    quickSort(arr, start, index-1)
    quickSort(arr, index+1, end)

def partiton(arr, left, right):
    t = random.randint(left, right)
    arr[t], arr[left] = arr[left], arr[t]
    pivot = arr[left]
    while left < right:
        while left < right and arr[right] >= pivot:
            right -=1
        arr[left] = arr[right]
        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]
        arr[left] = pivot
    return left

arr = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
quickSort(arr, 0, len(arr)-1)
print(arr)