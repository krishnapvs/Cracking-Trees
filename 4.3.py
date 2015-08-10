'''Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.'''

1 2 3 4 5 6 7 8 9 10

class BinTree:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

    def addNode(self,key):
        if self.key >= key:
            if not self.left:
                self.left=BinTree(key)
            else:
                self.left.addNode(key)
        else:
            if not self.right:
                self.right=BinTree(key)
            else:
                self.right.addNode(key)

def inorder(tree):
    if not tree:
        return
    else:
        inorder(tree.left)
        print tree.key
        inorder(tree.right)


def bin(l,start,end,n1=None):
    if end < start:
        return
    else:
        mid=(start+end)/2
        if not n1:
            n1=BinTree(l[mid])
        else:
            n1.addNode(l[mid])
        bin(l,start,mid-1,n1)
        bin(l,mid+1,end)
        
