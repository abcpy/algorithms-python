"""
解题思路：
维护一个min_stack: 将严格按照递减
push时如果x <= min_stack的栈顶元素，则将元素加入min_stack
pop 时如果 stack 和min_stack 的栈顶元素相同，则同时pop
"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [float('inf')]

    def push(self, x:int) -> None:
        self.stack.append(x)
        if x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]