"""
Max-Heap: is a complete binary tree which the value in each internal node is greater than
or equal to the values in the children of that node

A Max Heap is a Complete Binary Tree.
A Max Heap is typically represented as an array
The root element Arr[0]
i.e Arr[i]

parent node: Arr[(i-1)/2]
left children node: Arr[(2*i)+1]
right children node: Arr[(2*i)+2]

Operations on Max Heap:
1. getMax(): It returns the root element of Max Heap. O(1)
2. extracMax(): Removes the maximum element from Max Heap. O(Log n)
3. insert(): Inserting a new key takes O(log n) time
"""

import sys
class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return (2 * pos) + 1

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    # Function to heapify the node at pos
    def maxHeapify(self, pos):
        # If the node is a non-leaf node and smaller than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
                self.Heap[pos] < self.Heap[self.rightChild(pos)]):

                #Swap with the left child and heapify the left child
                if self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))

                # Swap with the right cild and heapify the righe child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

    # Function to insert a node the heap
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size
        while self.Heap[current] > self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    # Function to remove and return the maximum
    # element from the heap
    def extractMax(self):
        poped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)
        return poped

    def print(self):
        for i in range(1, (self.size // 2) + 1):
            print("PARENT: " + str(self.Heap[i]) +
                  " LEFT CHILD: " + str(self.Heap[2 * i]) +
                  " RIGHT CHILD: " + str(self.Heap[2 * i + 1]))

if __name__ == "__main__":
    print("The maxHeap is ")

    maxHeap = MaxHeap(15)
    maxHeap.insert(5)
    maxHeap.insert(3)
    maxHeap.insert(17)
    maxHeap.insert(10)
    maxHeap.insert(84)
    maxHeap.insert(19)
    maxHeap.insert(6)
    maxHeap.insert(22)
    maxHeap.insert(9)

    maxHeap.print()

    print("The max val is " + str(maxHeap.extractMax()))

    print("---------------------------------")
    maxHeap.print()








