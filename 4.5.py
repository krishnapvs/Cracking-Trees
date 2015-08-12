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
    flag=False
    if (not (tree.left) and not (tree.right)):
        return True
    elif not tree.left:
        if tree.right.key <= tree.key:
            return False
        else:
            return isBinarySearchTree(tree.right)
    elif not tree.right:
        if tree.left.key > tree.key:
            return False
        else:
            return isBinarySearchTree(tree.left)
    else:
        return (tree.left.key <= tree.key < tree.right.key) and isBinarySearchTree(tree.left) and isBinarySearchTree(tree.right)

tree=BinTree(10)
for i in range(20):
    tree.addNode(i)
print isBinarySearchTree(tree)                                                                 
                                                                 
                                                                
