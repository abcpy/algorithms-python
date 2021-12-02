def quickSort(arr, start, end):
    if start >= end:
        return
    pivot = arr[start]
    low = start
    hight = end
    index = partition(arr, pivot, low, hight)
    quickSort(arr, start, index-1)
    quickSort(arr, index+1, end)

def partition(arr, pivot, low, high):
    # 前后两个指针没有重合
    while low < high:
        # 从后向前。直到遇到比privot 小的
        while low < high and arr[high] >= pivot:
            high -=1
        arr[low] = arr[high]
        # 从前往后， 直到遇到比privot 大的
        while low < high and arr[low] <= pivot:
            low +=1
        arr[high] = arr[low]
        arr[low] = pivot
    return low

arr = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
quickSort(arr, 0, len(arr)-1)
print(arr)


