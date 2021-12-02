"""
problem:
1 Find the sum of elements from index l to r where 0 <= l <= r <= n-1
2 Change value of a specified element of the array to a new value x. We need to do arr[i] = x where 0 <= i <= n-1.

O(Logn) time
1. Leaf Nodes are the elements of the input array.
2. Each internal node represents some merging of the leaf nodes. The merging may be different for different problems. For this problem, merging is sum of leaves under a node.
An array representation of tree is used to represent Segment Trees:
For each node at index i, the left child is at index 2*i+1
 right child at 2*i+2
 the parent is at  ⌊(i – 1) / 2⌋

 How does above segment tree look in memory?
 Like Heap, the segment tree is also represented as an array
 It is rather a full binary tree (every node has 0 or 2 children)
  all levels are filled except possibly the last level

Below is memory representation of segment tree for input array {1, 3, 5, 7, 9, 11}
st[] = {36, 9, 27, 4, 5, 16, 11, 1, 3, DUMMY, DUMMY, 7, 9, DUMMY, DUMMY}

Construction of Segment Tree from given array:
We start with a segment arr[0 . . . n-1]
 every time we divide the current segment into two halves
  then call the same procedure on both halves
All levels of the constructed segment tree will be completely filled except the last level
"""

"""
A utility function to get the middle index from corner indexes
"""
def getMid(s, e):
    return s + (e-s) // 2

"""
   A recursive function to get the sum of values
   in the given range of the array. The following 
   are parameters for this function
   
    st --> Pointer to segment tree
    si --> Index of current node in the segment tree.
           Initially 0 is passed as root is always at index 0
    ss & se --> Starting and ending indexes of the segment
                represented by current node, i.e., st[si]
    qs & qe --> Starting and ending indexes of query range 
"""
def getSumUtil(st, ss, se, qs, qe, si):
    if qs <= ss and qe >=se:
        return st[si]

    if se < qs or ss > qe:
        return 0

    mid = getMid(ss, se)
    return getSumUtil(st, ss, mid, qs, qe, si*2 +1) + getSumUtil(st, mid+1, se, qs, qe, si*2 + 2)

def getSum(st, n, qs, qe):
    if qs < 0 or qe > n-1 or qs > qe:
        print("Invalid Input", end = "")
        return -1
    return getSumUtil(st, 0, n-1, qs, qe, 0)

"""
A recursive function that constructs
Segement Tree for array[ss..se]
si is the index of current node in segment tree st
"""
def constructSTUtil(arr, ss, se, st, si):
    """
    if there is one element in array,
    store it in current node of segment tree and return
    :param arr:
    :param ss:
    :param se:
    :param st:
    :param si:
    :return:
    """
    if ss == se:
        st[si] = arr[ss]
        return arr[ss]
    mid = getMid(ss, se)
    st[si] = constructSTUtil(arr, ss, mid, st, si * 2 + 1) + constructSTUtil(arr, mid+1, se, st, si*2 + 2)
    return st[si]

def contructST(arr, n):
    max_size = 4 * n
    st = [0] * max_size
    constructSTUtil(arr, 0, n-1, st, 0)
    return st

"""
i: index of the element to be updated.
      This index is in the input array.
diff --> Value to be added to all nodes
"""
def updateValueUtil(st, ss, se, i, diff, si):
    if i < ss or i > se:
        return

    st[si] = st[si] + diff

    if se != ss:
        mid = getMid(ss, se)
        updateValueUtil(st, ss, mid, i, diff, si*2+1)
        updateValueUtil(st, mid+1, se, i, diff, si *2 + 2)

def updateValue(arr, st, n, i, new_val):
    if i < 0 or i > n -1:
        print("Invalid Input", end = "")
        return

    diff = new_val - arr[i]

    arr[i] = new_val
    updateValueUtil(st, 0, n-1, i, diff, 0)

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    n = len(arr)

    st = contructST(arr, n)

    print("Sum of values in given range = ",
          getSum(st,n,1,3))

    updateValue(arr, st, n, 1, 10)

    print("Updated Sum of values in given range = ",
          getSum(st, n, 1, 3))






