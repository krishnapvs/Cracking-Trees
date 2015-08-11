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
