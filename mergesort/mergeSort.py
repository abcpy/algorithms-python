def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2  # 将列表分成更小的两个列表
    print(mid)
    # 分别对左右两个列表进行处理, 分别返回两个排序好的列表
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge(left, right)


def merge(left, right):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    result = []
    i=j=0
    # 对两个列表中元素，两两对比
    # 将最小的元素，放到result中，并对当前列表的下标+1
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result += left[i:]
    result += right[j:]
    return result

seq = [5,3,0,6,1]
result = mergeSort(seq)
print(result)