from heapq import heapify, heappush, heappop

heap = []
heapify(heap)

heappush(heap, 10)
heappush(heap, 30)
heappush(heap, 20)
heappush(heap, 400)

print("Head value of heap :" + str(heap[0]))

for i in heap:
    print(i, end = ' ')
print("\n")

print("----------------------")
element = heappop(heap)
print(element)

print("----------------------")
for i in heap:
    print(i, end = ' ')
print("\n")

