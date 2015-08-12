'''Implement a function to check if a binary tree is a binary search tree.'''

class BinTree:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

    def addNode(self,key):
        if key <= self.key:
            if self.left:
                self.left.addNode(key)
            else:
                self.left=BinTree(key)
        else:
            if self.right:
                self.right.addNode(key)
            else:
                self.right=BinTree(key)

def isBinarySearchTree(tree):
    ''' Function to check if the tree is a binary search tree. Returns True if the tree is binarySearchTree else returns False'''
    # case when no child nodes are present
    if (not (tree.left) and not (tree.right)):
        return True
    # case when only right child is present
    elif not tree.left:
        if tree.right.key <= tree.key:
            return False
        else:
            return isBinarySearchTree(tree.right)
    # case when only left child is present
    elif not tree.right:
        if tree.left.key > tree.key:
            return False
        else:
            return isBinarySearchTree(tree.left)
    # case when both the children are present
    else:
        return (tree.left.key <= tree.key < tree.right.key) and isBinarySearchTree(tree.left) and isBinarySearchTree(tree.right)

tree=BinTree(10)
for i in range(20):
    tree.addNode(i)
print isBinarySearchTree(tree)                                                                 
                                                                 
                                                                
