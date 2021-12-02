"""
AVL tree is a self-balancing Binary Search Tree(BST) where the
difference between heights of left and right subtrees cannot be more
than one for all nodes

Why AVL Trees?
Most of the BST operations (e.g., search, max, min, insert, delete.. etc) take O(h) time where h is the height of the BST.
The cost of these operations may become O(n) for a skewed Binary tree

If we make sure that height of the tree remains O(Logn) after every insertion and deletion,
then we can guarantee an upper bound of O(Logn) for all these operations.

The height of an AVL tree is always O(Logn) where n is the number of nodes in the tree


Insertion:
To make sure that the given tree remains AVL after every insertion,
we must augment the standard BST insert operation to perform some re-balancing

Balance Factor = Height Of Left Subtree - Height Of Right Subtree

Remember that every AVL Tree is a binary search tree
but every Binary Search Tree need not be AVL Tree.

1. Single Rotation
Single rotation switches the roles of the parent and child while maintaining the search order.
We rotate the node and its child, the child becomes a parent.

Single LL(Left Left) Rotation:
Here, every node of the tree moves towards the left from its current position.
Therefore, a parent becomes the right child in LL rotation.

Single RR(Right Right) Rotation:
Here, every node of the tree moves towards the right from the current position.
Therefore, the parent becomes a left child in RR rotation

2. Double Rotation
LR(Left-Right) Rotation:
The LR rotation is the process where we perform a single left rotation followed by a single right rotation
RL (Right-Left) Rotation:
The RL rotation is the process where we perform a single right rotation followed by a single left rotation

Insertion Operation In AVL Tree:
In the AVL tree, the new node is always added as a leaf node
After the insertion of the new node, it is necessary to modify the balance factor of each node in the AVL tree
using the rotation operations

1. Find the appropriate empty subtree where the new value should be added by comparing the values in the tree
2. Create a new node at the empty subtree
3. The new node is a leaf ad thus will have a balance factor of zero
4. Return to the parent node and adjust the balance factor of each node through the rotation process and
continue it until we are back at the root. Remember that the modification of the balance factor must happen in a bottom-up fashion


Reblancing:

bf(root) = 2: Indicates the tree is left heavy (also called left-left imbalance)

bf(root) = -2: Indicates the tree is right heavy (right-right imbalance)

bf(root) = 2 & bf(root.left) < 0: Indicates the tree is left heavy and
the left child's right subtree is taller than its left (left-right)

bf(root) = -2 & bf(root.right) > 0: Indicates the tree is right heavy and
the right child's left subtree is taller than its right (right-left)
"""

class AVLTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        #1.  Perform normal BST
        if root is None:
            return AVLTreeNode(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        #2. Update the height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        #3. Get the balance factor
        balance = self.getBalance(root)

        #4.  If the node is unbalanced
        # Case1. Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        # Case2. Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        # Case3. Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # Case4 Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key):
        if not root:
            return
        elif key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if root.left and root.right:
                tmp = self.minValueNode(root.right)
                root.val = tmp.val
                root.right = self.delete(root.right, tmp.val)
            elif root.left is None and root.right is None:
                root = None
            elif root.right is None:
                root = root.left
            else:
                root = root.right

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

            # Case2. Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

            # Case3. Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
            # Case4 Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Return the new root
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def preorder(self, root):
        if not root:
            return

        print("{0} ".format(root.val), end="")
        self.preorder(root.left)
        self.preorder(root.right)


if __name__ == "__main__":
    myTree = AVLTree()
    root = AVLTreeNode(4)

    root = myTree.insert(root, 10)
    root = myTree.insert(root, 20)
    root = myTree.insert(root, 30)
    root = myTree.insert(root, 40)
    root = myTree.insert(root, 50)
    root = myTree.insert(root, 25)

    myTree.preorder(root)

    print("------------------------------------------------\n")

    myTree.delete(root, 20)
    myTree.preorder(root)
