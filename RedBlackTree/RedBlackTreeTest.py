"""
What is a Red-Black Tree?

Every node of the red-black tree contains an extra attribute denoting the color of the node,
specifically, either red or black.

The importance of these colors in the nodes of the tree ensures that
the tree is balanced while insertion and deletion operations of the node

1. Tree Property: Red-Black tree should be a binary search tree.
2. Red/Black Property: Every node of the tree is colored either red or black.
3. Root Property: The color attribute of the root node is always black.
4. Leaf Property: Every leaf of the tree is black.
5. Red Property: The child node is always black if the parent node is red in color. Therefore, there should not be two consecutive red nodes.
6. Depth Property: Every path from the root node to any leaf node should have the same number of black-colored nodes.

Insertion Operation:
When you insert a new node in the tree, it will always be inserted as Red Node.

1. Recoloring
Recolouring is the change in colour of the node.
2. Rotation

1. Perform standard BST insertion and make the colour of newly inserted nodes as RED.
2. If x is the root, change the colour of x as BLACK (Black height of complete tree increases by 1).
3. Do the following if the color of x’s parent is not BLACK and x is not the root.
a) If x’s uncle is RED
(i) Change the colour of parent and uncle as BLACK.
(ii) Colour of a grandparent as RED.
(iii) Change x = x’s grandparent, repeat steps 2 and 3 for new x.
b) If x’s uncle is BLACK, then there can be four configurations for x, x’s parent (p) and x’s grandparent (g) (This is similar to AVL Tree)
(i) Left Left Case (p is left child of g and x is left child of p)
(ii) Left Right Case (p is left child of g and x is the right child of p)
(iii) Right Right Case (Mirror of case i)
(iv) Right Left Case (Mirror of case ii)

"""

class TreeNode:
    def __init__(self, data, left=None, right=None, parent=None, color="RED"):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color

class RBTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def insert(self, node):
        temp_root = self.root
        temp_node = None

        while temp_root:
            temp_node = temp_root
            if node.data == temp_node.data:
                return False
            elif node.data > temp_node.data:
                temp_root = temp_root.right
            else:
                temp_root = temp_root.left

        # 在相应位置插入节点
        if not temp_root:
            # insert case1
            self.root = node
            node.color = "BLACK"
        elif node.data < temp_node.data:
            temp_node.left = node
            node.parent = temp_node
        else:
            temp_node.right = node
            node.parent = temp_node

        # 调整树
        self.insert_fixup(node)
    def insert_fixup(self, node):
        if node.data == self.root.data:
            return
        while node.parent and node.parent.color == "RED":
            pass
