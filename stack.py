"""
LIFO Last-In/Fist-Out
In stack, a new element is added at one end
and an element is removed from that end only
This insert and delete operations are often called push and pop

Using Lists as Stacks
"""
# list

list_stack = []
list_stack.append('a')
list_stack.append('b')
list_stack.append('c')

print("Initial stack")
print(list_stack)

"""
  pop() function to pop
  element from stack in LIFO order
"""
print("\nElements popped from stack:")
print(list_stack.pop())
print(list_stack.pop())
print(list_stack.pop())
print(list_stack.pop())

