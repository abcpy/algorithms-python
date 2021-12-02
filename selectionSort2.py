def selectionSort(arr):
    for i in range(len(arr)-1,-1,-1):
        max_idx = i
        for j in range(i-1,-1,-1):
            if arr[max_idx] < arr[j]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx],arr[i]
    return arr

# A = [22, 11]
A = [64, 25, 12, 22, 11]
# for i in range(len(A)-2,-1,-1):
#     print(A[i])
print(selectionSort(A))