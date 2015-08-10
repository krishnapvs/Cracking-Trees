'''Implement a function to check if a binary tree is balanced. For the purposes of this
question, a balanced tree is defined to be a tree such that the heights
of the two subtrees of any node never differ by more than one.'''

class BinTree:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    def addNode(self,key):
        if key<=self.key:
            if self.left:
                self.left.addNode(key)
            else:
                self.left=BinTree(key)
        else:
            if self.right:
                self.right.addNode(key)
            else:
                self.right=BinTree(key)
        
def isBalanced(tree):
    # returns balanced if the tree is balanced else false
    if tree==None:
        return True
    else:
        if isBalanced(tree.left) and isBalanced(tree.right) and abs(height(tree.left)-height(tree.right))<=1:
            return True
        else:
            return False

def height(tree):
    # returns the height of the tree
    if not tree:
        return 0
    else:
        return max(height(tree.left),height(tree.right))+1

def isBalancedImproved(tree):
    if checkHeight(tree)==-1:
        return False
    else:
        return True

def checkHeight(tree):
    if not tree:
        return 0
    else:
        a=checkHeight(tree.left)
        if a==-1:
            return -1
        b=checkHeight(tree.right)
        if b==-1:
            return -1
        if abs(a-b)>1:
            return -1
        return max(a,b)+1

    

tree= BinTree(10)
tree.addNode(5)
tree.addNode(15)
tree.addNode(2)
tree.addNode(1)
tree.addNode(7)
#tree.addNode(13)
print isBalanced(tree)
print isBalancedImproved(tree)
