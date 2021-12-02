from maxheap.maxheaptest import MaxHeap

class PriorityQueue:
    def __init__(self, maxsize):
        self.heap = MaxHeap(maxsize)
        self.len = 0

    def push(self, value):
        self.heap.insert(value)
        self.len += 1

    def pop(self):
        return self.heap.extractMax()

pq = PriorityQueue(32)
arr = [4, 6, 8, 3, 2, 9, 1]
for i in range(1, len(arr)+1):
    pq.push(arr[i-1])
print(pq.pop())
