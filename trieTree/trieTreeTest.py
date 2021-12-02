"""
特性：
1. 根节点不包含字符，除根节点外的每一个子节点都包含一个字符
2. 从根节点到某一节点，路径上经过的字符连接起来，就是该节点对应的字符串
3. 每个单词的公共前缀作为一个字符节点保存

Trie is a tree-like data structure made up of nodes.
Each node may have none, one or more children
When used to store a vocabulary, each node is used to store a character,
and consequently each "branch" of the trie represents a unique word


There are two major operations that can be performed on a trie, namely:

Inserting a word into the trie
Searching for words using a prefix

Inserting Words into the Trie:
In order to insert a new word into the trie, we need to first check whether any prefix of the word is already in the trie
 Therefore, we will start traverse the trie from the root node, and follow the algorithm below:

 1. Set the current node to be the root node
 2. Set the current character as the first character of the input word
 3. Check if the current character is a child of the current node
If yes, set the current node to be this child node, set the current character to the next character in the input word, and perform this step again
If no, it means from this character onwards, we will need to create new nodes and insert them into the trie

"""

"""
To implement a trie, we can first create a TrieNode class, which can be used to represent a node in the trie. Below is how this class can be implemented

"""
class TrieNode:
    """A node in the trie structure"""
    def __init__(self, char):
        # the character stored in this node
        self.char = char
        # whether this can be the end of a word
        self.is_end = False
        # a counter indicating how many times a word is inserted
        self.counter = 0
        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}

class Trie(object):
    def __init__(self):
        """
        The trie has at least the root node
        the root node does not store any character
        """
        self.root = TrieNode("")

    def insert(self, word):
        """
        Insert a word into the trie
        :param word:
        :return:
        """
        node = self.root

        # Loop through each character in the word
        # check if there is no child containg the character, create a new child of the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found
                # crate a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True

        node.counter += 1

    def dfs(self, node, prefix):
        """
        Depth-first traversal of the trie

        :param node: the node to start with
        :param prefix: the current prefix, for tracing a word while traversing the trie
        :return:
        """

        if node.is_end:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x):
        """
        Given an input(a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of
        times they have been inserted
        :param x:
        :return:
        """
        self.output = []
        node = self.root
        # check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        self.dfs(node, x[:-1])

        return sorted(self.output, key=lambda x:x[1], reverse=True)

if __name__ == "__main__":
    t = Trie()
    t.insert("was")
    t.insert("word")
    t.insert("war")
    t.insert("what")
    t.insert("where")
    print(t.query("o"))



