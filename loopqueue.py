"""
enqueue O(1)
dequeue O(n)

loop queue:
  front: 队首
  tail: 指向下一个元素入队的位置
  队列为空： front == tail
  当队列最后一个位置入队元素后，我们从队列最开始的位置
  继续入队元素

  由于特意浪费了一个空间，所以arr的实际大小应该是用户传入的
  容量 + 1

"""
import datetime

class LoopQueue:
    def __init__(self, n=10):
        self.arr = [None] * (n + 1)
        self.front = 0
        self.tail = 0
        self.size = 0

    def __str__(self):
        return str(self.arr)

    def __len__(self):
        return len(self.arr)

    def __iter__(self):
        return iter(self.arr)

    def get_size(self):
        """
        获取队列元素个数
        :return:
        """
        return self.size

    def get_capaticty(self):
        """
        获取队列的容积（实际可存储元素的个数）
        :return:
        """
        return self.__len__() - 1

    def is_full(self):
        """
        判断队列是否为满
        :return:
        """
        return (self.tail + 1) % len(self.arr) == self.front

    def is_empty(self):
        """
        判断队列是否为空
        :return:
        """
        return self.size == 0

    def get_front(self):
        """
        获取队首
        :return:
        """
        return self.arr[self.front]

    def enqueue(self, e):
        """
        入队
        :param e:
        :return:
        """
        if self.is_full():
            self.resize(self.get_capaticty() * 2)
        self.arr[self.tail] = e
        self.tail = (self.tail + 1) % len(self.arr)
        self.size += 1

    def dequeue(self):
        """
        出队
        :return:
        """
        if self.is_empty():
            raise Exception("Cannot dequeue from an empty queue")
        result = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % len(self.arr)
        self.size -= 1

        # 如果元素的个数少于容积的1/4 缩容
        if self.size < self.get_capaticty() //4 and self.get_capaticty() > 1:
            self.resize(self.get_capaticty() // 2)
        return result

    def resize(self, new_capacity):
        new_arr = [None] * (new_capacity + 1)
        for i in range(self.size):
            new_arr[i] = self.arr[(i + self.front) % len(self.arr)]
        self.arr = new_arr
        self.front = 0
        self.tail = self.size

if __name__ == "__main__":
    loop_queue = LoopQueue()
    start_time = datetime.datetime.now()
    for i in range(20):
        loop_queue.enqueue(i)
    print('--------测试enqueue----------')
    print("Loop Queue size = {0}, capacity = {1}\n".format(loop_queue.get_size(), loop_queue.get_capaticty()))
    print("is_empty:", loop_queue.is_empty())
    print("is_full:", loop_queue.is_full())






