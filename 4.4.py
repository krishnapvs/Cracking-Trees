'''Given a binary tree, design an algorithm which creates a linked list of all the nodes at
each depth (e.g., if you have a tree with depth D, you'll have D linked lists).'''


class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

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
        print tree.key
        inorder(tree.left)
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
        bin(l,mid+1,end,n1)
    return n1

def llist(tree,n=0,l=[]):
    if tree==None:
        return
    else:
        print n
        if l[n]==None:
            l[n]=Node(tree.key)
        else:
            temp=l[n]
            while(temp.next):
                temp=temp.next
            temp.next=Node(tree.key)
        llist(tree.left,n+1,l)
        llist(tree.right,n+1,l)
        return l

a=[i for i in range(20)]
l=[]
for i in range(10):
    l.append(None)

tree=bin(a,0,19)
inorder(tree)
l=llist(tree,0,l)

