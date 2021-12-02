"""
The left subtree of a node contains only nodes with keys lesser than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
The left and right subtree each must also be a binary search tree.
There must be no duplicate nodes.
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BST:
    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
             if root.value == key:
                 return root
             elif root.value < key:
                 root.right = self.insert(root.right, key)
             else:
                 root.left = self.insert(root.left, key)
        return root

    def search(self, root, key):
        if root:
            res = self._search(root, key)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def _search(self, current_node, key):
        if current_node is None:
            return None
        if key == current_node.value:
            return current_node
        elif key < current_node.value:
            return self._search(current_node.left, key)
        else:
            return self._search(current_node.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value)
            self.inorder(root.right)

    def preOrder(self, root):
        if root:
            print(root.value)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self, root):
        if root:
            self.preOrder(root.left)
            self.preOrder(root.right)
            print(root.value)


    """"
    Delete: 1. Node to be deleted is the leaf
              50                            50
           /     \         delete(20)      /   \
          30      70       --------->    30     70 
         /  \    /  \                     \    /  \ 
       20   40  60   80                   40  60   80
            2. Node to be deleted has only one child: Copy the child to the node and delete the child 
              50                            50
           /     \         delete(30)      /   \
          30      70       --------->    40     70 
            \    /  \                          /  \ 
            40  60   80                       60   80
            
            3. Node to be deleted has two children
            Find inorder successor of the node. 
            Copy contents of the inorder successor to the node and delete the inorder successor. 
            Note that inorder predecessor can also be used. 
              50                            60
           /     \         delete(50)      /   \
          40      70       --------->    40    70 
                 /  \                            \ 
                60   80                           80
    """

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def deleteNode(self, root, key):
        """
        删除BST中的值为key的节点
        :param root:
        :param key:
        :return:
        """
        if root is None:
            return
        elif key < root.value:
            root.left = self.deleteNode(root.left, key)
        elif key > root.value:
            root.right = self.deleteNode(root.right, key)
        else:
            # key == root.value时, 分为三种情况 1. 只有左子树或右子树 2. 有左右子树 3. 无左右子树
            if root.left and root.right:
                # 既有左子树又有右子树, 则找到右子树中最小值节点
                tmp = self.minValueNode(root.right)
                root.value = tmp.value
                root.right = self.deleteNode(root.right, tmp.value)
            elif root.right is None and root.left is None:
                # 左右子树为空
                root = None
            elif root.right is None:
                # 右子树为空
                root = root.left
            elif root.left is None:
                # 左子树为空
                root = root.right
        return root





bst = BST()
r = Node(50)
bst.insert(r, 30)
bst.insert(r, 40)
bst.insert(r, 60)
print(bst.inorder(r))
# print(bst.search(r, 30))
print("--------------------------------")
# print(bst.preOrder(r))
# print("--------------------------------")
# print(bst.postOrder(r))

r = bst.deleteNode(r, 40)
print(bst.inorder(r))
print("--------------------------------")
