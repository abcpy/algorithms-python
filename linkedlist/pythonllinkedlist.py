"""
Each node in a list consists of at least two parts:
1) data
2) Pointer (Or Reference) to the next node
"""
"""
 Node class
"""


class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data #Assign data
        self.next = None # Initialize next as null


"""
Linked list class
"""
class LinkedList:

    # Function to initialize the linked list object
    def __init__(self):
        self.head = None

    def printList(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next

    #This function is in LinkedList class
    #Function to insert a new node at the begining
    def push(self, new_data):
        #1. Allocate the node and put in the data
        new_data = Node(new_data)

        #2. Make next of new node as head
        new_data.next = self.head

        #3. Move the head to point to new Node
        self.head = new_data

    #Insert a new node after the given prev_node.
    def insertAfter(self, prev_node, new_data):
        #1 check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must in Linked List")
        #2 Create new node and put in the data
        new_data = Node(new_data)
        #3 make next of new Node as new of pre_node
        new_data.next = prev_node.next
        #4 make next of prev node as new_node
        prev_node.next = new_data

    # Appends a new node at the end
    def append(self, new_data):
        #1. Create a new node
        new_data = Node(new_data)
        #2. if the Linked List is empty, then make the new node as head
        if self.head is None:
            self.head = new_data
            return
        #3. Else traverse till the last node
        last = self.head
        while last.next:
            last = last.next

        #4 Change the next of last node
        last.next = new_data

    # Given a reference to the head of a list and a key
    # delete the first occurrence of key in linked list
    def deleteNode(self, key):
        # store head node
        tmp = self.head

        # If head node itself holds the key to be deleted
        if tmp is not None:
            if tmp.data == key:
                self.head = tmp.next
                tmp = None
                return

        # Search for the key to be deleted. keep track of the
        # previous node as we need to change prev.next
        while tmp:
            if tmp.data == key:
                break
            prev = tmp
            tmp = tmp.next

        if tmp is None:
            return

        #Unlink the node from linked list
        prev.next = tmp.next

        tmp = None

    def deleteNode_posotion(self, position):
        # If linked list is empty
        tmp = self.head
        if tmp is None:
            return

        # If head needs to be removed
        if position == 0:
            self.head = tmp.next
            tmp = None
            return

        # Find previous node of the node to be deleted
        for i in range(position - 1):
            tmp = tmp.next
            if tmp is None:
                break
        if tmp is None:
            return
        if tmp.next is None:
            return

        afterDeleteNode = tmp.next.next
        tmp.next = None
        tmp.next = afterDeleteNode


if __name__ == "__main__":
    linklist = LinkedList()
    linklist.head = Node(1)
    second = Node(2)
    third  = Node(3)
    linklist.head.next = second # Link first node with secode
    # Now next of first Node refers to secode. So they both are linked

    second.next = third # Link secode node with third node
    # linklist.printList()

    linklist.append(6)
    # linklist.printList()

    linklist.push(7)
    # linklist.printList()

    linklist.insertAfter(linklist.head.next.next, 8)
    linklist.printList()

    print("-------------------------------")
    linklist.deleteNode(8)
    linklist.printList()

    print("-------------------------------")
    linklist.deleteNode_posotion(0)
    linklist.printList()

    print("-------------------------------")
    linklist.deleteNode_posotion(1)
    linklist.printList()



